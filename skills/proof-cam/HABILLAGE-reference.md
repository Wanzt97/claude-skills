# Habillage de référence — theyo

L'habillage, c'est la peau du style : couleurs, polices, textures. Il se change sans toucher à la grammaire, qui vit dans [FICHE.md](FICHE.md).

Cet habillage est celui de la vidéo de référence. Il sert de modèle pour remplir les suivants. Monter une vidéo avec lui, c'est ressembler à theyo.

## Les cases à remplir

Un habillage remplit ces cases, et seulement celles-là. Elles se recopient dans `gabarit/lib/habillages/reference.css`.

Le style a deux fonds. Le **fond principal** porte l'essentiel de la vidéo (68 % du temps dans la référence). Le **fond secondaire** sert pour « l'autre monde » : une analogie, l'ancienne façon de faire. Dans la référence, le principal est sombre et le secondaire clair. Une marque claire inverse les deux.

| Case | Valeur de référence | Preuve |
|---|---|---|
| Fond principal | `#0A0A0A` | Mesuré : valeur la plus fréquente sur 8 images en pleine résolution |
| Texte sur fond principal | `#F5F5F5` | Mesuré |
| Gris sur fond principal | `#8A8A8A` | Choix |
| Filet et trame sur fond principal | `#2E2E2E`, `#2A2A2A` | Choix |
| Carte sur fond principal | `#131313`, sans ombre | Lu |
| Fond secondaire | `#F3F3F3` | Mesuré, non remesuré |
| Texte sur fond secondaire | `#0A0A0A` | Même valeur que le fond principal |
| Gris sur fond secondaire | `#6B6B6B` | Choix |
| Filet et trame sur fond secondaire | `#CFCFCF`, `#D4D4D4` | Choix |
| Carte sur fond secondaire | `#FFFFFF`, ombre douce et courte | Lu |
| **Accent** | `#D1F916` (lime) | Mesuré sur 25 000 pixels d'aplats ; quartiles rouge 206–211, vert 247–251, bleu 17–26 |
| Texte posé sur l'accent | `#0A0A0A` | Lu |
| Force du surlignage | 100 % (aplat plein) | Lu |
| Police des chiffres et mots-clés | grotesque très grasse, approche serrée | Lu ; nom d'origine inconnu |
| Graisse et approche de cette police | 800 ; −0,035 em | Choix, pour s'approcher de la référence |
| Police des dates, libellés, sources | monospace, capitales espacées | Lu ; nom d'origine inconnu |
| Police de la chute | serif italique | Lu ; nom d'origine inconnu |

**Polices de remplacement proposées** (*Choix*, libres de droits) : Inter Tight 800, JetBrains Mono 400, Instrument Serif italique.

La valeur de l'accent a une marge d'erreur : la vidéo vient de YouTube, dont la compression décale légèrement les couleurs.

## Les textures

| Élément | Description | Preuve |
|---|---|---|
| Trame de points | sur tous les fonds | Lu |
| Croix de repérage « + » | aux angles | Lu |
| Année géante en filigrane | derrière les frises | Lu |
| Extraits externes | noir et blanc, contraste relevé, légère trame | Lu |
| Cartes | plates, filet de 1 px ; pas d'ombre sur fond sombre, ombre douce et courte sur fond clair | Lu |
| Objets filaires | monochromes, translucides, accent seulement sur la partie à désigner | Lu |
| Flou, lueur | aucun | Lu sur 3 déplacements |

## Créer un autre habillage

1. Copier ce fichier et le renommer au nom de la marque.
2. Remplir les cases depuis le design system de la marque, sans en ajouter. Noter pour chaque case si la valeur vient de la marque ou si c'est un choix.
3. Garder **un seul accent**. C'est une règle de la grammaire, pas de l'habillage. Une marque qui a deux couleurs vives en laisse une de côté.
4. Dire quel fond est le principal. Une marque claire prend le clair.
5. Vérifier que le texte se lit sur l'accent. Si l'accent est foncé, baisser la force du surlignage et passer le texte posé dessus en clair.
6. Recopier les cases dans `gabarit/lib/habillages/<marque>.css`, sur le modèle des fichiers voisins, et y déposer les polices.
7. Regarder la démonstration du gabarit dans ce nouvel habillage avant de s'en servir.

Les habillages qui existent : [référence](HABILLAGE-reference.md), [Digital Black](HABILLAGE-digital-black.md), [Wanzt](HABILLAGE-wanzt.md).
