#!/usr/bin/env python3
"""Découpe des vidéos et images d'inspiration en éléments à classer.

  python3 decouper.py --lot LOT SOURCE [SOURCE...] [--mode auto|court|long]
                      [--debut 12:00 --fin 25:00] [--max 60] [--refaire]

SOURCE = fichier vidéo, image, ou dossier (non récursif). Les vidéos téléchargées par
sources.py ont un fichier <video>.tri.json (titre, chaîne, URL, chapitres, décalage).
Sortie : LOT/_travail/elements/NNN_slug_tSSS.S_FMT.(jpg|mp4), LOT/_travail/index.json,
LOT/sources.md. Ne modifie jamais les fichiers sources.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import (IMAGE_EXT, VIDEO_EXT, charger_index, dist, fmt_t, hms, parse_temps,  # noqa: E402
                    sauver_index, slug_depuis_nom, slugifier, sonde, tag_format, travail)

# Réglages par mode. Les distances sont des écarts moyens 0-255 sur des vignettes 16x16.
REGLAGES = {
    "court": dict(fps=4, seuil=0.30, t_sub=22, t_dup=9, min_plan=0.35, anime=4.5,
                  part_principal=0.20, par_principal=3, max=40, dedup=1.15),
    "long": dict(fps=2, seuil=0.30, t_sub=22, t_dup=13, min_plan=0.5, anime=4.5,
                 part_principal=0.08, par_principal=1, max=60, dedup=1.4),
}
SEUIL_LONG = 180  # s : au-delà, une vidéo est traitée en mode long


def meta_source(video):
    for p in (video + ".tri.json", os.path.splitext(video)[0] + ".info.json"):
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                d = json.load(f)
            chap = d.get("chapitres") or [
                {"debut": c.get("start_time", 0), "fin": c.get("end_time"), "titre": c.get("title", "")}
                for c in d.get("chapters") or []]
            return {"titre": d.get("titre") or d.get("title"),
                    "chaine": d.get("chaine") or d.get("channel") or d.get("uploader"),
                    "url": d.get("url") or d.get("webpage_url"),
                    "decalage": float(d.get("decalage") or 0), "chapitres": chap}
    return {"titre": None, "chaine": None, "url": None, "decalage": 0.0, "chapitres": []}


def analyser(video, debut, fin, fps, seuil):
    """Une passe ffmpeg : coupes (détection de scène) + vignettes 16x16 rgb à `fps` i/s."""
    def lancer(hw):
        cmd = ["ffmpeg", "-hide_banner", "-nostats", "-v", "info"]
        if hw:
            cmd += ["-hwaccel", "videotoolbox"]
        if debut:
            cmd += ["-ss", f"{debut:.3f}"]
        cmd += ["-i", video]
        if fin is not None:
            cmd += ["-t", f"{fin - (debut or 0):.3f}"]
        cmd += ["-an", "-sn", "-dn", "-filter_complex",
                f"[0:v]scale=320:-2,split=2[a][b];[a]select='gt(scene,{seuil})',showinfo[s];"
                f"[b]fps={fps},scale=16:16:flags=area,format=rgb24[t]",
                "-map", "[s]", "-f", "null", "-", "-map", "[t]", "-f", "rawvideo", "pipe:1"]
        with tempfile.TemporaryFile() as err:
            out = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=err)
            err.seek(0)
            log = err.read().decode("utf-8", "replace")
        return out.returncode, out.stdout, log

    code, raw, log = lancer(sys.platform == "darwin")
    if code != 0 or not raw:
        code, raw, log = lancer(False)
    if code != 0 or not raw:
        raise RuntimeError(f"ffmpeg a échoué sur {video}:\n{log[-1500:]}")
    off = debut or 0
    coupes = [off + float(m) for m in re.findall(r"pts_time:([\d.]+)", log)]
    n = len(raw) // 768
    vign = [raw[i * 768:(i + 1) * 768] for i in range(n)]
    temps = [off + i / fps for i in range(n)]
    return coupes, temps, vign


def segmenter(coupes, temps, vign, t0, t1, r):
    bornes = [t0]
    for c in sorted(coupes):
        if t0 < c < t1 and c - bornes[-1] >= r["min_plan"]:
            bornes.append(c)
    bornes.append(t1)
    segs = []
    for s, e in zip(bornes, bornes[1:]):
        idx = [i for i, t in enumerate(temps) if s <= t < e]
        if not idx:
            j = min(range(len(temps)), key=lambda i: abs(temps[i] - (s + e) / 2))
            segs.append({"debut": s, "fin": e, "idx": [j], "plan": len(segs)})
            continue
        # découpe interne : un titre, une UI ou un recadrage qui arrive sans coupe
        cur, ref = [idx[0]], vign[idx[0]]
        debut = s
        for i in idx[1:]:
            if dist(vign[i], ref) > r["t_sub"]:
                segs.append({"debut": debut, "fin": temps[i], "idx": cur})
                debut, cur, ref = temps[i], [i], vign[i]
            else:
                cur.append(i)
        segs.append({"debut": debut, "fin": e, "idx": cur})
    for g in segs:
        ids = g["idx"]
        g["rep"] = ids[len(ids) // 2]
        diffs = [dist(vign[a], vign[b]) for a, b in zip(ids, ids[1:])]
        g["mouvement"] = sum(diffs) / len(diffs) if diffs else 0.0
        g["duree"] = g["fin"] - g["debut"]
    return segs


def grouper(segs, vign, t_dup):
    groupes = []
    for k, g in enumerate(segs):
        v = vign[g["rep"]]
        best, bd = None, 1e9
        for G in groupes:
            d = dist(v, G["centre"])
            if d < bd:
                best, bd = G, d
        if best is not None and bd < t_dup:
            best["membres"].append(k)
            best["duree"] += g["duree"]
        else:
            groupes.append({"centre": v, "membres": [k], "duree": g["duree"]})
    for n, G in enumerate(groupes):
        for k in G["membres"]:
            segs[k]["groupe"] = n
    return groupes


def etaler(membres, segs, n):
    """n membres répartis dans le temps (les plus longs de chaque tranche)."""
    if len(membres) <= n:
        return list(membres)
    tri = sorted(membres, key=lambda k: segs[k]["debut"])
    tranches = [tri[i * len(tri) // n:(i + 1) * len(tri) // n] for i in range(n)]
    return [max(t, key=lambda k: segs[k]["duree"]) for t in tranches if t]


def chapitre_de(t, chapitres):
    for c in chapitres:
        if c["debut"] <= t < (c["fin"] if c["fin"] is not None else 1e12):
            return c["titre"]
    return None


def choisir(segs, groupes, vign, mode, r, total, plafond, chapitres, decalage, t0):
    principaux = sorted([n for n, G in enumerate(groupes) if G["duree"] / total >= r["part_principal"]],
                        key=lambda n: -groupes[n]["duree"])
    if not principaux and groupes:
        principaux = [max(range(len(groupes)), key=lambda n: groupes[n]["duree"])]
    choix = {}

    # 1. accroche : images fixes des premières secondes
    if t0 == 0 and decalage == 0:
        for t in ((0.3, 1.3, 2.5) if mode == "court" else (0.5,)):
            k = next((k for k, g in enumerate(segs) if g["debut"] <= t < g["fin"]), None)
            if k is not None:
                choix[("acc", t)] = {"seg": k, "t": t, "accroche": True, "score": 999}

    # 2. plans récurrents (face caméra, mise en page d'écran qui revient) : très peu d'images.
    #    Ce n'est pas toujours le face caméra qui domine (vidéos faites surtout d'écrans).
    if mode == "long":
        quota = [(n, 2 if i < 2 else 1) for i, n in enumerate(principaux)]
    else:
        quota = [(n, r["par_principal"]) for n in principaux]
    for n, q in quota:
        for k in etaler(groupes[n]["membres"], segs, q):
            choix[("seg", k)] = {"seg": k, "principal": True, "score": 500}

    # 3. tout le reste : un élément par groupe, classé par écart au plan principal
    centres = [groupes[n]["centre"] for n in principaux]
    autres = []
    for n, G in enumerate(groupes):
        if n in principaux:
            continue
        k = max(G["membres"], key=lambda k: (segs[k]["mouvement"] > r["anime"], segs[k]["duree"]))
        g = segs[k]
        ecart = min((dist(vign[g["rep"]], c) for c in centres), default=40)
        anime = g["mouvement"] > r["anime"]
        score = ecart + (12 if anime else 0) + min(len(G["membres"]), 4)
        autres.append((score, k))
    autres.sort(reverse=True)
    place = max(0, plafond - len(choix))
    pris = []
    if mode == "long" and chapitres:      # au moins un élément par chapitre si possible
        vus = set()
        for score, k in autres:
            ch = chapitre_de(segs[k]["debut"] + decalage, chapitres)
            if ch not in vus and len(pris) < place:
                vus.add(ch)
                pris.append((score, k))
    for item in autres:
        if len(pris) >= place:
            break
        if item not in pris:
            pris.append(item)
    # s'il reste de la place : un 2e exemple des groupes qui reviennent à plusieurs moments
    if len(pris) < place:
        for score, k in list(pris):
            G = groupes[segs[k]["groupe"]]
            if len(G["membres"]) >= 3 and len(pris) < place:
                for k2 in etaler(G["membres"], segs, 2):
                    if k2 != k and abs(segs[k2]["debut"] - segs[k]["debut"]) > 20:
                        pris.append((score / 2, k2))
                        break
    for score, k in pris:
        choix[("seg", k)] = {"seg": k, "score": round(score, 1)}
    return list(choix.values()), principaux


def extraire(video, sortie, t, duree=None):
    if duree is None:
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", video, "-frames:v", "1",
               "-q:v", "2", sortie]
    else:
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", video, "-t", f"{duree:.2f}",
               "-an", "-vf", "scale='if(gt(iw,ih),min(1280,iw),-2)':'if(gt(iw,ih),-2,min(1280,ih))'",
               "-c:v", "libx264", "-preset", "veryfast", "-crf", "24", "-pix_fmt", "yuv420p",
               "-movflags", "+faststart", sortie]
    subprocess.run(cmd, check=False)
    return os.path.exists(sortie)


def traiter_video(video, num, lot, args):
    meta = meta_source(video)
    w, h, duree = sonde(video)
    fmt = tag_format(w, h)
    mode = args.mode if args.mode != "auto" else ("long" if (duree or 0) > SEUIL_LONG else "court")
    r = dict(REGLAGES[mode])
    plafond = args.max or r["max"]
    dec = meta["decalage"]
    t0 = max(0.0, (args.debut - dec) if args.debut is not None else 0.0)
    t1 = min(duree or 1e9, (args.fin - dec) if args.fin is not None else (duree or 1e9))
    slug = slugifier(meta["chaine"]) if meta["chaine"] else slug_depuis_nom(video)
    print(f"[{num:03d}] {os.path.basename(video)} : {fmt}, {hms(duree or 0)}, mode {mode}, "
          f"plage {hms(t0 + dec)}-{hms(t1 + dec)}", flush=True)

    coupes, temps, vign = analyser(video, t0, t1 if t1 < (duree or 1e9) else None, r["fps"], r["seuil"])
    segs = segmenter(coupes, temps, vign, t0, t1, r)
    groupes = grouper(segs, vign, r["t_dup"])
    choix, principaux = choisir(segs, groupes, vign, mode, r, max(t1 - t0, 1), plafond,
                                meta["chapitres"], dec, t0)

    # dernier filtre : deux éléments choisis qui se ressemblent trop -> on garde le meilleur
    def vign_t(t):
        return vign[min(range(len(temps)), key=lambda i: abs(temps[i] - t))]
    for c in choix:
        g = segs[c["seg"]]
        anime = g["mouvement"] > r["anime"]
        c["_t"] = c.get("t", (g["debut"] + min(g["fin"], g["debut"] + 3)) / 2 if anime else temps[g["rep"]])
        c["_v"] = vign_t(c["_t"])
        c["_prio"] = (c.get("accroche", False), anime, c.get("score") or 0)
    gardes = []
    for c in sorted(choix, key=lambda c: c["_prio"], reverse=True):
        if c.get("accroche") or all(dist(c["_v"], o["_v"]) >= r["t_dup"] * r["dedup"] for o in gardes):
            gardes.append(c)
    choix = gardes

    dossier = travail(lot, "elements")
    os.makedirs(dossier, exist_ok=True)
    elements, taches = [], []
    for c in choix:
        g = segs[c["seg"]]
        anime = g["mouvement"] > r["anime"] and not c.get("principal") and not c.get("accroche")
        if c.get("accroche"):
            t, dur_x = c["t"], None
        elif anime:
            t, dur_x = g["debut"], min(3.0, max(2.0, g["duree"]))
            t = min(t, max(t0, t1 - dur_x))
        else:
            t, dur_x = temps[g["rep"]], None
        nom = f"{num:03d}_{slug}_t{fmt_t(t + dec)}_{fmt}.{'mp4' if dur_x else 'jpg'}"
        el = {"fichier": nom, "source": num, "t": round(t + dec, 2),
              "fin_plan": round(g["fin"] + dec, 2), "duree_plan": round(g["duree"], 2),
              "type": "extrait" if dur_x else "image", "format": fmt,
              "mouvement": round(g["mouvement"], 1), "groupe": g.get("groupe"),
              "principal": bool(c.get("principal")), "accroche": bool(c.get("accroche")),
              "score": c.get("score"), "chapitre": chapitre_de(t + dec, meta["chapitres"])}
        elements.append(el)
        taches.append((video, os.path.join(dossier, nom), t, dur_x))
    with ThreadPoolExecutor(4) as ex:
        ok = list(ex.map(lambda a: extraire(*a), taches))
    elements = [e for e, o in zip(elements, ok) if o]
    elements.sort(key=lambda e: e["t"])
    src = {"num": num, "chemin": os.path.abspath(video), "slug": slug, "format": fmt,
           "duree": duree, "mode": mode, "plage": [round(t0 + dec, 1), round(t1 + dec, 1)],
           "titre": meta["titre"], "chaine": meta["chaine"], "url": meta["url"],
           "chapitres": len(meta["chapitres"]), "plans": len(segs), "groupes": len(groupes),
           "groupes_principaux": len(principaux), "elements": len(elements)}
    print(f"      {len(coupes)} coupes, {len(segs)} segments, {len(groupes)} groupes visuels "
          f"({len(principaux)} plan(s) principal), {len(elements)} éléments gardés "
          f"dont {sum(e['type'] == 'extrait' for e in elements)} extraits", flush=True)
    return src, elements


def traiter_image(img, num, lot):
    w, h, _ = sonde(img)
    fmt = tag_format(w, h)
    slug = slug_depuis_nom(img)
    nom = f"{num:03d}_{slug}_t0_{fmt}{os.path.splitext(img)[1].lower()}"
    dossier = travail(lot, "elements")
    os.makedirs(dossier, exist_ok=True)
    shutil.copy2(img, os.path.join(dossier, nom))
    src = {"num": num, "chemin": os.path.abspath(img), "slug": slug, "format": fmt, "duree": None,
           "mode": "image", "titre": None, "chaine": None, "url": None, "elements": 1}
    return src, [{"fichier": nom, "source": num, "t": 0, "type": "image", "format": fmt,
                  "principal": False, "accroche": False, "score": None, "chapitre": None}]


def ecrire_sources_md(lot, idx):
    lignes = ["# Sources du lot", "",
              "| N° | Titre | Chaîne | URL | Format | Durée | Plage analysée | Éléments | Fichier |",
              "|---|---|---|---|---|---|---|---|---|"]
    for s in idx["sources"]:
        plage = f"{hms(s['plage'][0])}-{hms(s['plage'][1])}" if s.get("plage") else ""
        lignes.append(f"| {s['num']:03d} | {s.get('titre') or ''} | {s.get('chaine') or ''} | "
                      f"{s.get('url') or ''} | {s['format']} | {hms(s['duree']) if s.get('duree') else ''} | "
                      f"{plage} | {s.get('elements', '')} | `{s['chemin']}` |")
    with open(os.path.join(lot, "sources.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lignes) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lot", required=True)
    ap.add_argument("sources", nargs="+")
    ap.add_argument("--mode", default="auto", choices=["auto", "court", "long"])
    ap.add_argument("--debut")
    ap.add_argument("--fin")
    ap.add_argument("--max", type=int)
    ap.add_argument("--refaire", action="store_true", help="refait une source déjà découpée")
    args = ap.parse_args()
    args.debut, args.fin = parse_temps(args.debut), parse_temps(args.fin)

    fichiers = []
    for s in args.sources:
        if os.path.isdir(s):
            fichiers += sorted(os.path.join(s, f) for f in os.listdir(s) if not f.startswith("."))
        else:
            fichiers.append(s)
    fichiers = [f for f in fichiers if os.path.splitext(f)[1].lower() in VIDEO_EXT | IMAGE_EXT]

    os.makedirs(args.lot, exist_ok=True)
    idx = charger_index(args.lot)
    for f in fichiers:
        chemin = os.path.abspath(f)
        deja = next((s for s in idx["sources"] if s["chemin"] == chemin), None)
        if deja and not args.refaire:
            print(f"déjà découpé : {f} (n° {deja['num']:03d}), --refaire pour recommencer")
            continue
        if deja:
            # on retire les éléments générés de cette source (jamais la source elle-même)
            for e in idx["elements"]:
                if e["source"] == deja["num"]:
                    p = travail(args.lot, "elements", e["fichier"])
                    if os.path.exists(p):
                        os.remove(p)
            idx["elements"] = [e for e in idx["elements"] if e["source"] != deja["num"]]
            idx["sources"].remove(deja)
            num = deja["num"]
        else:
            num = max([s["num"] for s in idx["sources"]] + [0]) + 1
        if os.path.splitext(f)[1].lower() in VIDEO_EXT:
            src, els = traiter_video(f, num, args.lot, args)
        else:
            src, els = traiter_image(f, num, args.lot)
        idx["sources"].append(src)
        idx["elements"] += els
        idx["sources"].sort(key=lambda s: s["num"])
        sauver_index(args.lot, idx)
        ecrire_sources_md(args.lot, idx)
    print(f"Index : {travail(args.lot, 'index.json')} ({len(idx['elements'])} éléments)")


if __name__ == "__main__":
    main()
