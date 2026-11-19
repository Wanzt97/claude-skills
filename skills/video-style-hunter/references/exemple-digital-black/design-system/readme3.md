# Digital Black Edit Style

Le style de montage des vidéos de Wanzt Koffi (chaîne Digital Black) : reels 9:16 et vidéos YouTube 16:9. Ce système est la **source unique** du style : les guides (skills), HyperFrames et ChatCut prennent ses composants et ses jetons tels quels, sans les réinterpréter. (Ancien nom : DS Montage Wanzt.)

Construit planche par planche à partir du tri des inspirations de Wanzt et du montage de référence, du 6 au 7 novembre 2026. Chaque composant existe en **9:16 et en 16:9**.

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
Une petite amorce qui suit la voix, puis **un mot géant en Doto 900** qui s’allume lettre par lettre ; rien sur le visage ; un seul objet héros par scène ; une seule couleur d’accent, la braise.

## Ce qui est gardé, ce qui est refusé
- **Gardé** : le duo de mots (amorce petite + mot clé géant dans une 2e police) ; le texte, le logo ou les objets qui passent derrière la personne ; le mot ou le chiffre géant de l’accroche ; le cadre de sélection, comme dans un logiciel ; le mot clé révélé de gauche à droite avec un flou ; un petit élément de « vrai logiciel » près de toi ; un objet héros en volume (touches de clavier) ; une interface sombre et propre.
- **Refusé** : les sous-titres petits et sobres en bas ; les plaques, pastilles et surlignages de sous-titres ; le mot en couleur dans la même police ; les majuscules condensées ; le serif, l’italique serif et le script (remplacés par Doto) ; les aplats de couleur en fond ; les affiches chargées, captures entières et grilles d’avatars ; tout effet sur le décor ou sur le visage.

## Couleur
- Texte : `os` (#efefef), jamais de blanc pur.
- Un seul accent : `braise` (#ff7033). Le mot le plus fort, au plus 1 bloc sur 3, les poignées de sélection, la touche ou la pastille héros. **Jamais deux éléments braise à l’écran.**
- Fonds : noir `noir-digital` (#121212) pour un logiciel, blanc `os` (#efefef) pour une idée, toujours un **Fond** du pack. Jamais d’aplat de couleur.
- Sur fond blanc, le texte est en `noir-digital` (secondaire `encre-2`) et le mot fort en `braise-fonce` (#c2410c) : la braise n’a pas assez de contraste sur le blanc pour du texte, elle n’y sert qu’en aplat.

## Ombre
Tout texte posé sur la vidéo porte le halo `halo-sombre`. Sur un fond clair graphique : pas de halo, et les objets posés portent `ombre-claire`. Les touches et objets en volume portent une ombre portée (`ombre-touche-*`). Jamais d’ombre colorée ni décalée.

## Typographie
- `text` — Inter 800 : l’amorce (`amorce-916` 56 px, `amorce-169` 44 px) et la grosse phrase des animations (`.ms-phrase`, 96 à 120 px). Casse de phrase.
- `accent` — Doto 900 : le mot clé (`motcle-916` 240 px, `motcle-169` 200 px, plancher `motcle-min` 180 px), le titre-choc (`titre-916` ≤ 420 px, `titre-169` ≤ 340 px) et le mot mis en valeur des animations. Approche −0,04 em.
- `display` — Big Shoulders Display 900 : **seulement le logo** (`logo-916` 52 px, `logo-carte` 40 px).
- `mono` — JetBrains Mono 600 : étiquettes, listes, terminal, pastilles. MAJUSCULES pour les étiquettes.
- Jamais de serif ni de script. Jamais Inter sous 500.

## Placement et zone visage
- **Rien ne couvre le visage** (du front au menton). Un élément peut passer derrière la tête grâce au détourage, jamais devant.
- 9:16 : bloc de sous-titres centré, largeur 920 px, bas à `bloc-916-bas` (y 1330), descendu si le visage est bas, jusqu’à `bloc-916-bas-max` (y 1560). Haut du bloc au moins `sous-menton` (40 px) sous le menton.
- 16:9 : bloc centré, largeur 1600 px, bas à `bloc-169-bas` (y 900). Dans les scènes graphiques, le sujet d’un côté, le texte de l’autre.

## Mouvement
Jetons `duration`, `easing`, `blur`. Les entrées en `ease-out`, les sorties en `ease-in`, les déplacements d’un point à un autre (zoom, cadrage) en `ease-in-out`.
- Amorce : 1 à 4 mots au plus (au-delà, on coupe en deux blocs) ; mot par mot, à l’instant où le mot est dit, fondu + flou 6 → 0 px en 120 ms. Aucun déplacement.
- Mot clé : lettre par lettre, de gauche à droite, fondu + flou 12 → 0 px en 240 ms par lettre, 30 ms d’écart.
- Sortie : tout le bloc d’un coup, fondu + flou → 8 px en 140 ms, juste avant le bloc suivant.
- Objets : montée de 48 px ou échelle 0,92 → 1 + fondu en 400 ms, 120 ms d’écart. Touches : tombent, se posent, sont pressées une fois.
- Jamais de rebond, d’élastique, de glissement de texte ni de zoom sur le texte.

## Composants
| Composant | Quand |
|---|---|
| **SousTitreDuo** | chaque phrase dite face caméra |
| **MotCle** | dans chaque bloc, et dans le titre-choc |
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
| **Logo** | le logo Digital Black (mot en Big Shoulders 900 + carré orange), en signature ou sur un carton |
| **GuideVisuel** | le reel d’exemple de **Edit for Digital B**, image par image, avec la frise du temps |
| **Abonnement** | le bouton S’abonner : ta photo, le nom de la chaîne, le clic qui passe à « Abonné » (proposition à valider) |

## Types de scène
Pour chaque phrase du script, un type : 1 · sous-titres seuls (**SousTitreDuo**) ; 2 · pendant que tu parles, avec une petite animation (**SceneC2**) ; 3 · écran partagé (**SceneC3**) ; 4 · plein écran (**SceneC4**), dont le contenu est un type d’animation (**AnimTexte**, **AnimPersonne**, **AnimObjet**, **AnimGraphique**) construit selon **Composition**. Fond blanc pour expliquer une idée, noir pour montrer un logiciel. La vidéo s’ouvre sur l’**Accroche**.

## Pour les agents (HyperFrames, ChatCut, guides)
- Ne décris pas le style avec tes mots : prends le composant. Les classes sont dans `components/bundle.css` (préfixe `.ms-`) et lisent les jetons (`tokens.css`).
- Un mot de l’amorce : `<span class="ms-mot" style="--t:<ms>">`. Le mot clé : `<span class="ms-motcle" style="--t:<ms>">` avec une `<span class="ms-lettre" style="--i:<rang>">` par lettre. La sortie d’un bloc : classe `ms-sortie` et `--sortie:<ms>`. Un retour (plan flouté, cadrage, voile) : classe `ms-retour` et `--retour:<ms>`. Les temps viennent de la transcription mot à mot. L’amorce fait 1 à 4 mots ; le mot clé tient en 6 à 7 signes en 9:16 (sinon `motcle-min`, puis 2 lignes).
- Les zooms et les positions (`--ox`, `--oy`, `--x1`, `--y1`, place du visage) se recalent sur chaque vraie vidéo : les valeurs des aperçus sont celles du plan test.
- Polices : Inter, Doto, JetBrains Mono et Big Shoulders Display (logo seulement) depuis Google Fonts.
- Les valeurs ne s’inventent pas : si un cas manque, demande à Wanzt et ajoute-le ici.
