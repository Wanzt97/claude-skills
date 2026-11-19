# Habillage Wanzt

L'habillage de la marque Wanzt pour le style proof-cam. La grammaire reste celle de [FICHE.md](FICHE.md) : seule la peau change.

**Source** : `Wanzt brand/Design/Wanzt-design.md`, le design system de la marque. Ce fichier-là n'est pas modifié. Quand il change, cet habillage se met à jour, puis `gabarit/lib/habillages/wanzt.css`.

**Créé le** 2026-10-11, à la demande de Wanzt.

## Comment lire les preuves

| Mention | Ce que ça veut dire |
|---|---|
| **Marque** | Valeur prise telle quelle dans le design system de la marque. |
| **Choix** | La marque ne dit rien pour ce cas : valeur décidée ici, pour la vidéo seulement. |

## Les cases

Fond principal : **clair**. Wanzt est une marque claire, donc la proportion de la référence est inversée : l'essentiel de la vidéo est sur le crème, et le fond sombre devient « l'autre monde ».

| Case | Valeur | Preuve |
|---|---|---|
| Fond principal | `#FAF8F5` | Marque (Background) |
| Texte sur fond principal | `#1A1A1A` | Marque (Foreground) |
| Gris sur fond principal | `#4C4C4C` | Marque (Foreground Muted) |
| Filet et trame sur fond principal | `#D7D7D7` | Marque (Border) |
| Carte sur fond principal | `#FAF8F5`, filet, ombre douce | Marque pour la surface ; Choix pour l'ombre |
| Fond secondaire | `#1A1A1A` | Choix : la marque n'a pas de fond sombre, on prend sa valeur la plus sombre |
| Texte sur fond secondaire | `#FAF8F5` | Marque (Background) |
| Gris sur fond secondaire | `#A6A39F` | Choix |
| Filet et trame sur fond secondaire | `#3A3A3A`, `#333333` | Choix |
| Carte sur fond secondaire | `#1A1A1A`, sans ombre | Choix |
| **Accent** | `#C2410C` (orange) | Marque (Primary) |
| Texte posé sur l'accent | `#FAF8F5` | Marque : c'est la règle de ses boutons |
| Force du surlignage | 38 % (lavis) | Choix : voir plus bas |
| Police des chiffres et mots-clés | Epilogue | Marque (Headings) |
| Graisse | 600 | Marque : elle demande de ne pas dépasser 600 sans nécessité |
| Approche ; espace entre les mots | −0,03 em ; normal | Choix |
| Police des dates, libellés, sources | JetBrains Mono | Choix : la marque n'a pas de monospace |
| Police de la chute | Newsreader italique | Marque (c'est son serif) ; décision de Wanzt du 2026-10-11, voir plus bas |

## Ce qui est laissé de côté

- **Le vert sarcelle de la marque** (`#0F766E`, Accent). Le style ne veut qu'une couleur vive.
- **Newsreader droit**, la police de texte courant de la marque : le style n'a pas de texte courant. Seule son italique sert, pour la chute.

## Trois choix à connaître

- **Le surlignage est un lavis, pas un aplat.** L'orange de la marque est foncé : en aplat plein, le texte noir d'une capture ne s'y lit plus. Il est donc posé à 38 %, comme un vrai surligneur. Le geste reste celui de la fiche (de gauche à droite, en 80 ms).
- **Les chiffres sont moins gras que dans la référence** (600 au lieu de 800). Le fichier Epilogue de la marque va jusqu'à 900 : passer la graisse à 800 est possible en changeant une seule valeur, mais c'est une exception à la règle de la marque. À décider par Wanzt.
- **La chute est en Newsreader italique.** C'est la décision de Wanzt (2026-10-11), après avoir comparé avec Fraunces, qu'il a écartée. La marque ne fournit que le Newsreader droit : le fichier de l'italique a été téléchargé du dépôt Google Fonts (licence OFL), avec son accord. Il ne vit que dans le gabarit ; le paquet `wanzt-ui` de la marque n'a pas été touché.
