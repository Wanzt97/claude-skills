---
name: vidiq-thumbnail-text
description: Génère le texte overlay (accroche courte affichée sur l'image) d'une miniature YouTube, ainsi qu'un prompt prêt à coller dans l'outil de génération de miniatures de vidIQ (app.vidiq.com/thumbnails), à partir du titre de la vidéo de Wanzt et de sa description d'idée de miniature. Utilise ce skill dès que Wanzt demande de "trouver le texte pour ma miniature", "rédiger l'overlay", "créer ma miniature avec vidIQ", "faire un prompt vidIQ", donne un titre de vidéo accompagné d'une idée visuelle de thumbnail, ou parle de "texte overlay", "accroche miniature", "texte pour ma thumbnail" — même s'il ne cite pas vidIQ explicitement. Ne pas utiliser pour rédiger le titre de la vidéo lui-même, ni pour la conception graphique complète (c'est vidIQ qui génère l'image, ce skill prépare le texte et la description à lui donner).
---

# Générateur de texte overlay + prompt vidIQ pour miniatures

## Objectif

Ce skill prend deux informations données par Wanzt :
1. **Le titre de la vidéo**
2. **Sa description de l'idée de miniature** (sujet, décor, élément visuel, ambiance)

Et produit deux livrables :
1. Des propositions de **texte overlay** (le texte court affiché sur l'image de la miniature)
2. Un **prompt prêt à copier-coller** dans le champ "Text Input" de vidIQ, qui combine l'idée visuelle et le texte overlay retenu, dans le format que vidIQ interprète le mieux.

## Entrées nécessaires

Si Wanzt n'a donné qu'une seule des deux informations (titre OU idée de miniature), demande uniquement celle qui manque avant de continuer. Ne redemande jamais une information déjà fournie. S'il a donné les deux d'un coup, ne pose aucune question et passe directement à la génération.

## Étape 1 — Analyser le titre

À partir du titre de la vidéo, identifie en une ou deux lignes :
- **La promesse centrale** : qu'est-ce que le spectateur va apprendre, obtenir ou éviter ?
- **L'émotion dominante** qui sert le mieux cette promesse — choisis-en UNE parmi : surprise, curiosité, urgence, soulagement, indignation, désir, peur de rater quelque chose.
- **Le hook déjà présent** dans le titre, pour ne pas le répéter dans l'overlay.

## Étape 2 — Générer le texte overlay

Règle d'or (issue de la doc vidIQ) : **le texte overlay ne doit jamais dupliquer le titre**. Le titre annonce le sujet ; l'overlay ajoute la tension, l'émotion ou le chiffre choc qui donne envie de cliquer.

Produis 3 propositions de texte overlay, chacune :
- **3 à 5 mots maximum** (lisible en gros caractères sur un écran de 5 pouces)
- Alignée sur **une seule émotion** (celle identifiée à l'étape 1)
- Complémentaire au titre, jamais une redite
- En français, sauf si Wanzt précise que la vidéo est dans une autre langue

Présente les 3 options sous forme de liste courte, avec pour chacune l'émotion visée entre parenthèses.

## Étape 3 — Construire le prompt vidIQ

Retiens l'option d'overlay la plus forte (ou celle que Wanzt choisit s'il réagit aux 3 propositions), puis assemble une phrase descriptive courte et concrète — c'est le format que l'IA de vidIQ interprète le mieux (elle réagit mal aux prompts trop longs ou trop abstraits) :

**Format** : « [Sujet/scène de l'idée de Wanzt] + [expression/émotion du sujet] + [décor ou élément clé] + texte en gras qui dit "[overlay retenu]" »

Exemple : « Un créateur surpris devant son écran d'ordinateur, fond bureau minimaliste, texte en gras qui dit "0€ à 10K€" »

Livre ce prompt sur une ligne à part, prêt à copier-coller tel quel dans le champ texte de vidIQ.

## Étape 4 — Rappels qualité (checklist finale)

Affiche brièvement, en 2-3 puces max :
- Un seul message, une seule émotion sur la miniature
- Couleurs à fort contraste (le flux YouTube est sombre — les tons qui ressortent performent mieux)
- Si Wanzt veut apparaître sur la miniature : rappelle la différence **Likeness** (photo attachée avant génération → visage cohérent sur toutes les propositions, utile pour la reconnaissance de marque) vs **Face Swap** (remplacement après génération, sur un visuel déjà choisi)
- Si le rendu de vidIQ ne correspond pas au prompt : suggérer d'ajouter une miniature de référence ou d'utiliser les Smart Commands de vidIQ pour affiner

## Note sur l'identité de marque

Si Wanzt précise que la vidéo appartient à une identité visuelle spécifique (par exemple sa charte personnelle ou une charte de chaîne), adapte les couleurs et le ton mentionnés dans le prompt vidIQ à cette charte. Sinon, reste neutre sur les couleurs et laisse vidIQ proposer l'optimisation CTR par défaut.

## Format de sortie

Toujours répondre avec cette structure, de façon concise (Wanzt veut un livrable actionnable, pas un essai) :

1. Analyse rapide du titre (1-2 lignes)
2. 3 propositions de texte overlay (avec émotion visée)
3. Le prompt vidIQ prêt à copier-coller
4. Checklist qualité (2-3 puces max)
