# Habillage Digital Black

L'habillage de la marque Digital Black pour le style proof-cam. La grammaire reste celle de [FICHE.md](FICHE.md) : seule la peau change.

**Source** : `Digital black/Design/design.md`, le design system de la marque. Ce fichier-là n'est pas modifié. Quand il change, cet habillage se met à jour, puis `gabarit/lib/habillages/digital-black.css`.

**Créé le** 2026-10-11, à la demande de Wanzt.

## Comment lire les preuves

| Mention | Ce que ça veut dire |
|---|---|
| **Marque** | Valeur prise telle quelle dans le design system de la marque. |
| **Choix** | La marque ne dit rien pour ce cas : valeur décidée ici, pour la vidéo seulement. |

## Les cases

Fond principal : **sombre**, comme la référence. C'est l'habillage le plus proche du style d'origine : le noir est exactement le même.

| Case | Valeur | Preuve |
|---|---|---|
| Fond principal | `#0A0A0A` | Marque (Background) |
| Texte sur fond principal | `#FAFAF8` | Marque (Foreground) |
| Gris sur fond principal | `#B9B9B8` | Marque (Foreground Muted) |
| Filet et trame sur fond principal | `#2C2C2C` | Marque (Border) |
| Carte sur fond principal | `#0A0A0A`, filet, sans ombre | Marque : une carte a la même surface que la page |
| Fond secondaire | `#FAFAF8` | Choix : la marque n'a pas de fond clair, on prend sa valeur la plus claire |
| Texte sur fond secondaire | `#0A0A0A` | Marque (Background) |
| Gris sur fond secondaire | `#5E5E5D` | Choix |
| Filet et trame sur fond secondaire | `#D9D9D6`, `#DEDEDB` | Choix |
| Carte sur fond secondaire | `#FAFAF8`, ombre douce | Choix |
| **Accent** | `#EBB52E` (jaune) | Marque (Primary) |
| Texte posé sur l'accent | `#0A0A0A` | Marque : le noir sur ce jaune se lit à 10,5 pour 1 |
| Force du surlignage | 100 % (aplat plein) | Choix |
| Police des chiffres et mots-clés | Special Gothic Expanded One | **Choix de Wanzt** (2026-10-11), après comparaison avec Clash Display. Voir plus bas. |
| Graisse | une seule, très noire | La police n'en a pas d'autre |
| Taille | 82 % de la taille normale | Choix : elle est environ 22 % plus large que Clash Display ; sans cette réduction, les mots-clés sortent de l'image |
| Approche ; espace entre les mots | −0,02 em ; +0,14 em | Choix : ses espaces sont étroits pour des lettres aussi larges |
| Police des dates, libellés, sources | JetBrains Mono | Choix : la marque n'a pas de monospace |
| Police de la chute | Instrument Serif italique | Choix : la marque n'a pas de serif |

## Ce qui est laissé de côté

- **Le bleu de la marque** (`#374AE9`, Accent). Le style ne veut qu'une couleur vive.
- **Albert Sans**, la police de texte courant de la marque. Le style n'a pas de texte courant.

## À savoir

- **La police des chiffres n'est pas celle du design system.** `design.md` impose Clash Display pour les titres. Wanzt a préféré Special Gothic Expanded One pour la vidéo, après les avoir comparées côte à côte (`apercus-habillages/comparaison-digital-black.png`). L'écart est voulu, et il ne vaut que pour la vidéo : `design.md` n'a pas été modifié. Si la marque adopte cette police ailleurs, c'est à Wanzt de l'y écrire.
- **Les chiffres sont plus larges et plus noirs que dans la référence, mais moins hauts.** C'est le prix de la réduction à 82 %.
- **Sur le fond secondaire, le jaune ne s'écrit pas.** Il se lit mal sur le clair (1,8 pour 1). Il y sert en aplat (surlignage, étiquette, dessus d'un objet), jamais comme couleur de texte.
- **Toutes les polices de cet habillage sont libres** (licence OFL). Le fichier vient de `Digital black/Special_Gothic_Expanded_One.zip`, fourni par Wanzt.
