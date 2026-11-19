# Exemple : les générateurs du pilote « Digital Black Edit Style »

Copies des scripts qui ont produit l'atelier et le design system de Digital Black (novembre 2026). Ce sont des **modèles à lire**, pas des outils prêts à lancer : les identifiants `/_blob/…`, les couleurs, les polices et les textes sont ceux de Digital Black, et les chemins d'entrée (`sel.json`, `uploads.txt`, `favoris.json`) n'existent plus.

- Atelier en ligne : https://claude.ai/artifact/6PzwSbydxjPnuC5QdKWTkA
- Design system en ligne : https://claude.ai/artifact/3mrM6RcBNRoQGu4fgDfw9B
- Sources du brand kit HyperFrames : `wanzt-style-montage-skills/montage-digital-black/brand-kit-hyperframes-v2/`

## atelier/

| Fichier | Ce qu'il fait |
|---|---|
| `moodboard-C.py`, `gen-atelier.py` | Pages de moodboard : images en grille, pastilles `++`, refusés encadrés, légendes |
| `compC.py`, `compC2.py` | Composants des types de scène (C2 contient les aides partagées : `Anim`, aperçus 9:16 et 16:9, rangées) |
| `compD.py` | Types d'animation (texte, personne, objet, graphique), 9:16 et 16:9 |
| `compB.py`, `compH.py`, `compF.py` | Accroche, animations pendant que je parle, composition |
| `genI.py`, `rassembler.py` | Planche I : bibliothèque des favoris, rassemblés depuis les autres planches |

## design-system/

| Fichier | Ce qu'il fait |
|---|---|
| `gen3.py` | Écrit tout le design system (jetons, composants, README) ; exécute les fichiers ci-dessous |
| `planche_c.py`, `planche_suite.py` | CSS et composants des planches C, D, H, B, F, avec leurs jetons |
| `marque.py` | Logo (texte) et bouton S'abonner |
| `guide.py` | Les deux sections de guide et la carte d'exemple GuideVisuel |
| `01-guide-utilisation.md`, `02-guide-son.md` | Les deux guides, tels que publiés |
| `readme3.md` | Le README du design system |
| `build3.sh` | Construit le dossier de test local (jetons en CSS, aperçus, images) |

## labos/ (8 novembre 2026)

| Fichier | Ce qu'il fait |
|---|---|
| `gen-banque-et-animations.py` | La banque de sons (écoute, sélection à copier) et les premières planches d'animation avec sons ; contient le moteur audio (`MOTEUR`) et l'enveloppe des planches (`doc()`) que les autres réutilisent |
| `gen_polices.py` | Les 5 combinaisons de polices sur le vrai plan |
| `gen_labo.py` | Le Labo du sous-titre : croquis, 4 variantes, sons, sortie, 9:16 / 16:9, taille selon le plan, place à côté de la tête ou derrière, contrôles, recette à copier |
| `gen_textes.py` | Le Labo des textes : titre d'accroche, mot géant, scène texte, étiquettes et chiffres, logo |
| `mini-dc.js`, `chk.js` | Le rendu local des planches interactives et la vérification des scripts |
| `mesures-sons.txt` | Crête (dBFS) et sonie momentanée la plus haute (LUFS) des 37 sons du pack, pour la règle « jamais plus fort que la voix » |

## design-system-v2/ (8 novembre 2026, après les labos)

La version du design system qui reprend les recettes des labos. Mêmes fichiers que `design-system/`, plus `croquis_lib.py` (le CSS et les fonctions du croquis : 4 variantes, placement 9:16 et 16:9) et `sous_titre.py` (les composants SousTitreDuo et MotCle). `build4.sh` construit le dossier de test.
