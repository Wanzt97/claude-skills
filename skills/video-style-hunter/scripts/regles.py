#!/usr/bin/env python3
"""Prépare la compilation des règles après le tri de Wanzt dans le Finder.

  python3 regles.py --lot LOT [--lot LOT2 ...] [--sortie DOSSIER]

Plusieurs --lot : les dossiers de même code sont fusionnés (utile pour croiser 9:16 et 16:9).

Pour chaque dossier final : liste de ce qui est gardé (favoris ++ en premier) et refusé
(_rejete/), formats présents, planches contact numérotées gardés / refusés.
Sortie (par défaut dans le premier lot) : LOT/_travail/regles/dossier.md + <code>-gardes_01.jpg, <code>-rejetes_01.jpg
(carré vert = favori ++, orange = extrait vidéo).
"""
import argparse
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import ARBO, FAVORI, REJET, format_de, planches_contact, travail  # noqa: E402


def fichiers(d):
    if not os.path.isdir(d):
        return []
    return sorted(os.path.join(d, f) for f in os.listdir(d)
                  if not f.startswith(".") and os.path.isfile(os.path.join(d, f)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lot", required=True, action="append")
    ap.add_argument("--sortie")
    a = ap.parse_args()
    sortie = a.sortie or travail(a.lot[0], "regles")
    os.makedirs(sortie, exist_ok=True)
    md = ["# Dossier de compilation des règles", "", "Lots : " + ", ".join(f"`{l}`" for l in a.lot), "",
          "Pour chaque dossier : regarder les planches gardés puis refusés, écrire les règles "
          "(rôles, pas de valeurs), et une règle par format quand elle en dépend.", ""]
    for code, chemin in ARBO.items():
        g, r = [], []
        for lot in a.lot:
            d = os.path.join(lot, chemin)
            g += fichiers(d)
            r += fichiers(os.path.join(d, REJET))
        g.sort(key=lambda f: (not os.path.basename(f).startswith(FAVORI), os.path.basename(f).lstrip("+")))
        fav = [f for f in g if os.path.basename(f).startswith(FAVORI)]
        fm = Counter(format_de(os.path.basename(f)) for f in g)
        md.append(f"## {code} — {chemin}")
        md.append(f"Gardés {len(g)} (dont {len(fav)} favoris), refusés {len(r)}. "
                  f"Formats gardés : {', '.join(f'{k} ×{v}' for k, v in fm.most_common()) or 'aucun'}.")
        safe = code.replace(".", "-")
        marques = {f: (40, 200, 90) for f in fav}
        if g:
            pl = planches_contact(g, os.path.join(sortie, f"{safe}-gardes"), marques=marques)
            md.append("Planches gardés : " + ", ".join(f"`{os.path.basename(p)}`" for p in pl))
        if r:
            pl = planches_contact(r, os.path.join(sortie, f"{safe}-rejetes"))
            md.append("Planches refusés : " + ", ".join(f"`{os.path.basename(p)}`" for p in pl))
        md += ["", "- Règles (d'après les gardés) :", "- À éviter (d'après les refus) :", ""]
        print(f"{code:14s} gardés {len(g):3d}  favoris {len(fav):2d}  refusés {len(r):3d}")
    with open(os.path.join(sortie, "dossier.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    print(os.path.join(sortie, "dossier.md"))


if __name__ == "__main__":
    main()
