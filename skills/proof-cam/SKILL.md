---
name: "proof-cam"
description: "Monte des rushs face caméra dans le style proof-cam avec HyperFrames : dérush, plan phrase par phrase, scènes animées sur canevas sombre avec caméra virtuelle, preuves surlignées. Fournit aussi les scènes animées seules, en clips, pour ChatCut ou Palmier Pro. À utiliser quand Wanzt demande le style proof-cam (ancien nom : cam-search), le style theyo, ou de monter ses rushs avec ce motion design."
---

# proof-cam

Ce skill prend les rushs de Wanzt (face caméra, français) et produit une vidéo dans le style proof-cam : le visage fait tourner le raisonnement, le motion design montre tout ce qui est réel.

Le style n'est pas décrit ici. Il vit dans trois fichiers de ce dossier, et ce skill ne fait que les appliquer.

| Fichier | Ce qu'il contient | Quand le lire |
|---|---|---|
| `FICHE.md` | La grammaire : quand animer, comment, à quel rythme, ce qu'on ne fait jamais. **Elle fait foi.** | En entier, avant le plan. |
| `HABILLAGE-*.md` | Couleurs, polices, textures. Un fichier par habillage : `reference` (theyo), `digital-black`, `wanzt`. | Avant la construction : celui que Wanzt a choisi. |
| `SIGNATURE-wanzt.md` | Les deux bruitages de Wanzt. | Avant de poser le son. |
| `gabarit/` | Un projet HyperFrames prêt à copier : six modèles de scène, un moteur, un habillage. | Avant la construction : lire `gabarit/README.md`. |
| `references/bruitages-par-outil.md` | Les noms de fichiers et réglages de son selon l'outil. | Au moment de poser le son. |
| `scripts/` | Contrôle du plan, contrôle des valeurs, export scène par scène. | Aux étapes 3, 6 et 7. |

Déclencheurs : « monte mes rushs en proof-cam », « style proof-cam », « fais-le en proof-cam », « style theyo », « fais les animations proof-cam pour ChatCut ». L'ancien nom, « cam-search », déclenche aussi ce skill.

## Les quatre règles qui ne se discutent pas

1. **La fiche fait foi.** Si elle contredit ce skill, le gabarit ou une habitude HyperFrames, c'est elle qui a raison.
2. **Aucune durée, aucune courbe écrite à la main.** Tout mouvement passe par les fonctions du moteur (`gabarit/lib/cam-search.js`). Dans une scène, les seuls chiffres qu'on règle sont les temps de la voix.
3. **La liste des scènes est fermée.** Douze types, six modèles (FICHE, section 7). Si un passage demande autre chose, le dire à Wanzt et proposer le modèle le plus proche. Ne pas inventer un treizième type en cours de montage.
4. **Une preuve est toujours réelle.** Tweet, article, page, interface, logo, extrait : fournis par Wanzt. S'il en manque un, laisser le bloc « À remplacer » du modèle et l'ajouter à la liste des pièces à fournir. Ne jamais inventer une citation, un chiffre ou une capture.

## Avant de commencer

- **HyperFrames.** Lire `/hyperframes-core` (contrat de composition) avant d'écrire du HTML, et utiliser `transcript-cut.mjs` de `/media-use` pour les coupes. Si ces skills ne sont pas disponibles dans le projet, le dire à Wanzt. Ne pas les installer soi-même : la commande d'installation les répand dans tous ses projets, ce qu'il ne veut pas.
- **Ce skill remplace le routage de `/hyperframes`** pour cette demande. Ne pas utiliser `talking-head-recut` : il pose des cartes par-dessus la vidéo, alors qu'ici on coupe les rushs et l'animation occupe 69 % du temps.
- **Le style prime sur les défauts HyperFrames.** Les blueprints HyperFrames proposent des rebonds, du flou de mouvement, des lueurs, des sous-titres. Rien de tout cela ici. Les règles techniques de `/hyperframes-core` (lint, déterminisme, sous-compositions) restent obligatoires.
- Vérifier l'environnement : `npx hyperframes doctor`.

## Deux façons de travailler

Demander à Wanzt laquelle il veut s'il ne l'a pas dit.

| Mode | Entrée | Sortie | Étapes |
|---|---|---|---|
| **Montage complet** | Les rushs bruts. | La vidéo finie, visage et animations. | 1 à 7 |
| **Animations seules** | Une vidéo déjà coupée ailleurs (ChatCut, Palmier Pro). | Un clip par scène animée, et la liste des endroits où les poser. | 2 à 7, sans le dérush |

En mode « animations seules », les clips sont plein cadre et opaques : ils se posent sur une piste au-dessus du visage, en coupe franche. Le zoom lent du visage (de 100 à 104,4 % par bloc) reste à faire dans l'outil de montage : le rappeler à Wanzt.

Tout vit dans `videos/<nom-du-projet>/`.

## Étape 1 : dérush

**Inventaire.** Lister les rushs (`ffprobe` : durée, résolution, images par seconde). Ordre : celui du script si Wanzt en fournit un, sinon l'ordre des noms de fichiers, sinon la date de création. Annoncer l'ordre retenu en une ligne.

**Transcription de chaque rush**, en français :

```bash
npx hyperframes transcribe rushs/rush-01.mp4 -d derush/rush-01 --json --language fr
```

Corriger les noms propres et les termes techniques mal transcrits, sans toucher aux temps.

**Choix des prises.**
- Quand une phrase est dite plusieurs fois, garder la dernière prise complète.
- Retirer les faux départs, les phrases abandonnées, les « euh », « heu », « hum ». Garder les tics qui font la voix de Wanzt (« bah », « en fait »), sauf s'ils s'empilent.
- Lister les cas douteux dans le bilan, sans bloquer.

**Coupes.** La voix ne laisse aucun trou (FICHE, section 6).

```bash
node <MEDIA_USE_DIR>/scripts/transcript-cut.mjs \
  --input rushs/rush-01.mp4 \
  --transcript derush/rush-01/transcript.json \
  --remove "12.41-15.02,88.30-91.70" \
  --remove-fillers "euh,heu,hum" \
  --cut-silence 0.35 \
  --out derush/rush-01.cut.mp4
```

Passer d'abord `--plan` pour vérifier les segments gardés. Assembler ensuite les rushs coupés en un seul `voix.mp4` (concat ffmpeg, réencodage pour des coupes nettes).

## Étape 2 : transcription en temps de montage

```bash
npx hyperframes transcribe voix.mp4 -d . --json --language fr
```

Ce `transcript.json` donne le temps de chaque mot dans la vidéo finale. Tous les temps d'animation en sortent. Regrouper les mots en phrases, à la ponctuation et aux pauses.

## Étape 3 : le plan

1. **Classer chaque phrase** avec le tableau de décision de la fiche (section 3) : poser les sept questions dans l'ordre et s'arrêter à la première réponse « oui ». Noter le numéro de la décision.
2. **Appliquer les arbitrages** de la même section. Les deux pièges : un mot de liaison (« donc », « parce que oui ») ne suffit pas à ramener le visage, et un fait l'emporte toujours.
3. **Regrouper en planches.** Les faits d'un même sujet vont sur la même planche, la caméra glisse de l'un à l'autre. Respecter le rythme de la section 3 : durée d'une planche, durée d'un bloc visage, absence maximale du visage.
4. **Choisir un modèle du gabarit** pour chaque planche (`gabarit/README.md`). Un passage sans modèle : le signaler.
5. **Régler le début et la fin** avec la partie « Début, milieu, fin » de la fiche.

**Sorties.**
- `STORYBOARD.md`, avec les colonnes du skill `storyboard-visualizer` : Scène | Code | Durée | Point clé | Type d'animation | Position | Traitement UI/texte | Mouvement | Captions/voix off | Assets | Transition. Laisser **Code** vide. Dans **Point clé**, mettre le numéro de la décision et sa raison.
- `storyboard.json`, au format de `gabarit/storyboard.exemple.json` : une entrée par bloc visage et par scène animée, avec son modèle, sa décision et ses beats.

**Contrôle du plan.** Avant de le montrer :

```bash
node <DOSSIER_DU_SKILL>/scripts/controle-plan.mjs storyboard.json
```

Corriger le plan tant qu'une ligne affiche « À REVOIR », ou expliquer à Wanzt pourquoi on la laisse.

## Étape 4 : validation

C'est le seul arrêt obligatoire. Montrer à Wanzt :

- le résultat du contrôle du plan ;
- le nombre de scènes et d'animations ;
- l'habillage retenu, ou la question s'il n'a pas été choisi ;
- les pièces à fournir (captures, extraits, logos, musique) ;
- les prises douteuses ;
- **les trois décisions les moins évidentes**, chacune avec sa raison en une phrase. Wanzt apprend ainsi à les prendre lui-même.

Construire après son accord, ou tout de suite s'il a dit d'enchaîner.

## Étape 5 : construction

1. Copier `gabarit/` dans `videos/<projet>/`, sans les dossiers cachés.
2. Suivre « Monter une vidéo avec le gabarit » dans `gabarit/README.md` : une copie de modèle par scène, les textes, les pièces, puis la section **LES BEATS**.
3. Les beats sont en secondes **locales à la scène** : temps du mot dans `transcript.json`, moins le `data-start` de la scène.
4. Appliquer l'habillage que Wanzt a choisi : `reference`, `digital-black` ou `wanzt`. S'il ne l'a pas dit, le lui demander avec la validation du plan : c'est le choix de la marque qui signe la vidéo. Il se règle en une ligne dans `index.html` et dans le champ `habillage` de `storyboard.json` (voir `gabarit/README.md`). Lire le fichier `HABILLAGE-<nom>.md` avant : chacun a ses particularités. Une autre marque demande d'abord son fichier d'habillage, sur le modèle de `HABILLAGE-reference.md`.
5. Poser la musique et les bruitages : règles dans `SIGNATURE-wanzt.md`, fichiers et réglages dans `references/bruitages-par-outil.md`.

## Étape 6 : contrôle

1. `node <DOSSIER_DU_SKILL>/scripts/verifier-jetons.mjs videos/<projet>` : le moteur du projet doit dire la même chose que la fiche.
2. `npx hyperframes check --snapshots` jusqu'à « Check passed ». Un avertissement de contraste sur un élément éteint est normal : c'est le focus par extinction.
3. Regarder une image au milieu de chaque scène. Vérifier : un seul accent, texte héros à gauche, pièces lisibles, visage présent aux bons moments.
4. Relancer `controle-plan.mjs` si le plan a bougé pendant la construction.
5. Relire la liste « Ce que le style ne fait jamais » de la fiche (section 8), ligne par ligne.
6. `npx hyperframes preview` pour que Wanzt regarde.

## Étape 7 : rendu

Seulement après l'accord de Wanzt.

**Montage complet :**

```bash
npx hyperframes render --quality draft -o renders/brouillon.mp4
npx hyperframes render --fps 30 --quality delivery -o renders/final.mp4
```

**Animations seules :**

```bash
node <DOSSIER_DU_SKILL>/scripts/exporter-scenes.mjs videos/<projet>
```

Chaque scène sort dans `renders/scenes/`, avec son instant de départ dans le nom. `placement.csv` dit où poser chaque clip dans l'autre outil.

## Exemple de lecture

```
[00:41.20] Sauf que le 24 septembre dernier, Higgsfield annonce avoir dépassé un rythme d'un milliard de dollars de revenus par an en 18 mois. Et le même jour, OpenAI coupe pour de bon l'accès à Sora.
[00:56.84] D'ailleurs, c'était un modèle dont Higgsfield était, d'après Forbes, le plus gros client. Alors, comment est-ce qu'une boîte…
```

- « Sauf que » ouvre la phrase, mais elle porte une date, un montant, une durée : **décision 1**, animation. Modèle `m02-frise-compteur`.
- Le milliard et Sora tombent le même jour : **même planche**, la caméra vole de la frise à la pièce.
- « d'après Forbes » : **décision 1**, la source se montre. Modèle `m03-piece-a-conviction`.
- « Alors, comment est-ce que… » : une question. **Décision 7**, coupe franche vers le visage, pour une phrase.

## Limites

- Le style vient d'une seule vidéo. Chaque règle de la fiche porte son niveau de preuve : s'y fier en conséquence.
- Les preuves, extraits, logos et musique viennent de Wanzt. Le skill ne les fabrique pas.
- Le gabarit vise HyperFrames. Pour ChatCut et Palmier Pro, seul le mode « animations seules » existe.
- Trois habillages existent : la référence, Digital Black et Wanzt. Funelio n'a pas le sien.
- Les habillages de marque ont été vus sur la démonstration du gabarit, pas sur une vraie vidéo.
