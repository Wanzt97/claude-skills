# Digital Black Edit Style

Le style de montage des vidéos de Wanzt Koffi (chaîne Digital Black) : reels 9:16 et vidéos YouTube 16:9. Ce système est la **source unique** du style : les guides (skills), HyperFrames et ChatCut prennent ses composants et ses jetons tels quels, sans les réinterpréter. (Ancien nom : DS Montage Wanzt.)

Construit planche par planche à partir du tri des inspirations de Wanzt et du montage de référence, du 6 au 7 novembre 2026. Le 8 novembre, les textes et leurs animations ont été réglés dans deux labos de l’atelier (le **Labo du sous-titre** et le **Labo des textes**) : trio Arial / Anton / Inter, le croquis du sous-titre en 4 variantes, la taille selon le plan, la règle 16:9 et les sons sous la voix. Chaque composant existe en **9:16 et en 16:9**.

Atelier (moodboards, composants d’origine, bibliothèque d’inspirations) : https://claude.ai/artifact/6PzwSbydxjPnuC5QdKWTkA

## Les deux guides
- **Edit for Digital B** (section du même nom) : le mode d’emploi. Le déroulé d’une vidéo, comment lire ton plan de montage (.md), quel type de scène et quelle animation pour chaque ligne du script, 9:16 et 16:9, un reel d’exemple monté de bout en bout (carte **GuideVisuel**), la grille avant de livrer.
- **SFX for Digital B** (section du même nom) : le son. Chaque composant et le son du pack qui va dessus, les niveaux, la musique, la méthode en 4 passes, la palette des 37 sons, l’écoute avec earshot.

## Les planches
| Planche | Sujet | Ici |
|---|---|---|
| A | Sous-titres et typo | **SousTitreDuo**, **MotCle**, **TitreChoc** |
| B | L’accroche, les 3 premières secondes | **Accroche** (+ **TitreChoc**) |
| C | Types de scène | **SceneC2**, **SceneC3**, **SceneC4** |
| D + G | Types d’animation et principes de design | **AnimTexte**, **AnimPersonne**, **AnimObjet**, **AnimGraphique** |
| E | Fonds | **Fond** (le pack de 4 fonds, noir et blanc os) |
| F | Composition | **Composition** (la règle des 4 couches) |
| H | Pendant que tu parles (fusionnée avec C2) | **SceneC2** |
| Marque | Logo et appel à s’abonner | **Logo**, **Abonnement** |
| I | Bibliothèque | page « Planche I · Bibliothèque » de l’atelier : tes 57 favoris rangés en interfaces, graphiques et chiffres, scènes avec toi, scènes plein écran ; chaque image renvoie à son composant |

## L’idée en une phrase
Le croquis : une petite amorce en Arial qui suit la voix, **un mot clé géant en Anton braise** qui claque, un mot de fin en Inter dessous ; quatre façons de l’animer, à alterner ; rien sur le visage (en 16:9, à côté de la tête ou derrière toi) ; un seul objet héros par scène ; une seule couleur d’accent, la braise ; des sons toujours sous la voix.

## Ce qui est gardé, ce qui est refusé
- **Gardé** : le duo de mots devenu le croquis (amorce petite + mot clé géant dans une 2e police + mot de fin) ; le texte, le logo ou les objets qui passent derrière la personne ; le mot ou le chiffre géant de l’accroche ; le cadre de sélection, comme dans un logiciel ; le mot clé révélé de gauche à droite avec un flou ; un petit élément de « vrai logiciel » près de toi ; un objet héros en volume (touches de clavier) ; une interface sombre et propre.
- **Refusé** : les sous-titres petits et sobres en bas ; les plaques, pastilles et surlignages de sous-titres ; le mot en couleur dans la même police ; les majuscules condensées ; le serif, l’italique serif et le script (remplacés par Anton) ; les aplats de couleur en fond ; les affiches chargées, captures entières et grilles d’avatars ; tout effet sur le décor ou sur le visage.

## Couleur
- Texte : `os` (#efefef), jamais de blanc pur.
- Un seul accent : `braise` (#ff7033). Le mot clé du croquis, le titre d’accroche, les chiffres, le cadre de sélection, la touche ou la pastille héros, le carré du logo. **Jamais deux éléments braise à l’écran** (le croquis compte pour un).
- Fonds : noir `noir-digital` (#121212) pour un logiciel, blanc `os` (#efefef) pour une idée, toujours un **Fond** du pack. Jamais d’aplat de couleur.
- Sur fond blanc, le texte est en `noir-digital` (secondaire `encre-2`) et le mot fort en `braise-fonce` (#c2410c) : la braise n’a pas assez de contraste sur le blanc pour du texte, elle n’y sert qu’en aplat.

## Ombre
Tout texte posé sur la vidéo porte le halo `halo-sombre`. Sur un fond clair graphique : pas de halo, et les objets posés portent `ombre-claire`. Les touches et objets en volume portent une ombre portée (`ombre-touche-*`). Jamais d’ombre colorée ni décalée.

## Typographie
Trio réglé dans le Labo du sous-titre (8 novembre 2026) : contraste de taille et de caractère.
- `text` — Arial 400 (Arimo en secours, mêmes dimensions) : l’amorce (`amorce-916` 54 px, `amorce-169` 45 px), une capitale puis des minuscules. Arial 700 : la phrase des scènes texte (`phrase`, 110 px).
- `accent` — Anton : le mot clé (`motcle-916` 180 px, `motcle-169` 150 px, plancher `motcle-min` 140 px), le titre d’accroche (`titre-916` ≤ 420 px, `titre-169` ≤ 350 px), le mot géant (`mot-geant` 240 px), les chiffres (`chiffre` 240 px). Une capitale puis des minuscules. Approche 0.
- `fin` — Inter 400 : le mot de fin du croquis (`fin-916` 54 px, `fin-169` 45 px), en minuscules.
- `display` — Big Shoulders Display 900 : **seulement le logo** (`logo-916` 52 px, `logo-carte` 40 px).
- `mono` — JetBrains Mono 600 : étiquettes, listes, terminal, pastilles. MAJUSCULES pour les étiquettes.
- Jamais de serif ni de script. Doto (l’ancien mot clé) n’est plus utilisé.

## Placement et zone visage
- **Rien ne couvre le visage** (du front au menton). Un élément peut passer derrière la tête grâce au détourage, jamais devant.
- 9:16 : croquis centré, largeur utile 920 px, bas à 360 px du bas de l’image sur un plan rapproché (`bloc-916-bas`, y 1560), au-dessus de la tête sur un gros plan ; taille selon le plan (`ech-*`). Rien dans les 360 px du bas (`zone-shorts`).
- 16:9 — **règle de Wanzt** : tout texte posé sur toi va **à gauche ou à droite de ta tête, ou derrière toi** (détourage), jamais sur le visage ni en bas au centre (`tete-ecart`, `col-169-marge`). Rien dans les 100 px du bas (`zone-youtube`). Dans les scènes graphiques, le sujet d’un côté, le texte de l’autre.

## Mouvement
Jetons `duration`, `easing`, `blur`. Les entrées en `ease-out`, les sorties en `ease-in`, les déplacements d’un point à un autre (zoom, cadrage) en `ease-in-out`.
- Amorce et mot de fin : mot par mot, à l’instant où le mot est dit, fondu + flou 12 → 0 px + 10 px de montée en 350 ms. Amorce 4 mots au plus, mot de fin 3.
- Mot clé : selon la variante du croquis — V1 sélection (cadre, curseur, clic, noir sur braise), V2 punch, V3 machine à écrire, V4 sélection agrandie (voir **SousTitreDuo**).
- Sortie : tout le bloc d’un coup, flou rapide (300 ms), 1 s après le dernier mot ou juste avant le bloc suivant.
- Objets : montée de 48 px ou échelle 0,92 → 1 + fondu en 400 ms, 120 ms d’écart. Touches : tombent, se posent, sont pressées une fois.
- Jamais d’élastique ni de glissement de texte. Seules exceptions : le punch du mot clé (V2) et la sélection agrandie (V4).

## Composants
| Composant | Quand |
|---|---|
| **SousTitreDuo** | chaque phrase dite face caméra : le croquis, en 4 variantes à alterner |
| **MotCle** | le mot clé Anton du croquis, du titre d’accroche et le mot géant seul |
| **TitreChoc** | les 3 premières secondes, ou l’ouverture d’une partie (V3 : sélection tirée depuis un coin) |
| **Accroche** | les 3 premières secondes : plan serré + geste, recul ou avance, titre (sélection, chiffre, derrière toi, à côté, qui s’écrit), puis le 1er sous-titre |
| **Fond** | le fond de tout plan graphique : 4 fonds, noir ou blanc, 9:16 et 16:9 |
| **SceneC2** | pendant que tu parles : 9:16 plan net + un élément (au-dessus de la tête, autour, en bas) ; 16:9 plan flouté, ou toi collé à un bord avec l’autre côté noirci |
| **SceneC3** | écran partagé : bande 9:16, panneau 16:9, A-roll rétracté dans un coin |
| **SceneC4** | plein écran : un objet sur un Fond |
| **AnimTexte** | le texte est la star (D1) |
| **AnimPersonne** | une personne porte l’idée (D2) |
| **AnimObjet** | un objet héros, surtout une touche de clavier (D3) |
| **AnimGraphique** | une checklist, un schéma, un terminal (D4) |
| **Composition** | la règle des 4 couches, à vérifier sur toute scène graphique |
| **Logo** | le logo Digital Black (mot en Big Shoulders 900 + carré braise), en signature ou sur un carton |
| **GuideVisuel** | le reel d’exemple de **Edit for Digital B**, image par image, avec la frise du temps |
| **Abonnement** | le bouton S’abonner : ta photo, le nom de la chaîne, le clic qui passe à « Abonné » (proposition à valider) |

## Types de scène
Pour chaque phrase du script, un type : 1 · sous-titres seuls (**SousTitreDuo**) ; 2 · pendant que tu parles, avec une petite animation (**SceneC2**) ; 3 · écran partagé (**SceneC3**) ; 4 · plein écran (**SceneC4**), dont le contenu est un type d’animation (**AnimTexte**, **AnimPersonne**, **AnimObjet**, **AnimGraphique**) construit selon **Composition**. Fond blanc pour expliquer une idée, noir pour montrer un logiciel. La vidéo s’ouvre sur l’**Accroche**.

## Pour les agents (HyperFrames, ChatCut, guides)
- Ne décris pas le style avec tes mots : prends le composant. Les classes sont dans `components/bundle.css` (préfixe `.ms-`) et lisent les jetons (`tokens.css`).
- Un sous-titre : `.ms-bloc` > `.ms-croquis.ms-v1|v2|v3|v4` avec `.ms-amorce` (des `.ms-mot` avec `--t`), `.ms-cle` (`--t` du mot clé) > `.ms-motcle`, et `.ms-fin`. V3 : une `.ms-frappe` par lettre, chacune avec son `--t`. V4 : le croquis dans `.ms-agrandie` (`--dx`, `--dy`, `--cadre`, `--clic`, `--drag`, `--lache`). Détail et sons dans **SousTitreDuo**. La sortie d’un bloc : classe `ms-sortie` et `--sortie:<ms>`. Un retour (plan flouté, cadrage, voile) : classe `ms-retour` et `--retour:<ms>`. Les temps viennent de la transcription mot à mot. L’amorce fait 4 mots au plus, le mot de fin 3 ; si le mot clé ne tient pas à côté de l’amorce, `.ms-croquis--dessus`, puis `motcle-min`, puis on change de mot.
- Les zooms et les positions (`--ox`, `--oy`, `--x1`, `--y1`, place du visage) se recalent sur chaque vraie vidéo : les valeurs des aperçus sont celles du plan test.
- Polices : Arial (Arimo en secours), Anton, Inter, JetBrains Mono et Big Shoulders Display (logo seulement) ; Anton, Arimo, Inter et JetBrains Mono depuis Google Fonts.
- Sons : jamais plus forts que la voix (règle d’or de **SFX for Digital B**).
- Les valeurs ne s’inventent pas : si un cas manque, demande à Wanzt et ajoute-le ici.
