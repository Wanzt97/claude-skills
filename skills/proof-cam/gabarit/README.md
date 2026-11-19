# Gabarit proof-cam pour HyperFrames

Un projet HyperFrames prêt à copier. Il applique [la fiche](../FICHE.md) : on ne règle ici aucune durée ni aucune courbe, on pose du contenu et des temps.

**La fiche fait foi.** Si une règle change, corriger la fiche, puis recopier la valeur dans `lib/cam-search.js`.

## Ce qu'il y a dedans

| Pièce | Rôle |
|---|---|
| `index.html` | La démonstration : six scènes animées entre des blocs visage, comme un vrai montage. |
| `compositions/` | Un modèle par type de scène. On les copie, on ne les modifie pas. |
| `lib/cam-search.js` | Le moteur : caméra virtuelle, fondus, compteur, surlignage, zoom du visage. Il porte toutes les valeurs de la fiche. |
| `lib/composition.css` | La composition de la fiche : les trois rôles typographiques, les cartes, le surlignage, les objets. Aucune couleur de marque. |
| `lib/habillages/` | Un fichier par habillage : `reference`, `digital-black`, `wanzt`. Couleurs et polices. |
| `assets/fonts/` | Les polices de tous les habillages, avec leurs licences. |
| `voix.mp4` | Une fausse piste muette, pour que la démonstration tourne. À remplacer par les rushs coupés. |
| `storyboard.exemple.json` | Le plan de la démonstration : le format à suivre pour `storyboard.json`. |

## Les six modèles

| Modèle | Types de scène couverts | Décision de la fiche |
|---|---|---|
| `m01-mur-vignettes` | mur de vignettes, extrait vidéo, zoom à travers | montrer le nombre, ouvrir par une preuve |
| `m02-frise-compteur` | frise, compteur, pièce liée | un fait chiffré et daté |
| `m03-piece-a-conviction` | pièce à conviction, surlignage, note « * » | un fait prouvé par sa source |
| `m04-texte` | texte mot à mot, chute en italique, titre masqué, fond clair | une définition, une citation |
| `m05-objet-filaire` | objet filaire | une idée abstraite |
| `m06-interface` | maquette d'interface, extrait en cadre, logos en énumération | un produit en usage, un exemple |

Le douzième type, le texte sur le visage, est dans `index.html`.

Si un passage demande un type qui n'est pas dans cette liste, le dire : on ne l'invente pas en cours de montage.

## Monter une vidéo avec le gabarit

1. Copier tout le dossier `gabarit/` dans le projet vidéo, sans les dossiers cachés que le studio y laisse.
2. Remplacer `voix.mp4` par les rushs coupés. Mettre sa durée dans `data-duration`, sur la racine et sur la vidéo.
3. Pour chaque scène animée du storyboard, copier le modèle qui correspond dans `compositions/`, sous un nouveau nom (`s03.html`). Remplacer l'identifiant du modèle (`m02`) partout dans le fichier.
4. Changer les textes, déposer les vraies captures dans `assets/preuves/` et les extraits dans `assets/broll/`.
5. Régler la section **LES BEATS** du fichier : ce sont les seuls chiffres à toucher. Ils viennent de la transcription, en secondes comptées depuis le début de la scène.
6. Dans `index.html`, poser un bloc par scène (`data-start`, `data-duration`) et lister les blocs visage dans `BLOCS_VISAGE`.
7. Supprimer les scènes de démonstration qui ne servent pas.

## Ce que le moteur sait faire

Chaque fonction applique une règle de la fiche. Les temps sont en secondes locales à la scène.

| Fonction | Effet |
|---|---|
| `p.cadrer(cible, zoom)` | cadrage de la première image |
| `p.voler(t, cible, zoom)` | vol de caméra ; renvoie l'instant où elle se pose |
| `p.aGauche(cible)` | cible qui ancre un texte héros à gauche, à 24 % du cadre |
| `p.traverser(t, cible)` | zoom à travers, jusqu'à ce que la cible remplisse l'écran |
| `p.auMot(t)` | ajoute les 100 ms de calage après le début d'un mot |
| `p.apparaitre(cible, t)` | fondu d'entrée, sur place |
| `p.surgir(cible, t)` | vignette vidéo : visible d'un coup |
| `p.cascade(cible, t)` | éléments décoratifs, 200 ms entre chacun |
| `p.motAMot(cible, temps)` | texte mot à mot ; un temps par mot |
| `p.titreMasque(cible, t)` | lettres qui montent de sous la ligne |
| `p.compteur(cible, {a, t, fin})` | compteur qui s'arrête à la fin du nombre prononcé |
| `p.surligner(cible, t)` | surlignage, à lancer quand le vol se pose |
| `p.eteindre(cible, t)` | focus par extinction : l'élément quitté passe en gris |
| `p.desaturer(cible, t)` | l'extrait précédent perd sa couleur |
| `p.accentuer(cible, t)` | passe un élément à la couleur d'accent |
| `p.basculer(cible, t)` | carte qui bascule en 3D et reste inclinée |
| `p.pastille(cible, t)` | point de frise |
| `p.taper(cible, texte, t)` | texte tapé au clavier |
| `p.barre(cible, t, durée)` | jauge qui se remplit |
| `CamSearch.visage(tl, cible, blocs)` | zoom lent du visage, de 100 à 104,4 % par bloc |
| `CamSearch.motsSurVisage(tl, cible, temps)` | texte sur le visage |

La dérive lente entre deux vols est automatique : l'image ne se fige jamais.

## Vérifier

```bash
node ../scripts/verifier-jetons.mjs
```

Pour un projet vidéo, donner son dossier : `node <dossier-du-skill>/scripts/verifier-jetons.mjs videos/<projet>`.

```bash
npx hyperframes check --snapshots
```

Le contrôle HyperFrames doit finir sur « Check passed ». Il signale un contraste insuffisant sur les éléments éteints : c'est voulu, c'est le focus par extinction.

Regarder ensuite une image au milieu de chaque scène, puis recalculer les indicateurs de la section 9 de la fiche. Le rendu final ne se lance qu'après l'accord de Wanzt.

## Changer d'habillage

Dans `index.html`, une seule ligne choisit l'habillage :

```html
<link rel="stylesheet" href="lib/habillages/reference.css">
```

Remplacer `reference` par `digital-black` ou `wanzt`. Mettre le même nom dans le champ `habillage` de `storyboard.json` : l'export scène par scène s'en sert.

Rien d'autre ne change. Les modèles de scène ne connaissent ni les couleurs ni les polices : ils demandent « le fond principal », « l'accent », « la police des chiffres ».

Une scène est sur le fond principal de l'habillage. La classe `cs-second` la passe sur le fond secondaire (modèle `m04`). Selon la marque, le principal est sombre (référence, Digital Black) ou clair (Wanzt).

Pour créer un habillage : suivre « Créer un autre habillage » dans `../HABILLAGE-reference.md`.

## Les limites à connaître

- **Tout le contenu de la démonstration est fictif.** Les blocs rayés « À remplacer » tiennent la place des captures, extraits et logos que Wanzt fournit. Une preuve n'est jamais inventée.
- **Le surlignage est réglé pour une capture claire.** Sur une capture sombre, le texte ne restera pas lisible sous l'accent : prévoir une capture en mode clair.
- **Les mouvements des objets filaires ne sont pas mesurés** dans la référence. Le modèle prend la courbe de la caméra et une seconde par cran de rotation.
- **Les bruitages ne sont pas dans le gabarit.** Les fichiers viennent de la bibliothèque de l'outil ; les règles sont dans [SIGNATURE-wanzt.md](../SIGNATURE-wanzt.md).
- **La position d'une cible se mesure quand la scène devient visible.** Ne pas changer la taille d'un élément en cours de scène : la caméra viserait à côté.
- **Une seule scène a été rendue en vidéo** (`m02`, 11 s). Les cinq autres ont passé le contrôle HyperFrames et une revue image par image, pas un export.
