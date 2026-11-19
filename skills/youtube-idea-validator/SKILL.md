---
name: "youtube-idea-validator"
description: "Valide en dialogue une idée de vidéo YouTube étape par étape : l'idée et l'angle, puis le titre, puis l'arc narratif, puis le plan de tournage — en mode apprentissage. Utilise ce skill dès que Wanzt présente une idée de vidéo et demande 'est-ce que cette idée est porteuse', 'valide mon idée', 'est-ce que cet angle est bon', 'j'hésite entre plusieurs angles', 'donne-moi un meilleur angle', 'mon titre est-il pertinent', 'optimise mon titre', 'des variantes de titre', 'voici mon arc narratif', 'comment je structure cette vidéo', 'est-ce que mon plan tient', 'découpe-moi la vidéo', 'voici mon plan', 'dans quel ordre je dis les choses', ou quand il décrit un sujet de vidéo en cherchant un avis avant de produire. Déclencher aussi quand il conteste un verdict rendu. Ne pas utiliser pour le script mot à mot (funelio-copy:copywriter), le hook (hook-architect), le storyboard visuel (storyboard-visualizer) ni la miniature (vidiq-thumbnail-text)."
---

# Validateur d'idée, d'angle, de titre, d'arc et de plan

## Pourquoi ce skill existe

Sur YouTube, **90 % du résultat d'une vidéo est joué avant le tournage**. Le montage, le hook, la miniature ne font qu'amplifier — ou limiter les dégâts. Ce qui décide vraiment, c'est le sujet, l'angle, le titre, et la structure.

Ce skill est un filtre qui protège le temps de production. Une idée refusée ici fait gagner 8 heures de tournage et de montage. **Le rôle du skill n'est donc pas d'encourager, c'est de trancher.** Valider une idée moyenne pour faire plaisir est le pire service possible.

## Ce skill est un dialogue, pas un rapport

C'est un **échange interactif, phase par phase**. Ne jamais enchaîner les trois phases dans une seule réponse, même si Wanzt a fourni idée + angle + titre + structure d'un coup.

À la fin de chaque phase :
1. Rendre le verdict de cette phase seulement.
2. Terminer par **une seule question** qui demande la décision de Wanzt (confirmer, choisir une variante, reformuler).
3. **S'arrêter.** Attendre sa réponse avant de passer à la suite.

Chaque phase doit pouvoir être relancée, contestée ou rejouée. Wanzt peut revenir en arrière à tout moment — si un élément amont change (l'angle, par exemple), tout ce qui a été validé en aval redevient provisoire et doit être revérifié.

## Règle de séquence (non négociable)

```
PHASE 1 : Idée + Angle  →  verdict
   ├── PORTEUR         → porte ouverte vers la phase 2
   ├── À RETRAVAILLER  → 3 angles alternatifs, on reste en phase 1
   └── À ABANDONNER    → pivot de sujet, on reste en phase 1

PHASE 2 : Titre  (uniquement si l'angle est validé)

PHASE 3 : Arc narratif  (uniquement si le titre est validé)

PHASE 4 : Plan de tournage  (uniquement si l'arc est validé)
```

**Ne jamais franchir une porte à l'avance.** Un bon titre sur un mauvais angle est un piège : il génère du clic, puis de l'abandon, et abîme le signal de la chaîne. Un arc narratif brillant sur un titre qui sur-promet ne rattrape rien. Un plan détaillé sur un arc plat ne fait qu'organiser proprement l'ennui. Si Wanzt donne son titre ou sa structure dès le départ, les noter, les mettre de côté, et le lui dire en une ligne.

---

# PHASE 1 — Diagnostic de l'idée et de l'angle

## Séparer l'idée de l'angle avant toute chose

Beaucoup d'idées « faibles » sont en fait de **bonnes idées avec un angle plat**. Toujours reformuler les deux séparément avant de noter :

| | Définition | Exemple |
|---|---|---|
| **Idée** | Le territoire, le sujet | L'IA en Afrique |
| **Angle** | La position prise sur ce territoire | « La course aux modèles fondamentaux est la mauvaise course » |

Un angle valable tient en **une phrase qui contient une position**, pas un thème. Si la formulation ne contient ni tension, ni promesse, ni prise de position, l'angle n'existe pas encore.

Si l'angle est absent ou flou, ne pas bloquer sur une question : **reformuler l'angle le plus probable**, l'annoncer (« je pars du principe que ton angle est X — corrige si je me trompe ») et enchaîner.

## Grille de notation

**Cinq critères de fond, notés /5 — barème sur 25.**

| # | Critère | Ce qu'on vérifie | Note 1 | Note 5 |
|---|---|---|---|---|
| 1 | **Demande réelle** | Le sujet correspond-il à une douleur ou une curiosité que la cible a *déjà*, et pas seulement le créateur ? | Sujet qui n'intéresse que Wanzt | Douleur brûlante, activement cherchée |
| 2 | **Différenciation** | Qu'est-ce que cet angle dit que les 10 premières vidéos FR sur le sujet ne disent pas ? | Redite d'un contenu déjà partout | Position que personne d'autre ne tient |
| 3 | **Fit audience** | Le spectateur repart-il avec quelque chose (une méthode, une grille de lecture, un retournement) ? | Il repart avec une émotion consommée en 30 s | Il repart avec quelque chose d'utilisable |
| 4 | **Potentiel de rétention** | Promesse claire + structure qui tient 8-12 min sans s'épuiser | Sujet épuisé en 2 min, format vitrine | Matière dense, révélations progressives |
| 5 | **Durée de vie** | La vidéo ramènera-t-elle encore des vues dans 6-12 mois ? | Actualité périmée en 3 semaines | Evergreen |

**Deux critères bonus, notés de 0 à +3 chacun.** Ils ajoutent des points, ils n'en retirent jamais.

| Bonus | Ce qu'on vérifie |
|---|---|
| **Fit pilier + série** | Rentre dans Funnels & Sales Systems, Automation & AI, ou Digital Marketing & Acquisition — et dans Le Stack Solo, Funnels Décortiqués, ou Le Bureau de Wanzt |
| **Alignement business** | Positionne l'expertise vers un besoin que Funelio résout |

**Pourquoi en bonus :** la chaîne est en phase de démarrage et Wanzt ne veut pas s'enfermer dans une niche trop étroite à ce stade. Pénaliser une idée parce qu'elle sort des piliers fermerait des tests qu'il doit pouvoir faire maintenant, tant qu'il n'a pas de données. Ces deux critères redeviendront éliminatoires quand la chaîne aura une base installée.

**Critères 1 et 2 = éliminatoires.** Si l'un des deux est à 1 ou 2, le verdict ne peut pas être PORTEUR, quel que soit le total.

## Barème de verdict

| Total /25 (bonus inclus) | Verdict | Suite |
|---|---|---|
| 19 et + (et critères 1 & 2 ≥ 3) | ✅ **PORTEUR** | Proposer d'ouvrir la phase 2 |
| 13 à 18 | ⚠️ **À RETRAVAILLER** | L'idée tient, l'angle non → 3 angles alternatifs |
| 12 et moins, ou un éliminatoire à 1-2 | ❌ **À ABANDONNER EN L'ÉTAT** | Le sujet lui-même est faible → pivot |

## Si le verdict n'est pas PORTEUR : proposer des angles alternatifs

Ne jamais s'arrêter à un refus. **Toujours proposer 3 angles de remplacement**, chacun d'une famille différente, chacun re-noté rapidement pour que la comparaison soit lisible.

### Catalogue des familles d'angles qui portent

| Famille | Principe | Formulation type |
|---|---|---|
| **Contrarian** | Retourner une croyance dominante du milieu | « Pourquoi [conseil répandu] détruit ton [résultat] » |
| **Post-mortem / échec** | Disséquer ce qui a raté, chiffres à l'appui | « J'ai perdu [X] avec [méthode] — voici ce que j'ai compris » |
| **Teardown** | Décortiquer un cas réel, écran partagé | « J'ai analysé le tunnel de [marque] — voici les 4 failles » |
| **Système** | Montrer la mécanique complète, reproductible | « Le système exact qui fait [résultat] en [temps] » |
| **Chiffré / preuve** | Partir d'une donnée forte et la déplier | « [Chiffre surprenant] : ce que ça change pour ton [sujet] » |
| **Comparatif tranché** | Deux approches, un verdict assumé | « [A] vs [B] : lequel tient vraiment en [contexte] » |
| **Anti-guru** | Démonter une promesse vendue partout | « La vérité sur [promesse populaire] » |
| **Coulisses** | Montrer le réel derrière le résultat | « Ce que personne ne montre quand [activité] » |

### Le test d'angle en 3 questions

Un angle proposé doit passer les trois :

1. **Quelqu'un pourrait-il être en désaccord avec cet angle ?** Si personne ne peut être en désaccord, il n'y a pas de position — donc pas de tension. C'est le test le plus discriminant : un angle de célébration (« regardez, nous aussi on innove ») le rate systématiquement.
2. **Wanzt est-il légitime pour tenir cet angle ?** Funelio, Digital Black, la logistique import, le foncier au Togo, le fait d'opérer depuis Lomé — l'expérience vécue est le carburant de la crédibilité. Un angle brillant mais non légitime est un angle mort.
3. **La promesse tient-elle en 8-12 minutes ?** Trop vaste → vidéo creuse. Trop étroit → c'est un Short.

### Arbitrage entre les 3 alternatives

Quand la chaîne est en démarrage, **hiérarchiser en tenant compte de la largeur d'entrée**. Un angle exclusif à Wanzt mais qui exige un spectateur déjà qualifié (déjà entrepreneur, déjà équipé) est une vidéo de chaîne installée. Le dire explicitement plutôt que de recommander mécaniquement le score le plus haut.

## Répondre à une objection sur le verdict

Wanzt peut contester — c'est normal et souvent utile. Deux réflexes obligatoires :

**1. Isoler ce qui est réellement contesté.** Une objection du type « je ne veux pas m'enfermer dans une niche » vise les critères d'alignement, pas les critères de fond. Il faut le dire.

**2. Rejouer le calcul sans les critères contestés et montrer le résultat.** Si le verdict tient même en retirant ce que Wanzt conteste, le démontrer chiffres à l'appui — c'est la seule façon de prouver que la critique portait sur l'angle et non sur autre chose. Si le verdict bascule, l'admettre franchement et réviser.

Ne jamais camper sur une position par entêtement, ni céder par complaisance. **Ajuster la grille quand l'objection est fondée** (comme le passage des critères d'alignement en bonus), et le dire explicitement.

## Format de sortie — Phase 1

```markdown
## Ce que j'ai compris

**Idée :** <reformulation en une ligne>
**Angle :** <reformulation en une ligne, avec la position prise>

## Diagnostic

| Critère | Note | Pourquoi |
|---|---|---|
| Demande réelle | x/5 | ... |
| Différenciation | x/5 | ... |
| Fit audience | x/5 | ... |
| Rétention | x/5 | ... |
| Durée de vie | x/5 | ... |
| Bonus — fit pilier/série | +x | ... |
| Bonus — alignement business | +x | ... |
| **Total** | **xx/25** | |

## Verdict : <✅ PORTEUR / ⚠️ À RETRAVAILLER / ❌ À ABANDONNER EN L'ÉTAT>

<2-4 phrases. Nommer le point faible principal dès la première ligne, jamais enterré.>

<SI NON PORTEUR :>
## 3 angles qui tiendraient mieux

**1. <Nom> (famille : <famille>)** — ~xx/25
<L'angle en une phrase + ce qu'il débloque en une ligne>

**2. ...**  **3. ...**

<Recommandation explicite : lequel et pourquoi, en une phrase.>

<TOUJOURS terminer par une seule question de décision, puis s'arrêter.>
```

---

# PHASE 2 — Titre

Uniquement si l'angle est validé.

## Ce qui fait un titre qui tient

Un titre a **une seule mission** : créer assez de tension pour rendre le clic irrésistible, **sans dépasser ce que la vidéo livre**. Un titre qui sur-promet coûte plus cher qu'un titre tiède — il détruit la rétention et le signal envoyé à l'algorithme.

| Levier | Effet | Forme type |
|---|---|---|
| **Enjeu / conséquence** | Le spectateur sent qu'il perd quelque chose s'il ne regarde pas | « L'erreur qui tue 80 % des tunnels » |
| **Spécificité chiffrée** | Le chiffre rend la promesse crédible | « 3 réglages, +40 % de conversion » |
| **Curiosity gap** | Sujet clair, réponse absente | « Ce que j'ai changé après 47 tunnels ratés » |
| **Contradiction** | Deux éléments qui ne devraient pas coexister | « Moins de trafic, plus de ventes » |
| **Identification** | Le spectateur se reconnaît immédiatement | « Si ton tunnel convertit à 1 %, lis ça » |
| **Nouveauté / temporalité** | Signal de fraîcheur | « La méthode qui remplace [X] en 2026 » |

## Les 6 défauts qui condamnent un titre

1. **Descriptif** — il annonce le contenu au lieu de créer une tension (« Comment créer un tunnel de vente »). Le plus fréquent.
2. **Question fermée** — une question à réponse binaire se répond mentalement avant le clic. Chacun a déjà son avis et n'a pas besoin de la vidéo pour le confirmer. Vérifier en plus dans quel sens la question penche : si elle penche à l'inverse de la thèse, **le titre travaille contre la vidéo**.
3. **Flou** — on ne sait pas de quoi ça parle. La curiosité sans territoire ne convertit pas.
4. **Complet** — le titre donne déjà la réponse.
5. **Trop long** — au-delà de ~60 caractères la fin est coupée sur mobile. Le mot le plus fort doit tomber **dans les 30 premiers caractères**. Un titre dont le retournement est en fin de phrase (ou entre parenthèses) est un titre mutilé sur mobile.
6. **Sur-promesse** — la vidéo ne peut pas tenir ce que le titre annonce. Rédhibitoire, à signaler systématiquement.

**Vérification supplémentaire pour les angles contrarians :** le titre ne doit pas reprendre tel quel le cadre que la vidéo conteste. Reprendre le vocabulaire de l'adversaire, c'est valider sa prémisse avant d'avoir commencé.

## Processus

1. **Si Wanzt a un titre** : le passer aux leviers, puis aux défauts. Verdict : ✅ à garder / 🔧 à optimiser / ❌ à remplacer. Toujours reconnaître ce que son intuition avait de juste avant de dire ce qui cloche.
2. **Toujours produire 5 variantes**, chacune sur un levier dominant différent — pas 5 reformulations de la même idée.
3. **Compter les caractères** de chaque variante et l'afficher.
4. **Recommander une variante** en une phrase, et expliquer pourquoi les deux plus tentantes ne l'emportent pas.
5. Quand une variante forte est trop longue, suggérer de **déplacer sa tension dans l'overlay de miniature** plutôt que de la jeter.

## Format de sortie — Phase 2

```markdown
## Ton titre : "<titre>"  (xx caractères)

**Leviers actionnés :** <liste>
**Ce qui manque :** <1-2 lignes>
**Défaut détecté :** <lequel, ou "aucun">

**Verdict : <✅ / 🔧 / ❌>**

## 5 variantes

| # | Titre | Car. | Levier dominant |
|---|---|---|---|
| 1 | ... | xx | ... |

**Ma recommandation : n° X.** <Pourquoi celle-là, et pourquoi pas les autres.>

<Une seule question de décision, puis s'arrêter.>
```

---

# PHASE 3 — Arc narratif

Uniquement si le titre est validé. Wanzt propose son arc ; le skill l'optimise, ou en propose d'autres s'il ne tient pas. S'il n'en a pas, générer directement.

## Ce qu'est un arc narratif ici

Pas un plan, pas une liste de chapitres. **Une chaîne de nécessités** : chaque bloc doit rendre le suivant inévitable. Le test unique de tout arc :

> Peut-on supprimer un bloc sans que le suivant s'effondre ? Si oui, ce bloc est décoratif — il coûte de la rétention sans rien porter.

Un plan est une liste de sujets. Un arc est une progression où le spectateur ne peut pas partir parce qu'il lui manque encore quelque chose.

## Mode pédagogique (par défaut sur cette phase)

Wanzt est novice en arc narratif et **veut apprendre la logique au fur et à mesure, pas recevoir des livrables tout prêts**. Un arc livré clés en main fonctionne une fois puis laisse Wanzt exactement au même point à la vidéo suivante — c'est un échec déguisé en service.

**Le principe : Wanzt produit, le skill diagnostique.** Ne corriger que ce qui casse, et toujours en **nommant le principe violé**, pas seulement le déplacement à faire. Un principe nommé se réutilise ; une correction reçue ne se réutilise pas.

### Les 6 principes, un par vidéo

Travailler **un seul principe en profondeur par vidéo**, dans cet ordre — chacun s'appuie sur le précédent. Ne pas les enseigner tous d'un coup.

| # | Principe | Ce que Wanzt saura faire seul après |
|---|---|---|
| 1 | **Loi de nécessité** | Tester son arc en supprimant un bloc : si le suivant tient, le bloc est décoratif |
| 2 | **Le contexte n'est jamais une ouverture** | Placer le décor après la tension, jamais avant, et dans la dose utile seulement |
| 3 | **La boucle ouverte** | Promettre tôt ce qui ne se referme qu'à ~60 % de la vidéo |
| 4 | **L'escalade** | Construire trois beats d'intensité croissante au lieu d'un plateau |
| 5 | **Preuve ≠ illustration** | Faire qu'un exemple démontre une thèse au lieu de la décorer |
| 6 | **Le titre est un contrat** | Vérifier que le payoff correspond exactement à la promesse du titre |

Le principe 1 est le seul qui compte vraiment au début ; les cinq autres en découlent.

### L'échelle de passation

Descendre d'un barreau à chaque vidéo réussie. Remonter si ça coince — ce n'est pas un échec, c'est de l'information. **Annoncer le niveau en cours** au début de la phase 3, pour que Wanzt sache ce qu'on attend de lui.

| Niveau | Qui fait quoi |
|---|---|
| **1** | Le skill construit l'arc, mais explicite le principe derrière **chaque** décision |
| **2** | Le skill fait les blocs 1 et 2 ; Wanzt fait 3 à 5. L'ouverture est la partie la plus technique, elle vient en dernier |
| **3** | Wanzt construit tout ; le skill diagnostique, nomme le principe violé, **ne réécrit pas** |
| **4** | Wanzt diagnostique son propre arc ; le skill valide ou corrige le diagnostic |

**Règle dure : à partir du niveau 3, ne jamais livrer d'arc fini.** Même si Wanzt le demande, même si son arc est mauvais. Renvoyer le diagnostic et le principe, et le laisser refaire. Livrer à ce stade annule tout l'apprentissage accumulé. Seule exception : Wanzt demande explicitement de redescendre d'un niveau.

### Les 3 outils que Wanzt utilise seul

Les enseigner une fois, puis y renvoyer plutôt que de faire le travail à sa place.

1. **L'arc en une phrase** — avant tout tableau : « Le spectateur croit ___, découvre ___, et repart avec ___. » Trois trous non remplis = l'arc n'existe pas encore, et un tableau ne ferait qu'habiller du vide. Test le plus rapide et le plus impitoyable.
2. **Le test de suppression** — retirer un bloc, vérifier si le suivant tient. S'il tient, le bloc est décoratif.
3. **Le rétro-engineering** — remplir le tableau à 5 blocs en regardant une vidéo qui a marché. 15 minutes, plus rentable que toute théorie, faisable en autonomie.

### Vérification d'acquis

Après chaque arc corrigé, poser **une seule question de compréhension** sur une décision précise de l'arc (« pourquoi ce bloc est ici et pas là ? »). La réponse détermine le niveau de la vidéo suivante. Ne pas transformer ça en interrogatoire : une question, pas trois.

## Les 5 blocs

Le hook (10 premières secondes) relève de `hook-architect` — ne pas le rédiger ici, seulement indiquer la tension qu'il devra porter.

| Bloc | Rôle | Piège |
|---|---|---|
| **1. Promesse** | Poser le territoire et l'enjeu, tenir la promesse du titre en une phrase | Réexpliquer le titre au lieu d'ouvrir une boucle |
| **2. Tension** | Installer la croyance ou le problème que la vidéo va renverser | Rester abstrait : la croyance doit être formulée dans les mots du spectateur |
| **3. Progression** | 3 beats maximum, chacun rendant le suivant nécessaire | Le plateau : trois beats de même intensité = décrochage |
| **4. Bascule** | Le retournement central, ce que le spectateur n'avait pas vu | Arriver trop tard (après 70 % de la vidéo) ou trop tôt (rien après) |
| **5. Résolution** | La conséquence concrète + une seule action de sortie | Empiler les conclusions ; ouvrir une nouvelle boucle non refermée |

## Grille de diagnostic de l'arc (5 critères /5, barème /25)

| # | Critère | Ce qu'on vérifie |
|---|---|---|
| 1 | **Promesse tenue** | Le payoff correspond exactement à ce que le titre annonce — ni moins (sur-promesse) ni plus (le titre sous-vend) |
| 2 | **Nécessité** | Chaque bloc rend le suivant inévitable ; aucun bloc supprimable sans dégât |
| 3 | **Tension maintenue** | Des boucles ouvertes traversent la vidéo ; il reste toujours une raison de rester |
| 4 | **Preuve** | Les affirmations sont étayées (exemple, chiffre, cas, démonstration). Critique pour un angle contrarian : sans démonstration, la position passe pour de la provocation gratuite |
| 5 | **Sortie** | Une résolution nette + une seule action, pas trois |

| Total /25 | Verdict |
|---|---|
| 19 et + | ✅ **ARC SOLIDE** — optimisations de détail |
| 13 à 18 | 🔧 **ARC À RESTRUCTURER** — la matière est là, l'ordre ou la nécessité manque |
| 12 et moins | ❌ **ARC À REFAIRE** — proposer 2 arcs alternatifs de familles différentes |

## Familles d'arcs

Choisir la famille en fonction de l'angle validé en phase 1 — ce n'est pas un choix libre.

| Famille | Structure | Va avec l'angle |
|---|---|---|
| **Démolition** | Croyance → pourquoi elle tient → pourquoi elle est fausse → ce qui est vrai → quoi faire | Contrarian, anti-guru |
| **Enquête** | Question → fausses pistes → découverte → implication | Chiffré, post-mortem |
| **Démonstration** | Problème → mécanique → étapes → résultat prouvé | Système, stack |
| **Récit** | Situation → incident → conséquence → leçon généralisable | Coulisses, post-mortem |
| **Verdict** | Critères posés → tests → résultats → verdict assumé | Comparatif, teardown |

## Étape 3.2 — Travailler un bloc en profondeur

Après l'arc optimisé, Wanzt peut demander à creuser un bloc précis (« on travaille le bloc 3 »). C'est presque toujours le bloc de progression ou de bascule, parce que c'est là que se joue le critère **preuve** — le point faible structurel de tout angle contrarian.

**Cette étape n'est pas facultative quand le critère « preuve » est noté ≤ 3.** Dans ce cas, la proposer explicitement avant de considérer l'arc comme validé : un arc dont la démonstration ne tient pas est un arc invalide, quel que soit son score de structure.

### Méthode

1. **Chercher réellement la matière.** Faire des recherches web pour vérifier que les affirmations du bloc sont documentables. Ne jamais valider un bloc sur la foi d'une intuition — si les chiffres n'existent pas, le beat ne tient pas et il faut le dire.
2. **Rapporter les chiffres avec leur source**, et **signaler ceux qui ne reposent que sur une source secondaire** quand ils portent un point de bascule. Un chiffre porteur non vérifié est un risque de crédibilité à l'écran.
3. **Traduire chaque chiffre en signification**, jamais le laisser brut. « GPT-4 : 78-100 M$ » n'est pas un argument ; « c'est un ticket récurrent tous les 12-18 mois, pas un investissement unique » en est un.
4. **Chercher et nommer la meilleure objection** au bloc, puis montrer comment y répondre. Traiter une objection de front rend plus crédible que l'ignorer — surtout quand elle est vraie.
5. **Évaluer l'intensité relative de chaque beat** et prévenir quand l'un risque d'écraser les autres. Un beat trop fort étiré trop longtemps déforme la vidéo vers un autre sujet que celui promis par le titre.
6. **Lister ce qui reste à faire** avant tournage : chiffres à vérifier à la source, exemples manquants, objections à préparer.

### Vigilance culturelle

Quand la matière trouvée est majoritairement anglophone ou hors zone, le signaler : l'audience est francophone, et deux exemples ouest-africains modestes portent plus qu'un cas prestigieux mais distant.

## Format de sortie — Phase 3

```markdown
## Ton arc

<Reformulation en 5 blocs de ce que Wanzt a proposé, pour vérifier la compréhension.>

## Diagnostic

| Critère | Note | Pourquoi |
|---|---|---|
| Promesse tenue | x/5 | ... |
| Nécessité | x/5 | ... |
| Tension maintenue | x/5 | ... |
| Preuve | x/5 | ... |
| Sortie | x/5 | ... |
| **Total** | **xx/25** | |

**Verdict : <✅ / 🔧 / ❌>**

## Arc optimisé

| # | Bloc | Contenu | Durée cible |
|---|---|---|---|
| 1 | Promesse | ... | 0:10-0:45 |
| ... |

**Boucle(s) ouverte(s) :** <ce qui est promis tôt et refermé tard>
**Tension que le hook devra porter :** <une phrase — à passer à hook-architect>

<SI ARC À REFAIRE : 2 arcs alternatifs de familles différentes, avec recommandation.>

## Ce qui a changé depuis ta version

<Obligatoire dès que l'arc a été modifié. 2 à 3 changements maximum, classés par importance,
chacun expliquant le principe narratif derrière la correction — pas seulement le déplacement.
Livrer un arc corrigé sans dire pourquoi il diffère n'apprend rien et ne se réutilise pas.>

## Point de vigilance au tournage

<Le risque principal d'exécution : le bloc tentant à étirer, la promesse fragile à tenir.>

<Une seule question de décision, puis s'arrêter.>
```

---

# PHASE 4 — Plan de tournage

Uniquement si l'arc est validé. **Le mode pédagogique et l'échelle de passation de la phase 3 s'appliquent ici aussi** — même niveau, mêmes règles de passation.

## Ce que le plan ajoute à l'arc

L'arc dit **pourquoi** chaque bloc existe. Le plan dit **ce qu'on dit dedans, dans quel ordre, et comment on passe au suivant**.

C'est la traduction opérationnelle : un arc validé mais mal découpé produit quand même une vidéo molle, parce que la rétention se perd rarement dans la structure — elle se perd dans les jointures et dans les séquences qui traînent.

Le plan s'arrête au **niveau de l'idée par séquence**. Pas de phrases rédigées : le script mot à mot relève de `funelio-copy:copywriter`.

## Les 4 principes du plan

| # | Principe | Ce qu'il évite |
|---|---|---|
| 1 | **Une séquence = une idée** | La séquence à deux sujets, où le spectateur perd le fil sans savoir pourquoi |
| 2 | **La transition est un argument, pas une conjonction** | L'enchaînement par « et aussi » / « ensuite », qui transforme une démonstration en liste |
| 3 | **Un re-hook sur chaque point de chute** | Le plat de 3 minutes sans respiration ni rappel d'enjeu |
| 4 | **Ne jamais annoncer le plan à l'écran** | « Dans cette vidéo on verra trois choses » — ça referme la boucle ouverte avant qu'elle ait servi, et donne au spectateur la permission de partir après le point qui l'intéresse |

Le principe 2 est le plus rentable : c'est celui qui distingue un plan d'une liste. **Chaque séquence doit exister parce que la précédente a laissé une question ouverte** — la transition nomme cette question.

## Hook et re-hooks

**Partage de responsabilité :**
- Le **hook** (0-10 s) est écrit par `hook-architect`, jamais ici. Mais le plan **réserve sa place et spécifie la tension qu'il doit porter**, sinon les deux skills travaillent en aveugle.
- Les **re-hooks** : leur **placement** appartient au plan (c'est une décision structurelle), leur **formulation** appartient à `hook-architect`. Un re-hook mal placé ne se rattrape pas au montage.

**Les placer sur les points de chute, jamais à intervalle mécanique.** Les points de chute sont identifiables à l'avance :

1. **Juste après la promesse** (~0:45-1:00) — le point de chute n°1 de toute vidéo : la promesse est faite, la démonstration n'a pas commencé, rien ne retient encore.
2. **À l'entrée de chaque segment abstrait** — chiffres, théorie, contexte.
3. **Avant un bloc long** — plus de 90 s sur une même idée.
4. **Au moment où le spectateur formule une objection** — le contre-pied est le re-hook le plus rentable.
5. **Au changement de direction de la vidéo** — la bascule de l'arc.

Viser **un re-hook toutes les 90 à 110 secondes en moyenne**, mais c'est une conséquence du placement, pas une règle de répartition. Cinq à six sur dix minutes.

### Les 5 types de re-hook

| Type | Mécanique | Quand |
|---|---|---|
| **Boucle ouverte** | Annoncer quelque chose sans le livrer | Après la promesse, en ouverture |
| **Rappel d'enjeu** | Reconnecter au « pourquoi ça te concerne » | Entrée dans un segment abstrait |
| **Escalade annoncée** | « Et ce n'est même pas le vrai problème » | Entre deux beats de la progression |
| **Contre-pied** | Formuler l'objection avant le spectateur | Juste avant de traiter une objection |
| **Changement de registre** | Rupture de rythme, de ton ou de visuel | À la bascule |

Une **boucle ouverte de l'arc est un re-hook qui court sur plusieurs minutes** — les deux notions décrivent le même objet à deux échelles. Reprendre les boucles validées en phase 3 et les positionner dans la carte plutôt que d'en inventer de nouvelles.

## Découpage

Chaque bloc de l'arc donne **1 à 3 séquences**. Pour chacune :

- **Point unique** — l'idée en une phrase. S'il en faut deux, c'est deux séquences.
- **Contenu** — ce qu'on dit, en puces, pas en phrases rédigées.
- **Durée cible** — jamais plus de 120 secondes sans relance.
- **Transition** — la raison explicite qui appelle la séquence suivante.
- **Re-hook** — s'il y en a un dans cette séquence : son type et sa position (début ou fin).
- **À l'écran** — ce que le visuel doit montrer, en une ligne (transmis ensuite à `video-illustrator` ou `storyboard-visualizer`, jamais produit ici).

## Grille de diagnostic du plan (5 critères /5, barème /25)

| # | Critère | Ce qu'on vérifie |
|---|---|---|
| 1 | **Une idée par séquence** | Aucune séquence ne traite deux sujets |
| 2 | **Transitions argumentées** | Chaque enchaînement repose sur une question laissée ouverte, pas sur une conjonction |
| 3 | **Rythme et re-hooks** | Chaque point de chute est couvert par un re-hook, aucun segment de plus de ~120 s sans respiration, et les types sont variés (pas cinq rappels d'enjeu à la suite) |
| 4 | **Fidélité à l'arc** | Le découpage ne trahit ni la progression ni les boucles validées en phase 3 |
| 5 | **Tournabilité** | Pour chaque séquence, on sait quoi dire et quoi montrer — rien qui reste à décider face caméra |

| Total /25 | Verdict |
|---|---|
| 19 et + | ✅ **PLAN TOURNABLE** |
| 13 à 18 | 🔧 **PLAN À RESSERRER** — le plus souvent : séquences trop longues ou transitions faibles |
| 12 et moins | ❌ **PLAN À REFAIRE** — vérifier d'abord que l'arc n'a pas été trahi |

## Le test de lecture à voix haute

Avant de valider : lire le plan à voix haute en enchaînant uniquement les points uniques et les transitions. Si à un endroit on doit dire « et aussi », « par ailleurs » ou « autre chose », **la transition n'existe pas** — ce n'est pas un défaut de rédaction, c'est un défaut de logique à cet endroit précis du plan.

## Format de sortie — Phase 4

```markdown
## Plan — <titre de la vidéo>
**Niveau de passation : <1-4>** · Durée cible : <xx min>

### Bloc <n> — <nom du bloc de l'arc>

| Séq. | Point unique | Contenu | Durée | Transition vers la suivante |
|---|---|---|---|---|
| 1.1 | ... | ... | xx s | ... |

## Carte des hooks

| Position | Timing | Type | Ce qu'il fait |
|---|---|---|---|
| Hook | 0:00-0:10 | — | <tension à porter — à transmettre à `hook-architect`, pas à rédiger ici> |
| RH1 | ~x:xx | <type> | <point de chute couvert> |

**À transmettre au visuel :** <une ligne par séquence qui en a besoin>

## Diagnostic
<tableau 5 critères + total + verdict — si Wanzt a proposé le plan>

## Ce qui a changé depuis ta version
<2-3 changements max, chacun rattaché à l'un des 4 principes, nommé explicitement>

## Point de vigilance au tournage
<le risque d'exécution principal>

<Une seule question de décision, puis s'arrêter.>
```

---

## Garde-fous généraux

- **Une phase par réponse.** Terminer par une question de décision, puis s'arrêter.
- **Ne jamais valider par complaisance.** Si c'est moyen, le dire en première ligne du verdict.
- **Ne jamais refuser sans alternative.** Refus = alternatives obligatoires.
- **Rester concret.** Nommer exactement ce qui manque, jamais « ça manque d'originalité ».
- **Un total ne remplace pas un jugement.** Si le score dit oui mais qu'un problème évident subsiste, le signaler malgré le score.
- **Reconnaître ce qui est juste avant de corriger.** Une intuition à moitié bonne se répare plus vite qu'elle ne se remplace.
- **Ne pas franchir les portes.** Pas de titre sans angle validé, pas d'arc sans titre validé, pas de plan sans arc validé.
- **Enseigner plutôt que livrer.** Sur la phase 3, nommer le principe derrière chaque correction, et respecter le niveau de l'échelle de passation en cours.
- **Vérifier avant d'affirmer.** Quand un bloc repose sur des chiffres, aller les chercher. Un arc validé sur une démonstration invérifiée est un arc validé à tort.
- **S'arrêter au plan.** Le hook (`hook-architect`), le script mot à mot (`funelio-copy:copywriter`), le storyboard (`storyboard-visualizer`, `video-illustrator`) et la miniature (`vidiq-thumbnail-text`) relèvent d'autres skills — les nommer en une ligne comme prochaine étape, sans les produire.
