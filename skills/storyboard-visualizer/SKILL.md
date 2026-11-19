---
name: storyboard-visualizer
description: Transforme le tableau de production d'un STORYBOARD.md (Scène, Code, Durée, Point clé, Type d'animation, Position, Traitement UI/texte, Mouvement, Captions/voix off, Assets, Transition) en une frise horizontale interactive avec timeline proportionnelle et chip de code copiable par scène. Utilise ce skill dès que Wanzt demande de visualiser, afficher, voir en frise, "voir le tableau", explorer, ou remettre à jour la visualisation d'un storyboard, d'un tableau de production vidéo, ou d'un fichier nommé STORYBOARD.md / story.md — même s'il ne prononce pas les mots "skill" ou "storyboard visualizer". Génère aussi les codes de scène (format S{NN}_{slug}) avec l'algorithme slugify partagé avec le pipeline Claude Code, pour que les codes restent identiques partout.
---

# Storyboard Visualizer

Affiche le tableau de production d'un STORYBOARD.md sous forme de frise horizontale
interactive : bandeau de synthèse (timeline proportionnelle aux durées) + cartes de
scènes défilant horizontalement, chacune avec un chip de code copiable ancré en bas.

## Étapes

1. Lire le STORYBOARD.md fourni (ou le plus récent dans le contexte) et localiser le
   tableau de production (section généralement titrée « Tableau de production »).
2. Parser chaque ligne en objet scène avec les champs :
   - `id` — numéro de la scène
   - `title` — nom après le tiret (ex. « Preuve Stripe »)
   - `code` — colonne **Code** si elle existe déjà ; sinon la calculer (voir plus bas)
   - `t` — plage horaire (ex. « 0:21–0:24 »)
   - `dur` — durée en secondes, extraite du « (N s) »
   - `anim` — Type d'animation
   - `pos` — Position
   - `point` — Point clé
   - `treat` — Traitement UI / texte
   - `mvt` — Mouvement
   - `vo` — Captions / voix off
   - `assets` — Assets
   - `trans` — Transition
3. Catégorie visuelle de chaque scène (pour la couleur du bloc dans la timeline et le
   fond de carte) :
   - `screen` si Position ou Type d'animation contient « Plein écran » / « screen-rec »
   - `breath` si Type d'animation contient « RESPIRATION »
   - `talk` sinon (défaut, talking-head)
4. Voltage (accent couleur), en cherchant dans le Traitement :
   - « rust » mentionné → `v = "rust"` → pastille `#C2410C`
   - « teal » mentionné → `v = "teal"` → pastille `#0F766E`
   - ni l'un ni l'autre → `v = null` (pas de pastille)
5. Charger silencieusement `visualize:read_me` avec les modules `["diagram","interactive"]`
   avant le premier appel à `show_widget`.
6. Copier `references/widget-template.html`, remplacer uniquement le tableau
   `const scenes = [...]` par les scènes parsées à l'étape 2–4. Garder le reste du
   code identique (timeline, cartes, chip copiable, toggle détail), sauf si Wanzt
   demande explicitement de changer la disposition.
7. Appeler `show_widget` avec ce code, un titre snake_case descriptif (ex.
   `storyboard_<nom-de-la-video>`), et 1–2 `loading_messages` courts et neutres.

## Algorithme de code (doit rester identique partout : storyboard, widget, pipeline Claude Code)

`S{NN}_{slug}` où `NN` = numéro de scène zero-paddé sur 2 chiffres, et `slug` = titre
passé dans :

```js
function slugify(str) {
  return str.normalize('NFD').replace(/[\u0300-\u036f]/g,'')
    .toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/(^-|-$)/g,'');
}
```

Si le tableau source a déjà une colonne **Code**, toujours la réutiliser telle quelle
plutôt que de la recalculer — un code déjà validé/gelé et communiqué ailleurs
(pipeline, prompts précédents) ne doit pas changer.

## Palette (spécifique à ce système de storyboard — ne pas remplacer par des tokens génériques)

- Fond / bordures des cartes et de la timeline : variables CSS du thème
  (`var(--surface-2)`, `var(--border)`, `var(--border-strong)`, `var(--text-primary)`,
  `var(--text-secondary)`, `var(--text-muted)`, `var(--bg-accent)`, `var(--text-accent)`).
- Voltage rust : littéral `#C2410C` — emphase principale, en général une seule par plan.
- Voltage teal : littéral `#0F766E` — emphase alternative rare (ex. garantie).
- Ces deux hex ne sont pas décoratifs : ils reflètent le système de design réel décrit
  dans le STORYBOARD.md (section décisions validées). Ne pas les étendre à d'autres
  usages sans que le document source le précise, et ne pas introduire d'autres hex.

## Points d'attention (bugs déjà rencontrés — corrigés dans le template, ne pas les réintroduire)

- Toujours fixer `line-height` explicitement sur les blocs de texte des cartes
  (titre, type d'animation, position, point clé, détail). Sans ça, un titre qui
  passe sur 2 lignes peut visuellement chevaucher le bloc suivant.
- Pour la ligne « pastille de voltage + titre », ne pas utiliser
  `display:flex; align-items:center` quand le titre peut être long — le template
  utilise une pastille en `inline-block` + `vertical-align:middle` et laisse le
  titre en flux normal, pour que le wrap sur 2 lignes ne chevauche jamais le
  bloc suivant.
- Le conteneur de cartes reste `overflow-x:auto` en ligne (pas de carousel à onglets,
  pas de contenu cliqueté en `display:none` avant interaction) : tout le contenu
  compact est visible d'emblée, seul le détail (Traitement / Mouvement / VO / Assets /
  Transition) est replié par défaut et se déplie au clic sur la carte.
- Chaque segment de la timeline du haut reste cliquable et fait défiler
  horizontalement jusqu'à la carte correspondante
  (`scrollIntoView({behavior:'smooth', inline:'center', block:'nearest'})`).
- Le clic sur le chip de code (`stopPropagation`) ne doit jamais déplier/replier
  la carte — ce sont deux zones cliquables indépendantes.

## Hors périmètre

Ce skill est spécifique au format « tableau de production vidéo » de Wanzt (Scène /
Code / Durée / Point clé / Type d'animation / Position / Traitement / Mouvement /
Captions-VO / Assets / Transition). Pour tout autre type de tableau, timeline ou
diagramme, construire un widget ad hoc plutôt que de forcer ce template.
