# ---------------- SousTitreDuo + MotCle (croquis du 8 novembre 2026) ----------------
BOUCLE52 = BOUCLE.replace('3600', '5200')
v1, _ = bloc_croquis('v1', 'Ton montage', '1 heure', 'par vidéo')
v2, _ = bloc_croquis('v2', 'Et la première', 'coûte', 'très cher')
v3, _ = bloc_croquis('v3', 'Garde le', 'contrôle', 'sur ton rythme')
v4, _ = bloc_croquis('v4', 'Le secret', 'simple', 'le rythme', dessus=True, dx=200, dy=150)
h_g, _ = bloc_croquis('v2', 'Et la première', 'coûte', 'très cher', fmt='169', place='gauche', y=500, tete_g=760, dessus=True)
h_d, _ = bloc_croquis('v4', 'Le secret', 'simple', 'le rythme', fmt='169', place='droite', y=480, tete_d=950, dessus=True, dx=-560, dy=330)
h_b, _ = bloc_croquis('v1', 'Ton montage', '1 heure', 'par vidéo', fmt='169', place='derriere', y=470)
h_b = h_b + f'<img class="ms-detour-169" src="{D169}" alt="" aria-hidden="true">'
prev = f'''<!-- @dsCard group="Sous-titres" height=1000 width=1320 subtitle="Le croquis : amorce Arial à gauche, mot clé Anton braise, mot de fin Inter dessous à droite · rangée 1 : 9:16 V1 à V4 · rangée 2 : 16:9 à gauche de la tête, à droite, derrière toi" -->
<!doctype html>
<html lang="fr"><head><meta charset="utf-8">{PREV_CSS}</head>
<body><div class="rang">{ap('916',v1,'9:16 · V1 · Sélection',zone=Z916)}{ap('916',v2,'9:16 · V2 · Punch',zone=Z916)}{ap('916',v3,'9:16 · V3 · Machine à écrire',zone=Z916)}{ap('916',v4,'9:16 · V4 · Sélection agrandie',zone=Z916)}</div><div class="rang">{ap('169',h_g,'16:9 · V2 · À gauche de la tête',sc=0.2,zone=Z169)}{ap('169',h_d,'16:9 · V4 · À droite de la tête',sc=0.2,zone=Z169)}{ap('169',h_b,'16:9 · V1 · Derrière toi',sc=0.2)}</div>{BOUCLE52}</body></html>
'''
w('components/SousTitreDuo/preview.html', prev)
w('components/SousTitreDuo/README.md', '''# SousTitreDuo — le croquis

Le sous-titre du style, réglé avec Wanzt dans le **Labo du sous-titre** de l’atelier (8 novembre 2026). Trois polices qui contrastent en taille et en caractère, toujours dans la même composition, le « croquis » :

- **Amorce** `.ms-amorce` : Arial 400 (Arimo en secours, mêmes dimensions), `amorce-916` 54 px / `amorce-169` 45 px, os, halo sombre. Une capitale puis des minuscules. **4 mots au plus.**
- **Mot clé** `.ms-motcle` dans `.ms-cle` : Anton, `motcle-916` 180 px / `motcle-169` 150 px, **braise**, halo sombre. Une capitale puis des minuscules. **1 ou 2 mots.**
- **Mot de fin** `.ms-fin` : Inter 400, `fin-916` 54 px / `fin-169` 45 px, os, minuscules. **3 mots au plus.** Facultatif.

**Ce que tu fournis :** la transcription mot à mot (avec les temps), découpée en blocs ; pour chaque bloc l’amorce, le mot clé et le mot de fin ; la variante ; le plan (gros, rapproché, moyen, large) ; en 16:9, la place (à gauche ou à droite de la tête, ou derrière toi) et la position de la tête.

## La composition
`.ms-croquis` (grille) : l’amorce à gauche du mot clé, à mi-hauteur ; le mot clé ; le mot de fin sous le mot clé, calé sur son bord droit. Écart `ecart-croquis` (10 px).

- **Mot clé trop long :** s’il ne tient pas à côté de l’amorce, l’amorce passe **au-dessus**, calée à gauche (`.ms-croquis--dessus`). S’il ne tient toujours pas, il descend jusqu’à `motcle-min` (140 px en 9:16, 117 px en 16:9). Au-delà, on change de mot.
- Largeur utile : 920 px en 9:16 ; en 16:9, la place libre à côté de la tête (voir Placement).

## Les 4 variantes, à alterner
Même croquis, mêmes polices, mêmes couleurs : seule l’animation change. Règle d’alternance : **V2 par défaut**, V1 pour le mot le plus fort de chaque partie, V3 pour une phrase calme ou technique, V4 pour poser un mot qui mérite un temps fort ; **jamais deux fois la même de suite**. V1 et V4 ont besoin d’environ 2 s après le mot clé : seulement si la phrase continue après lui, sinon V2.

| Variante | Classe | Ce qui se passe (temps depuis le mot clé `--t`) | Sons (`data-volume` sur le fichier d’origine) |
|---|---|---|---|
| **V1 · Sélection** | `.ms-v1` | amorce mot par mot ; le mot clé arrive en **os** ; le cadre braise se trace (+450 ms, `dur-cadre`), les 4 poignées (+750 ms), le curseur arrive (+850 ms) et clique (+1 300 ms, `v1-clic`) : le mot passe en **noir sur fond braise** ; le mot de fin suit (+1 550 ms). Le cadre reste. | amorce et fin : Short Shutter Click 0,30 · cadre : Gear Turn Click 0,40 (0,3 s) · clic : Mouse Click 0,60 |
| **V2 · Punch** | `.ms-v2` | amorce mot par mot ; le mot clé tombe en braise, trop grand (×1,7) puis à sa taille (`dur-punch` 420 ms) ; le mot de fin (+450 ms). Sans cadre. | amorce et fin : Short Shutter Click 0,30 · mot clé : Mouse Click 0,45 |
| **V3 · Machine à écrire** | `.ms-v3` | amorce, mot clé puis mot de fin s’écrivent lettre par lettre (`.ms-frappe`, `dur-frappe` 55 ms, chaque lettre a son `--t`). Sans cadre. | chaque lettre de l’amorce et de la fin : Gear Single Click 0,25 · mot clé : Camera Shutter 0,35 |
| **V4 · Sélection agrandie** | `.ms-v4` + `.ms-agrandie` | tout le croquis arrive **petit (40 %)**, décalé de `--dx` / `--dy` ; un cadre braise et 4 poignées le sélectionnent (`--cadre`), le curseur clique (`--clic`), puis le tire et l’agrandit jusqu’à sa place (`--drag`, `dur-agrandie` 700 ms). Au lâcher (`--lache`), le cadre s’efface et le mot clé passe de l’os à la braise. En 16:9, il part du bas au centre et finit à côté de la tête. | amorce et fin : Short Shutter Click 0,30 · cadre : Gear Turn Click 0,40 · clic : Mouse Click 0,60 · posé : Camera Shutter 0,35 |

Volumes mesurés le 8 novembre : tous restent au moins 6 LU sous ta voix (voir **SFX for Digital B**, règle d’or).

## Placement
| Plan | 9:16 (`.ms-bloc--916`) | Taille (`--ech`) 9:16 / 16:9 |
|---|---|---|
| Gros plan (visage) | au-dessus de la tête : `.ms-bloc--haut`, `--haut: 250px` | `ech-gros` 0,8 / 0,8 |
| Plan rapproché (poitrine) | sous le menton, bas du bloc à 360 px du bas : `--bas: 1560px` (`bloc-916-bas`) | `ech-rapproche` 1 / 1 |
| Plan moyen (taille) | `--bas: 1540px` | `ech-moyen` 1,05 / 1 |
| Plan large (en pied) | `--bas: 1520px` | `ech-large` 1,08 / 1 |

- **9:16** : rien sous y 1560 (`zone-shorts`, l’interface des Shorts) ; rien sur le visage.
- **16:9 — règle de Wanzt** : tout texte posé sur toi va **à gauche ou à droite de ta tête, ou derrière toi**. Jamais sur le visage, jamais en bas au centre. Classes `.ms-bloc--169 .ms-bloc--cote` + `.ms-bloc--gauche` (`--tete-g` = x du bord gauche de ta tête) ou `.ms-bloc--droite` (`--tete-d` = x du bord droit) ; `--y` = hauteur du centre du bloc (à hauteur du visage par défaut). Écart `tete-ecart` (50 px) entre ta tête et le texte, marge `col-169-marge` (100 px). Derrière toi : `.ms-bloc--derriere` puis ton détourage `<img class="ms-detour-169">` par-dessus, avec le même cadrage. Rien dans les 100 px du bas (`zone-youtube`).
- La taille et la place se recalent sur chaque vraie vidéo : la position de la tête change avec le cadrage.

## Mouvement
| Élément | Entrée | Sortie |
|---|---|---|
| Mot de l’amorce ou de la fin `.ms-mot` | à l’instant où il est dit (`--t`) : fondu + flou `flou-mot` + 10 px de montée, `dur-mot` (350 ms), `ease-out` | avec le bloc |
| Mot clé | selon la variante (tableau ci-dessus) | avec le bloc |
| Bloc `.ms-bloc` | — | tout d’un coup, `tenue` (1 s) après le dernier mot, ou plus tôt si la phrase suivante commence (`.ms-sortie` + `--sortie`) : flou rapide, `dur-sortie` (300 ms), `ease-in` |

## À ne pas faire
Plaque ou pastille derrière le texte (sauf le fond braise du clic en V1), surlignage, mot clé dans la police de l’amorce, plus de 4 mots d’amorce, majuscules forcées, serif ou script, ombre colorée ou décalée, texte sur le visage, en 16:9 un texte en bas au centre, deux fois la même variante de suite.
''')

prev = f'''<!-- @dsCard group="Sous-titres" height=420 width=1200 subtitle="Anton braise, une capitale puis des minuscules" -->
<!doctype html>
<html lang="fr"><head><meta charset="utf-8">{PREV_CSS}
<style>.case{{flex:1;background:var(--noir-digital);border:2px solid var(--acier);border-radius:6px;padding:28px;display:flex;flex-direction:column;gap:18px;min-height:300px;box-sizing:border-box}}
.case p{{margin:0;font-size:16px;line-height:1.45;color:var(--brume)}}
.case .ms-motcle{{font-size:110px}}</style></head>
<body><div class="rang">
<section class="case"><span class="leg">Braise · le croquis (V2, V3)</span><span class="ms-motcle">1 Heure</span><p>Anton, une capitale puis des minuscules. 180 px en 9:16, 150 px en 16:9.</p></section>
<section class="case"><span class="leg">V1 · noir sur braise au clic</span><span class="ms-motcle" style="color:var(--abysse);background:var(--braise);padding:4px 18px;align-self:flex-start;text-shadow:none">Contrôle</span><p>Le mot arrive en os, le cadre se trace, le curseur clique : noir sur fond braise.</p></section>
<section class="case"><span class="leg">Interdit</span><span class="ms-amorce" style="font-size:52px">le <span style="color:var(--braise)">tunnel</span></span><p>Mot clé dans la police de l’amorce, plaque, surlignage, serif, script, majuscules forcées.</p></section>
</div></body></html>
'''
w('components/MotCle/preview.html', prev)
w('components/MotCle/README.md', '''# MotCle

Le mot mis en avant : un ou deux mots en **Anton**, la pièce centrale du style. Dans le sous-titre (le croquis, voir **SousTitreDuo**), dans le titre d’accroche, et seul en mot géant.

**Ce que tu fournis :** le mot, la variante d’animation.

- Police `accent` (Anton 400), styles `motcle-916` (180 px), `motcle-169` (150 px), plancher `motcle-min` (140 px / 117 px). Approche 0. Mot géant seul : `mot-geant` (240 px en 9:16, 200 px en 16:9).
- **Une capitale puis des minuscules** (« 1 Heure », « Contrôle »).
- Couleur **braise** dans le croquis. V1 : os, puis noir (`abysse`) sur fond braise au clic. V4 : os, puis braise une fois posé. `.ms-motcle--os` pour un mot os.
- Toujours le halo `halo-sombre` (sauf noir sur braise).
- Choix du mot : le nom, le chiffre ou le verbe qui porte le sens. Jamais « le », « et », « de », « c’est ».
- Mot trop long : l’amorce passe au-dessus, puis le mot descend jusqu’à `motcle-min`, puis on change de mot.

**À ne pas faire :** mot clé dans la police de l’amorce, plaque, surlignage, serif, script, majuscules forcées, Doto (l’ancien mot clé, remplacé le 8 novembre 2026).
''')
