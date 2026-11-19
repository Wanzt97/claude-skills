---
name: design-prompt-generator
description: >
  Génère des prompts optimisés pour Claude Design (outil de création visuelle d'Anthropic Labs).
  Utilise cette compétence dès que l'utilisateur veut créer un design, une interface, un prototype,
  une landing page, un dashboard, une présentation ou tout autre élément visuel avec Claude Design.
  Déclencher aussi si l'utilisateur dit "rédige un prompt pour Claude Design", "comment demander à
  Claude Design de faire X", "génère le prompt pour créer Y", ou s'il décrit un élément visuel
  qu'il veut faire générer. Ne pas utiliser pour du design dans Canva ou d'autres outils.
---

# Claude Design Prompt Generator

Génère un prompt structuré et efficace pour Claude Design — l'outil de création visuelle d'Anthropic Labs (disponible en research preview sur les plans Pro, Max, Team, Enterprise).

## Architecture d'un bon prompt Claude Design

Un prompt efficace contient **4 blocs** dans cet ordre :

```
[GOAL] Ce qu'on construit (type de design + contexte)
[LAYOUT] Disposition et structure des éléments
[CONTENT] Informations à afficher / sections incluses
[AUDIENCE] À qui ça s'adresse
```

Ajouter si pertinent :
- `[STYLE]` : tonalité visuelle (dark, minimal, playful, corporate...)
- `[RESPONSIVE]` : mobile / desktop / tablet
- `[BRAND]` : couleurs, typographie, composants du système de design

---

## Workflow

### Étape 1 — Comprendre l'intention

Extraire les informations clés de la demande de l'utilisateur :
- Quel type de design ? (dashboard, landing page, formulaire, app mobile, présentation...)
- Quel contenu ou données ?
- Quel style visuel souhaité ?
- Pour quelle plateforme / audience ?

Si des informations manquent, poser **une seule question ciblée** avant de rédiger.

### Étape 2 — Rédiger le prompt structuré

Toujours utiliser ce format de sortie :

```
[GOAL] ...
[LAYOUT] ...
[CONTENT] ...
[AUDIENCE] ...
[STYLE] ...           ← si pertinent
[RESPONSIVE] ...      ← si pertinent
[BRAND] ...           ← si le contexte le précise
[WIREFRAMES] Generate 3 wireframe versions of this design: Version 1 — [variation A, ex: minimal/single column], Version 2 — [variation B, ex: grid layout/multi-column], Version 3 — [variation C, ex: hero-focused/asymmetric]. Use low-fidelity grayscale wireframes with labeled placeholders. No colors, no images.
```

**⚠️ Règle obligatoire — Wireframes :** Tout prompt généré **doit inclure** un bloc `[WIREFRAMES]` qui **demande à Claude Design** de produire 3 versions wireframe distinctes. C'est Claude Design qui génère les wireframes — pas toi. Ta seule responsabilité est d'inclure cette instruction dans le prompt, avec 3 directions de mise en page adaptées au contexte (ex: single column / grid / hero-focused). Ce bloc est non-optionnel.

Être **spécifique et concret** dans chaque bloc. Éviter le vague.

### Étape 3 — Proposer des variantes d'itération

Après le prompt principal, suggérer 2-3 **instructions de suivi** que l'utilisateur peut envoyer dans Claude Design pour affiner :
- Une pour ajuster le style global (chat)
- Une pour une retouche ciblée (inline comment)
- Une pour demander des variantes

---

## Règles de rédaction

| ✅ Faire | ❌ Éviter |
|---|---|
| Nommer les sections précisément | "Quelque chose de beau" |
| Indiquer des valeurs concrètes (8px, 3 colonnes...) | Descriptions vagues |
| Référencer les composants du design system si connu | Ignorer le système de design existant |
| Préciser mobile/desktop dès le départ | Laisser la responsivité implicite |
| Demander des variations ("montre-moi 2-3 options") | Partir sur une seule direction sans explorer |
| **Toujours inclure `[WIREFRAMES]` avec 3 versions distinctes** | **Omettre le bloc wireframe — c'est une règle non-négociable** |

---

## Exemples de prompts générés

### Dashboard analytics
```
[GOAL] Create an analytics dashboard for a digital content strategy platform.
[LAYOUT] Top row: 3 KPI cards (views, engagement rate, subscribers). Center: line chart for monthly growth. Bottom: table of top-performing content.
[CONTENT] Monthly views, engagement rate %, subscriber count, content performance table with title/views/CTR columns.
[AUDIENCE] Content strategists and channel managers.
[STYLE] Dark background, blue accent colors, gold highlights for key metrics. Premium, minimal aesthetic.
[RESPONSIVE] Desktop-first, tablet-compatible.
[WIREFRAMES] Generate 3 wireframe versions: Version 1 — KPIs top row + full-width chart below + table at bottom (classic stacked layout). Version 2 — Left sidebar with KPIs + main area with chart + table side-by-side. Version 3 — Card grid with chart embedded in hero card, compact table below. Low-fidelity grayscale, labeled placeholders, no colors.
```

### Landing page
```
[GOAL] Design a landing page for a premium digital strategy YouTube channel called Digital Black.
[LAYOUT] Hero section full-width, 3-column feature cards, testimonials row, CTA section with email capture.
[CONTENT] Channel value proposition, 3 core topics (strategy / branding / monetization), social proof, newsletter signup.
[AUDIENCE] Young professionals aged 25-35 interested in digital entrepreneurship.
[STYLE] Dark navy/black background, royal blue accents, gold typography for headlines. Apple-inspired clean aesthetic.
[RESPONSIVE] Mobile and desktop.
[BRAND] DM Serif Display for headings, DM Sans for body text.
[WIREFRAMES] Generate 3 wireframe versions: Version 1 — Centered hero with headline + CTA button, feature cards below in 3 columns, testimonials, email capture footer. Version 2 — Split hero (text left / visual right), 2-column feature list, single testimonial highlight, CTA banner. Version 3 — Full-screen hero with scroll arrow, staggered feature sections alternating left/right, testimonials carousel, sticky CTA bar. Low-fidelity grayscale, labeled placeholders, no colors.
```

### Formulaire / outil interne
```
[GOAL] Design an internal content review form for a media team.
[LAYOUT] Single-column form with section dividers. Submit button fixed at bottom.
[CONTENT] Fields: content title, category (dropdown), review status (radio), notes (textarea), reviewer name.
[AUDIENCE] Internal ops team, non-technical users.
[STYLE] Clean, light mode, professional. No decorative elements.
[WIREFRAMES] Generate 3 wireframe versions: Version 1 — Single column, all fields stacked, submit at bottom. Version 2 — Two-column layout with metadata fields left + notes textarea right, submit below. Version 3 — Step-by-step wizard (3 steps: Info / Review / Submit) with progress bar at top. Low-fidelity grayscale, labeled placeholders, no colors.
```

---

## Conseils pour l'itération dans Claude Design

**Chat** (changements larges) :
- "Make the color scheme darker and more minimal."
- "Rearrange so metrics are in the top row."
- "Show me 2–3 alternative layouts for this section."
- "Review this design for accessibility and contrast."

**Inline comments** (retouches ciblées) :
- "Make this button padding larger."
- "Use the primary brand color here."
- "Change this to a dropdown instead of radio buttons."
- "Make this section collapsible."

> Si un commentaire inline disparaît avant d'être lu, coller le feedback directement dans le chat.

---

## Formats d'export disponibles

Une fois le design prêt, Claude Design permet d'exporter en :
- `.zip`, `PDF`, `PPTX`
- HTML standalone
- Envoi vers Canva
- Handoff vers Claude Code (local ou web)
