#!/usr/bin/env python3
"""Vidéos YouTube : annoncer ce qui sera téléchargé, puis télécharger avec yt-dlp.

  python3 sources.py info URL [URL...] [--hauteur 1080]
  python3 sources.py telecharger URL --lot LOT [--debut 10:00 --fin 25:00] [--hauteur 1080] [--avec-son]

`info` ne télécharge rien : titre, chaîne, durée, chapitres, format et taille estimée.
`telecharger` écrit la vidéo dans LOT/_travail/sources/<id>.mp4 et un fichier
<id>.mp4.tri.json (titre, chaîne, URL, chapitres, décalage de la plage) que decouper.py lit.
Avec --debut/--fin, seule la plage est téléchargée (coupe exacte, ré-encodée par yt-dlp).
"""
import argparse
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import hms, parse_temps, travail  # noqa: E402


def format_yt(h, son):
    v = f"bv*[height<={h}][vcodec^=avc1]/bv*[height<={h}]"
    return f"{v.split('/')[0]}+ba[ext=m4a]/{v.split('/')[1]}+ba/b[height<={h}]" if son else f"{v}/b[height<={h}]"


def infos(url, h, son):
    out = subprocess.run(["yt-dlp", "-J", "--no-playlist", "--no-warnings", "-f", format_yt(h, son), url],
                         capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"yt-dlp : {out.stderr.strip()[-800:]}")
    return json.loads(out.stdout)


def taille(d):
    fs = d.get("requested_formats") or [d]
    t = sum((f.get("filesize") or f.get("filesize_approx") or 0) for f in fs)
    return t / 1e6


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["info", "telecharger"])
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--lot")
    ap.add_argument("--debut")
    ap.add_argument("--fin")
    ap.add_argument("--hauteur", type=int, default=1080)
    ap.add_argument("--avec-son", action="store_true")
    a = ap.parse_args()
    deb, fin = parse_temps(a.debut), parse_temps(a.fin)

    for url in a.urls:
        d = infos(url, a.hauteur, a.avec_son)
        duree = d.get("duration") or 0
        chap = d.get("chapters") or []
        fmt = "+".join(f.get("format_id", "") for f in (d.get("requested_formats") or [d]))
        mo = taille(d)
        if deb is not None or fin is not None:
            part = ((fin or duree) - (deb or 0)) / duree if duree else 1
            mo *= part
        print(f"- {d.get('title')} — {d.get('channel') or d.get('uploader')}\n"
              f"  {d.get('webpage_url')}\n"
              f"  durée {hms(duree)}, {len(chap)} chapitres, {d.get('width')}x{d.get('height')}, "
              f"format {fmt} ({'avec' if a.avec_son else 'sans'} son), ~{mo:.0f} Mo"
              + (f", plage {hms(deb or 0)}-{hms(fin or duree)}" if (deb or fin) else ""))
        if a.action == "info":
            continue
        if not a.lot:
            sys.exit("--lot obligatoire pour telecharger")
        dossier = travail(a.lot, "sources")
        os.makedirs(dossier, exist_ok=True)
        sortie = os.path.join(dossier, f"{d['id']}.mp4")
        cmd = ["yt-dlp", "--no-playlist", "--no-warnings", "-f", format_yt(a.hauteur, a.avec_son),
               "--merge-output-format", "mp4", "--remux-video", "mp4", "-o", sortie, url]
        if deb is not None or fin is not None:
            cmd[1:1] = ["--download-sections", f"*{deb or 0}-{fin if fin is not None else 'inf'}",
                        "--force-keyframes-at-cuts"]
        subprocess.run(cmd, check=True)
        meta = {"titre": d.get("title"), "chaine": d.get("channel") or d.get("uploader"),
                "url": d.get("webpage_url"), "duree_totale": duree, "decalage": deb or 0,
                "chapitres": [{"debut": c.get("start_time", 0), "fin": c.get("end_time"),
                               "titre": c.get("title", "")} for c in chap]}
        with open(sortie + ".tri.json", "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=1)
        print(f"  -> {sortie}")


if __name__ == "__main__":
    main()
