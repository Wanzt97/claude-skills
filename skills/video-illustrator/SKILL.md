---
name: video-illustrator
description: "Analyse une transcription vidéo horodatée (format ElevenLabs Scribe, style '[MM:SS] texte') ligne par ligne pour décider où placer une animation à l'écran et ce qu'elle doit montrer, par opposition aux moments où un simple sous-titre suffit. Utilise ce skill dès que Wanzt partage un script ou une transcription et demande 'annote mon script', 'où placer les animations', 'quelles lignes ont besoin d'un visuel', 'planifie les animations de cette vidéo', 'quels moments sont cruciaux pour la compréhension', ou parle de rétention, moments de respiration, swipe en lien avec le montage. Ne pas utiliser pour écrire le script lui-même (funelio-copy:copywriter), ni pour le montage/rendu technique final (skill supermonteur) — ce skill se situe entre les deux : il planifie, il ne rédige ni ne monte."
---

# Annotateur Visuel

## Pourquoi ce skill existe

À l'écran, un visuel remplit toujours l'une de ces deux fonctions (jamais aucune des deux, jamais les deux en même temps par accident — c'est un choix) :

1. **Expliquer** — le spectateur comprend un concept bien plus vite en le voyant qu'en l'entendant seul.
2. **Retenir** — chaque animation garde la vidéo "vivante" pour empêcher le spectateur de swiper.

Un monteur senior ne décore pas un script au hasard. Il le lit ligne par ligne et se pose une seule question pour chacune : **cette ligne est-elle cruciale pour la compréhension du spectateur ?**

- **Oui** → elle reçoit une animation qui explique le propos.
- **Non, c'est un moment de respiration** → elle reste en simple sous-titre, pour que le spectateur se repose et se reconnecte à l'orateur.

Ce skill applique exactement ce test à n'importe quel script, ligne par ligne, et documente le résultat.

## Processus

Pour chaque ligne horodatée de la transcription, dans l'ordre :

1. **Lire la ligne isolément puis en contexte** (ce qui précède et suit compte — une ligne peut sembler anodine seule mais amorcer un concept développé juste après).
2. **Appliquer le test de comprehension.** Une ligne est **crucial** (→ ANIMATION) si elle fait au moins une de ces choses :
   - introduit un concept, un terme technique, un nom de framework ou une définition ;
   - avance un chiffre, une statistique, un pourcentage, une comparaison ;
   - énumère plusieurs éléments (étapes, options, catégories) qu'il est plus rapide de saisir d'un coup d'œil que d'entendre égrener ;
   - fait une affirmation qui bénéficie d'une preuve visuelle (avant/après, split-screen, courbe) ;
   - contient une métaphore ou une image mentale qu'on peut littéralement dessiner.
3. Une ligne est un **moment de respiration** (→ RESPIRATION, sous-titre simple) si elle :
   - raconte une anecdote personnelle, une transition, une pause narrative ;
   - pose une question rhétorique ou s'adresse directement au spectateur ("toi", "tu") sans apporter d'info nouvelle ;
   - exprime une opinion, une émotion ou une réaction sans contenu factuel à illustrer ;
   - reformule ou résume ce qui vient d'être montré (le visuel précédent suffit encore).
4. **Si l'animation est retenue, préciser ce qu'elle doit montrer** — pas juste "animation", mais le type précis et son contenu (voir catalogue ci-dessous).
5. **Vérifier le rythme global** avant de rendre la sortie (voir garde-fous).

## Catalogue de types d'animation

Choisis le type le plus précis, ne te limite pas à cette liste si un autre type sert mieux la ligne :

| Type | Quand l'utiliser |
|---|---|
| Texte cinétique (mot/phrase clé qui apparaît) | Terme technique, definition courte, punchline |
| Compteur / stat animée | Chiffre, pourcentage, montant |
| Comparaison split-screen (avant/après, A vs B) | Opposition, transformation, "sans X vs avec X" |
| Liste à puces séquencée | Énumération d'étapes, critères, options |
| Diagramme / flowchart | Processus, séquence logique, système |
| Zoom / highlight sur un élément déjà à l'écran | Renforcer un point déjà visible sans nouvel élément |
| Timeline / frise | Évolution dans le temps, historique, roadmap |
| Métaphore visuelle | Concept abstrait qu'on peut représenter par une image concrète |
| B-roll suggéré | Illustrer une action, un contexte, une ambiance |

## Format de sortie

Toujours produire un Markdown annoté ligne par ligne, dans cet ordre exact, en conservant le timestamp d'origine :

```markdown
[MM:SS] **[ANIMATION]** — "texte exact de la ligne"
→ Type : <type précis du catalogue ou équivalent>
→ Contenu : <ce que l'animation montre concrètement, en une phrase>

[MM:SS] **[RESPIRATION]** — "texte exact de la ligne"
→ Sous-titre simple. <raison brève : pourquoi c'est un moment de repos/connexion>
```

Termine toujours la sortie par un court résumé : nombre de lignes ANIMATION vs RESPIRATION, et un signal d'alerte si le rythme pose problème (voir garde-fous).

## Garde-fous de rythme

- **Jamais plus de 3 lignes RESPIRATION consécutives** — au-delà, le spectateur décroche faute de stimulation visuelle. Si le test en produit 4+, retourne à la ligne la moins "creuse" du lot et repasse-la en ANIMATION légère (ex. simple highlight).
- **Jamais 100% ANIMATION non plus** — si chaque ligne reçoit une animation, plus aucune ne se démarque et le spectateur n'a plus de moment pour respirer et se connecter à l'orateur. Un ratio sain tourne généralement autour de 50-70% ANIMATION selon la densité du script (un script très pédagogique/dense penchera plus haut, un script narratif/storytelling plus bas).
- En cas de doute entre les deux catégories, penche du côté qui sert le rythme global plutôt que la ligne prise isolément.

## Exemple travaillé

**Entrée :**
```
[5:34] Les visuels à l'écran font deux choses importantes. D'abord, ils expliquent ce que dit l'orateur — quand un spectateur voit un concept, il le comprend bien mieux qu'avec des mots seuls. Ensuite, ils maintiennent la rétention : chaque animation rend la vidéo fraîche pour que personne ne swipe.
[5:48] Un monteur de haut niveau prend le script et va ligne par ligne, en se posant une question : cette ligne est-elle cruciale pour la compréhension du spectateur ? Si oui, elle reçoit une animation qui l'explique. Si c'est un moment de respiration, elle reste en simple sous-titre pour que le spectateur se repose et se connecte à l'orateur.
```

**Sortie attendue :**
```markdown
[5:34] **[ANIMATION]** — "Les visuels à l'écran font deux choses importantes."
→ Type : Liste à puces séquencée
→ Contenu : deux items qui apparaissent l'un après l'autre : "1. Expliquer" puis "2. Retenir"

[5:34] **[ANIMATION]** — "ils expliquent ce que dit l'orateur — quand un spectateur voit un concept, il le comprend bien mieux qu'avec des mots seuls"
→ Type : Comparaison split-screen
→ Contenu : côte à côte, "mots seuls" (icône oreille, flou) vs "mots + visuel" (icône œil, net)

[5:34] **[ANIMATION]** — "chaque animation rend la vidéo fraîche pour que personne ne swipe"
→ Type : Métaphore visuelle
→ Contenu : une jauge de rétention qui redescend puis qui remonte à chaque pulse d'animation

[5:48] **[ANIMATION]** — "Un monteur de haut niveau prend le script et va ligne par ligne, en se posant une question"
→ Type : Diagramme / flowchart
→ Contenu : une ligne de script qui entre dans une boîte de décision "Crucial ?"

[5:48] **[ANIMATION]** — "cette ligne est-elle cruciale pour la compréhension du spectateur ? Si oui, elle reçoit une animation qui l'explique."
→ Type : Diagramme / flowchart (suite)
→ Contenu : branche "Oui" du flowchart qui mène à une icône "animation"

[5:48] **[RESPIRATION]** — "Si c'est un moment de respiration, elle reste en simple sous-titre pour que le spectateur se repose et se connecte à l'orateur."
→ Sous-titre simple. Cette ligne décrit elle-même un moment de respiration — la traiter en respiration est cohérent avec son propre principe, et referme la boucle avant la ligne suivante.

Résumé : 5 ANIMATION / 1 RESPIRATION. Rythme dense mais cohérent avec un script pédagogique sur le montage ; pas d'alerte de rythme (aucune série de 3+ RESPIRATION consécutives, et la seule respiration referme intentionnellement la boucle).
```
