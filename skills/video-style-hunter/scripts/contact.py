#!/usr/bin/env python3
"""Planches contact numérotées des éléments d'un lot, pour les regarder et les classer.

  python3 contact.py --lot LOT [--source 2] [--colonnes N --lignes N]  (auto : 10x3 en 9:16, 5x6 en 16:9)
  python3 contact.py --sortie PREFIXE fichier1 fichier2 ...

Sortie : LOT/_travail/contact/elements[_sNNN]_01.jpg ... + légende .txt (numéro -> fichier).
Carré orange en haut à droite = extrait vidéo (la case montre son image du milieu).
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import charger_index, planches_contact, travail  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lot")
    ap.add_argument("--source", type=int)
    ap.add_argument("--sortie")
    ap.add_argument("--colonnes", type=int)
    ap.add_argument("--lignes", type=int)
    ap.add_argument("fichiers", nargs="*")
    a = ap.parse_args()
    if a.lot:
        idx = charger_index(a.lot)
        els = [e for e in idx["elements"] if a.source in (None, e["source"])]
        els.sort(key=lambda e: (e["source"], e["t"]))
        fichiers = [travail(a.lot, "elements", e["fichier"]) for e in els]
        prefixe = a.sortie or travail(a.lot, "contact", "elements" + (f"_s{a.source:03d}" if a.source else ""))
    else:
        fichiers, prefixe = a.fichiers, a.sortie
    for p in planches_contact(fichiers, prefixe, a.colonnes, a.lignes):
        print(p)
    print(prefixe + ".txt")


if __name__ == "__main__":
    main()
