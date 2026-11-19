import json, sys, html, datetime
D=sys.argv[1]+'/project'
P916='/_blob/0f54acc71e0c38ce5df062e0b3c2ba03'; P169='/_blob/0cb1089dcae3ac9ce3e07fc26d68fe54'
def w(p,s):
    if p.endswith('preview.html'):
        import re as _re
        s=_re.sub(r'class="(ms-bloc|ms-titre)\b', r'class="\1 ms-sortie', s)
    import os as _os; _os.makedirs(_os.path.dirname(f'{D}/{p}'),exist_ok=True)
    open(f'{D}/{p}','w').write(s)
now=datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')

# ---------------- tokens ----------------
T=lambda n,v,u: {"name":n,"value":v,"usage":u}
tokens={"name":"Digital Black Edit Style","version":1,
"color":{"themes":[{"id":"noir","name":"Noir"}],"tokens":[
 T("abysse","#0a0a0a","Noir le plus profond. Base du halo sombre."),
 T("noir-digital","#121212","Fond de tout plan graphique (cartons, plein écran)."),
 T("graphite","#1a1a1a","Surface 1 : fond d’aperçu, cartes posées."),
 T("fonte","#232323","Surface 2 : objets placés derrière la personne (cartes, logo)."),
 T("acier","#3a3a3a","Trait 2 px des objets et des cadres d’aperçu. Jamais porteur de sens."),
 T("cendre","#6e6e6e","Repères de travail seulement (zone visage). Jamais dans une vidéo livrée."),
 T("brume","#a3a3a3","Texte secondaire et étiquettes mono sur noir-digital (7,4:1)."),
 T("os","#efefef","Tout le texte des sous-titres : amorce et mot clé par défaut. Jamais de blanc pur."),
 T("braise","#ff7033","L’unique accent (nuance N4 choisie le 2026-11-06 : clarté 60 %, saturation 100 %, 6,8:1 sur noir-digital). Le mot le plus fort, au plus 1 bloc sur 3, et les poignées de sélection. Un seul élément braise à l’écran."),
 T("braise-fonce","#c2410c","Texte braise sur fond clair (4,5:1 sur os) : le mot clé ou le titre le plus fort. Validé le 2026-11-06. Jamais sur la vidéo ni sur fond noir."),
 T("encre-2","#5c5a55","Texte secondaire et étiquettes sur fond clair."),
 T("blanc-carte","#ffffff","Cartes posées sur fond clair ou sur la vidéo (carte idée). Jamais pour du texte."),
 T("grille-noir","rgba(255,255,255,0.06)","Lignes 1 px de la grille des fonds noirs."),
 T("grille-clair","rgba(18,18,18,0.08)","Lignes 1 px de la grille des fonds blancs."),
 T("case-noir","rgba(255,255,255,0.05)","Case allumée neutre sur fond noir."),
 T("case-clair","rgba(18,18,18,0.05)","Case allumée neutre sur fond blanc."),
 T("case-braise","rgba(255,77,0,0.16)","Case orange des fonds, 3 au plus (orange d’origine des fonds, gardé tel quel à la demande de Wanzt)."),
 T("case-braise-trait","rgba(255,77,0,0.5)","Bordure 1 px de la case orange."),
 T("croix-clair","#c9c7c2","Petites croix du fond Plan d’architecte en blanc (en noir : acier)."),
 T("bord-clair","#e6e5e2","Bord du fond Grappes en blanc (dégradé depuis os).")]},
"type":{"fonts":[],"families":{"text":"Inter, \"Inter Tight\", system-ui, sans-serif","accent":"Doto, \"JetBrains Mono\", ui-monospace, monospace","mono":"\"JetBrains Mono\", \"IBM Plex Mono\", ui-monospace, monospace"},
 "groups":[
  {"name":"Sous-titres","family":"text","styles":[
   {"name":"amorce-916","fontSize":"56px","lineHeight":1.05,"fontWeight":800,"letterSpacing":"-0.01em","sample":"ce tunnel m’a rapporté","usage":"Amorce du bloc en 9:16. Casse de phrase, os, halo sombre."},
   {"name":"amorce-169","fontSize":"44px","lineHeight":1.05,"fontWeight":800,"letterSpacing":"-0.01em","sample":"et tout tourne grâce à","usage":"Amorce du bloc en 16:9."}]},
  {"name":"Mot clé","family":"accent","styles":[
   {"name":"motcle-916","fontSize":"240px","lineHeight":0.9,"fontWeight":900,"letterSpacing":"-0.04em","sample":"200 €","usage":"Mot clé en 9:16 (≈ 4× l’amorce, validé le 2026-11-06 après le test). 6 à 7 signes dans 920 px."},
   {"name":"motcle-169","fontSize":"200px","lineHeight":0.9,"fontWeight":900,"letterSpacing":"-0.04em","sample":"Claude.","usage":"Mot clé en 16:9 (≈ 4,5× l’amorce)."},
   {"name":"motcle-min","fontSize":"180px","lineHeight":0.9,"fontWeight":900,"letterSpacing":"-0.04em","sample":"système","usage":"Plancher du mot clé en 9:16 : trop large pour 920 px, il descend jusqu’ici, puis passe sur 2 lignes. Jamais plus petit."},
   {"name":"titre-916","fontSize":"420px","lineHeight":0.8,"fontWeight":900,"letterSpacing":"-0.04em","sample":"5","usage":"Titre-choc en 9:16 : le plus gros qui tient, 420 px au plus."},
   {"name":"titre-169","fontSize":"340px","lineHeight":0.8,"fontWeight":900,"letterSpacing":"-0.04em","sample":"5","usage":"Titre-choc en 16:9, 340 px au plus."}]},
  {"name":"Étiquettes","family":"mono","styles":[
   {"name":"label","fontSize":"22px","lineHeight":1.2,"fontWeight":600,"letterSpacing":"0.08em","sample":"ÉTAPE 01","usage":"Étiquette dans un objet ou une carte, 16:9. MAJUSCULES."},
   {"name":"label-916","fontSize":"28px","lineHeight":1.2,"fontWeight":600,"letterSpacing":"0.08em","sample":"VENTES","usage":"Étiquette en 9:16."}]}]},
"spacing":{"tokens":[
 T("bloc-916-bas","1330px","9:16 : y du bas du bloc de sous-titres par défaut."),
 T("bloc-916-bas-max","1560px","9:16 : y le plus bas autorisé pour le bas du bloc (au-delà, l’interface des Shorts)."),
 T("bloc-916-marge","80px","9:16 : marge gauche et droite du bloc (largeur utile 920 px)."),
 T("bloc-169-bas","900px","16:9 : y du bas du bloc par défaut."),
 T("bloc-169-marge","160px","16:9 : marge gauche et droite du bloc (largeur utile 1600 px)."),
 T("sous-menton","40px","Écart minimal entre le menton et le haut du bloc ou du titre. Rien ne couvre le visage."),
 T("ecart-ligne","20px","Écart entre l’amorce et le mot clé en variante En ligne."),
 T("montee-objet","48px","Montée d’entrée d’un objet placé derrière la personne."),
 T("poignee","16px","Côté d’une poignée carrée du cadre de sélection."),
 T("case","60px","Côté d’une case de la grille des fonds (32 × 18 en 16:9, 18 × 32 en 9:16)."),
 T("bande-916","760px","9:16 : hauteur de la bande graphique de l’écran partagé (40 %)."),
 T("panneau-169","820px","16:9 : largeur du panneau graphique de l’écran partagé (≈ 43 %)."),
 T("incrust-marge","56px","16:9 : marge de l’A-roll rétracté dans le coin bas-droite."),
 T("incrust-taille","0.3","16:9 : échelle de l’A-roll rétracté (30 %).")]},
"radius":{"tokens":[T("radius-none","0px","Poignées de sélection, cadre de sélection."),T("radius-sm","3px","Étiquettes."),T("radius-md","6px","Objets et cartes derrière la personne. Le maximum.")]},
"shadow":{"note":"Deux ombres : le halo sombre sur tout texte posé sur la vidéo, et l’ombre claire sous les objets posés sur un fond clair. Jamais d’ombre colorée ni décalée.","tokens":[T("halo-sombre","0 0 36px rgba(10,10,10,0.8), 0 2px 6px rgba(10,10,10,0.6)","text-shadow de l’amorce, du mot clé et du titre-choc (choix O3 du 2026-11-06). Sur la vidéo seulement : pas sur un fond clair graphique."),T("ombre-claire","0 18px 40px rgba(18,18,18,0.12), 0 2px 6px rgba(18,18,18,0.08)","box-shadow des objets posés sur un fond clair (cartes, pastilles). Validée le 2026-11-06. Jamais sur fond noir.")]},
"stroke":{"tokens":[T("trait-selection","3px","Cadre de sélection, en os."),T("trait-objet","2px","Bordure des objets derrière la personne, en acier."),T("trait-zone","4px","Pointillé de la zone visage, repère de travail.")]},
"duration":{"tokens":[
 T("dur-mot","120ms","Entrée d’un mot de l’amorce (fondu + flou), à l’instant où il est dit."),
 T("dur-lettre","240ms","Entrée d’une lettre du mot clé ou du titre ; entrée du cadre de sélection."),
 T("dur-char","30ms","Écart entre deux lettres du mot clé."),
 T("dur-sortie","140ms","Sortie de tout le bloc d’un coup (60 % de dur-lettre, arrondi)."),
 T("dur-objet","400ms","Entrée d’un objet derrière la personne."),
 T("dur-ecart-objet","120ms","Écart entre deux objets qui entrent l’un après l’autre."),
 T("dur-bande-sortie","240ms","Sortie de la bande ou du panneau de l’écran partagé."),
 T("dur-lg","600ms","Mouvements longs : A-roll qui se rétracte et revient, sélection tirée depuis le coin.")]},
"easing":{"tokens":[T("ease-out","cubic-bezier(0.16, 1, 0.3, 1)","Toute entrée."),T("ease-in","cubic-bezier(0.7, 0, 0.84, 0)","Toute sortie."),T("ease-in-out","cubic-bezier(0.65, 0, 0.35, 1)","Mouvements qui vont d’un point à un autre : A-roll rétracté, sélection tirée.")]},
"blur":{"tokens":[T("flou-mot","6px","Flou de départ d’un mot de l’amorce."),T("flou-lettre","12px","Flou de départ d’une lettre du mot clé."),T("flou-titre","16px","Flou de départ d’une lettre du titre-choc."),T("flou-sortie","8px","Flou d’arrivée à la sortie du bloc.")]}}
w('tokens.json',json.dumps(tokens,ensure_ascii=False,indent=1))

# ---------------- bundle.css ----------------
css='''@import url("https://fonts.googleapis.com/css2?family=Doto:wght@900&family=Inter:wght@500;700;800&family=JetBrains+Mono:wght@600&display=swap");
/* DS Montage Wanzt : classes des composants. Toutes les valeurs viennent des jetons (tokens.css). */
.ms-stage{position:relative;overflow:hidden;background:var(--noir-digital)}
.ms-stage--916{width:1080px;height:1920px}
.ms-stage--169{width:1920px;height:1080px}
.ms-plan{position:absolute;left:0;top:0;width:100%;height:100%;object-fit:cover}
.ms-bloc{position:absolute;display:flex;flex-direction:column;align-items:center;text-align:center}
/* sortie : classe .ms-sortie + variable --sortie (sans elle, pas de fondu de sortie ; un sélecteur [style*=] est refusé par hyperframes check) */
.ms-bloc.ms-sortie,.ms-titre.ms-sortie{animation:ms-sortie var(--dur-sortie) var(--ease-in) forwards;animation-delay:var(--sortie)}
.ms-bloc--916{left:var(--bloc-916-marge);right:var(--bloc-916-marge);bottom:calc(1920px - var(--bas, var(--bloc-916-bas)))}
.ms-bloc--169{left:var(--bloc-169-marge);right:var(--bloc-169-marge);bottom:calc(1080px - var(--bas, var(--bloc-169-bas)))}
.ms-ligne{display:flex;align-items:baseline;justify-content:center;gap:var(--ecart-ligne)}
.ms-amorce{font-family:var(--font-text);font-weight:800;font-size:56px;line-height:1.05;letter-spacing:-0.01em;color:var(--os);text-shadow:var(--halo-sombre)}
.ms-bloc--169 .ms-amorce{font-size:44px}
.ms-motcle{font-family:var(--font-accent);font-weight:900;font-size:240px;line-height:0.9;letter-spacing:-0.04em;color:var(--os);text-shadow:var(--halo-sombre);white-space:nowrap}
.ms-bloc--169 .ms-motcle{font-size:200px}
.ms-motcle--braise{color:var(--braise)}
.ms-empile .ms-motcle{margin-top:-6px}
.ms-escalier .ms-amorce:first-child{align-self:flex-start;margin-left:40px}
.ms-escalier .ms-amorce:last-child{align-self:flex-end;margin-right:40px;margin-top:6px}
.ms-mot{display:inline-block;animation:ms-entree-mot var(--dur-mot) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-lettre{display:inline-block;animation:ms-entree-lettre var(--dur-lettre) var(--ease-out) both;animation-delay:calc(var(--t,0ms) + var(--i,0) * var(--dur-char))}
.ms-espace{display:inline-block;width:0.5em}
.ms-titre{position:absolute;font-family:var(--font-accent);font-weight:900;line-height:0.8;letter-spacing:-0.04em;color:var(--os);text-shadow:var(--halo-sombre);white-space:nowrap}
.ms-titre--braise{color:var(--braise)}
.ms-titre .ms-lettre{animation-name:ms-entree-titre}
.ms-selection{position:absolute;border:var(--trait-selection) solid var(--os);border-radius:var(--radius-none);animation:ms-entree-cadre var(--dur-lettre) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-poignee{position:absolute;width:var(--poignee);height:var(--poignee);background:var(--braise)}
.ms-poignee--hg{left:-10px;top:-10px}.ms-poignee--hd{right:-10px;top:-10px}.ms-poignee--bg{left:-10px;bottom:-10px}.ms-poignee--bd{right:-10px;bottom:-10px}
.ms-objet{position:absolute;box-sizing:border-box;border-radius:var(--radius-md);background:var(--fonte);border:var(--trait-objet) solid var(--acier);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;animation:ms-entree-objet var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-objet-label{font-family:var(--font-mono);font-weight:600;font-size:28px;letter-spacing:0.08em;color:var(--brume)}
.ms-zone-visage{position:absolute;box-sizing:border-box;border:var(--trait-zone) dashed var(--cendre);border-radius:var(--radius-md)}
@keyframes ms-entree-mot{from{opacity:0;filter:blur(var(--flou-mot))}to{opacity:1;filter:blur(0)}}
@keyframes ms-entree-lettre{from{opacity:0;filter:blur(var(--flou-lettre))}to{opacity:1;filter:blur(0)}}
@keyframes ms-entree-titre{from{opacity:0;filter:blur(var(--flou-titre))}to{opacity:1;filter:blur(0)}}
@keyframes ms-entree-cadre{from{opacity:0;transform:scale(1.03)}to{opacity:1;transform:scale(1)}}
@keyframes ms-entree-objet{from{opacity:0;transform:translateY(var(--montee-objet))}to{opacity:1;transform:translateY(0)}}
@keyframes ms-sortie{from{opacity:1;filter:blur(0)}to{opacity:0;filter:blur(var(--flou-sortie))}}
'''
w('components/bundle.css',css)

# ---------------- helpers ----------------
def mots(txt,t0,ecart=160):
    out=[];t=t0
    for m in txt.split(' '):
        out.append(f'<span class="ms-mot" style="--t:{t}ms">{html.escape(m)}</span>'); t+=ecart
    return ' '.join(out),t
def lettres(txt):
    return ''.join('<span class="ms-espace"></span>' if c==' ' else f'<span class="ms-lettre" style="--i:{i}">{html.escape(c)}</span>' for i,c in enumerate(txt))
def fin_lettres(txt,t0): return t0+(len(txt)-1)*30+240
PREV_CSS='''<style>
body{margin:0;background:var(--graphite);font-family:var(--font-text);color:var(--os)}
.rang{display:flex;gap:24px;padding:24px;align-items:flex-start}
.ap{display:flex;flex-direction:column;gap:8px}
.cadre{position:relative;overflow:hidden;border:2px solid var(--acier);border-radius:6px}
.cadre .ms-stage{transform-origin:0 0}
.leg{font-family:var(--font-mono);font-weight:600;font-size:12px;letter-spacing:0.08em;text-transform:uppercase;color:var(--brume)}
</style>'''
BOUCLE='''<script>
(function(){setInterval(function(){document.querySelectorAll('[data-boucle]').forEach(function(n){var c=n.cloneNode(true);n.parentNode.replaceChild(c,n);});},3600);})();
</script>'''
def ap(fmt,inner,leg,sc=0.25,plan=True,zone=None):
    W,H=(1080,1920) if fmt=='916' else (1920,1080)
    img=f'<img class="ms-plan" src="{P916 if fmt=="916" else P169}" alt="Plan test face caméra">' if plan is True else (plan or '')
    z=f'<div class="ms-zone-visage" style="left:{zone[0]}px;top:{zone[1]}px;width:{zone[2]}px;height:{zone[3]}px"></div>' if zone else ''
    return f'<figure class="ap" style="margin:0"><div class="cadre" style="width:{int(W*sc)}px;height:{int(H*sc)}px"><div class="ms-stage ms-stage--{fmt}" style="transform:scale({sc})" data-boucle>{img}{z}{inner}</div></div><figcaption class="leg">{leg}</figcaption></figure>'
Z916=(290,740,300,390)  # visage sur le plan test 9:16 (front -> menton)
Z169=(770,410,175,225)  # visage sur le plan test 16:9
SIL='<svg aria-hidden="true" width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0"><circle cx="540" cy="760" r="190" fill="#2c2c2c"></circle><path d="M150 1920 C150 1380 340 1110 540 1110 C740 1110 930 1380 930 1920 Z" fill="#2c2c2c"></path></svg>'
SIL_TETE='<svg aria-hidden="true" width="1080" height="1920" viewBox="0 0 1080 1920" style="position:absolute;left:0;top:0"><circle cx="540" cy="760" r="190" fill="#2c2c2c"></circle><path d="M150 1920 C150 1380 340 1110 540 1110 C740 1110 930 1380 930 1920 Z" fill="#2c2c2c"></path></svg>'

exec(open('planche_c.py').read())
exec(open('planche_suite.py').read())
exec(open('marque.py').read())
exec(open('guide.py').read())

# ---------------- SousTitreDuo ----------------
a1,t=mots("grâce à",0); k1="l’IA."
v1=f'<div class="ms-bloc ms-bloc--916" style="--bas:1450px;--sortie:3200ms"><div class="ms-ligne"><span class="ms-amorce">{a1}</span><span class="ms-motcle" style="--t:{t+120}ms">{lettres(k1)}</span></div></div>'
a2,t=mots("ce tunnel m’a rapporté",0); k2="200 €"
v2=f'<div class="ms-bloc ms-bloc--916 ms-empile" style="--bas:1450px;--sortie:3200ms"><div class="ms-amorce">{a2}</div><div class="ms-motcle ms-motcle--braise" style="--t:{t+120}ms">{lettres(k2)}</div></div>'
a3,t=mots("le secret, c’est",0); k3="tunnel"; t3=fin_lettres(k3,t+120); a3b,_=mots("pas la pub.",t3+80)
v3=f'<div class="ms-bloc ms-bloc--916 ms-escalier" style="--bas:1450px;--sortie:3200ms"><div class="ms-amorce">{a3}</div><div class="ms-motcle" style="--t:{t+120}ms">{lettres(k3)}</div><div class="ms-amorce">{a3b}</div></div>'
a4,t=mots("ce tunnel m’a rapporté",0)
v4=f'<div class="ms-bloc ms-bloc--169" style="--sortie:3200ms"><div class="ms-ligne"><span class="ms-amorce">{a4}</span><span class="ms-motcle ms-motcle--braise" style="--t:{t+120}ms">{lettres(k2)}</span></div></div>'
a5,t=mots("tout tourne grâce à",0,140)
v5=f'<div class="ms-bloc ms-bloc--169 ms-empile" style="--sortie:3200ms"><div class="ms-amorce">{a5}</div><div class="ms-motcle" style="--t:{t+120}ms">{lettres("Claude.")}</div></div>'
prev=f'''<!-- @dsCard group="Sous-titres" height=980 width=1300 subtitle="Amorce + mot clé · rangée 1 : 9:16 (V1, V2, V3) · rangée 2 : 16:9 (V1, V2)" -->
<!doctype html>
<html lang="fr"><head><meta charset="utf-8">{PREV_CSS}</head>
<body><div class="rang">{ap('916',v1,'9:16 · V1 · En ligne',zone=Z916)}{ap('916',v2,'9:16 · V2 · Empilé · braise',zone=Z916)}{ap('916',v3,'9:16 · V3 · Escalier',zone=Z916)}</div><div class="rang">{ap('169',v4,'16:9 · V1 · En ligne · braise',sc=0.3,zone=Z169)}{ap('169',v5,'16:9 · V2 · Empilé',sc=0.3,zone=Z169)}</div>{BOUCLE}</body></html>
'''
w('components/SousTitreDuo/preview.html',prev)
w('components/SousTitreDuo/README.md','''# SousTitreDuo

Le bloc de sous-titres du style : une amorce en petit, puis un mot clé géant en Doto 900, sans plaque, avec le halo sombre.

**Ce que tu fournis :** la transcription mot à mot (avec les temps), découpée en blocs ; pour chaque bloc, le mot clé ; la position du menton sur le plan (ou le cadrage).

## Structure
- **Amorce** : `.ms-amorce`, style `amorce-916` / `amorce-169`, couleur `os`, halo `halo-sombre`. Casse de phrase. **1 à 4 mots, jamais plus** : une phrase plus longue se coupe en plusieurs blocs, chacun avec son mot clé.
- **Mot clé** : `.ms-motcle`, style `motcle-916` / `motcle-169`, couleur `os` ; `.ms-motcle--braise` pour le mot le plus fort (au plus 1 bloc sur 3). Voir **MotCle**.
- Chaque bloc a un mot clé : le nom, le chiffre ou le verbe qui porte le sens. Jamais un mot de liaison.

## Variantes
| Variante | Classe | Quand |
|---|---|---|
| V1 En ligne | `.ms-ligne` | amorce ≤ 12 signes et mot clé ≤ 5 signes en 9:16 ; amorce ≤ 28 signes en 16:9 |
| V2 Empilé | `.ms-empile` | amorce plus longue : elle passe au-dessus |
| V3 Escalier | `.ms-escalier` | 9:16 seulement : petit, géant, petit, quand la phrase a une suite courte |

## Placement
- 9:16 : `.ms-bloc--916`, centré, largeur 920 px (`bloc-916-marge`). Bas du bloc à `bloc-916-bas` (y 1330) par défaut.
- 16:9 : `.ms-bloc--169`, centré, largeur 1600 px. Bas du bloc à `bloc-169-bas` (y 900). Pas de V3.
- **Jamais sur le visage.** Le haut du bloc reste au moins `sous-menton` (40 px) sous le menton. Si le visage est bas, descends le bloc (variable `--bas`) jusqu’à `bloc-916-bas-max` (y 1560). Sur le plan test, `--bas: 1450px`.
- Mot clé trop large pour 920 px : il descend jusqu’à `motcle-min` (140 px), puis passe sur 2 lignes.

## Mouvement
| Élément | Entrée | Sortie |
|---|---|---|
| Mot de l’amorce `.ms-mot` | à l’instant où il est dit (`--t`) : fondu + flou `flou-mot` → 0, `dur-mot` (120 ms), `ease-out`. Aucun déplacement. | avec le bloc |
| Lettre du mot clé `.ms-lettre` | à l’instant où le mot est dit (`--t` sur `.ms-motcle`), de gauche à droite : chaque lettre fondu + flou `flou-lettre` → 0, `dur-lettre` (240 ms), `ease-out`, décalée de `dur-char` (30 ms) × son rang `--i` | avec le bloc |
| Bloc `.ms-bloc` | — | tout d’un coup, juste avant le 1er mot du bloc suivant (classe `.ms-sortie` + `--sortie`) : fondu + flou 0 → `flou-sortie`, `dur-sortie` (140 ms), `ease-in` |

Le bloc reste fixe entre l’entrée et la sortie. Jamais de rebond, de glissement ni de zoom.

## À ne pas faire
Plaque ou pastille derrière le texte, surlignage, mot en couleur dans la police de l’amorce, petits sous-titres sobres sans mot clé, majuscules forcées, serif ou script, ombre colorée ou décalée, texte sur le visage.
''')

# ---------------- MotCle ----------------
prev=f'''<!-- @dsCard group="Sous-titres" height=420 width=1200 subtitle="Os par défaut, braise pour le mot le plus fort" -->
<!doctype html>
<html lang="fr"><head><meta charset="utf-8">{PREV_CSS}
<style>.case{{flex:1;background:var(--noir-digital);border:2px solid var(--acier);border-radius:6px;padding:28px;display:flex;flex-direction:column;gap:18px;min-height:300px;box-sizing:border-box}}
.case p{{margin:0;font-size:16px;line-height:1.45;color:var(--brume)}}
.case .ms-motcle{{font-size:110px}}</style></head>
<body><div class="rang">
<section class="case"><span class="leg">Os · par défaut</span><span class="ms-motcle">Claude.</span><p>La plupart des blocs. Le contraste vient de la taille et de la police.</p></section>
<section class="case"><span class="leg">Braise · le mot le plus fort</span><span class="ms-motcle ms-motcle--braise">12 400 €</span><p>Un chiffre, un résultat, le mot de l’accroche. Au plus 1 bloc sur 3.</p></section>
<section class="case"><span class="leg">Interdit</span><span class="ms-amorce" style="font-size:52px">le <span style="color:var(--braise)">tunnel</span></span><p>Mot en couleur dans la police de l’amorce, plaque, surlignage, serif, script.</p></section>
</div></body></html>
'''
w('components/MotCle/preview.html',prev)
w('components/MotCle/README.md','''# MotCle

Le mot mis en avant : un ou deux mots en Doto 900, la pièce centrale du style, dans le bloc de sous-titres comme dans le titre-choc.

**Ce que tu fournis :** le mot, et s’il est le plus fort du passage.

- Police `accent` (Doto 900), styles `motcle-916` (240 px), `motcle-169` (200 px), plancher `motcle-min` (180 px). Approche −0,04 em. En 9:16, 6 à 7 signes tiennent dans 920 px.
- Couleur `os` par défaut. `braise` (`.ms-motcle--braise`) pour le mot le plus fort : un chiffre, un résultat, le mot de l’accroche. Au plus 1 bloc sur 3, et jamais deux éléments braise à l’écran.
- Toujours le halo `halo-sombre`.
- Choix du mot : le nom, le chiffre ou le verbe qui porte le sens. Jamais « le », « et », « de », « c’est ».
- Casse de la phrase. Le point final reste collé au mot (« Claude. »).
- Entrée lettre par lettre : voir **SousTitreDuo**, Mouvement.

**À ne pas faire :** mot en couleur dans la police de l’amorce, plaque, surlignage, serif, script, majuscules forcées.
''')

# ---------------- TitreChoc ----------------
# V1 chiffre + amorce, sous le menton du plan test
t1=fin_lettres("5",200)
am1,_=mots("outils qui",t1); am2,_=mots("font tout",t1+320)
v1=f'<div class="ms-titre ms-titre--braise" style="left:120px;top:1200px;font-size:420px;--t:200ms;--sortie:3200ms"><span style="--t:200ms;display:inline-block">{lettres("5").replace("--i:0","--i:0;--t:200ms")}</span></div><div class="ms-bloc ms-bloc--916" style="--bas:1520px;--sortie:3200ms;left:420px;align-items:flex-start;text-align:left"><div class="ms-amorce">{am1}</div><div class="ms-amorce">{am2}</div></div>'
# V3 sélection au-dessus de la tête (plan test : haut de tête ~ y 740)
tc=fin_lettres("Claude",260)
am,_=mots("monte tes vidéos avec",0,140)
v3=f'<div class="ms-bloc ms-bloc--916" style="--bas:300px;--sortie:3200ms"><div class="ms-amorce">{am}</div></div><div class="ms-titre" style="left:0;right:0;top:360px;text-align:center;font-size:220px;--sortie:3200ms"><span style="--t:260ms;display:inline-block">{lettres("Claude")}</span></div><div class="ms-selection" style="left:110px;right:110px;top:330px;height:240px;--t:{tc+120}ms"><span class="ms-poignee ms-poignee--hg"></span><span class="ms-poignee ms-poignee--hd"></span><span class="ms-poignee ms-poignee--bg"></span><span class="ms-poignee ms-poignee--bd"></span></div>'
# V2a/b/c derrière la personne (schéma : silhouette = détourage)
tt=fin_lettres("TUNNEL",200); amt,_=mots("le vrai secret :",tt)
d_titre=f'<div class="ms-titre" style="left:0;right:0;top:440px;text-align:center;font-size:250px;--sortie:3200ms"><span style="--t:200ms;display:inline-block">{lettres("TUNNEL")}</span></div>'
devant_t=f'<div class="ms-bloc ms-bloc--916" style="--bas:1180px;--sortie:3200ms"><div class="ms-amorce">{amt}</div></div>'
play='<svg aria-hidden="true" width="260" height="260" viewBox="0 0 32 32"><path d="M11 7 L25 16 L11 25 Z" fill="none" stroke="#efefef" stroke-width="2"></path></svg>'
d_logo=f'<div class="ms-objet" style="left:290px;top:170px;width:500px;height:500px;--t:200ms">{play}<span class="ms-objet-label" style="position:absolute;left:24px;top:20px">LOGO / IMAGE</span></div>'
amy,_=mots("tout part de",600); 
devant_l=f'<div class="ms-bloc ms-bloc--916" style="--sortie:3200ms"><div class="ms-amorce">{amy}</div><div class="ms-motcle" style="--t:1000ms;margin-top:-6px">{lettres("TikTok")}</div></div>'
ic_doc='<svg aria-hidden="true" width="120" height="120" viewBox="0 0 32 32"><path d="M8 4 H19 L25 10 V28 H8 Z M19 4 V10 H25 M12 16 H21 M12 21 H21" fill="none" stroke="#efefef" stroke-width="2"></path></svg>'
ic_bar='<svg aria-hidden="true" width="120" height="120" viewBox="0 0 32 32"><path d="M6 26 H27 M9 26 V17 M15 26 V11 M21 26 V6" fill="none" stroke="#efefef" stroke-width="3"></path></svg>'
ic_eng='<svg aria-hidden="true" width="120" height="120" viewBox="0 0 32 32"><circle cx="16" cy="16" r="5" fill="none" stroke="#efefef" stroke-width="2"></circle><path d="M16 3 V8 M16 24 V29 M3 16 H8 M24 16 H29 M7 7 L10.5 10.5 M21.5 21.5 L25 25 M25 7 L21.5 10.5 M10.5 21.5 L7 25" fill="none" stroke="#efefef" stroke-width="2"></path></svg>'
d_objs=f'<div class="ms-objet" style="left:60px;top:330px;width:300px;height:320px;--t:200ms">{ic_doc}<span class="ms-objet-label">PAGE</span></div><div class="ms-objet" style="left:390px;top:150px;width:300px;height:320px;--t:320ms">{ic_bar}<span class="ms-objet-label">VENTES</span></div><div class="ms-objet" style="left:720px;top:330px;width:300px;height:320px;--t:440ms">{ic_eng}<span class="ms-objet-label">AUTO</span></div>'
amo,_=mots("trois outils, un",700)
devant_o=f'<div class="ms-bloc ms-bloc--916" style="--sortie:3200ms"><div class="ms-amorce">{amo}</div><div class="ms-motcle" style="--t:1100ms;margin-top:-6px;font-size:180px">{lettres("système")}</div></div>'
ZS=(330,550,420,420)
SIL169='<svg aria-hidden="true" width="1920" height="1080" viewBox="0 0 1920 1080" style="position:absolute;left:0;top:0"><circle cx="960" cy="420" r="160" fill="#2c2c2c"></circle><path d="M600 1080 C600 780 780 640 960 640 C1140 640 1320 780 1320 1080 Z" fill="#2c2c2c"></path></svg>'
ZS169=(790,250,340,340)
t1h=fin_lettres("5",200); h1,_=mots("outils qui",t1h); h2,_=mots("font tout",t1h+320)
h_v1=f'<div class="ms-titre ms-titre--braise" style="left:200px;top:360px;font-size:340px;--sortie:3200ms"><span style="--t:200ms;display:inline-block">{lettres("5")}</span></div><div class="ms-bloc" style="left:430px;top:470px;bottom:auto;align-items:flex-start;text-align:left;--sortie:3200ms"><div class="ms-amorce" style="font-size:44px">{h1}</div><div class="ms-amorce" style="font-size:44px">{h2}</div></div>'
tch=fin_lettres("Claude",260); hs,_=mots("monte tes vidéos avec",0,140)
h_v3=f'<div class="ms-bloc ms-bloc--169" style="--bas:110px;--sortie:3200ms"><div class="ms-amorce">{hs}</div></div><div class="ms-titre" style="left:0;right:0;top:150px;text-align:center;font-size:190px;--sortie:3200ms"><span style="--t:260ms;display:inline-block">{lettres("Claude")}</span></div><div class="ms-selection" style="left:640px;right:640px;top:126px;height:200px;--t:{tch+120}ms"><span class="ms-poignee ms-poignee--hg"></span><span class="ms-poignee ms-poignee--hd"></span><span class="ms-poignee ms-poignee--bg"></span><span class="ms-poignee ms-poignee--bd"></span></div>'
th=fin_lettres("TUNNEL",200); ht,_=mots("le vrai secret :",th)
h_v2=f'<div class="ms-titre" style="left:0;right:0;top:200px;text-align:center;font-size:260px;--sortie:3200ms"><span style="--t:200ms;display:inline-block">{lettres("TUNNEL")}</span></div>'+SIL169+f'<div class="ms-bloc ms-bloc--169" style="--bas:760px;--sortie:3200ms"><div class="ms-amorce">{ht}</div></div>'
prev=f'''<!-- @dsCard group="Accroche" height=900 width=1500 subtitle="Rangée 1 : 9:16 (V1, V3, V2a, V2b, V2c) · rangée 2 : 16:9 (V1 à côté du visage, V3, V2a)" -->
<!doctype html>
<html lang="fr"><head><meta charset="utf-8">{PREV_CSS}</head>
<body><div class="rang">{ap('916',v1,'9:16 · V1 · Chiffre + amorce',zone=Z916)}{ap('916',t9,l9,zone=Z916)}{ap('916',d_titre+SIL+devant_t,'9:16 · V2a · Derrière : titre',plan=False,zone=ZS)}{ap('916',d_logo+SIL+devant_l,'9:16 · V2b · Derrière : logo',plan=False,zone=ZS)}{ap('916',d_objs+SIL+devant_o,'9:16 · V2c · Derrière : objets',plan=False,zone=ZS)}</div><div class="rang">{ap('169',h_v1,'16:9 · V1 · À côté du visage',zone=Z169)}{ap('169',t16,l16,zone=Z169)}{ap('169',h_v2,'16:9 · V2a · Derrière : titre',plan=False,zone=ZS169)}</div>{BOUCLE}</body></html>
'''
w('components/TitreChoc/preview.html',prev)
w('components/TitreChoc/README.md','''# TitreChoc

Le titre d’accroche : un mot ou un chiffre géant en Doto 900, ou un élément placé derrière la personne, pour les 3 premières secondes ou l’ouverture d’une partie.

**Ce que tu fournis :** le mot ou le chiffre, la ou les lignes d’amorce, la position du visage sur le plan, et pour V2 un détourage (matte) de la personne et l’élément à placer derrière (titre, logo, image ou 2 à 4 objets).

## Règle d’or
Rien ne couvre le visage, du front au menton : ni titre, ni cadre, ni sous-titre. Un élément peut passer **derrière** la tête (grâce au détourage), jamais devant.

## Variantes
| Variante | Où | Détail |
|---|---|---|
| V1 Chiffre + amorce | 9:16 : sous le menton (`sous-menton`). 16:9 : à côté du visage, dans la partie libre du cadre | `.ms-titre`, style `titre-916` (420 px max) / `titre-169` (340 px max), `os` ou `braise` ; amorce `.ms-amorce` collée à droite sur 1 ou 2 lignes |
| V2 Derrière la personne | derrière la tête et les épaules | un titre (`.ms-titre`), un logo ou une image, ou 2 à 4 objets (`.ms-objet` : fond `fonte`, trait `trait-objet` `acier`, arrondi `radius-md`). Le texte d’amorce reste devant. |
| V3 Sélection tirée | arrivée au-dessus de la tête, jamais dessus (16:9 : à côté du visage) | `.ms-tire` (avec `--dx` / `--dy` = coin de départ − place d’arrivée) qui contient le mot (`.ms-titre`, déjà complet) et son cadre `.ms-selection` (`trait-selection` `os`, sans arrondi, 4 poignées `.ms-poignee` `braise`) ; un curseur `.ms-curseur` (`--cx` / `--cy`) sur la poignée bas-droite. Le cadre compte comme l’élément braise de l’image. Validée le 2026-11-06. |

Le titre-choc ne s’affiche jamais en même temps qu’un bloc de sous-titres. Une fois par vidéo, ou une par partie.

## Mouvement
| Élément | Entrée | Sortie |
|---|---|---|
| Lettre du titre | lettre par lettre, fondu + flou `flou-titre` (16 px) → 0, `dur-lettre`, écart `dur-char`, `ease-out` | tout d’un coup : fondu + flou → `flou-sortie`, `dur-sortie`, `ease-in` |
| Amorce | mot par mot après la dernière lettre, `dur-mot` | avec le titre |
| Objet derrière | montée de `montee-objet` (48 px) + fondu, `dur-objet` (400 ms), `ease-out`, l’un après l’autre tous les `dur-ecart-objet` (120 ms) | avec le titre |
| Sélection tirée | 1 · le mot sélectionné apparaît en petit (30 %) dans le coin haut-gauche, fondu `dur-mot` ; 2 · à +200 ms le curseur prend la poignée bas-droite et clique (85 %) ; 3 · de +320 à +920 ms le cadre et le mot glissent jusqu’à leur place en grandissant de 30 % à 100 %, `dur-lg`, `ease-in-out`, le curseur suit ; 4 · le curseur relâche puis s’en va, le cadre et les poignées s’effacent à +1 400 ms (`dur-lettre`, `ease-in`) : il ne reste que le mot. L’amorce arrive mot par mot. | tout le titre d’un coup (`ms-sortie`) |
''')

# ---------------- Fonds README ----------------
w('assets/Fonds/README.md','''# Fonds

Plans de test pour juger un composant sur une vraie image : Wanzt face caméra, rush « hook 1 » (dossier « Arrêtez d’attendre le ChatGPT africain »), image à 10 s.

- `plan-test-916.jpg` : recadré en 9:16 (1080 × 1920). Visage du front (y ≈ 740) au menton (y ≈ 1110) : le bloc de sous-titres se place avec `--bas: 1450px`.
- `plan-test-169.jpg` : plan entier en 16:9 (1920 × 1080).

- `detour-916.png`, `detour-169.png` : toi détouré sur ces deux plans (PNG transparent, `npx hyperframes remove-background`). Posé par-dessus le plan avec le même cadrage, il permet de faire passer un texte ou un logo **derrière** toi (Accroche, AnimPersonne).

Fond clair et chargé : c’est le cas difficile pour la lisibilité, d’où le halo sombre.
''')

# ---------------- README ----------------
w('README.md',open('readme3.md').read())

# ---------------- Cover ----------------
cover='''<!-- @dsCard height=300 -->
<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<style>
body{margin:0;background:var(--noir-digital)}
.c{position:relative;width:960px;height:300px;overflow:hidden;background:var(--noir-digital)}
.braise{fill:var(--braise)}.os{fill:var(--os)}.fonte{fill:var(--fonte)}.graphite{fill:var(--graphite)}.point{fill:var(--os)}.point-b{fill:var(--braise)}
.tile{rx:var(--radius-md)}
.nom{position:absolute;left:40px;bottom:64px;margin:0;font-family:var(--font-accent);font-weight:900;font-size:68px;line-height:0.95;letter-spacing:-0.04em;color:var(--os);max-width:440px}
.tag{position:absolute;left:40px;bottom:36px;margin:0;font-family:var(--font-text);font-weight:500;font-size:14px;color:var(--brume);max-width:440px}
</style></head>
<body><div class="c">
<svg aria-hidden="true" width="960" height="300" viewBox="0 0 960 300" style="position:absolute;left:0;top:0">
<!-- blocs : braise (300×300 qui déborde en haut), fonte 160×180, graphite 160×100, os 80×80 (radius-md 6px)
     disposition : une dalle braise haute avec satellites, à droite de x 480
     motif : grille de points (Doto est une police matricielle : le mot clé s’allume en points), pas de 24 px
     échelles : pas 24 px, écarts 24 px, arrondi radius-md -->
<rect class="fonte tile" x="504" y="24" width="160" height="180"></rect>
<rect class="graphite tile" x="504" y="228" width="160" height="96"></rect>
<rect class="braise tile" x="688" y="-24" width="248" height="300"></rect>
<rect class="os tile" x="856" y="196" width="80" height="80"></rect>
POINTS
</svg>
<p class="nom">Digital Black<br>Edit Style</p>
<p class="tag">Une amorce qui suit la voix, un mot géant qui s’allume.</p>
</div></body></html>
'''
pts=[]
for gx in range(0,7):
    for gy in range(0,5):
        x=520+gx*20; y=40+gy*30
        if x< 664 and y<204: pts.append(f'<circle class="point" cx="{x}" cy="{y}" r="3"></circle>')
pts=pts[:30]
cover=cover.replace('POINTS','\n'.join(pts))
w('components/Cover/preview.html',cover)

# ---------------- index ----------------
idx={"v":3,"layout":"files","createdOnFiles":{"v":1,"at":"2026-11-06T12:51:42Z"},"title":"Digital Black Edit Style","namespace":"MontageWanzt","libraries":[],"sections":{},"groups":["Fonds","Marque"],
"assetGroups":{"Fonds":{"name":"Fonds","tile":"m","order":["plan-test-916.jpg","plan-test-169.jpg","detour-916.png","detour-169.png"],"files":{
 "plan-test-916.jpg":{"name":"plan-test-916.jpg","blob":"0f54acc71e0c38ce5df062e0b3c2ba03","size":140695,"type":"image/jpeg"},
 "plan-test-169.jpg":{"name":"plan-test-169.jpg","blob":"0cb1089dcae3ac9ce3e07fc26d68fe54","size":180101,"type":"image/jpeg"},**{k:v for k,v in DETOURS.items() if k.startswith("detour")}}},
 "Marque":{"name":"Marque","tile":"m","order":["photo-profil-yt.png"],"files":{"photo-profil-yt.png":DETOURS["photo-profil-yt.png"]}}},
"blobs":{},"docs":{"readme":"project/README.md","sections":[]},
"lastChange":{"by":"Wanzt Koffi","at":now,"via":"Claude Code","note":"Toutes les planches : C (types de scène, fonds), D + G (AnimTexte, AnimPersonne, AnimObjet, AnimGraphique), H fusionnée avec C2 (SceneC2), B (Accroche), F (Composition), I (bibliothèque dans l’atelier) ; 16:9 partout. Renommé Digital Black Edit Style. Marque : logo Digital Black et bouton S’abonner (proposition). Guides : Edit for Digital B (utilisation) et SFX for Digital B (son)."}}
w('design-system.json',json.dumps(idx,ensure_ascii=False,indent=1))
print('ok')
