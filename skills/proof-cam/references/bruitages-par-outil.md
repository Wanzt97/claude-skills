# Les bruitages, outil par outil

Les règles (quand, pourquoi, à quel volume) sont dans [SIGNATURE-wanzt.md](../SIGNATURE-wanzt.md). Ce fichier ne donne que les noms de sons et les réglages propres à chaque outil.

Dans tous les cas : une piste par famille de sons, aucun bruitage pendant un bloc visage.

## HyperFrames

Chercher les sons par leur nom exact dans la recherche de sons de l'application, et vérifier que le fichier reçu porte bien ce nom. Sinon, demander le fichier à Wanzt.

| Son | Nom à chercher | Durée |
|---|---|---|
| Cliquet de zoom, vol de 1,3 s ou moins | `Mechanical ratchet clicks` | 1,56 s |
| Cliquet de zoom, vol de plus de 1,3 s | `Plastic ratchet clicks` | 3,44 s |
| Clic de surlignage | `Short Click` | 0,24 s |
| Frappe clavier (option) | `Keyboard typing` | tranche de 0,5 s |

**Cliquet de zoom**
- `data-start` = début du vol ; `data-duration` = durée du vol.
- Zoom avant : `data-media-start` = durée du fichier − durée du vol. Recul : `data-media-start="0"`.
- Volume par une piste `data-automation` : 50 % au départ, 100 % au milieu du vol, 0 à l'arrivée, fondu final de 100 ms.
- Pas de `data-playback-rate` : on coupe le son, on ne l'étire pas.

**Clic de surlignage**
- `data-start` = instant de l'animation − 0,09 s.
- `data-volume="0.2"`.

Dans le gabarit, les balises `<audio>` se posent à la racine de `index.html`, là où le commentaire « MUSIQUE ET BRUITAGES » l'indique. Chaque `<audio>` a besoin d'un `id`, sinon il n'est pas mixé.

## ChatCut Desktop

Testé sur le montage Stripe / Paypal. La bibliothèque n'a ni « ratchet clicks » ni « Short Click ». Utiliser à la place :

| Son | Remplaçant | Identifiant | Durée |
|---|---|---|---|
| Cliquet de zoom, tous les vols | `Mechanical Clicking Loop` | `library:sound:mechanical-clicking-loop` | 87 images à 30 i/s (2,9 s) |
| Clic de surlignage | `Mouse Click` | `library:sound:mouse-click` | 6 images (0,2 s) |
| Clic plus sec (alternative) | `Short Shutter Click` | `library:sound:short-shutter-click` | |

**Cliquet de zoom**
- Poser l'élément à l'image de début du vol ; `durationFrames` = durée du vol ; `fadeOutDurationFrames` 3 ; volume 0,1.
- Zoom avant : `sourceIn` = (87 − durée du vol en images) / 30 s, en microsecondes. Recul : `sourceIn` 0.

**Clic de surlignage**
- À l'image du surlignage − 3 ; volume 0,2.

**Particularités**
- Tous les sons sur une piste audio « SFX ».
- Vérifier qu'aucun clic ne chevauche un cliquet sur la même piste ; sinon décaler le clic de quelques images.
- Pas de courbe de volume disponible : volume fixe et fondu de sortie de 3 images.

## Palmier Pro

Aucun réglage testé. Appliquer les règles de la signature avec les sons que Wanzt fournit, et noter ici ce qui marche.
