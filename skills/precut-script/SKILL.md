---
name: "precut-script"
description: Rédige ou reformate un script vidéo pour qu'il se colle directement dans l'éditeur de Precut (un paragraphe = un plan, titres
---

# Écrire pour Precut

Precut est un outil de pré-production : on écrit le script, on lie des rushs aux paragraphes, puis on exporte une timeline. Le script doit donc être écrit comme un découpage, pas comme un texte à lire.

## Les règles de l'éditeur

- **Un paragraphe = une coupe.** Chaque nouveau paragraphe peut être lié à un clip. Un changement d'image à l'écran = un nouveau paragraphe.
- **Titre avec `#`** : sert à structurer le script. Il n'est pas exporté vers la timeline.
- **Sous-titre avec `##`** : pour les sous-parties sous un titre.
- **Pas de hashtags.** Wanzt tague ses paragraphes lui-même, à la main, dans Precut. Ne jamais écrire de tags (`/#...`) dans le script.
- **Commentaire avec `//`** : ligne placée sous un paragraphe. Il est exporté vers la timeline, donc visible par le monteur. C'est là que vont les consignes visuelles.
- Le texte est un éditeur classique (gras et italique possibles). Les autres commandes passent par le menu `/`.

## Comment rédiger

1. **Le corps du paragraphe ne contient que la voix**, dite d'un souffle. Pas de didascalie, pas de « [coupe] », pas de timecode dans le texte.
2. **Une idée par paragraphe.** Si une phrase change d'image, on la coupe en deux paragraphes.
3. **Toute consigne visuelle va en commentaire `//`**, directement sous le paragraphe concerné : plan, texte à l'écran (3 à 6 mots), mouvement, capture à montrer.
4. **Phrases courtes, à l'oral.** Si on ne peut pas la dire sans reprendre sa respiration, on la raccourcit.
5. **Un titre `#` en tête** pour s'y retrouver (nom du projet). Sur une vidéo longue, un titre `#` par grande partie et des sous-titres `##` à l'intérieur.

## Ordre des beats pour un short (30 à 45 s)

1. Hook (la douleur, une rupture, pas la solution)
2. Révélation (le produit ou l'idée)
3. Preuve (ce qu'on voit à l'écran, une phrase = une image)
4. Contraste (reboucle sur le hook)
5. Appel à l'action (une phrase)

Pour écrire le hook, appliquer la méthode du skill `hook-architect`.

## Garde-fous

- Ne jamais inventer une fonctionnalité du produit présenté. Pour le beat de la preuve, partir de ce que Wanzt a réellement filmé ou décrit ; si l'info manque, écrire une version marquée comme à vérifier et le dire.
- Ne pas affirmer de comportement de Precut au-delà des règles ci-dessus (lien paragraphe/clip, export, formats).

## Format de sortie

Toujours livrer le script dans **un seul bloc de code**, prêt à copier, puis, hors du bloc, une ligne sur ce qui reste à vérifier.

````
# Nom du projet

Voix du premier plan.
// Consigne visuelle du premier plan

Voix du deuxième plan.
// Consigne visuelle du deuxième plan
````
