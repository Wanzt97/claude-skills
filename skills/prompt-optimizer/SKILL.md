---
name: prompt-optimizer
description: Optimise et restructure des prompts basiques en prompts avancés selon la méthodologie officielle d'Anthropic pour Claude 4.x. Utilise ce skill dès que l'utilisateur veut améliorer un prompt, reformuler une instruction, transformer une demande vague en prompt structuré, ou quand il dit "améliore ce prompt", "optimise ça", "rends ce prompt plus efficace", "transforme cette idée en bon prompt", ou toute formulation indiquant qu'il veut un prompt de meilleure qualité. Déclencher aussi si l'utilisateur colle un texte court et demande à Claude d'en faire un prompt professionnel.
---

# Prompt Optimizer

Ce skill transforme des instructions vagues ou des descriptions d'intention en prompts structurés et performants selon les meilleures pratiques documentées par Anthropic pour Claude 4.x.

## Ce que tu reçois

L'utilisateur fournit l'un des éléments suivants :
- Un prompt basique ou maladroit qu'il veut améliorer
- Une description d'intention ("je veux que Claude fasse X")
- Un texte brut à transformer en prompt
- Un prompt existant à raffiner

## Ce que tu produis

Un prompt optimisé en français, structuré avec les balises XML appropriées, accompagné d'explications sur les choix effectués.

---

## Processus d'optimisation

### Étape 1 — Analyser l'intention

Avant de restructurer, identifie :
- **La tâche principale** : que veut-on obtenir ?
- **Le contexte manquant** : quelles informations sont implicites mais importantes ?
- **Le format de sortie attendu** : longueur, structure, ton ?
- **Les contraintes** : ce qu'il faut éviter ou respecter

Si l'intention est trop vague pour produire un bon prompt, pose une seule question ciblée avant de continuer.

### Étape 2 — Appliquer le framework en 10 composants

Selon la documentation officielle d'Anthropic, un prompt professionnel intègre ces composants dans l'ordre suivant (n'inclure que ceux pertinents pour la tâche) :

1. **Contexte de tâche** — rôle ou persona + mission générale
2. **Ton** — registre, style de communication
3. **Données de fond** — documents, contexte, exemples fournis
4. **Règles détaillées** — instructions précises, contraintes
5. **Exemples** — inputs/outputs idéaux (few-shot)
6. **Conversation** — historique si multi-tours
7. **Entrée immédiate** — la requête de l'utilisateur final
8. **Instruction de raisonnement** — demande de Chain of Thought si pertinent
9. **Format de sortie** — structure, longueur, format attendu
10. **Précautions** — ce à quoi rester attentif

### Étape 3 — Appliquer les règles de rédaction

#### Règles fondamentales (toujours appliquer)

**Être explicite, jamais implicite**
- Dire ce que Claude doit faire, pas ce qu'il doit éviter
- Mauvais : "Ne sois pas trop long" → Bon : "Limite ta réponse à 3 paragraphes maximum"
- Mauvais : "Sois créatif" → Bon : "Propose 3 variations avec des angles d'accroche différents"

**Ajouter le contexte et la raison**
- Expliquer le "pourquoi" améliore la généralisation du comportement
- Exemple : "Évite les listes à puces — les lecteurs de cette newsletter préfèrent la prose fluide"

**Spécifier le format de sortie avec précision**
- Utiliser des bornes chiffrées plutôt que des adjectifs vagues
- Préciser : nombre de mots, nombre de variations, structure attendue

#### Règles avancées (appliquer selon la complexité)

**Balises XML pour l'organisation**
Utiliser des balises XML pour séparer les composants dans les prompts complexes :
```
<contexte>...</contexte>
<tâche>...</tâche>
<contraintes>...</contraintes>
<format_sortie>...</format_sortie>
```

**Demande explicite de qualité**
Claude 4.x est plus concis que ses prédécesseurs. Pour des sorties riches :
- Ajouter : "Va au-delà des bases, inclus un maximum de détails pertinents"
- Ajouter : "Propose une implémentation complète, pas un simple exemple"

**Contrôle du format de sortie**
Pour supprimer le markdown excessif dans les sorties longues :
```
<avoid_excessive_markdown>
Écris en prose fluide avec des paragraphes complets.
N'utilise pas de listes à puces sauf si les éléments 
sont véritablement discrets ou si l'utilisateur en demande.
</avoid_excessive_markdown>
```

**Chain of Thought pour les tâches complexes**
Ajouter si la tâche nécessite un raisonnement approfondi :
- "Réfléchis étape par étape dans des balises <thinking> avant de répondre"
- "Après avoir analysé, cite les passages pertinents avant de formuler tes recommandations"

**Few-shot avec balises délimitantes**
Structurer les exemples pour une meilleure compréhension :
```
<exemples>
  <exemple>
    <input>...</input>
    <output>...</output>
  </exemple>
</exemples>
```

---

## Format de réponse

Présente toujours le résultat en deux parties :

### Partie 1 — Le prompt optimisé

Présente le prompt final dans un bloc de code ou entre balises claires, prêt à être copié-collé.

### Partie 2 — Explications (concises)

Explique en 3 à 5 points les principaux choix effectués :
- Pourquoi tel composant a été ajouté
- Quelle technique a été appliquée et pourquoi
- Ce qui manquait dans le prompt original

---

## Exemples de transformation

### Exemple 1 — Prompt marketing

**Entrée basique :**
"Écris une pub Facebook pour mon logiciel"

**Prompt optimisé :**
```
<contexte>
Tu es un expert en copywriting Facebook Ads spécialisé dans les SaaS B2B francophones.
</contexte>

<tâche>
Rédige 3 accroches publicitaires pour une annonce Facebook.
</tâche>

<produit>
[NOM DU LOGICIEL] — [DÉCRIRE EN 1 PHRASE CE QUE ÇA FAIT]
Cible : [AUDIENCE PRINCIPALE]
Bénéfice clé : [CE QUE L'UTILISATEUR GAGNE]
</produit>

<contraintes>
- Maximum 2 lignes par accroche
- Commence par un problème client concret
- Ton direct, pas de jargon technique
- Pas de point d'exclamation
</contraintes>

<format_sortie>
3 accroches numérotées. Pas d'introduction ni de commentaires.
</format_sortie>
```

### Exemple 2 — Analyse de document

**Entrée basique :**
"Analyse ce texte et dis-moi ce qui va pas"

**Prompt optimisé :**
```
<tâche>
Analyse la page de vente ci-dessous et identifie les points d'amélioration.
</tâche>

<document>
[COLLER LE TEXTE ICI]
</document>

<méthode>
Avant de formuler tes recommandations, cite les passages exacts 
qui posent problème entre balises <passage_problématique>. 
Explique ensuite pourquoi chaque passage réduit la conversion.
</méthode>

<format_sortie>
Pour chaque problème identifié :
1. Citation du passage
2. Diagnostic (1 phrase)
3. Réécriture suggérée

Maximum 5 problèmes prioritaires, du plus impactant au moins impactant.
</format_sortie>
```

---

## Règles de calibration selon la complexité

| Complexité de la tâche | Composants à inclure |
|------------------------|---------------------|
| Simple (1 action, 1 output) | Tâche + Contraintes + Format sortie |
| Moyen (contexte important) | Contexte + Tâche + Contraintes + Format sortie |
| Complexe (raisonnement, multi-étapes) | Tous les composants pertinents + CoT + Exemples |
| Système / Agent | System prompt complet avec tous les composants + balises de comportement |

Ne surcharge pas un prompt simple avec une structure lourde. La règle : **minimum de structure pour maximum de clarté**.
