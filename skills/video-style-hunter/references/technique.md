# Notes techniques (tirées du pilote Digital Black, novembre 2026)

## L'atelier (artifact de type « Design »)

- Fichiers : `project/canvas.json` (la liste des cartes et leur place) et un `*.dc.html` par carte.
- Publication : `url` de l'atelier + `root` (dossier local qui contient `project/`) + `file_path` = `project/canvas.json` + `files` (la map des `.dc.html` modifiés).
- Images et GIF : envoyés en assets (`asset: true`, jusqu'à 25 par appel) ; on les référence par l'url `/_blob/<id>` renvoyée. Garde un fichier `uploads.txt` (« numéro id ») pour reconstruire les urls.
- Une publication refusée pour une carte « pas lue » : relis-la (`action: read`, `path`), compare avec ta version, puis republie.
- Quand une carte grandit (ajout du 16:9 par exemple), décale dans `canvas.json` les cartes placées dessous.

## Les labos (planches interactives de l'atelier)

- Une planche interactive est un `.dc.html` avec un `<script type="text/x-dc">` (`class Component extends DCLogic`, `renderVals()`) ; dans `canvas.json`, la carte porte `"is_interactive": true`. Trous `{{x}}` (lecture pointée seulement), listes `<sc-for>`, conditions `<sc-if>`, évènements `onClick="{{fn}}"`.
- **Son** : Web Audio. `fetch` + `decodeAudioData` sur l'asset, une source par son, un gain par son (`jouer(id, quand, volume, durée)`), tout programmé depuis `currentTime` au clic sur « Jouer ». Les `.mp3` sont refusés en assets : convertis en `.mp4` AAC (`ffmpeg -i son.mp3 -vn -c:a aac -b:a 160k son.mp4`).
- **Relancer une animation** : basculer un booléen qui entoure la scène dans un `<sc-if>` (faux puis vrai) : les éléments sont recréés et les keyframes repartent.
- **Couleur qui change à un instant** (noir sur braise au clic) : un keyframe avec seulement `to{…}` et `both` : avant son départ, l'élément garde sa couleur à lui.
- **Mot qui grandit depuis un point** (sélection agrandie) : `transform` de départ en ligne (`translate(dx, dy) scale(0.4)`) et keyframe `to{transform:none}` ; le curseur garde sa taille avec un contre-zoom (`scale(2.5)` → `none`).
- **Largeur d'un texte** (mot clé trop long) : `canvas.getContext('2d').measureText`, après `document.fonts.load(...)` ; recalcule quand les polices sont chargées.
- **Copier depuis la planche** : `navigator.clipboard` est bloqué dans le cadre ; sélectionne une `<textarea>` (ref) et `document.execCommand('copy')`, avec un message « Cmd+A puis Cmd+C » si ça échoue.
- **Tester en local** : `labos/mini-dc.js` (un petit moteur qui rend les `.dc.html` hors de Claude Design) et `labos/chk.js` (lance chaque script avec un faux `DCLogic`). Dans le navigateur intégré caché, `requestAnimationFrame` ne tourne pas : `mini-dc.js` dessine avec `setTimeout`. Ajoute `?v=N` à l'adresse pour éviter le cache.
- **Ne publie pas sur une version qu'il vient d'enregistrer** sans la relire : relis la carte, compare, puis republie. Dis-lui quelles cartes tu remplaces.

## Le design system (artifact de type « Design System »)

- `project/design-system.json` est l'index : écris-le **en dernier**, garde `createdOnFiles`, mets à jour `lastChange`.
- `project/tokens.json` : des familles en listes (`color.tokens`, `spacing.tokens`, `duration.tokens`… chacun `{name, value, usage}` ; `type.families`).
- `project/README.md` + d'autres `*.md` à la racine de `project/` = des sections, rangées par nom de fichier et titrées par leur premier `#`. Les deux guides sont `01-guide-utilisation.md` et `02-guide-son.md`.
- Composants : `components/<Comp>/README.md` et `preview.html`. `preview.html` commence par `<!-- @dsCard group="…" height="…" width="…" subtitle="…" -->`.
- `components/bundle.css` : les classes partagées (préfixe court, par exemple `.ms-*`), animées par keyframes et pilotées par des variables (`--t` départ, `--i` rang, `--sortie` sortie).
- Images (photo de profil, détourages) : en assets, rangées dans `assetGroups`.
- Publication : `url` + `root` + `file_path` + `files`. Ne passe pas `title`. Un refus « You haven't viewed the latest version » → relis l'artifact en entier (`action: read`, sans `path`), puis republie.

## Vérifier en local avant de publier

- Génère tout avec un script (`gen.py`), jamais à la main : un retour se reporte alors partout d'un coup.
- Construis un dossier `test/` : `tokens.css` tiré de `tokens.json`, `bundle.css`, chaque `preview.html` avec ces deux feuilles, et les images `/_blob/…` copiées en local (modèle : `exemple-digital-black/design-system/build3.sh`).
- Sers-le avec `python3 -m http.server 8767` et regarde-le dans le navigateur intégré. Pour juger une image fixe, mets les animations en pause à un instant donné (`document.getAnimations()` → `currentTime`, `pause()`) et arrête les intervalles.
- Piège : si un générateur ajoute automatiquement une classe de sortie (`ms-sortie`) aux blocs, chaque bloc doit avoir sa variable `--sortie`, sinon il disparaît dès le départ.
- Piège : une légende trop longue élargit sa figure et casse la rangée. Garde les légendes courtes.
- Ne dis jamais avoir vu une carte dans l'atelier ou le design system si tu ne l'as vue qu'en local.

## Le brand kit HyperFrames (application `dev.hyperframes.desktop`)

- Les kits sont dans `~/Library/Application Support/HyperFrames/brand-kits/bkit_*` ; un projet est relié à un kit par `.hyperframes/brand-kit.json` (`{"brand_kit_id": …}`) ; les projets sont dans `~/.hyperframes-studio/`.
- Créer un kit : « New brand kit » → « Start in chat ». C'est Framey, l'assistant de l'application, qui le crée ; il faut une connexion Claude Code, que l'utilisateur fait lui-même.
- Dépose les fichiers de contexte depuis un dossier dédié (`contexte-kit/`) : les deux guides, `COMPOSANTS.md` (tous les README de composants à la suite), `frame.md`, `GUIDE.md`, `DS-README.md`, `tokens.json`, et les feuilles de style en **`.txt`** (le kit refuse l'extension `.css`). Retire les `@import` du bundle.
- Polices : fournis des fichiers statiques (`.woff2` d'une graisse). Une police variable est refusée.
- Couleurs : vérifie les valeurs exactes et donne un **rôle** à chacune (Background, Text, Accent, Neutral). Laisse sans rôle une couleur qui ne doit servir qu'à un détail (le carré du logo, par exemple).
- **Logos** : Framey peut mettre la photo de profil comme logo principal. HyperFrames la placerait alors en tête de chaque titre et carton de fin. Si le logo est un texte, retire-la des logos et remets-la dans les fichiers (la retirer des logos l'enlève aussi des fichiers).
- Règles : recopie-les mot pour mot depuis le guide.
- Description et nom d'une couleur : la page du kit ne les modifie pas. Demande-le à Framey dans le projet où il a créé le kit (il propose les changements, approuve-les), puis vérifie sur la page du kit. Framey renomme une couleur en la supprimant puis en la recréant. Ni la page ni Framey ne savent retirer une police : n'en ajoute pas une dont tu n'es pas sûr.
- À la fin : coche « Used for videos » et vérifie dans les fichiers du kit que les fichiers de contexte sont identiques octet pour octet aux originaux.
- Piège de `hyperframes check` : un sélecteur d'attribut comme `[style*="--sortie"]` est refusé ; utilise une classe (`.ms-sortie`).
- Pilotage de l'application : passe par les outils `app_*` (clic par `element_index` après `app_ax_find`). Une surcouche dans le haut de l'écran (NotchNook) peut bloquer les clics par coordonnées. Dans un panneau d'ouverture de fichiers : cmd+shift+g, le chemin, cmd+a, Entrée.
- Détourer une personne pour « derrière la personne » : `npx hyperframes remove-background`.
