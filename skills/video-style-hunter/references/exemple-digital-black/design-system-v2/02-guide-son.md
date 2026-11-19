# SFX for Digital B

Le guide du son du système : quel son poser sur chaque composant, à quel niveau, dans quel ordre. Il reprend la méthode de sound design du montage de référence et **ton pack « ChatCut - Effets sonores »** (37 sons écoutés par earshot et validés par Wanzt le 2026-11-05). Les visuels viennent de **Edit for Digital B** et des composants : ils sont la partition que le son habille.

## 1. La philosophie

1. **Le son souligne le mouvement.** Chaque son existe pour souligner quelque chose qu’on voit. Rien ne se passe à l’écran → rien dans le son.
2. **Trois familles, trois rôles.** **Whooshes** → ce qui **bouge** (glisse, tombe, zoome dans une animation). **Textures** → ce qui **arrive sans glisser** (pop, clic, révélation, écriture). **Risers & hits** → l’**anticipation** (on fait monter vers la suite, puis on relâche). En plus : les **réactions**, un sel à doser.
3. **Jamais trop fort.** Whooshes bas, textures plus haut (courtes), risers le plus haut. Rien ne couvre la voix.
4. **Sous les animations : des effets, pas de musique.** La musique vit sous le face caméra seulement.
5. **Un seul impact par scène.** Le reste passe dessous.
6. **L’échelle du son suit l’échelle du plan.** Plan large → son ample ; gros plan → son petit et proche.
7. **Le son réel d’abord.** Une touche pressée sonne comme une touche, un clic comme un clic.
8. **La crête du whoosh sur l’image la plus rapide** du mouvement.
9. **Le silence est un outil.** Un vrai trou de son, voulu, fait plus qu’un son de plus.

## 2. Composant → son

Chaque événement des composants du système, et le son du pack qui va dessus. Le moment exact vient des temps du composant (`--t`, `--clic`, `--sortie`…) : on cale la **crête** du son sur l’image de l’événement.

| Composant | Ce qui se passe | Son du pack | Famille |
|---|---|---|---|
| **SousTitreDuo** V1 · sélection | amorce et mot de fin, mot par mot ; le cadre se trace ; le clic | **Short Shutter Click** 30 % par mot · **Gear Turn Click** 40 % sur le cadre (0,3 s) · **Mouse Click** 60 % sur le clic | texture |
| **SousTitreDuo** V2 · punch | amorce et mot de fin, mot par mot ; le mot clé tombe | **Short Shutter Click** 30 % par mot · **Mouse Click** 45 % sur le mot clé | texture |
| **SousTitreDuo** V3 · machine à écrire | chaque lettre de l’amorce et du mot de fin ; le mot clé | **Gear Single Click** 25 % par lettre · **Camera Shutter** 35 % sur le mot clé | texture |
| **SousTitreDuo** V4 · sélection agrandie | amorce et mot de fin ; le cadre ; le clic ; le texte se pose | **Short Shutter Click** 30 % par mot · **Gear Turn Click** 40 % sur le cadre · **Mouse Click** 60 % sur le clic · **Camera Shutter** 35 % quand il se pose | texture |
| **TitreChoc**, **MotCle** seul | le titre ou le mot géant arrive | les sons de la variante choisie (punch, sélection, machine à écrire, sélection agrandie), aux mêmes volumes que le sous-titre | texture |
| **Accroche** | plan serré, coup de zoom au geste | rien (punch-in du face caméra) | — |
| **Accroche** | recul ou avance de l’ouverture (600 ms) | Simple Whoosh (lent, ample) | whoosh |
| **Accroche** | un mot, une image ou un logo sort de derrière toi | Airy Short Whoosh | whoosh |
| **Accroche** | texte qui s’écrit à côté de toi | Gear Single Click, un par signe | texture |
| **Accroche** | plan large qui se resserre sur un objet (1,2 s) | Simple Whoosh, crête au milieu du mouvement | whoosh |
| après l’accroche (~5 s) | bascule vers le corps | Long Suspense Riser + Taiko Hit sur la coupe | riser + hit |
| **SceneC2** | une carte (fenêtre logiciel, carte idée) monte | New Notification Ping | texture |
| **SceneC2** | points d’étape, puces autour de toi | Synthetic Bubble Pop, un par case ou par puce | texture |
| **SceneC2** 16:9 | ton plan se floute (animation dessus) | TV Switch Off Noise | texture |
| **SceneC2** 16:9 | zoom qui te colle au bord (600 ms) | Deep Short Whoosh | whoosh |
| **SceneC3** | la bande ou le panneau glisse | Airy Short Whoosh | whoosh |
| **SceneC3** | l’objet de la bande se pose | UI Pop-up Alert | texture |
| **SceneC3** 16:9 | A-roll qui se rétracte dans le coin / revient | Deep Short Whoosh / Airy Short Whoosh | whoosh |
| passage face caméra → **SceneC3** ou **SceneC4** | la coupe vers l’animation | Sharp Bass Riser qui finit sur la coupe (ou Camera Shutter si la coupe doit claquer) | riser |
| **SceneC4** | l’objet se pose sur le fond | UI Pop-up Alert | texture |
| **AnimTexte** | le mot Anton s’allume | Tiny Bubble Pop sur sa 1re lettre | texture |
| **AnimTexte** | le cadre de sélection se pose | Mouse Click | texture |
| **AnimTexte** | les barres montent une à une | Synthetic Bubble Pop par barre ; la dernière (braise) : Cash Register Success si c’est un gain | texture |
| **AnimPersonne** | tes plans en cartes montent | Synthetic Bubble Pop, un par carte | texture |
| **AnimPersonne** | la personne en noir et blanc apparaît | TV Switch Off Noise | texture |
| **AnimObjet** | la touche tombe et se pose (400 ms) | Airy Short Whoosh, crête à la pose | whoosh |
| **AnimObjet** | la touche est pressée | Mouse Click (à remplacer par une vraie frappe taillée dans Keyboard Typing Loop, à faire avec earshot `find`) | texture |
| **AnimObjet** | une icône se pose | UI Pop-up Alert | texture |
| **AnimGraphique** | une ligne de la checklist se coche | Mouse Click par ligne ; Clean Ding sur la dernière | texture |
| **AnimGraphique** | les deux ronds du schéma, puis la pastille | Synthetic Bubble Pop ×2, puis New Notification Ping | texture |
| **AnimGraphique** | les lignes du terminal | Mouse Click par ligne (Keyboard Typing Loop si le texte se tape) | texture |
| **Composition** | les éléments de profondeur dérivent | rien : ils ne doivent jamais attirer l’oreille | — |
| **Abonnement** | la carte monte | New Notification Ping | texture |
| **Abonnement** | le clic, puis « Abonné » | Mouse Click, puis Clean Ding | texture |
| **Logo** | carton de fin | Short Drum Roll Sting | hit |
| chaque nouvelle partie | l’étape suivante s’allume | Fast Suspense Riser + Taiko Hit, ou Short Drum Roll Sting pour un petit accent | riser + hit |

Ces choix suivent les rôles écoutés et validés du pack (section 6). Ceux qui n’ont pas encore été entendus sur une vraie vidéo (touche pressée, flou du plan, zoom au bord) sont à confirmer à la première écoute avec Wanzt.

### Réactions (à doser)
Record Scratch Rewind (« attends… »), Record Scratch Stop (arrêt net), Vine Boom Impact (énorme révélation, punchline), Dramatic Thunder Roll (tension), Anime Wow Reaction (révélation magique : un glissando de carillons, pas une voix), Awkward Crow Flyby (silence gênant), Sitcom Laugh Track (blague), Censor Beep (mot censuré).
- **1 à 2 par vidéo au maximum**, seulement sur une vraie blague, une vraie bascule ou une vraie punchline du script.
- Jamais deux de suite, jamais sous une animation sérieuse (chiffres, démonstration). Elles comptent comme l’impact de la scène.

### Les risers sont tous des swells inversés
Les trois « risers » du pack sont des sons aspirés qui gonflent jusqu’à la coupe, pas de longues montées de tension. Règle : **très bas ou très fort, jamais entre les deux.** **Au moins 2 montées par vidéo**, en alternant les trois swells.

## 3. Niveaux

### La règle d’or : jamais plus fort que la voix (Wanzt, 8 novembre 2026)
Un effet sonore ne dépasse **jamais** le volume de ta voix. On le mesure en sonie momentanée (fenêtre de 400 ms, LUFS), la mesure qui suit ce que l’oreille entend, pas seulement la crête.

| Où passe le son | Limite, voix ramenée à −18 LUFS intégrés |
|---|---|
| Pendant que tu parles : sous-titres, textures, whooshes, clics | **−24 LUFS momentanés au plus** (6 LU sous ta voix), crête −6 dBFS au plus |
| Entre deux phrases : risers, hits, réactions | **−18 LUFS momentanés au plus** (jamais au-dessus de ta voix) |
| Nappe continue (Light Clock Tick) | −34 LUFS au plus |

Les gains de la palette (section 6) respectent déjà ces limites : chaque son a été mesuré un par un. Si tu poses deux sons en même temps, ou un son sur un mot très calme, vérifie la vidéo finie (grille, section 8) : la piste des effets doit rester au moins 6 LU sous la piste de la voix à chaque instant où tu parles. Si un son dépasse, **baisse le son, jamais la voix**.

### Les niveaux cibles par famille (avant la règle d’or)

Les fichiers du pack n'ont pas le même volume (crêtes de 0 à −25 dBFS). Chaque son a donc un **niveau cible** (crête du clip une fois posé) selon sa famille, et la palette donne le **gain à appliquer** pour l'atteindre.

| Famille | Niveau cible |
|---|---|
| Whooshes | −12 dB par défaut, −10 dB maximum pour un gros mouvement |
| Textures | −6 à −7 dB (les plus courtes un peu plus haut) |
| Risers | −5 dB |
| Hits sous un riser | −6 dB ; le couple riser + hit est le plus fort de la transition |
| Réactions | −8 dB |
| Nappe (Light Clock Tick) | −20 dB |
| Musique (face caméra seulement) | −19 dB sous la voix |
| Voix | la reine, jamais couverte |

Avant de poser les sons, ramène la voix vers **−18 LUFS intégrés** (mesure : `ffmpeg -i <audio> -af ebur128 -f null -`). Si le couple le plus fort risque de saturer, **baisse le hit, jamais la voix**. Vérifie à l'écoute et à la mesure à la fin : un premier jet prudent s'est déjà révélé trop discret ; rééquilibrer vers le bas est plus simple que remonter partout.

**Appliquer un gain** :
- HyperFrames : `data-volume` = 10^(gain/20) quand le gain est négatif (−6 dB ≈ 0,5 ; −12 dB ≈ 0,25) ; un gain positif passe par un effet de gain en dB (syntaxe dans le skill `hyperframes-audio`).
- ChatCut : le volume du clip en dB.

### Les sons du sous-titre, mesurés
Les 4 variantes du sous-titre (réglées dans le Labo du sous-titre, atelier, 8 novembre) utilisent 5 sons. Le volume est le `data-volume` HyperFrames sur le fichier d’origine.

| Son | Volume | En dB | Fort au plus | Crête |
|---|---|---|---|---|
| Short Shutter Click | 0,30 | −10,5 dB | −35 LUFS | −17 dBFS |
| Mouse Click (V1, V4 : clic) | 0,60 | −4,4 dB | −32 LUFS | −8,5 dBFS |
| Mouse Click (V2 : mot clé) | 0,45 | −6,9 dB | −34 LUFS | −11 dBFS |
| Gear Turn Click | 0,40 | −8,0 dB | −38 LUFS | −21 dBFS |
| Gear Single Click | 0,25 | −12,0 dB | −50 LUFS (une lettre) | −25 dBFS |
| Camera Shutter | 0,35 | −9,1 dB | −25 LUFS | −12 dBFS |

Tous restent au moins 6 LU sous ta voix. Camera Shutter était réglé à 40 % dans le labo : il passait à −24 LUFS, juste à la limite, il est donc descendu à 35 %.

## 4. Musique

- **Uniquement sous le face caméra** (**SousTitreDuo**, **SceneC2** en 9:16), à −19 dB.
- **Jamais sous une animation** (**SceneC3**, **SceneC4**, **SceneC2** plan flouté en 16:9) : fondu court à l’entrée de l’animation, reprise au retour du face caméra.
- Elle se pose **en dernier**, après validation des passes 1 à 3.
- Wanzt fournit ses morceaux ou choisit parmi des propositions. Pas de génération, pas de musique posée sans qu’il l’ait choisie.

## 5. La méthode : analyser, puis 4 passes dans l’ordre

**Étape 0 — Préparer.** Ouvre la palette (section 6). Coupe le son d’origine qui n’est pas la voix (mute, jamais supprimer). Ramène la voix vers −18 LUFS.

**Étape 1 — Analyser d’abord.** Parcours la vidéo et écris une feuille de repérage horodatée : chaque moment classé **MOUVEMENT** (→ whoosh), **ÉVÉNEMENT** (→ texture), **MONTÉE** (→ riser/hit) ou **RÉACTION**, avec le composant qui le produit (section 2). Donne-la à Wanzt avant toute passe.

**Étape 2 — Poser 2 ou 3 questions, puis attendre.** Quelque chose à éviter ? Un moment à traiter à part ? Quel est le moment le plus fort ? Une réaction voulue quelque part ?

**Passe 1 — Whooshes**, du début à la fin, crête sur l’image la plus rapide.
**Passe 2 — Textures** (et réactions), chacune sur l’image de l’événement.
**Passe 3 — Risers & hits** : le riser se termine sur l’image de la transition, le hit juste dessous.
**Passe 4 — Musique**, seulement après validation des passes 1 à 3.

Après chaque passe : un court compte rendu (quoi, où, quel son, pourquoi). Quand Wanzt corrige un son à la main, comprends pourquoi et applique la même logique aux moments semblables.

### Pistes et calage
- **Une famille par piste** : WHOOSHES, TEXTURES, RISERS, HITS, REACTIONS, MUSIQUE. Dans HyperFrames, chaque `<audio>` a un `id` et chaque piste son `data-track-index`.
- Ajouter sur de nouvelles pistes, ne jamais toucher une piste que Wanzt a posée.
- **Caler la crête, pas le début du fichier** : début du clip = temps de l’image − « crête à » (palette).
- Lire les temps réels des animations dans la composition (`--t`, `--i`, `--clic`…), élément par élément ; ne jamais répartir des pops « régulièrement ».
- Fondus très courts en bout de chaque son coupé ; clips entiers, chevauchements permis.

### À ne jamais faire
Musique sous une animation ; un whoosh pour ce qui pop, un pop pour ce qui glisse ; un whoosh au-dessus de −10 dB ; un son plus fort que la voix (règle d’or, section 3) ; monter la voix pour passer au-dessus d’un son ; plus de 2 réactions ; générer un son sans demande de Wanzt ; supprimer le son d’origine au lieu de le couper.

## 6. La palette : le pack « ChatCut - Effets sonores »

Dossier : `~/Video/Studio de Création de style de Montage/ChatCut - Effets sonores/` (37 sons, 4 dossiers). Copie dans le projet de montage seulement les sons utilisés. « Crête à » = moment le plus fort du fichier, à caler sur l’image. « Gain à appliquer » = pour atteindre le niveau cible de la famille **sans jamais dépasser la limite de la voix** (section 3) : « (baissé) » signale un son qu’on a descendu sous son niveau cible pour rester sous la voix (mesures du 8 novembre 2026). « Volume » = la même valeur en `data-volume` HyperFrames (le fichier d’origine vaut 1). « Fort au plus » = sonie momentanée la plus haute du son une fois posé. Gear Single Click est un seul cran taillé dans Gear Turn Click. Si Wanzt entend un autre rôle pour un son, il a le dernier mot.

**Whooshes** (niveau cible -12 dB)

| Rôle | Fichier | Durée | Crête à | Gain à appliquer | Volume (`data-volume`) | Fort au plus, une fois posé |
|---|---|---|---|---|---|---|
| Glissement ou pan standard, entrée légère (défaut) | `2 - Transition & Emphasis/Airy Short Whoosh.mp3` | 0.79 s | 0.45 s | -10.0 dB | 0.32 | -30 LUFS |
| Mouvement lourd, transition de scène | `2 - Transition & Emphasis/Deep Short Whoosh.mp3` | 1.34 s | 0.47 s | -7.9 dB | 0.40 | -25 LUFS |
| Mouvement lent, ample et grave | `2 - Transition & Emphasis/Simple Whoosh.mp3` | 1.32 s | 0.60 s | -2.4 dB (baissé) | 0.76 | -24 LUFS |

**Textures** (niveau cible -6.5 dB)

| Rôle | Fichier | Durée | Crête à | Gain à appliquer | Volume (`data-volume`) | Fort au plus, une fois posé |
|---|---|---|---|---|---|---|
| Texte qui apparaît d'un bloc (pop) | `1 - UI & Motion Feedback/Tiny Bubble Pop.mp3` | 0.17 s | 0.05 s | -5.2 dB | 0.55 | -26 LUFS |
| Pop plus « numérique », éléments en série | `1 - UI & Motion Feedback/Synthetic Bubble Pop.mp3` | 0.36 s | 0.05 s | -3.6 dB (baissé) | 0.66 | -24 LUFS |
| UI qui apparaît (pop sourd, boisé) | `1 - UI & Motion Feedback/UI Pop-up Alert.mp3` | 0.41 s | 0.15 s | -8.0 dB (baissé) | 0.40 | -24 LUFS |
| Notification, carte ou badge qui entre (pop tonal) | `1 - UI & Motion Feedback/New Notification Ping.mp3` | 0.53 s | 0.07 s | -9.4 dB (baissé) | 0.34 | -24 LUFS |
| Message envoyé, bulle de chat | `1 - UI & Motion Feedback/Sent Message Ping.mp3` | 0.38 s | 0.25 s | -5.4 dB (baissé) | 0.54 | -24 LUFS |
| Clic, changement dans l'UI ; lettre par lettre plus net | `1 - UI & Motion Feedback/Mouse Click.mp3` | 0.24 s | 0.15 s | -2.4 dB | 0.76 | -30 LUFS |
| Lettre par lettre (un cran d'engrenage, défaut) | `3 - Device & Texture/Gear Single Click.mp3` | 0.05 s | 0.02 s | +8.2 dB | 2.57 | -30 LUFS |
| Molette ou pièce qui tourne (rafale de crans) | `3 - Device & Texture/Gear Turn Click.mp3` | 0.67 s | 0.55 s | +5.7 dB (baissé) | 1.93 | -24 LUFS |
| Mécanisme continu, compteur qui tourne | `3 - Device & Texture/Mechanical Clicking Loop.mp3` | 2.93 s | boucle | -6.2 dB (baissé) | 0.49 | -24 LUFS |
| Frappe clavier à l'écran | `1 - UI & Motion Feedback/Keyboard Typing Loop.mp3` | 15.58 s | boucle | -0.2 dB | 0.98 | -27 LUFS |
| Frappe clavier lente, longue | `1 - UI & Motion Feedback/Slow Dell Keyboard Typing.mp3` | 68.35 s | boucle | +1.6 dB | 1.20 | -28 LUFS |
| Glitch, scan, écran qui grésille | `3 - Device & Texture/Glitchy TV Signal.mp3` | 0.98 s | 0.53 s | +4.6 dB (baissé) | 1.70 | -24 LUFS |
| Révélation (impact sci-fi), entrée dans une nouvelle animation | `3 - Device & Texture/TV Switch Off Noise.mp3` | 0.24 s | 0.17 s | -9.1 dB (baissé) | 0.35 | -24 LUFS |
| Transition coupe à coupe, flash | `3 - Device & Texture/Camera Shutter.mp3` | 0.46 s | 0.25 s | -8.4 dB (baissé) | 0.38 | -24 LUFS |
| Flash plus discret | `3 - Device & Texture/Short Shutter Click.mp3` | 0.24 s | 0.12 s | +0.0 dB | 1.00 | -25 LUFS |
| Flash rétro, photo | `3 - Device & Texture/Vintage Camera Shutter.mp3` | 0.36 s | 0.15 s | -6.3 dB | 0.48 | -24 LUFS |
| Succès, conclusion, chiffre gagné | `1 - UI & Motion Feedback/Cash Register Success.mp3` | 2.06 s | 0.45 s | -13.6 dB (baissé) | 0.21 | -24 LUFS |
| Validation discrète, coche | `1 - UI & Motion Feedback/Clean Ding.mp3` | 1.68 s | 0.12 s | -11.1 dB (baissé) | 0.28 | -24 LUFS |
| Temps qui passe (nappe continue, très bas : cible −20 dB) | `3 - Device & Texture/Light Clock Tick.mp3` | 50.30 s | boucle | +0.7 dB | 1.08 | -40 LUFS |
| Téléphone à l'écran (son réel) | `1 - UI & Motion Feedback/Phone Notification Ping.mp3` | 0.82 s | 0.10 s | -11.7 dB (baissé) | 0.26 | -24 LUFS |
| Appel vidéo à l'écran (son réel) | `1 - UI & Motion Feedback/Video Call Ringtone.mp3` | 3.48 s | 2.48 s | -2.3 dB (baissé) | 0.77 | -24 LUFS |

**Risers & hits** (niveau cible -5 dB ; hits -6 dB)

| Rôle | Fichier | Durée | Crête à | Gain à appliquer | Volume (`data-volume`) | Fort au plus, une fois posé |
|---|---|---|---|---|---|---|
| Swell court et aspiré, juste avant la coupe | `2 - Transition & Emphasis/Sharp Bass Riser.mp3` | 0.94 s | 0.85 s | -0.4 dB | 0.95 | -20 LUFS |
| Swell profond, changement de partie ; aussi whoosh long | `2 - Transition & Emphasis/Fast Suspense Riser.mp3` | 4.42 s | 2.58 s | +0.6 dB (baissé) | 1.07 | -18 LUFS |
| Swell de cymbale inversée, métallique (~5 s après le hook) | `2 - Transition & Emphasis/Long Suspense Riser.mp3` | 3.77 s | 2.92 s | -11.1 dB (baissé) | 0.28 | -18 LUFS |
| Hit sous un riser (défaut) | `2 - Transition & Emphasis/Taiko Hit.mp3` | 2.23 s | 0.28 s | -11.0 dB (baissé) | 0.28 | -18 LUFS |
| Petit coup d'accent, titre de chapitre | `2 - Transition & Emphasis/Short Drum Roll Sting.mp3` | 0.74 s | 0.17 s | -0.5 dB | 0.94 | -18 LUFS |

**Réactions** (niveau cible -8 dB)

| Rôle | Fichier | Durée | Crête à | Gain à appliquer | Volume (`data-volume`) | Fort au plus, une fois posé |
|---|---|---|---|---|---|---|
| Retour en arrière, « attends… » | `2 - Transition & Emphasis/Record Scratch Rewind.mp3` | 1.49 s | 1.05 s | -10.2 dB (baissé) | 0.31 | -18 LUFS |
| Arrêt net, moment gênant | `2 - Transition & Emphasis/Record Scratch Stop.mp3` | 0.67 s | 0.07 s | -5.7 dB | 0.52 | -20 LUFS |
| Énorme révélation, punchline | `4 - Reaction & Mood/Vine Boom Impact.mp3` | 2.90 s | 0.62 s | -10.6 dB (baissé) | 0.30 | -18 LUFS |
| Tension dramatique | `4 - Reaction & Mood/Dramatic Thunder Roll.mp3` | 8.18 s | 0.40 s | -10.0 dB (baissé) | 0.32 | -18 LUFS |
| Révélation magique (glissando de carillons, pas une voix) | `4 - Reaction & Mood/Anime Wow Reaction.mp3` | 3.74 s | 0.40 s | +3.8 dB (baissé) | 1.55 | -18 LUFS |
| Silence gênant | `4 - Reaction & Mood/Awkward Crow Flyby.mp3` | 1.75 s | 0.15 s | -2.1 dB | 0.79 | -18 LUFS |
| Blague | `4 - Reaction & Mood/Sitcom Laugh Track.mp3` | 2.50 s | 0.50 s | +2.2 dB | 1.29 | -19 LUFS |
| Mot censuré | `1 - UI & Motion Feedback/Censor Beep.mp3` | 0.79 s | 0.25 s | -13.2 dB (baissé) | 0.22 | -18 LUFS |

### Ce qui manque au pack
| Encore absent | Remplacement |
|---|---|
| Longue montée de tension (5 à 10 s) | Fast Suspense Riser puis Long Suspense Riser, ou en chercher une (Openverse, CC0 ou CC BY) |
| Une vraie frappe de touche isolée | à tailler dans Keyboard Typing Loop (earshot `find "a single key press"`) |
| Chœur céleste | Anime Wow Reaction, compté comme réaction |

## 7. Écouter avec earshot

Claude n’entend pas : earshot (`~/Outils/earshot/`, serveur MCP `earshot`) transforme le son en verdicts chiffrés, en local. Ne dis jamais qu’un son « colle » sans une lecture earshot, et cite le chiffre.
- Un nouveau son : `describe`, puis `match` contre le rôle visé.
- Choisir entre deux sons : `ab a.mp3 b.mp3 --query "<rôle>"`.
- Trouver le bon morceau d’un long fichier : `find fichier.mp3 "a single key press"`.
- Contrôler le mix fini : `timeline film.mp4 --cues cues.json`, `sheet film.mp4 -o sheet.png`, `measure` (LUFS, crête).

## 8. Grille de vérification

- [ ] Chaque mouvement d’animation a un whoosh, crête sur l’image la plus rapide, ≤ −10 dB ; aucun sur les punch-ins du face caméra.
- [ ] Chaque événement qui ne glisse pas a une texture sur l’image de l’événement ; chaque bloc de sous-titres a les sons de sa variante (V1 à V4), aux volumes mesurés.
- [ ] Une montée vers 5 s, après l’accroche, avec un hit dessous ; au moins 2 montées dans la vidéo.
- [ ] 2 réactions au plus.
- [ ] Pas de musique sous une animation ; musique à −19 dB sous le face caméra seulement.
- [ ] La voix intacte, rien de plus fort qu’elle : piste des effets au moins 6 LU sous la voix quand tu parles (−24 LUFS momentanés au plus), et jamais au-dessus entre deux phrases (−18 LUFS). Mesure : `ffmpeg -i effets.wav -af ebur128 -f null -` sur la piste des effets seule, à comparer à la piste de la voix ; ou earshot `measure`. Aucune crête qui sature.
- [ ] Une famille par piste ; son d’origine coupé, pas supprimé.
- [ ] Synchro contrôlée par earshot au temps de chaque son important.
