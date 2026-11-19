#!/usr/bin/env python3
"""Écrit references/emplacements.md d'une skill de guide visuel : pour chaque code,
les favoris (++) puis les meilleurs gardés (ordre des rangs), chemins absolus.

  python3 emplacements.py --lot LOT [--lot LOT2 ...] --sortie CHEMIN.md [--max 6]
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import ARBO, FAVORI, format_de  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lot", required=True, action="append")
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--max", type=int, default=6)
    a = ap.parse_args()
    md = ["# Emplacements → images de référence", "",
          "Pour chaque code : favoris (++) d'abord, puis les meilleurs gardés. Les extraits .mp4 gardent le mouvement : "
          "regarde-les (image du milieu avec ffmpeg) quand la règle porte sur une animation.", ""]
    for code, chemin in ARBO.items():
        fs = []
        for lot in a.lot:
            d = os.path.join(lot, chemin)
            if os.path.isdir(d):
                fs += [os.path.join(d, f) for f in os.listdir(d)
                       if not f.startswith(".") and os.path.isfile(os.path.join(d, f))]
        fs.sort(key=lambda p: (not os.path.basename(p).startswith(FAVORI), os.path.basename(p).lstrip("+")))
        md.append(f"## {code} · {chemin}")
        if not fs:
            md.append("- (aucun exemple)")
        for p in fs[:a.max]:
            md.append(f"- `{p}` ({format_de(os.path.basename(p))})")
        md.append("")
    os.makedirs(os.path.dirname(os.path.abspath(a.sortie)), exist_ok=True)
    with open(a.sortie, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(a.sortie)


if __name__ == "__main__":
    main()
