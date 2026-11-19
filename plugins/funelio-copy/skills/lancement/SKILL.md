---
name: lancement
description: >
  Génère simultanément la séquence email (5 emails AIDA) et le script de publicité vidéo
  (méthode Sabri Suby — Pattern Interrupt + 17 étapes) pour lancer une offre.
  Lance deux agents en parallèle pour produire les deux livrables en même temps.
  Utilise ce skill quand l'utilisateur dit "génère les emails et les pubs",
  "crée ma séquence de lancement", "je veux lancer mon offre", "génère tout le contenu de lancement",
  "emails et publicités vidéo", "prépare mon lancement", ou après avoir terminé la page de vente
  et vouloir compléter le kit marketing.
tools:
  - Read
  - Write
  - Agent
---

Tu orchestres la phase de lancement marketing. Ta mission : lancer deux agents en parallèle — un pour la séquence email, un pour le script vidéo — et livrer les deux livrables simultanément.

## Ce dont tu as besoin pour démarrer

Vérifie que tu as (ou demande) :
1. **L'avatar client** — douleurs, désirs, langage exact (idéalement depuis le rapport Halo Strategy)
2. **L'offre** — nom, prix, Value Stack, garantie, mécanisme unique
3. **Le contexte de la page de vente** — angles utilisés, histoire, CTA

Si ces éléments sont déjà dans la conversation, démarre immédiatement sans poser de questions.

---

## Lancement des deux agents en parallèle

Lance les deux agents **simultanément** dans le même appel d'outil :

### Agent 1 — Séquence email
**Type** : `funelio-copy:email-sequence`

Passe en prompt :
- L'avatar complet (douleurs, désirs, langage exact)
- L'offre (nom, prix, Value Stack, garantie)
- La plateforme de vente
- Le nom de fichier de sortie

### Agent 2 — Script vidéo (Sabri Suby)
**Type** : `funelio-copy:video-ad`

Passe en prompt :
- L'avatar complet
- L'offre
- Les 3 angles de copy identifiés dans le rapport Halo Strategy
- Le nom de fichier de sortie

---

## Livraison

Une fois les deux agents terminés, présente les deux fichiers .docx à l'utilisateur et propose l'étape suivante :

> "Les deux livrables sont prêts ✓ — séquence email (5 emails) et script vidéo (3 hooks + script complet méthode Sabri Suby). Tu veux qu'on génère autre chose pour le lancement ?"

Consulte `references/sabri-suby-method.md` pour le détail complet de la méthode vidéo.
