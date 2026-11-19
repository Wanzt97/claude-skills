#!/usr/bin/env python3
"""Vitrine Claude Design d'un guide : une planche par lettre (A à I), avec les règles
du guide et les images gardées de chaque sous-catégorie, au format du canevas Design.

1. python3 vitrine.py preparer --lot LOT [--lot LOT2 ...] --racine RACINE [--max 6]
     -> RACINE/images/*.jpg (réduites ; image du milieu pour un extrait mp4) + RACINE/images.json
2. Claude crée le canevas (type Design), téléverse RACINE/images/*.jpg en assets et écrit
   RACINE/blobs.json  {"<nom>.jpg": "/_blob/<id>", ...}
3. python3 vitrine.py ecrire --racine RACINE --guide REGLES.md --titre "Guide visuel — X"
     (REGLES.md = le SKILL.md du guide écrit, ou le fichier des règles proposées avant
      validation : sections « ## A — … » ou « ### A — … » avec des puces)
     -> RACINE/project/canvas.json + RACINE/project/<lettre>-*.dc.html (+ Main.dc.html)
   puis Claude publie project/canvas.json et les planches (publish_files, une par une).
"""
import argparse
import datetime
import html
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import ARBO, FAVORI, VIDEO_EXT, format_de, sonde  # noqa: E402

PLANCHES = {
    "A": ("A-sous-titres", "Sous-titres et typographie"),
    "B": ("B-accroche", "L'accroche"),
    "C": ("C-types-de-scene", "Les 4 types de scène"),
    "D": ("D-animations", "Les 4 types d'animation"),
    "E": ("E-fonds", "Fonds"),
    "F": ("F-composition", "Principes de composition"),
    "G": ("G-design", "Principes de design"),
    "H": ("H-animations-parole", "Animations pendant que je parle"),
    "I": ("I-inspiration", "Tableau d'inspiration général"),
}
NOMS = {
    "A": "Références", "B1": "B1 · Intervenant toujours à l'écran", "B2": "B2 · Sous-titres dans la moitié basse",
    "B3": "B3 · Le mot qui donne envie de rester", "C1": "C1 · Sous-titres seuls",
    "C2": "C2 · Sous-titres + petite animation en bas", "C3": "C3 · Écran partagé",
    "C4": "C4 · Animation plein écran", "D1.texte": "D1 · Texte seul", "D1.objet": "D1 · Texte + objet",
    "D1.graphique": "D1 · Texte + graphique", "D2.centre": "D2 · Personne au centre",
    "D2.cote": "D2 · Personne sur le côté", "D3.texte": "D3 · Objet au milieu + texte",
    "D3.graphique": "D3 · Objet au milieu + graphique", "D4": "D4 · Charts, interfaces (UI)",
    "E1": "E1 · Grappes de carrés vers les bords", "E2": "E2 · Grille gommée autour du sujet",
    "E3": "E3 · Grille gommée d'ambiance", "F1": "F1 · Fond", "F2": "F2 · Point focal",
    "F3": "F3 · Éléments de soutien", "F4": "F4 · Éléments de profondeur", "G1": "G1 · Couleur",
    "G2": "G2 · Polices", "G3": "G3 · Textes", "G4": "G4 · Objets (ombres, textures)", "G5": "G5 · Fonds",
    "H": "Références", "IU": "IU · UI", "IG": "IG · Graphiques et data", "IS": "IS · Scènes complètes",
}
W = 2000            # largeur d'une planche
COL_REGLES = 560    # colonne des règles
H_IMG = 300         # hauteur des vignettes
GAP = 12


def base_nom(f):
    b = os.path.basename(f).lstrip("+")
    return b.split("-", 1)[1] if re.match(r"^\d{2}-", b) else b


def preparer(a):
    os.makedirs(os.path.join(a.racine, "images"), exist_ok=True)
    par_code, faits = {}, {}
    for code, chemin in ARBO.items():
        fs = []
        for lot in a.lot:
            d = os.path.join(lot, chemin)
            if os.path.isdir(d):
                fs += [os.path.join(d, f) for f in os.listdir(d)
                       if not f.startswith(".") and os.path.isfile(os.path.join(d, f))]
        fs.sort(key=lambda p: (not os.path.basename(p).startswith(FAVORI), os.path.basename(p).lstrip("+")))
        items = []
        for p in fs[:a.max]:
            b = base_nom(p)
            nom = os.path.splitext(b)[0] + ".jpg"
            if nom not in faits:
                sortie = os.path.join(a.racine, "images", nom)
                cmd = ["ffmpeg", "-v", "error", "-y"]
                if os.path.splitext(p)[1].lower() in VIDEO_EXT:
                    _, _, d = sonde(p)
                    cmd += ["-ss", f"{(d or 0) / 2:.2f}"]
                cmd += ["-i", p, "-frames:v", "1", "-vf",
                        "scale='if(gt(iw,ih),min(960,iw),-2)':'if(gt(iw,ih),-2,min(960,ih))'",
                        "-q:v", "4", sortie]
                subprocess.run(cmd, check=False)
                faits[nom] = os.path.exists(sortie)
            if faits[nom]:
                items.append({"nom": nom, "source": p, "format": format_de(b),
                              "extrait": b.lower().endswith(".mp4"),
                              "favori": os.path.basename(p).startswith(FAVORI)})
        par_code[code] = items
    with open(os.path.join(a.racine, "images.json"), "w", encoding="utf-8") as f:
        json.dump(par_code, f, ensure_ascii=False, indent=1)
    noms = sorted(n for n, ok in faits.items() if ok)
    print(f"{len(noms)} images à téléverser dans {os.path.join(a.racine, 'images')}")


def md_inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"\1", s)
    return s


def regles_par_lettre(guide):
    txt = open(guide, encoding="utf-8").read()
    out, cur = {}, None
    for l in txt.splitlines():
        m = re.match(r"^#{2,3}\s+([A-I])\s+[—–-]", l)
        if m:
            cur = m.group(1)
            out[cur] = []
            continue
        if l.startswith("#"):
            cur = None
            continue
        if cur and re.match(r"^\s*- ", l):
            niveau = 1 if l.startswith("  ") else 0
            out[cur].append((niveau, md_inline(l.strip()[2:])))
    return out


def ratio(fmt):
    m = re.match(r"(\d+)x(\d+)", fmt or "")
    return int(m.group(1)) / int(m.group(2)) if m else 9 / 16


def hauteur_rangee(items, largeur):
    """Hauteur d'une rangée de vignettes qui passe à la ligne dans `largeur`."""
    if not items:
        return 150
    lignes, x = 1, 0
    for it in items:
        w = H_IMG * ratio(it["format"])
        if x and x + w > largeur:
            lignes, x = lignes + 1, 0
        x += w + GAP
    return lignes * (H_IMG + GAP)


CSS = """body{margin:0}
a{color:#3A3A3A}a:hover{color:#111}
mark{background:#FFE58A;color:#1A1A1A;padding:0 10px;border-radius:4px}
.letter{width:52px;height:52px;flex:none;border-radius:12px;background:#1A1A1A;color:#FFF;font-size:26px;font-weight:800;display:flex;align-items:center;justify-content:center}
.rt{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#6B6B67}
.ln{margin:0;font-size:15px;line-height:1.45;color:#2A2A2A;border-bottom:1px solid #E4E4E0;padding-bottom:6px}
.ln2{margin:0 0 0 18px;font-size:14px;line-height:1.45;color:#3A3A38}
.sub{margin:0;font-size:17px;font-weight:800;color:#1A1A1A}
.vide{font-size:13px;color:#6B6B67;border:2px dashed #A3A39E;border-radius:10px;padding:24px 18px;background:#F9F9F8}
.tag{position:absolute;bottom:8px;left:8px;background:#1A1A1A;color:#FFF;font-size:11px;font-weight:700;padding:3px 7px;border-radius:5px}
.fav{position:absolute;top:8px;left:8px;background:#2E9E5B;color:#FFF;font-size:11px;font-weight:700;padding:3px 7px;border-radius:5px}
"""


def planche(lettre, titre, regles, codes, images, blobs, sous_titre):
    largeur_imgs = W - 96 - COL_REGLES - 40
    rangs, h = [], 48 + 52 + 40
    for code in codes:
        items = images.get(code, [])
        rh = hauteur_rangee(items, largeur_imgs)
        h += 40 + rh + 32
        vignettes = []
        for it in items:
            w = round(H_IMG * ratio(it["format"]))
            url = blobs.get(it["nom"])
            if not url:
                vignettes.append(f'<div class="vide" style="width: {w}px; height: {H_IMG}px; box-sizing: border-box">'
                                 f'{html.escape(it["nom"])}</div>')
                continue
            badges = ('<span class="fav">++</span>' if it["favori"] else "") + \
                     f'<span class="tag">{it["format"].replace("x", ":")}{" · extrait" if it["extrait"] else ""}</span>'
            vignettes.append(
                f'<div style="position: relative; width: {w}px; height: {H_IMG}px; flex: none">'
                f'<img src="{url}" alt="{html.escape(it["nom"])}" style="width: {w}px; height: {H_IMG}px; '
                f'object-fit: cover; border-radius: 10px; display: block">{badges}</div>')
        corps = "".join(vignettes) or '<div class="vide">Aucun exemple gardé</div>'
        rangs.append(f'<div style="display: flex; flex-direction: column; gap: 12px">'
                     f'<p class="sub">{html.escape(NOMS.get(code, code))} '
                     f'<span style="font-weight: 500; color: #6B6B67">({len(items)})</span></p>'
                     f'<div style="display: flex; flex-wrap: wrap; gap: {GAP}px">{corps}</div></div>')
    lignes = "".join((f'<p class="ln2">{t}</p>' if n else f'<p class="ln">{t}</p>') for n, t in regles) \
        or '<p class="ln">Pas encore de règle.</p>'
    h_regles = 48 + 52 + 40 + 90 + sum(30 * (1 + len(re.sub(r"<[^>]+>", "", t)) // 58) + 8 for _, t in regles)
    h = max(h, h_regles) + 48
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{lettre} — {html.escape(titre)}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<style>
{CSS}</style>
</helmet>
<div style="width: {W}px; height: {h}px; box-sizing: border-box; padding: 48px; background: #F2F2F0; font-family: 'Inter', system-ui, sans-serif; color: #1A1A1A; display: flex; flex-direction: column; gap: 32px">
<header style="display: flex; flex-direction: column; gap: 10px">
<div style="display: flex; align-items: center; gap: 16px"><span class="letter">{lettre}</span><h2 style="margin: 0; font-size: 36px; font-weight: 800; letter-spacing: -0.02em"><mark>{html.escape(titre)}</mark></h2></div>
<p style="margin: 0; font-style: italic; font-size: 17px; color: #555552">{html.escape(sous_titre)}</p>
</header>
<div style="display: grid; grid-template-columns: {COL_REGLES}px minmax(0, 1fr); gap: 40px; align-items: start">
<div style="background: #FFF; border: 1px solid #D6D6D2; border-radius: 10px; padding: 18px 20px; display: flex; flex-direction: column; gap: 8px">
<span class="rt">Règles compilées</span>
{lignes}
</div>
<div style="display: flex; flex-direction: column; gap: 32px">
{"".join(rangs)}
</div>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{W},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
"""
    return doc, h


def couverture(titre, sous_titre, lots, comptes):
    lignes = "".join(f'<p class="ln">{html.escape(l)}</p>' for l in lots)
    cases = "".join(
        f'<div style="background: #FFF; border: 1px solid #D6D6D2; border-radius: 10px; padding: 16px 18px; '
        f'display: flex; flex-direction: column; gap: 6px"><span class="letter">{k}</span>'
        f'<p class="sub">{html.escape(PLANCHES[k][1])}</p><p class="ln2" style="margin: 0">{v} images</p></div>'
        for k, v in comptes.items())
    h = 760
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{html.escape(titre)}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<style>
{CSS}</style>
</helmet>
<div style="width: {W}px; height: {h}px; box-sizing: border-box; padding: 64px; background: #F2F2F0; font-family: 'Inter', system-ui, sans-serif; color: #1A1A1A; display: flex; flex-direction: column; gap: 28px">
<h1 style="margin: 0; font-size: 64px; font-weight: 800; letter-spacing: -0.03em"><mark>{html.escape(titre)}</mark></h1>
<p style="margin: 0; font-size: 20px; color: #555552">{html.escape(sous_titre)}</p>
<div style="display: flex; flex-direction: column; gap: 6px; max-width: 1400px"><span class="rt">Sources</span>{lignes}</div>
<div style="display: grid; grid-template-columns: repeat(9, minmax(0, 1fr)); gap: 14px">{cases}</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{W},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
"""
    return doc, h


def ecrire(a):
    images = json.load(open(os.path.join(a.racine, "images.json"), encoding="utf-8"))
    p_blobs = os.path.join(a.racine, "blobs.json")
    blobs = json.load(open(p_blobs, encoding="utf-8")) if os.path.exists(p_blobs) else {}
    regles = regles_par_lettre(a.guide)
    proj = os.path.join(a.racine, "project")
    os.makedirs(proj, exist_ok=True)
    boards, order, comptes = {}, [], {}
    doc, h = couverture(a.titre, a.sous_titre or "", a.source or [],
                        {k: sum(len(images.get(c, [])) for c in ARBO if c[0] == k) for k in PLANCHES})
    open(os.path.join(proj, "Main.dc.html"), "w", encoding="utf-8").write(doc)
    boards["Main.dc.html"] = {"x": 0, "y": 0, "w": W, "h": h, "title": "Couverture"}
    order.append("Main.dc.html")
    y_rang, x, h_max, col = h + 120, 0, 0, 0
    for lettre, (stem, titre) in PLANCHES.items():
        codes = [c for c in ARBO if c[0] == lettre]
        doc, hp = planche(lettre, titre, regles.get(lettre, []), codes, images, blobs,
                          "Règles compilées depuis le tri ; images gardées, favoris (++) en premier.")
        nom = f"{stem}.dc.html"
        open(os.path.join(proj, nom), "w", encoding="utf-8").write(doc)
        boards[nom] = {"x": x, "y": y_rang, "w": W, "h": hp, "title": f"{lettre} — {titre}"}
        order.append(nom)
        h_max = max(h_max, hp)
        col += 1
        x += W + 80
        if col == 3:
            y_rang, x, h_max, col = y_rang + h_max + 120, 0, 0, 0
    canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": datetime.datetime.now(datetime.timezone.utc)
                                         .strftime("%Y-%m-%dT%H:%M:%SZ")},
              "title": a.titre, "launch": {"view": "canvas"}, "pages": [], "boards": boards,
              "order": order, "notes": {}, "designSystems": []}
    p_canvas = os.path.join(proj, "canvas.json")
    if os.path.exists(p_canvas):          # garder ce que le canevas avait déjà
        ancien = json.load(open(p_canvas, encoding="utf-8"))
        ancien.update({k: canvas[k] for k in ("boards", "order")})
        canvas = ancien
    json.dump(canvas, open(p_canvas, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    manquants = sorted({it["nom"] for its in images.values() for it in its} - set(blobs))
    print("\n".join(os.path.join(proj, n) for n in order))
    print(p_canvas)
    if manquants:
        print(f"ATTENTION : {len(manquants)} images sans url de blob (cases vides) : {manquants[:5]}…")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("preparer")
    p.add_argument("--lot", required=True, action="append")
    p.add_argument("--racine", required=True)
    p.add_argument("--max", type=int, default=6)
    e = sp.add_parser("ecrire")
    e.add_argument("--racine", required=True)
    e.add_argument("--guide", required=True)
    e.add_argument("--titre", required=True)
    e.add_argument("--sous-titre", dest="sous_titre")
    e.add_argument("--source", action="append", help="une ligne de source pour la couverture")
    a = ap.parse_args()
    preparer(a) if a.cmd == "preparer" else ecrire(a)


if __name__ == "__main__":
    main()
