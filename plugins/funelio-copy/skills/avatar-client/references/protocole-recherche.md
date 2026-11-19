# Protocole de recherche terrain — Guide Apify

## Acteurs Apify utilisés

| Plateforme | Acteur Apify | Fiabilité | Coût estimé |
|---|---|---|---|
| YouTube | `streamers/youtube-comments-scraper` | 99% succès — 16 500 utilisateurs | $0.002/commentaire |
| TikTok | `clockworks/tiktok-comments-scraper` | 98.7% succès — 30 000 utilisateurs | $0.00125/commentaire |
| Reddit | `easyapi/reddit-comments-search-scraper` | 95% succès | $0.003/résultat |
| Facebook | `easyapi/facebook-post-comments-scraper` | 94.9% succès — rating faible | $0.003/commentaire |

**Coût total estimé pour 1 000 commentaires toutes plateformes :**
- 500 YouTube + 300 TikTok + 200 Reddit ≈ $1.50 à $2.50

---

## Workflow complet

### Étape 1 — Trouver les URLs avec WebSearch

**YouTube — requêtes à lancer :**
```
[niche] problèmes difficultés site:youtube.com
[niche] "j'en peux plus" OR "je galère" site:youtube.com
[niche] témoignage avis honnête site:youtube.com
[niche] erreurs que j'ai faites site:youtube.com
[niche] vérité site:youtube.com
```
→ Cible les vidéos avec 1 000+ vues et 100+ commentaires. Retiens 5 à 10 URLs.

**TikTok — requêtes à lancer :**
```
[niche] site:tiktok.com
[niche] "moi aussi" tiktok
hashtag [niche] tiktok vidéo populaire
```
→ Retiens les URLs des vidéos avec le plus d'engagement (likes + commentaires).

**Reddit — recherche directe par mot-clé via l'acteur (pas besoin d'URLs à l'avance)**

---

### Étape 2 — Lancer les acteurs Apify

#### YouTube : `streamers/youtube-comments-scraper`

```json
{
  "startUrls": [
    {"url": "https://www.youtube.com/watch?v=ID1"},
    {"url": "https://www.youtube.com/watch?v=ID2"},
    {"url": "https://www.youtube.com/watch?v=ID3"}
  ],
  "maxComments": 200,
  "sortCommentsBy": "TOP_COMMENTS"
}
```
→ `TOP_COMMENTS` priorise les commentaires les plus likés = les douleurs les plus partagées.
→ Vise 200 commentaires × 5 vidéos = 1 000 commentaires YouTube.

#### TikTok : `clockworks/tiktok-comments-scraper`

```json
{
  "postURLs": [
    "https://www.tiktok.com/@username/video/ID1",
    "https://www.tiktok.com/@username/video/ID2"
  ],
  "commentsPerPost": 150,
  "maxRepliesPerComment": 0
}
```
→ `maxRepliesPerComment: 0` exclut les réponses imbriquées pour se concentrer sur les commentaires principaux.
→ Vise 150 × 3 à 5 vidéos = 400 à 750 commentaires TikTok.

#### Reddit : `easyapi/reddit-comments-search-scraper`

```json
{
  "queries": [
    "[niche] problème",
    "[niche] frustration aide",
    "[niche] conseil débutant"
  ],
  "maxResults": 200
}
```
→ Cherche directement par mot-clé dans toute la base Reddit.

**Fallback Reddit si l'acteur échoue :**
Utilise `web_fetch` directement sur les URLs Reddit trouvées à l'étape 1. Reddit est accessible sans JavaScript — ajoute `.json` à la fin de l'URL pour récupérer les données brutes.
Exemple : `https://reddit.com/r/[subreddit]/comments/[id].json`

---

### Étape 3 — Récupérer les résultats

Après chaque `call-actor`, récupère le run ID dans la réponse, puis appelle `get-actor-output` :
```
get-actor-output(runId: "RUN_ID_RETOURNÉ")
```
Les résultats contiennent le dataset avec tous les commentaires scrapés.

---

## Ce qu'on cherche dans les commentaires

### Signaux à haute valeur (prioriser)
- Commentaires avec 50+ likes → douleur très partagée
- Questions récurrentes ("comment vous faites pour...")
- Expressions d'échec et de frustration ("j'ai essayé X mais ça n'a pas marché")
- Aspirations claires ("mon rêve c'est de...")
- Critiques des solutions actuelles ("le problème avec [concurrent] c'est que...")

### Signaux à exclure
- Spam et commentaires hors-sujet
- Commentaires de bots ou de promotion
- Réponses trop courtes sans contenu exploitable ("super vidéo !", "merci")

---

## Saturation thématique

Continue à chercher tant que de nouveaux thèmes émergent dans les commentaires. Arrête quand les mêmes idées reviennent en boucle sur 80%+ des commentaires récents. Avec 1 000+ commentaires, la saturation est généralement atteinte.

---

## Notes sur Facebook

L'acteur `easyapi/facebook-post-comments-scraper` fonctionne uniquement sur les **posts publics** (pas les groupes privés). Rating faible (2.27/5) — utilise-le en dernier recours si YouTube et TikTok ont fourni suffisamment de données. Pour trouver des posts Facebook publics pertinents :
```
[niche] site:facebook.com "j'ai besoin" OR "quelqu'un sait"
```
