---
name: silence-repeat-cut
description: Nettoie un montage HyperFrames de vidéo face caméra en une passe — supprime les répétitions, faux départs et reformulations en gardant la meilleure prise, retire les bouts de plan rejoués en double, puis coupe tous les silences, sans couper un mot utile. Utiliser quand l'utilisateur dit « supprime les silences », « coupe les blancs », « supprime les répétitions », « garde les meilleures prises », « enlève les faux départs », « silence cut », « repeat cut », « nettoie le rush », « jump cut », ou demande un montage plus rythmé.
---

# Silence & repeat cut — nettoyer un rush face caméra

Une seule passe, dans cet ordre : **doublons → répétitions → silences → assemblage**. Les répétitions
passent avant les silences pour que la passe silences récupère aussi les blancs laissés
autour des prises coupées.

Toutes les coupes passent par l'outil du Script de l'app (`script.editWords`, comme son
Cut) : le Script les affiche barrées et la personne peut remettre chaque coupe. On ne
modifie jamais les timings des clips à la main, sauf pour les doublons (étape 1).

Si la personne ne demande qu'une partie (« juste les silences »), ne faire que cette partie.

## Pré-requis

- Projet HyperFrames ouvert dans l'app, rush transcrit : un fichier
  `.hyperframes/transcripts/*.json` dont `src` est le rush. Sinon, lancer
  `voice.transcribeAudio` sur le rush d'abord.
- `hyperframes history --json` lu ; ne jamais défaire une coupe faite par la personne.
- Si le projet contient le script écrit (notes `import-editorial-notes`, `data-editor-note`,
  un fichier script), le lire : c'est la référence de ce que la personne voulait dire.

Le script d'analyse est en lecture seule ; le lancer depuis le dossier du projet :

```bash
T=~/.claude/skills/silence-repeat-cut/scripts/talkcut.py
python3 -I $T doubles     # clips qui rejouent un bout de média déjà joué
python3 -I $T repeats     # mots joués clip par clip + candidats de répétition
python3 -I $T silences --min 0.4 --room 0.15   # pauses à couper, prêtes pour editWords
```

## 1. Doublons

`doubles` liste les clips qui rejouent un bout de rush déjà joué par un autre clip
(souvent un résidu d'import : la fin d'un mot entendue deux fois). `script.editWords` les
refuse (« no clip plays these words »). Dans ce cas seulement : retirer la balise
`<video>` du clip doublon dans `index.html`, reculer de sa durée le `data-start` de tout
ce qui commence après lui, et réduire d'autant le `data-duration` de la composition racine.

## 2. Répétitions — garder la meilleure prise

1. Lire **tout** `playedWords` de `repeats` (le détecteur ne voit pas tout) et ses
   `candidates` : `restart` (mot tronqué « de… » + reprise) et `repeated-phrase` (même
   groupe de mots redit à quelques mots d'écart). Beaucoup de candidats d'un seul mot
   sont normaux (« fait », « cette ») : les écarter s'ils ne sont pas des redites.
2. Pour chaque redite, choisir la prise à garder :
   - **Faux départ** (« L'outil permettait, en revanche, de… » puis « L'outil permettait
     d'écrire… ») → couper la tentative avortée, garder la reprise complète.
   - **Reformulation** (« réduire la distance ou de rapprocher… », « un agent IA,
     carrément un assistant ») → garder la formulation la plus claire / la plus proche du
     script écrit ; vérifier que la phrase restante est correcte.
   - **Mot ou groupe doublé** (« un lien de ce côté ou un lien à cet endroit ») → couper
     le doublon.
   - **En cas de doute** (les deux versions sont dans le script écrit, effet voulu) :
     ne pas couper, le dire à la personne et proposer la coupe.
3. Couper : `script.editWords` `kind: "cut"`, une entrée par passage — `src`,
   `from` = début du 1er mot, `to` = fin du dernier, `text` = mots exacts du transcript.
   Pour ne viser qu'un placement du rush, passer `take` = l'id du clip.

## 3. Silences

1. Lancer `silences`. Sortie : `stretches` (une entrée par pause jouée ≥ `--min` s, y
   compris aux raccords entre plans) et `secondsRemovedApprox`.
   - `--min` : pause minimale à couper (0.4 s ; 0.3 = plus serré, 0.6 = plus naturel).
   - `--room` : respiration gardée de chaque côté des mots (0.15 s, comme Clean up).
2. `script.editWords` `kind: "cut"` avec les `stretches` (garder `src`, `from`, `to`,
   `text: "pause"` ; retirer les champs `_…`). 200 max par appel : découper en lots.
   Passer `room` seulement si la personne demande plus ou moins d'air.

## 4. Vérifier

- Relancer les trois commandes : `doubles` vide, `silences` → `count: 0`, plus de
  redite non voulue dans `repeats`.
- `hyperframes check --json` → 0 erreur.
- `hyperframes snapshot --at …` autour de quelques coupes, regarder la planche.
- Les plans graphiques posés sur le rush (captures, titres) suivent les coupes et peuvent
  raccourcir : le signaler.

## 5. Assembler le face caméra (dernière étape, toujours)

Après la coupe, le rush est joué par des dizaines de `<video>` collés bout à bout. L'aperçu
saute dans le fichier à chaque coupe (il rame) et chaque coupe nette du son claque. On
assemble donc les morceaux en **une seule vidéo** : mêmes coupes, même timing, un fondu de
6 ms à chaque coupe du son (inaudible, supprime le clic), une image clé toutes les 15 images.

```bash
A=~/.claude/skills/silence-repeat-cut/scripts/assemble.py
python3 -I $A --dry-run   # dit quels morceaux seront assemblés
python3 -I $A             # fabrique assets/facecam/<rush>-monte.mp4 et remplace les morceaux
python3 -I $A --undo      # remet les morceaux d'origine, à l'identique
```

- **Quand** : seulement quand la coupe est finie. Si `/rythmize` (ou toute autre étape qui lit
  les morceaux) suit dans la même demande, assembler **après** elle, en tout dernier. Le
  script caméra de rythmize est adapté tout seul : il lit les coupes dans
  `<script id="facecam-cuts">`, donc les punch-ins restent sur les coupes.
- **Retoucher une coupe ensuite**, ou relancer `rythmize apply` : `--undo`, faire la
  retouche, puis assembler de nouveau.
- Le script refuse les morceaux avec une vitesse ou un volume différents : les signaler.
  Il ne touche pas aux extraits du rush posés dans les sous-compositions ; s'il y en a de
  longs, les couper en petits fichiers à part (ffmpeg `-ss … -t … -an`).
- Vérifier : `hyperframes check --json` sans erreur et une planche `hyperframes snapshot`
  sur quelques coupes (mêmes images qu'avant, les zooms suivent les coupes).

## 6. Répondre

En quelques lignes : nombre de silences coupés et secondes gagnées, chaque répétition
coupée sous la forme « … ~~passage coupé~~ … », doublons retirés, nouvelle durée, et ce
qui a été volontairement laissé (avec la proposition de coupe). Dire que le face caméra est
assemblé en une seule vidéo (aperçu fluide, coupes du son sans clic) : pour remettre ou
retoucher une coupe dans le Script, il faut d'abord défaire l'assemblage (`--undo`), ce que
l'agent fait sur simple demande.

## À ne pas faire

- Ne pas couper sur le seul avis du détecteur ; relire la phrase avant et après.
- Ne pas éditer `data-start` / `data-duration` à la main, sauf doublons (étape 1).
- Ne pas effacer de fichier du projet.
- Ne pas laisser le film en dizaines de morceaux : toujours finir par l'assemblage (étape 5).
