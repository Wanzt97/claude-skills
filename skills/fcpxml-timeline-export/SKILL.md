---
name: fcpxml-timeline-export
description: Convertit un fichier .fcpxml (Final Cut Pro) en un JSON autonome et exploitable par un agent qui n'a pas accès au FCPXML mais a accès au dossier de rushs — utilisé pour importer le montage dans PalmierPro (qui ne prend pas en charge .fcpxml). Résout toutes les références internes (assets, effets), calcule les positions absolues sur la timeline, sépare le texte parlé des notes de montage (hashtags de type de plan, indications de mouvement), et ne perd jamais une information du fichier source. Utilise ce skill dès que Wanzt upload un fichier .fcpxml et demande de le "convertir", de l'"exporter pour PalmierPro", de "reconstruire la timeline/le montage", ou tout simplement dès qu'un .fcpxml apparaît dans la conversation sans qu'il ait besoin de préciser le format de sortie.
---

# FCPXML → JSON de reconstruction de timeline

## Contexte

Wanzt monte ses vidéos sur Final Cut Pro. Pour certains projets, il envoie
ensuite le dossier de rushs (media) + un JSON à un agent externe (PalmierPro)
qui reconstruit/exploite le montage — mais PalmierPro ne sait pas lire le
`.fcpxml` directement. Ce skill produit le JSON qui sert d'intermédiaire.

**Principe non négociable : aucune information du FCPXML ne doit être perdue.**
Si quelque chose ne peut pas être interprété proprement, il doit être capturé
en brut plutôt qu'ignoré — voir "Gestion des cas non prévus" plus bas.

## Étapes

1. **Localiser le fichier** `.fcpxml` uploadé (vérifier `/mnt/user-data/uploads/`
   si besoin — ne jamais supposer qu'il est présent sans vérifier).

2. **Lancer le script de conversion** :
   ```bash
   python3 scripts/fcpxml_to_json.py <chemin_du_fcpxml> /mnt/user-data/outputs/<nom>_timeline_reconstruction.json
   ```
   Le script gère tout : résolution des références, calcul des positions
   absolues, séparation notes/script, extraction des rappels de production
   généraux. Ne pas réécrire cette logique à la main dans le chat — utiliser
   le script.

3. **Lire la sortie console du script.** Elle indique :
   - le nombre de segments et d'assets traités
   - le nombre de notes de production générales extraites
   - un éventuel bloc `⚠ avertissement(s)` listant les éléments FCPXML
     rencontrés que le script n'a pas su interpréter spécifiquement (ils
     sont quand même dans le JSON, en `raw_xml`, mais signalent qu'il vaut
     la peine de relire cette partie du fichier à la main avant d'envoyer
     le JSON à PalmierPro).

4. **Si des avertissements apparaissent** : ouvrir le JSON, chercher les
   entrées avec `raw_xml`, et décider avec Wanzt si elles méritent d'être
   intégrées proprement au schéma (nouveau type de segment, nouvel effet,
   etc.) — ne jamais les supprimer silencieusement.

5. **Présenter le fichier** avec `present_files`, et rappeler explicitement
   à Wanzt (en une phrase, pas un pavé) la liste `media_files_required` :
   c'est ce qu'il doit s'assurer d'avoir dans le dossier de rushs uploadé à
   PalmierPro, puisque les chemins d'origine (Mac) ne seront pas valides
   ailleurs — seul le nom de fichier compte pour le matching.

## Schéma de sortie (aperçu)

```
_meta                        — résumé, liste des fichiers médias requis, avertissements
project / format / sequence  — métadonnées du montage (résolution, fps, durée totale)
resources.assets             — chaque rush : nom, filename (pour matching), codecs, chemin d'origine (informatif seulement)
resources.effects            — effets utilisés (ex: "Basic Title")
resources.other_resources    — tout type de ressource FCPXML non prévu, capturé en brut
general_production_notes     — rappels qui concernent toute la vidéo, pas un plan précis
timeline.primary_track[]     — un objet par segment de la piste principale :
  - type: "clip" | "gap"
  - source_asset (résolu : ref + name + filename)
  - timeline_offset/duration (secondes + timecode + frames)
  - source_in_point / source_out_point (bornes dans le fichier source)
  - connected_items[]         — titres (texte/overlay) et b-roll superposés (lanes) :
      - type "title" : text_raw (intact), shot_tags, direction_notes, script_text (séparés), text_style
      - type "asset-clip" : b-roll résolu avec ses propres positions/bornes
      - type "marker" : marqueurs Final Cut le cas échéant
```

`shot_tags` = hashtags (`#CamIphone`, `#soneffect`...) = type de plan/effet
sonore. `direction_notes` = lignes `//...` = indications de mouvement/transition
pour le plan précis. `script_text` = texte parlé/sous-titre. Ces trois champs
sont dérivés de `text_raw`, qui reste présent intégralement à côté — rien n'est
perdu même si le découpage automatique se trompe sur un cas particulier.

## Gestion des cas non prévus

Ce fichier a été conçu à partir d'un seul projet (caméras + gap + titres en
lane 1 + b-roll en lane 2, pas de transitions ni de multicam). Si un futur
projet contient des éléments différents (transitions, clips composés,
multicam, marqueurs, rôles audio multiples...), le script les capture quand
même via son mécanisme de repli générique (`raw_xml` + entrée dans
`_warnings`) plutôt que de planter ou de les ignorer. Dans ce cas :

- Ne pas cacher l'avertissement à Wanzt — le mentionner brièvement.
- Si le même type d'élément revient dans plusieurs projets, ça vaut le coup
  d'ajouter un vrai handler dans `scripts/fcpxml_to_json.py` (suivre le
  patron de `parse_title` / `parse_connected_clip`) plutôt que de rester sur
  la capture brute indéfiniment.

## Autres formats de sortie possibles

Si Wanzt demande autre chose que le JSON pour PalmierPro (ex: un script
markdown lisible pour analyse narrative, ou un dump JSON 100% brut de l'arbre
XML sans aucune résolution), ce n'est pas ce que fait ce script — proposer de
construire l'export correspondant à la volée plutôt que de forcer ce schéma-ci.
