# Signature de Wanzt — les bruitages

La vidéo de référence n'a aucun bruitage mesurable. Ceux-ci sont un ajout de Wanzt : c'est ce qui fait que le style n'est plus une copie.

**Base** : validés à l'oreille par Wanzt, sur une seule vidéo de 55 s.

La grammaire reste dans [FICHE.md](FICHE.md). Les noms de fichiers et les réglages propres à chaque outil de montage vont dans le skill, pas ici.

## Le principe

Deux sons, chacun avec un seul sens. Plus il y a de sons, moins on remarque celui qui compte.

Aucun bruitage pendant un bloc visage.

## Le cliquet de zoom

La caméra « fait le point » comme une lunette.

| Règle | Valeur |
|---|---|
| Quand | seulement sur un vol où l'échelle change d'au moins 25 %, vers l'avant ou vers l'arrière |
| Jamais | sur un simple déplacement, ni pour dire autre chose (attente, énumération) |
| Début et fin | le son commence avec le vol et s'arrête quand la caméra se pose |
| Zoom avant | prendre la fin du son : les clics se resserrent jusqu'à l'arrivée |
| Recul | prendre le début du son |
| Vol de 1,3 s ou moins | clics serrés, sans trou |
| Vol de plus de 1,3 s | clics espacés qui se resserrent à la fin |
| Volume | bas : 0,09 à 0,12 pour une voix réglée à −18 LUFS |
| Enveloppe | moitié du volume au départ, plein au milieu, zéro à l'arrivée, avec un fondu final de 100 ms |
| Étirement | jamais : on coupe le son, on ne le ralentit pas |
| Vidéo de plus de 3 minutes | au plus un zoom sur deux, en priorité ceux qui arrivent sur une pièce à conviction |

## Le clic de surlignage

| Règle | Valeur |
|---|---|
| Quand | sur chaque surlignage, chaque trait qui barre, chaque élément d'une cascade |
| Limite | 3 à la suite au maximum |
| Calage | 90 ms avant l'animation |
| Volume | 0,2 |

## En option

Une frappe de clavier courte (0,5 s, volume 0,12) quand un texte est tapé à l'écran.

## Jamais

Souffle sur les déplacements, « toc » d'arrivée, pop, montée sonore. Tous ont été testés puis retirés.

## À savoir

Le volume du cliquet est donné pour une voix à −18 LUFS, le niveau du montage test de Wanzt. La voix de la référence est à −14,5 LUFS. Si la voix est mixée plus fort, remonter les bruitages d'autant.
