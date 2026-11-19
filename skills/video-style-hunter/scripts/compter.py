#!/usr/bin/env python3
"""Tableau du nombre d'éléments par planche et sous-dossier, avec la part 9:16 / 16:9.

  python3 compter.py --lot LOT        (écrit aussi LOT/_comptage.md)
"""
import argparse
import os
import sys
from collections import OrderedDict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commun import ARBO, FAVORI, REJET, format_de, planche  # noqa: E402


def fichiers(d):
    if not os.path.isdir(d):
        return []
    return [f for f in os.listdir(d) if not f.startswith(".") and os.path.isfile(os.path.join(d, f))]


def compter(lot):
    lignes = OrderedDict()
    for c, p in ARBO.items():
        d = os.path.join(lot, p)
        g = fichiers(d)
        r = fichiers(os.path.join(d, REJET))
        lignes[c] = {"chemin": p, "total": len(g),
                     "9x16": sum(format_de(f) == "9x16" for f in g),
                     "16x9": sum(format_de(f) == "16x9" for f in g),
                     "extraits": sum(f.lower().endswith(".mp4") for f in g),
                     "favoris": sum(f.startswith(FAVORI) for f in g), "rejetes": len(r)}
    return lignes


def tableau(lignes):
    cols = ["total", "9x16", "16x9", "extraits", "favoris", "rejetes"]
    out = ["| Planche / sous-dossier | Éléments | 9:16 | 16:9 | autres | dont extraits mp4 | ++ | _rejete |",
           "|---|--:|--:|--:|--:|--:|--:|--:|"]
    par_pl = OrderedDict()
    for c, l in lignes.items():
        par_pl.setdefault(planche(c), []).append((c, l))
    tot = {k: 0 for k in cols}
    for pl, ls in par_pl.items():
        s = {k: sum(l[k] for _, l in ls) for k in cols}
        for k in cols:
            tot[k] += s[k]
        autres = s["total"] - s["9x16"] - s["16x9"]
        out.append(f"| **{pl}** | **{s['total']}** | **{s['9x16']}** | **{s['16x9']}** | **{autres}** | "
                   f"**{s['extraits']}** | **{s['favoris']}** | **{s['rejetes']}** |")
        if len(ls) > 1:
            for c, l in ls:
                nom = l["chemin"].split("/", 1)[1]
                autres = l["total"] - l["9x16"] - l["16x9"]
                out.append(f"| &nbsp;&nbsp;{nom} | {l['total']} | {l['9x16']} | {l['16x9']} | {autres} | "
                           f"{l['extraits']} | {l['favoris']} | {l['rejetes']} |")
    autres = tot["total"] - tot["9x16"] - tot["16x9"]
    out.append(f"| **Total (copies)** | **{tot['total']}** | **{tot['9x16']}** | **{tot['16x9']}** | "
               f"**{autres}** | **{tot['extraits']}** | **{tot['favoris']}** | **{tot['rejetes']}** |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lot", required=True)
    a = ap.parse_args()
    t = tableau(compter(a.lot))
    with open(os.path.join(a.lot, "_comptage.md"), "w", encoding="utf-8") as f:
        f.write("# Comptage du tri\n\n" + t + "\n")
    print(t)


if __name__ == "__main__":
    main()
