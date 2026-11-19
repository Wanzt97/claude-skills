# Edit for Digital B

Le guide d’utilisation du système : comment monter une vidéo avec ce système, du script au rendu. Les valeurs sont dans les composants et les jetons : ce guide dit **quoi poser, et quand**. La carte **GuideVisuel** (groupe « Edit for Digital B ») montre le même déroulé en images, sur un reel d’exemple.

## 1. Le déroulé d’une vidéo

| Moment | Ce qu’on voit | Composants |
|---|---|---|
| 0 à 3 s | l’accroche : toi en plan serré, ton geste vers l’objectif, le titre pendant le geste, puis le 1er sous-titre à 1,7 s | **Accroche** (+ **TitreChoc**) |
| Vers 5 s | la bascule vers le corps de la vidéo (montée sonore) | le type de scène suivant |
| Le corps | une ligne du script = un type de scène ; on alterne face caméra et animations | **SousTitreDuo**, **SceneC2**, **SceneC3**, **SceneC4** + un type d’animation |
| Chaque chapitre | la même petite interface de partie revient (points d’étape : l’étape en cours s’allume) | **SceneC2** V1 |
| La fin | retour au face caméra, appel à s’abonner, logo | **SousTitreDuo**, **Abonnement**, **Logo** |

## 2. Le plan de montage (.md)

Wanzt écrit lui-même son **plan de montage** : un fichier Markdown, `<projet>/exports/<titre>-plan-de-montage.md`. Il n’y a pas de page de planification à faire : on part de ce fichier, on ne le réécrit pas.

Chaque plan du fichier donne : son numéro et son minutage (`#### Plan 3 · 00:00:14:17 → 00:00:20:24 (6.23 s) · Fullscreen`), le **type de scène**, le **texte du script**, souvent une **note de scène** (ce que Wanzt veut voir) et les **médias** (rush, plage source).

| Type dans le plan | Composant |
|---|---|
| Hook | **Accroche** (+ **TitreChoc**) |
| Captions Only | **SousTitreDuo** |
| Captions + UI | **SceneC2** |
| Halfscreen | **SceneC3** |
| Fullscreen | **SceneC4** + un type d’animation (section 4) |
| sans type de scène | demander à Wanzt, ne pas deviner |

Comment le lire :
1. Lis tout le fichier avant de construire : le résumé (durée, format, nombre de plans par type), puis chaque plan dans l’ordre.
2. La **note de scène est la commande de Wanzt** : ce qu’elle demande (une horloge, une timeline coupée, un zoom out…) se fait, avec les composants et les jetons du système (section 4 pour choisir le type d’animation, **Composition** pour la construire). Si elle demande quelque chose qu’aucun composant ne couvre, construis-le avec les jetons et signale-le à Wanzt.
3. Sans note de scène, applique le type du plan avec sa variante par défaut.
4. Chaque bloc de sous-titres se découpe en croquis : une **amorce** (4 mots au plus), un **mot clé** (1 ou 2 mots, celui qui porte le sens) et, si la phrase continue, un **mot de fin** (3 mots au plus). Voir la section 5 bis.
5. Respecte les minutages et les plages de rush du fichier ; un plan « à tourner » ou un clip « proposé » se signale, il ne s’invente pas.

## 3. Quel type de scène pour une ligne

| La ligne… | Type | Composant |
|---|---|---|
| …se dit simplement, face caméra | 1 · sous-titres seuls | **SousTitreDuo** : le croquis, variante choisie selon la section 5 bis |
| …annonce une étape, un outil, une liste courte, sans quitter ton visage | 2 · pendant que tu parles | **SceneC2** : 9:16 plan net + un seul élément (au-dessus de la tête par défaut, autour de toi, ou en bas) ; 16:9 plan flouté, ou toi collé à un bord avec l’autre côté noirci |
| …montre quelque chose pendant que tu restes présent | 3 · écran partagé | **SceneC3** : bande en haut (9:16), panneau à gauche ou A-roll rétracté dans un coin (16:9) |
| …explique une idée qui mérite tout l’écran | 4 · plein écran | **SceneC4** + un type d’animation (section 4) |

Fond : **blanc os pour expliquer une idée, noir pour montrer un logiciel**. Toujours un fond du pack (**Fond**), jamais un aplat de couleur.

## 4. Quel type d’animation pour une idée

| L’idée tient dans… | Composant | Exemple |
|---|---|---|
| une phrase et un mot fort | **AnimTexte** | « le montage prend **1 heure** », « tes vues ont **doublé** » + barres |
| une personne (toi, un client, une statue) | **AnimPersonne** | tes plans en cartes ; toi en noir et blanc détouré, titre à côté |
| un objet | **AnimObjet** | une touche Ctrl, Échap, Shift ; une icône au trait |
| une interface, une liste, un lien entre deux choses | **AnimGraphique** | checklist 6/6, schéma script → montage, terminal |

Puis vérifie la scène avec **Composition** : fond, **un seul** sujet, 2 à 4 éléments de soutien, 1 ou 2 éléments de profondeur flous ; **un seul élément braise à l’écran**.

## 5. 9:16 et 16:9

- Même plan de montage, mêmes composants : chaque composant a ses variantes dans les deux formats.
- 9:16 : tout s’empile (objet au-dessus, texte dessous) ; le croquis sous le menton, rien dans les 360 px du bas (interface des Shorts).
- **16:9 — règle de Wanzt (8 novembre 2026)** : tout texte posé sur ton image (sous-titre, titre d’accroche, mot géant) va **à gauche ou à droite de ta tête, ou derrière toi** grâce au détourage. Jamais sur le visage, jamais en bas au centre ; rien dans les 100 px du bas (barre de lecture). Choisis le côté où l’image a le plus de place libre ; « derrière toi » pour un mot qui doit marquer.
- Pendant que tu parles avec une animation (**SceneC2**), en 16:9 : plan flouté, ou zoom qui te colle au bord.
- Les zooms (`--ox`, `--oy`, `--x1`), la place de ta tête (`--tete-g`, `--tete-d`, `--y`) et la place du visage se recalent sur chaque vraie vidéo.

## 5 bis. Le sous-titre : le croquis et ses 4 variantes

Réglé avec Wanzt dans le Labo du sous-titre (atelier, 8 novembre 2026). Détails et classes : **SousTitreDuo**.

**La composition** : amorce en Arial 400 à gauche du mot clé ; mot clé en Anton braise ; mot de fin en Inter 400 sous le mot clé, calé à droite. Une capitale puis des minuscules pour l’amorce et le mot clé, minuscules pour le mot de fin. Si le mot clé ne tient pas à côté de l’amorce, l’amorce passe au-dessus ; s’il ne tient toujours pas, il rétrécit jusqu’à 140 px ; au-delà, choisis un autre mot.

**Quelle variante, quand** :
| Variante | Pour | Condition |
|---|---|---|
| **V2 · Punch** | la variante par défaut | toujours possible |
| **V1 · Sélection** | le mot le plus fort de chaque partie (un chiffre, un résultat) | la phrase continue au moins 2 s après le mot clé, sinon V2 |
| **V3 · Machine à écrire** | une phrase calme ou technique (une commande, une étape) | phrase courte : l’écriture prend 55 ms par lettre |
| **V4 · Sélection agrandie** | poser un mot qui mérite un temps fort, surtout en 16:9 (le texte part du bas et vient se poser à côté de ta tête) | la phrase continue au moins 2 s après le mot clé |

Règles : **jamais deux fois la même variante de suite** ; V1 et V4 au plus une fois sur trois blocs ; chaque mot arrive à l’instant où il est dit (transcription mot à mot) ; le bloc part 1 s après le dernier mot, ou dès que la phrase suivante commence.

**La taille et la place selon le plan** :
| Plan | 9:16 | 16:9 |
|---|---|---|
| Gros plan (visage) | 80 %, au-dessus de la tête (haut du bloc à 250 px) | 80 %, à gauche de la tête |
| Plan rapproché (poitrine) | 100 %, sous le menton (bas du bloc à 360 px du bas) | 100 %, à gauche de la tête |
| Plan moyen (taille) | 105 %, bas du bloc à 380 px du bas | 100 %, à droite de la tête |
| Plan large (en pied) | 108 %, bas du bloc à 400 px du bas | 100 %, derrière toi |

Ces valeurs sont celles du labo, sur ton plan test : sur une vraie vidéo, vérifie que rien ne touche le visage et ajuste la hauteur.

## 6. Exemple : un reel de 42 s, « 3 erreurs qui tuent ton montage »

Ce que donnerait un plan de montage de 10 plans, une fois traduit en composants.

| Temps | Texte du script | Type | Composant · variante | Fond | Son (voir **SFX for Digital B**) |
|---|---|---|---|---|---|
| 0–3 s | « 3 erreurs qui tuent ton montage » | accroche | **Accroche** V1 : plan serré, geste, titre en sélection au-dessus de la tête | ta vidéo | pop sur le titre, clic sur le cadre |
| 3–6 s | « et la première **coûte** très cher » | 1 | **SousTitreDuo** V2 punch | ta vidéo | Short Shutter Click sur les mots, Mouse Click sur le mot clé ; montée + hit sur la coupe vers 5 s |
| 6–10 s | « erreur **une** : tu montes sans plan » | 2 | **SceneC2** V1, étape 1 allumée | ta vidéo | un pop par case |
| 10–15 s | « tu ouvres le logiciel et tu coupes au hasard » | 3 | **SceneC3** bande noire + fenêtre du logiciel | noir | whoosh de la bande, pop de la fenêtre |
| 15–20 s | « un plan prend **10 min** » | 4 | **SceneC4** + **AnimTexte** V1 | blanc os | swell court avant la coupe, pop sur le mot |
| 20–24 s | « erreur **deux** : trop d’effets » | 2 | **SceneC2** V1, étape 2 allumée | ta vidéo | un pop par case |
| 24–30 s | « appuie sur **Échap** » | 4 | **SceneC4** + **AnimObjet** V1, touche braise | noir | whoosh de la chute, clic de la touche |
| 30–34 s | « erreur **trois** : pas de rythme » | 2 | **SceneC2** V1, étape 3 allumée | ta vidéo | un pop par case |
| 34–38 s | « garde le **contrôle** sur ton rythme » | 1 | **SousTitreDuo** V3 machine à écrire | ta vidéo | Gear Single Click par lettre, Camera Shutter sur le mot clé |
| 38–42 s | « abonne-toi pour la suite » | fin | **Abonnement** sous le menton, puis **Logo** | ta vidéo | pop de la carte, clic, ding |

## 7. Avant de livrer

- [ ] Rien sur le visage, du front au menton, à aucune image.
- [ ] Croquis : amorce 4 mots au plus, un seul mot clé (1 ou 2 mots), mot de fin 3 mots au plus ; jamais deux fois la même variante de suite ; jamais de serif ni d’italique.
- [ ] Un seul élément braise à l’écran ; texte sur fond blanc en `noir-digital` ou `braise-fonce`.
- [ ] Chaque scène graphique passe la règle **Composition**.
- [ ] Le titre de l’accroche et le 1er sous-titre ne sont jamais à l’écran en même temps.
- [ ] Rien dans les zones d’interface : sous y 1560 en 9:16 (Shorts), dans les 100 px du bas en 16:9 (barre de lecture).
- [ ] En 16:9, chaque texte posé sur toi est à gauche ou à droite de ta tête, ou derrière toi.
- [ ] Les deux formats demandés sont faits avec leurs propres variantes, pas recadrés.
- [ ] Le son suit **SFX for Digital B** ; aucun effet plus fort que ta voix.
