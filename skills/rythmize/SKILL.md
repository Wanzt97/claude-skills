---
name: rythmize
description: Rythme un montage HyperFrames de vidéo face caméra — analyse le rush (chapitres, coupes, moments forts) puis ajoute punch-ins qui cachent les jump cuts, push-ins lents sur les plans longs, zooms serrés et tremblement de caméra sur les mots forts, transitions de chapitre (flash, grille pixelisée, iris, light leak, glitch, zoom à travers) et whoosh. Utiliser quand l'utilisateur dit « rythme la vidéo », « rythmize », « ajoute les zooms et transitions », « dynamise le montage », « garde l'attention », ou après un silence/repeat cut.
---

# Rythmize — rythmer une vidéo face caméra

Quatre objectifs, dans cet ordre de priorité :
1. **Cacher les coupes** : à chaque jump cut, alterner plan large / punch-in serré (1.12x) centré sur le visage.
2. **Relancer l'attention** : push-in lent (+5 %) sur les plans ≥ 2,8 s.
3. **Souligner les moments forts** : zoom serré (1.25–1.32x) sur le mot clé, tremblement de caméra, whoosh grave — 3 à 5 moments par vidéo, pas plus.
4. **Marquer les chapitres** : une transition visible à chaque changement de partie, en variant les types.

Règle d'or : coupe franche ou punch-in pour ~90 % des raccords ; 1 effet fort pour 2–3 moments ; 1 transition par chapitre.

## Règle fixe : le hook commence par un zoom (validée par l'utilisateur)

Chaque vidéo démarre TOUJOURS par un zoom in ou un zoom out sur le premier plan (le hook), même si aucun autre effet n'est posé.
- Mouvement serré d'environ 100 % → 122 % en 0,5 s avec easing ease-out, puis poussée lente jusqu'à ~128 % à la fin du plan (zoom out : inversé).
- Ancrage sur le visage / le sujet, déterminé à partir de l'image de départ et du script, jamais sur le centre par défaut.
- Poser dès 0 s le son associé au zoom (ex. un whoosh court).
- Ne pas toucher à la voix ; vérifier les images 0, 8, 15 et ~120.

## Pré-requis

- Lire le skill `hyperframes` (contrat de rendu) et `hyperframes history --json`.
- Les plans du rush sont des `<video class="clip">` à la racine de `index.html`, avec `data-label` qui commence par le numéro de chapitre (« 01 · Hook », « 02 · … »). C'est le format laissé par l'import de timeline et par `silence-repeat-cut`. Faire le nettoyage silences/répétitions **avant**.
- Transcript du rush dans `.hyperframes/transcripts/` (sinon `voice.transcribeAudio`).
- Kit de marque : piocher les transitions dans ses transitions retenues (`transitions.md` du kit Digital Black). Les types fournis ici sont tous dans la sélection de Wanzt.

## Étapes

1. **Analyser** (lecture seule), depuis le dossier du projet :

   ```bash
   R=~/.claude/skills/rythmize/scripts/rythmize.py
   python3 -I $R analyze
   ```

   Sortie : durée, chaque plan (`t` en temps vidéo, durée, chapitre, mots avec leur temps vidéo `mot@12.34`), `chapterStarts`, images posées par-dessus (captures).

2. **Cadrer** : `hyperframes snapshot --at 3` puis regarder l'image pleine taille ; noter le centre du visage en pixels 1920×1080 → `origin` (ex. `[1110, 600]`). Les zooms se font autour de ce point.

3. **Écrire le plan** `plan.json` (dans un dossier temporaire, hors projet) — modèle : `exemples/plan-precut.json`.

   | Clé | Rôle |
   |---|---|
   | `origin` | centre du visage `[x, y]` |
   | `tight`, `push`, `pushMin` | punch-in (1.12), push-in (1.05), durée mini d'un plan pour le push (2.8 s) |
   | `chapters` | `{"01":1,"02":2,"03":2,…}` : regroupe les étiquettes en chapitres (chaque chapitre repart en plan large) |
   | `emphasis` | `[{"t":46.35,"scale":1.28}]` : zoom serré au temps vidéo du mot fort |
   | `shake` | `[47.02]` : tremblement de caméra (~0,3 s) |
   | `zoomThrough` | `[44.467]` : début d'un plan de chapitre où la caméra fonce puis se pose |
   | `transitions` | `[{"type":"flash","at":6.56}]` — types : `flash`, `grid` (gauche→droite), `grid-center`, `iris` (s'ouvre sur `origin`), `leak` (light leak), `glitch` |
   | `whoosh` | `[{"at":6.56,"file":"assets/….mp3","peakOffset":0.07,"duration":0.49,"volume":0.6}]` |

   Choix éditoriaux :
   - **Moments forts** : chiffres et prix, révélation (« j'ai décidé de… »), promesse du hook, appel à l'action. Le zoom se place sur le mot, pas au début du plan.
   - **Transitions** : une par `chapterStarts` qui change vraiment de sujet (pas entre deux étiquettes d'un même chapitre). Varier : flash ou zoom à travers pour l'énergie, grille pour entrer/sortir d'un plan graphique ou d'une capture, iris pour revenir sur le visage après une capture, light leak pour une bonne nouvelle, glitch pour un sujet tech.
   - **Whoosh** : sur 4–6 transitions max, et un whoosh grave sur le moment le plus fort. Les trouver avec `media.find` `kind: "sfx"`, `query: "whoosh"` (garder `peakOffset` pour caler le pic sur `at`).

4. **Appliquer** :

   ```bash
   python3 -I $R apply /chemin/plan.json
   ```

   Il enveloppe les vidéos dans `#cam` / `#shake` (une seule fois), écrit le plan dans `<script id="rhythm-plan">` et le script caméra, écrit `compositions/transitions.html` et les `<audio>` whoosh. Rejouable : relancer `apply` remplace l'application précédente. Les punch-ins suivent automatiquement les coupes si on les retouche dans Studio ; les temps des moments forts et transitions, eux, sont fixes.

5. **Vérifier** : `hyperframes check --json` (0 erreur), puis `hyperframes snapshot --at` sur un punch-in, chaque moment fort et chaque transition ; regarder la planche (visage jamais coupé, grille qui couvre bien la coupe, iris centré sur le visage).

6. **Répondre** : un tableau court — moments forts (mot + effet), transitions par chapitre, nombre de whoosh — et dire que tout se règle en relançant le skill avec un autre plan.

## À ne pas faire

- Ne pas animer les `<video>` eux-mêmes (toujours `#cam` / `#shake`), ni mettre de filtre CSS sur l'image filmée.
- Ne pas empiler plusieurs effets forts sur le même mot ; ne pas dépasser ~5 moments forts.
- Ne pas mettre de grille de marque sur l'image filmée en dehors des transitions.
