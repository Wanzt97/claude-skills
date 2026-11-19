#!/usr/bin/env python3
"""Copie les éléments dans l'arborescence du canevas d'après LOT/_travail/classement.tsv.

classement.tsv (une ligne par élément, # = commentaire) :
  fichier<TAB>codes<TAB>note<TAB>commentaire
  012_chaine_t734.5_16x9.jpg	C3,D4,IU	4	split UI à gauche
codes : voir `python3 classer.py --codes`. note 1-5 (5 = meilleur), sert à l'ordre et au plafond.

  python3 classer.py --lot LOT [--plafond 40] [--essai]

Chaque copie est préfixée de son rang dans le dossier (01-, 02-...). Un `_rejete/` est créé
dans chaque dossier final. Rien n'est supprimé ni écrasé : relancer ne fait qu'ajouter.
"""
import argparse
import os
import shutil
import sys
from collections import OrderedDict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import ARBO, REJET, charger_index, planche, travail  # noqa: E402


def lire_tsv(chemin):
    lignes = []
    with open(chemin, encoding="utf-8") as f:
        for n, l in enumerate(f, 1):
            l = l.rstrip("\n")
            if not l.strip() or l.lstrip().startswith("#"):
                continue
            p = l.split("\t")
            if p[0] == "fichier":
                continue
            codes = [c.strip() for c in (p[1] if len(p) > 1 else "").split(",") if c.strip()]
            inconnus = [c for c in codes if c not in ARBO]
            if inconnus:
                sys.exit(f"ligne {n} : code(s) inconnu(s) {inconnus}")
            note = float(p[2]) if len(p) > 2 and p[2].strip() else 3
            lignes.append({"fichier": p[0].strip(), "codes": codes, "note": note,
                           "com": p[3] if len(p) > 3 else ""})
    return lignes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lot")
    ap.add_argument("--plafond", type=int, default=40, help="éléments max par planche")
    ap.add_argument("--essai", action="store_true", help="affiche sans copier")
    ap.add_argument("--codes", action="store_true")
    a = ap.parse_args()
    if a.codes or not a.lot:
        for c, p in ARBO.items():
            print(f"{c:14s} {p}")
        return
    idx = charger_index(a.lot)
    t_par_fichier = {e["fichier"]: (e["source"], e["t"]) for e in idx["elements"]}
    lignes = lire_tsv(travail(a.lot, "classement.tsv"))
    for d in ARBO.values():
        if not a.essai:
            os.makedirs(os.path.join(a.lot, d, REJET), exist_ok=True)

    par_code = OrderedDict((c, []) for c in ARBO)
    for l in lignes:
        if not os.path.exists(travail(a.lot, "elements", l["fichier"])):
            print(f"absent, ignoré : {l['fichier']}")
            continue
        for c in l["codes"]:
            par_code[c].append(l)
    for c in par_code:
        par_code[c].sort(key=lambda l: (-l["note"], t_par_fichier.get(l["fichier"], (0, 0))))

    # plafond par planche, réparti entre ses sous-dossiers à tour de rôle (meilleurs d'abord)
    gardes = {c: [] for c in ARBO}
    planches = OrderedDict()
    for c in ARBO:
        planches.setdefault(planche(c), []).append(c)
    ecartes = 0
    for pl, codes in planches.items():
        total, rang = 0, 0
        while total < a.plafond and any(rang < len(par_code[c]) for c in codes):
            for c in codes:
                if rang < len(par_code[c]) and total < a.plafond:
                    gardes[c].append(par_code[c][rang])
                    total += 1
            rang += 1
        ecartes += sum(len(par_code[c]) for c in codes) - total

    copies = 0
    for c, ls in gardes.items():
        d = os.path.join(a.lot, ARBO[c])
        existants = [f for f in os.listdir(d) if not f.startswith(".")] if os.path.isdir(d) else []
        deja = {f.lstrip("+").split("-", 1)[-1] for f in existants}
        if os.path.isdir(os.path.join(d, REJET)):
            deja |= {f.lstrip("+").split("-", 1)[-1] for f in os.listdir(os.path.join(d, REJET))}
        rang = len([f for f in existants if f != REJET])
        for l in ls:
            if l["fichier"] in deja:
                continue
            rang += 1
            dest = os.path.join(d, f"{rang:02d}-{l['fichier']}")
            if a.essai:
                print(f"{c:14s} {os.path.basename(dest)}")
            else:
                shutil.copy2(travail(a.lot, "elements", l["fichier"]), dest)
            copies += 1
    print(f"{copies} copies {'prévues' if a.essai else 'faites'} ; {ecartes} écartées par le plafond "
          f"de {a.plafond} par planche.")


if __name__ == "__main__":
    main()
