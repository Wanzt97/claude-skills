---
name: "fusion-inspirations-design"
description: "Critique des inspirations de design (liens Refero Styles, etc.) pour une marque de Wanzt, choix de ce qu'on garde, puis prompt de fusion en un design system / brand kit."
---

# Fusion d'inspirations design → design system

Workflow en dialogue pour construire le design system d'une marque de Wanzt à partir d'inspirations (souvent des liens styles.refero.design). Wanzt colle des liens et dit ce qui lui plaît dans chacun ; Claude critique, on décide ensemble ce qu'on garde, puis Claude rédige le prompt qui fusionne tout.

Réponses en français, directes, peu de questions. Mode apprentissage : toujours expliquer la logique (le « pourquoi »), pas seulement le verdict.

## Étape 0 — Cadrer la marque (rapide)

Avant de critiquer, établir en 2-3 lignes :
- **La marque** et son sujet (vérifier la mémoire : Digital Black, marque perso wanzt-identite, Funelio, uwrite…).
- **Où le design sera vu en priorité** : miniatures YouTube, vidéo / brand kit pour agents de montage, site web, app… C'est le critère n°1 de toute la critique.
- **La direction couleur déjà posée** s'il y en a une.

Ne poser une question que si l'info manque vraiment ; sinon prendre une hypothèse raisonnable et l'énoncer.

Repères des marques existantes (pour garder chaque univers distinct, avec l'orange comme fil commun = couleur d'action) :
- Digital Black : noir dominant, orange accent, grille gommée, monospace, typo massive.
- Marque perso : cobalt / orange / crème, Archivo · DM Sans · Caveat, grain, correction au feutre bleu.
- Funelio : navy, orange, blanc cassé, charcoal ; Monument Extended, DM Serif Display, Neue Montreal, DM Sans ; motif de flux / nœuds.
- uwrite : outil de travail, neutre et calme, accent orange adouci.

## Étape 1 — Lire chaque inspiration

Pour chaque lien, WebFetch avec un prompt qui demande : nom, source, palette (hex + rôle), typographies, angles, ombres, composants, mise en page, ET en détail l'élément que Wanzt dit avoir aimé (ex. le fond).

Si la fiche ne documente pas l'élément qu'il a aimé (fréquent pour les fonds animés ou les effets visuels) : le dire honnêtement, proposer une interprétation, et demander une capture si l'interprétation risque d'être fausse.

## Étape 2 — Critique, inspiration par inspiration

Format pour chaque lien :
- **Nom + ambiance** en une phrase, avec les valeurs clés (hex, typo, angles).
- **Ce qui colle** à la marque.
- **Ce qui coince**, jugé d'après le support principal.

Règles de jugement :
- **Un style se juge là où il sera vu.** Les styles Refero sont pensés pour des sites en grand ; en miniature ou en vidéo, tout ce qui est fin (contours, titres légers, grilles serrées) perd sa force, tout ce qui est massif et plein en gagne.
- **Un seul accent chromatique**, utilisé rarement, pour ce que l'œil doit voir en premier. Toute couleur d'accent supplémentaire est à écarter ou à remplacer par l'accent de la marque.
- Repérer les contradictions internes des fiches Refero (ex. rayon de 9999px dans le prompt guide alors que la fiche dit « rien de rond ») et suivre les règles Do/Don't.
- Vérifier que la marque reste distincte des autres marques de Wanzt.

## Étape 3 — Proposer la fusion

Attribuer un **rôle** à chaque inspiration, pour éviter qu'une moyenne de tout donne un style tiède :
- **Base** : le style dominant.
- **Emprunt** : un ou deux éléments précis seulement.
- **Élément signature** (ex. le fond).
- **Presque rien** : on ne garde qu'une idée.

Terminer par un récap « Ta direction, à ce stade » en une liste courte, et signaler le principal piège (souvent : la version miniature / petit format). Laisser Wanzt valider ou ajuster. Répéter les étapes 1-3 à chaque nouvel ajout de liens.

## Étape 4 — Rédiger le prompt de fusion

Quand Wanzt le demande (il va télécharger les DESIGN.md des inspirations et les donner à Claude), livrer dans la réponse un prompt prêt à coller, dans un bloc de code, sur ce modèle :

```
Tu es directeur artistique. Je te joins N fichiers DESIGN.md issus de Refero Styles. Ta mission : fusionner les éléments retenus en UN SEUL design system pour « <marque> ».

## Contexte
<marque, sujet, public>
Usage principal : <support prioritaire>. Usages secondaires : <…>.
[Si brand kit pour agents de montage :] Ce design system sert AVANT TOUT à produire des brand kits pour le montage vidéo, donnés à des agents IA (PalmierPro, HyperFrames) et à des monteurs humains. Chaque règle doit être explicite et chiffrée (hex, px, %, ms, cubic-bezier), applicable sans interprétation. Pas de « subtil » ou « élégant » sans valeur.
<règle de base couleur : couleur dominante + un seul accent>

## Ce qu'on garde et ce qu'on écarte, fichier par fichier
### 1. <Nom> → <RÔLE>
GARDER : <liste précise avec valeurs>
ÉCARTER : <liste + raison courte>
AJOUTER (si besoin) : <évolution décidée ensemble>
### 2. …

## Usage <support prioritaire> (prioritaire)
<contraintes spécifiques. Pour la vidéo : formats 16:9 et 9:16 avec zones de sécurité, sous-titres, cartons de section, lower thirds, mise en avant des chiffres, fond fixe et animé, durées et easings, transitions autorisées/interdites. Pour les miniatures : tailles plus grandes, éléments moins nombreux, contraste fort.>

## Règles de fusion
- En cas de contradiction, priorité : <Base> > <…> > <…>, sauf éléments explicitement retenus.
- Un seul accent chromatique : <couleur>. Tout le reste en neutres.
- L'accent reste rare : il désigne ce que l'œil doit voir en premier.

## Livrables
1. DESIGN.md : référence lisible par un humain (palette nom+hex+rôle, typos avec alternatives gratuites, espacements, angles, composants, règles signature, usage de l'accent, variantes par support, À faire / À ne pas faire). Chaque décision avec une phrase de POURQUOI.
2. brand-kit.json : tous les tokens en format machine (couleurs, typos, tailles, espacements, durées, easings, zones de sécurité).
3. AGENT.md : instructions courtes et impératives pour un agent (« Toujours… », « Jamais… », « Si… alors… »), sans explications.
4. Une page HTML de démonstration : palette, typo, élément signature (animé si pertinent), composants clés, exemples sur le support prioritaire.
```

Adapter les livrables au besoin : JSON et AGENT.md seulement si des agents vont consommer le kit ; exemples HTML selon le support (miniatures, sous-titres, écrans d'app…).

Après le prompt, ajouter 2-3 puces « Pourquoi le prompt est construit comme ça » : rôles attribués (évitent la moyenne tiède), règle de priorité (règle d'avance les conflits), contrainte du support isolée, et si besoin la séparation humain (pourquoi) / machine (quoi exactement).