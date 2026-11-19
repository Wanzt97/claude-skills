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
"type":{"fonts":[],"families":{"text":"Arial, Arimo, \"Helvetica Neue\", sans-serif","accent":"Anton, \"Arial Narrow\", Impact, sans-serif","fin":"Inter, system-ui, sans-serif","mono":"\"JetBrains Mono\", \"IBM Plex Mono\", ui-monospace, monospace"},
 "groups":[
  {"name":"Sous-titres","family":"text","styles":[
   {"name":"amorce-916","fontSize":"54px","lineHeight":1.1,"fontWeight":400,"letterSpacing":"0em","sample":"Ton montage","usage":"Amorce du croquis en 9:16 : Arial 400, à gauche du mot clé. Une capitale puis des minuscules, os, halo sombre. 4 mots au plus."},
   {"name":"amorce-169","fontSize":"45px","lineHeight":1.1,"fontWeight":400,"letterSpacing":"0em","sample":"Ton montage","usage":"Amorce en 16:9."}]},
  {"name":"Mot de fin","family":"fin","styles":[
   {"name":"fin-916","fontSize":"54px","lineHeight":1.1,"fontWeight":400,"letterSpacing":"0em","sample":"par vidéo","usage":"Mot de fin du croquis en 9:16 : Inter 400, sous le mot clé, calé sur son bord droit. Minuscules, os, halo sombre. 3 mots au plus."},
   {"name":"fin-169","fontSize":"45px","lineHeight":1.1,"fontWeight":400,"letterSpacing":"0em","sample":"par vidéo","usage":"Mot de fin en 16:9."}]},
  {"name":"Mot clé","family":"accent","styles":[
   {"name":"motcle-916","fontSize":"180px","lineHeight":1,"fontWeight":400,"letterSpacing":"0em","sample":"1 Heure","usage":"Mot clé du croquis en 9:16 : Anton, braise (V1 : os puis noir sur braise au clic ; V4 : os puis braise une fois posé). Une capitale puis des minuscules. 1 ou 2 mots."},
   {"name":"motcle-169","fontSize":"150px","lineHeight":1,"fontWeight":400,"letterSpacing":"0em","sample":"1 Heure","usage":"Mot clé en 16:9."},
   {"name":"motcle-min","fontSize":"140px","lineHeight":1,"fontWeight":400,"letterSpacing":"0em","sample":"Transformation","usage":"Plancher du mot clé en 9:16 (117 px en 16:9). S’il ne tient pas à côté de l’amorce, l’amorce passe d’abord au-dessus ; s’il ne tient toujours pas, il descend jusqu’ici ; au-delà, on change de mot."},
   {"name":"titre-916","fontSize":"420px","lineHeight":0.95,"fontWeight":400,"letterSpacing":"0em","sample":"5","usage":"Titre d’accroche en 9:16, Anton braise : le plus gros qui tient, 420 px au plus."},
   {"name":"titre-169","fontSize":"350px","lineHeight":0.95,"fontWeight":400,"letterSpacing":"0em","sample":"5","usage":"Titre d’accroche en 16:9, 350 px au plus, à côté de la tête ou derrière toi."},
   {"name":"mot-geant","fontSize":"240px","lineHeight":1,"fontWeight":400,"letterSpacing":"0em","sample":"Contrôle","usage":"Mot géant seul (hors sous-titre), Anton braise, 9:16 (200 px en 16:9)."},
   {"name":"chiffre","fontSize":"240px","lineHeight":1,"fontWeight":400,"letterSpacing":"0em","sample":"+240 %","usage":"Chiffre d’un graphique ou d’une carte, Anton braise."}]},
  {"name":"Phrase","family":"text","styles":[
   {"name":"phrase","fontSize":"110px","lineHeight":1.05,"fontWeight":700,"letterSpacing":"0em","sample":"Le montage qui","usage":"Phrase de la scène texte plein écran (AnimTexte), Arial 700, 9:16 (92 px en 16:9). 6 mots au plus avec le mot mis en valeur (Anton 260 px)."}]},
  {"name":"Étiquettes","family":"mono","styles":[
   {"name":"label","fontSize":"22px","lineHeight":1.2,"fontWeight":600,"letterSpacing":"0.08em","sample":"ÉTAPE 01","usage":"Étiquette dans un objet ou une carte, 16:9. MAJUSCULES."},
   {"name":"label-916","fontSize":"28px","lineHeight":1.2,"fontWeight":600,"letterSpacing":"0.08em","sample":"VENTES","usage":"Étiquette en 9:16."}]}]},
"spacing":{"tokens":[
 T("bloc-916-bas","1560px","9:16 : y du bas du bloc de sous-titres, plan rapproché (360 px du bas). Plan moyen : 1540 px ; plan large : 1520 px ; gros plan : le bloc passe au-dessus de la tête, haut à 250 px."),
 T("bloc-916-bas-max","1560px","9:16 : y le plus bas autorisé pour le bas du bloc (au-delà, l’interface des Shorts)."),
 T("bloc-916-marge","80px","9:16 : marge gauche et droite du bloc (largeur utile 920 px)."),
 T("bloc-169-bas","900px","16:9 : ancien placement en bas au centre. Plus utilisé pour un texte posé sur toi : voir tete-ecart."),
 T("bloc-169-marge","160px","16:9 : marge gauche et droite d’un bloc derrière toi (largeur utile 1600 px)."),
 T("col-169-marge","100px","16:9 : marge entre le bord de l’image et un bloc posé à côté de ta tête."),
 T("tete-ecart","50px","16:9 : écart entre le bord de ta tête et un bloc posé à gauche ou à droite d’elle. Règle de Wanzt (8 novembre) : en 16:9, tout texte posé sur toi va à gauche ou à droite de la tête, ou derrière toi, jamais dessus."),
 T("zone-shorts","360px","9:16 : bas de l’image réservé à l’interface des Shorts (titre, chaîne, musique). Rien dedans."),
 T("zone-youtube","100px","16:9 : bas de l’image réservé à la barre de lecture YouTube. Rien dedans."),
 T("ecart-croquis","10px","Écart entre l’amorce et le mot clé dans le croquis."),
 T("ech-gros","0.8","Taille du croquis sur un gros plan (visage) : 80 %."),
 T("ech-rapproche","1","Taille du croquis sur un plan rapproché (poitrine) : 100 %, la référence."),
 T("ech-moyen","1.05","Taille du croquis sur un plan moyen (taille) : 105 % en 9:16, 100 % en 16:9."),
 T("ech-large","1.08","Taille du croquis sur un plan large (en pied) : 108 % en 9:16, 100 % en 16:9."),
 T("sous-menton","40px","Écart minimal entre le menton et le haut du bloc ou du titre. Rien ne couvre le visage."),
 T("ecart-ligne","20px","Écart entre l’amorce et le mot clé en variante En ligne."),
 T("montee-objet","48px","Montée d’entrée d’un objet placé derrière la personne."),
 T("poignee","18px","Côté d’une poignée carrée du cadre de sélection : os, bord braise 3 px."),
 T("case","60px","Côté d’une case de la grille des fonds (32 × 18 en 16:9, 18 × 32 en 9:16)."),
 T("bande-916","760px","9:16 : hauteur de la bande graphique de l’écran partagé (40 %)."),
 T("panneau-169","820px","16:9 : largeur du panneau graphique de l’écran partagé (≈ 43 %)."),
 T("incrust-marge","56px","16:9 : marge de l’A-roll rétracté dans le coin bas-droite."),
 T("incrust-taille","0.3","16:9 : échelle de l’A-roll rétracté (30 %).")]},
"radius":{"tokens":[T("radius-none","0px","Poignées de sélection, cadre de sélection."),T("radius-sm","3px","Étiquettes."),T("radius-md","6px","Objets et cartes derrière la personne. Le maximum.")]},
"shadow":{"note":"Deux ombres : le halo sombre sur tout texte posé sur la vidéo, et l’ombre claire sous les objets posés sur un fond clair. Jamais d’ombre colorée ni décalée.","tokens":[T("halo-sombre","0 0 36px rgba(10,10,10,0.8), 0 2px 6px rgba(10,10,10,0.6)","text-shadow de l’amorce, du mot clé et du titre-choc (choix O3 du 2026-11-06). Sur la vidéo seulement : pas sur un fond clair graphique."),T("ombre-claire","0 18px 40px rgba(18,18,18,0.12), 0 2px 6px rgba(18,18,18,0.08)","box-shadow des objets posés sur un fond clair (cartes, pastilles). Validée le 2026-11-06. Jamais sur fond noir.")]},
"stroke":{"tokens":[T("trait-selection","3px","Cadre de sélection, en os."),T("trait-objet","2px","Bordure des objets derrière la personne, en acier."),T("trait-zone","4px","Pointillé de la zone visage, repère de travail.")]},
"duration":{"tokens":[
 T("dur-mot","350ms","Entrée d’un mot de l’amorce ou du mot de fin (fondu + flou + 10 px de montée), à l’instant où il est dit."),
 T("dur-pas-mot","180ms","Écart entre deux mots de l’amorce dans le labo (V1, V2) ; dans la vidéo, chaque mot arrive à l’instant où il est dit."),
 T("dur-frappe","55ms","V3 machine à écrire : écart entre deux lettres."),
 T("dur-punch","420ms","V2 : le mot clé tombe trop grand (×1,7) puis se pose à sa taille."),
 T("dur-cadre","300ms","Tracé du cadre de sélection (V1, V4)."),
 T("v1-clic","1300ms","V1 : délai entre l’arrivée du mot clé et le clic (cadre à +450 ms, poignées à +750 ms, curseur à +850 ms)."),
 T("dur-agrandie","700ms","V4 : le texte sélectionné est tiré et agrandi de 40 % à 100 % jusqu’à sa place."),
 T("tenue","1000ms","Temps à l’écran après le dernier mot avant la sortie (le sous-titre part plus tôt si la phrase suivante commence)."),
 T("dur-lettre","240ms","Entrée d’une lettre du mot clé ou du titre ; entrée du cadre de sélection."),
 T("dur-char","30ms","Écart entre deux lettres du mot clé."),
 T("dur-sortie","300ms","Sortie de tout le bloc d’un coup : flou rapide (fondu + flou), tenue après le dernier mot."),
 T("dur-objet","400ms","Entrée d’un objet derrière la personne."),
 T("dur-ecart-objet","120ms","Écart entre deux objets qui entrent l’un après l’autre."),
 T("dur-bande-sortie","240ms","Sortie de la bande ou du panneau de l’écran partagé."),
 T("dur-lg","600ms","Mouvements longs : A-roll qui se rétracte et revient, sélection tirée depuis le coin.")]},
"easing":{"tokens":[T("ease-out","cubic-bezier(0.16, 1, 0.3, 1)","Toute entrée."),T("ease-in","cubic-bezier(0.7, 0, 0.84, 0)","Toute sortie."),T("ease-in-out","cubic-bezier(0.65, 0, 0.35, 1)","Mouvements qui vont d’un point à un autre : A-roll rétracté, sélection tirée.")]},
"blur":{"tokens":[T("flou-mot","12px","Flou de départ d’un mot de l’amorce ou du mot de fin."),T("flou-lettre","12px","Flou de départ d’une lettre du mot clé."),T("flou-titre","16px","Flou de départ d’une lettre du titre-choc."),T("flou-sortie","12px","Flou d’arrivée à la sortie du bloc.")]}}
w('tokens.json',json.dumps(tokens,ensure_ascii=False,indent=1))

# ---------------- bundle.css ----------------
css='''@import url("https://fonts.googleapis.com/css2?family=Anton&family=Arimo:wght@400;700&family=Inter:wght@400;500;700;800&family=JetBrains+Mono:wght@600&display=swap");
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
.ms-amorce{font-family:var(--font-text);font-weight:400;font-size:54px;line-height:1.1;letter-spacing:0;color:var(--os);text-shadow:var(--halo-sombre)}
.ms-bloc--169 .ms-amorce{font-size:45px}
.ms-fin{font-family:var(--font-fin);font-weight:400;font-size:54px;line-height:1.1;letter-spacing:0;color:var(--os);text-shadow:var(--halo-sombre);white-space:nowrap}
.ms-bloc--169 .ms-fin{font-size:45px}
.ms-motcle{font-family:var(--font-accent);font-weight:400;font-size:180px;line-height:1;letter-spacing:0;color:var(--os);text-shadow:var(--halo-sombre);white-space:nowrap}
.ms-bloc--169 .ms-motcle{font-size:150px}
.ms-motcle--braise{color:var(--braise)}
.ms-motcle--os{color:var(--os)}
.ms-empile .ms-motcle{margin-top:-6px}
.ms-escalier .ms-amorce:first-child{align-self:flex-start;margin-left:40px}
.ms-escalier .ms-amorce:last-child{align-self:flex-end;margin-right:40px;margin-top:6px}
.ms-mot{display:inline-block;animation:ms-entree-mot var(--dur-mot) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-lettre{display:inline-block;animation:ms-entree-lettre var(--dur-lettre) var(--ease-out) both;animation-delay:calc(var(--t,0ms) + var(--i,0) * var(--dur-char))}
.ms-espace{display:inline-block;width:0.5em}
.ms-titre{position:absolute;font-family:var(--font-accent);font-weight:400;line-height:0.95;letter-spacing:0;color:var(--os);text-shadow:var(--halo-sombre);white-space:nowrap}
.ms-titre--braise{color:var(--braise)}
.ms-titre .ms-lettre{animation-name:ms-entree-titre}
.ms-selection{position:absolute;border:var(--trait-selection) solid var(--os);border-radius:var(--radius-none);animation:ms-entree-cadre var(--dur-lettre) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-poignee{position:absolute;width:var(--poignee);height:var(--poignee);background:var(--braise)}
.ms-poignee--hg{left:-10px;top:-10px}.ms-poignee--hd{right:-10px;top:-10px}.ms-poignee--bg{left:-10px;bottom:-10px}.ms-poignee--bd{right:-10px;bottom:-10px}
.ms-objet{position:absolute;box-sizing:border-box;border-radius:var(--radius-md);background:var(--fonte);border:var(--trait-objet) solid var(--acier);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;animation:ms-entree-objet var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-objet-label{font-family:var(--font-mono);font-weight:600;font-size:28px;letter-spacing:0.08em;color:var(--brume)}
.ms-zone-visage{position:absolute;box-sizing:border-box;border:var(--trait-zone) dashed var(--cendre);border-radius:var(--radius-md)}
@keyframes ms-entree-mot{from{opacity:0;filter:blur(var(--flou-mot));transform:translateY(10px)}to{opacity:1;filter:blur(0);transform:none}}
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

exec(open('croquis_lib.py').read())
exec(open('planche_c.py').read())
exec(open('planche_suite.py').read())
exec(open('marque.py').read())
exec(open('guide.py').read())

exec(open('sous_titre.py').read())

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
h_v3=f'<div class="ms-bloc" style="left:1080px;right:100px;top:250px;bottom:auto;--sortie:3200ms"><div class="ms-amorce" style="font-size:45px">{hs}</div></div><div class="ms-titre" style="left:1080px;right:100px;top:330px;text-align:center;font-size:190px;--sortie:3200ms"><span style="--t:260ms;display:inline-block">{lettres("Claude")}</span></div><div class="ms-selection" style="left:1100px;right:120px;top:318px;height:200px;--t:{tch+120}ms"><span class="ms-poignee ms-poignee--hg"></span><span class="ms-poignee ms-poignee--hd"></span><span class="ms-poignee ms-poignee--bg"></span><span class="ms-poignee ms-poignee--bd"></span></div>'
th=fin_lettres("TUNNEL",200); ht,_=mots("le vrai secret :",th)
h_v2=f'<div class="ms-titre" style="left:0;right:0;top:200px;text-align:center;font-size:260px;--sortie:3200ms"><span style="--t:200ms;display:inline-block">{lettres("TUNNEL")}</span></div>'+SIL169+f'<div class="ms-bloc ms-bloc--169" style="--bas:760px;--sortie:3200ms"><div class="ms-amorce">{ht}</div></div>'
prev=f'''<!-- @dsCard group="Accroche" height=900 width=1500 subtitle="Rangée 1 : 9:16 (V1, V3, V2a, V2b, V2c) · rangée 2 : 16:9 (V1 à côté du visage, V3, V2a)" -->
<!doctype html>
<html lang="fr"><head><meta charset="utf-8">{PREV_CSS}</head>
<body><div class="rang">{ap('916',v1,'9:16 · V1 · Chiffre + amorce',zone=Z916)}{ap('916',t9,l9,zone=Z916)}{ap('916',d_titre+SIL+devant_t,'9:16 · V2a · Derrière : titre',plan=False,zone=ZS)}{ap('916',d_logo+SIL+devant_l,'9:16 · V2b · Derrière : logo',plan=False,zone=ZS)}{ap('916',d_objs+SIL+devant_o,'9:16 · V2c · Derrière : objets',plan=False,zone=ZS)}</div><div class="rang">{ap('169',h_v1,'16:9 · V1 · À côté du visage',zone=Z169)}{ap('169',t16,l16,zone=Z169)}{ap('169',h_v2,'16:9 · V2a · Derrière : titre',plan=False,zone=ZS169)}</div>{BOUCLE}</body></html>
'''
w('components/TitreChoc/preview.html',prev)
w('components/TitreChoc/README.md','''# TitreChoc

Le titre d’accroche : un mot ou un chiffre géant en **Anton braise** (`titre-916` 420 px, `titre-169` 350 px), avec une amorce en Arial 400 au-dessus, ou un élément placé derrière la personne, pour les 3 premières secondes ou l’ouverture d’une partie. Réglé dans le **Labo des textes** de l’atelier (8 novembre 2026).

**Ce que tu fournis :** le mot ou le chiffre, la ou les lignes d’amorce, la position du visage sur le plan, et pour V2 un détourage (matte) de la personne et l’élément à placer derrière (titre, logo, image ou 2 à 4 objets).

## Règle d’or
Rien ne couvre le visage, du front au menton : ni titre, ni cadre, ni sous-titre. Un élément peut passer **derrière** la tête (grâce au détourage), jamais devant. **En 16:9 (règle de Wanzt, 8 novembre)** : le titre va à gauche ou à droite de la tête, ou derrière toi ; jamais au centre sur toi.

## Animation et sons
Les mêmes que les 4 variantes du sous-titre (voir **SousTitreDuo**) : punch (V2, par défaut pour un chiffre), sélection (V1), machine à écrire (V3), ou sélection agrandie (V4 : le titre arrive petit, est sélectionné, puis tiré et agrandi jusqu’à sa place ; c’est la « sélection tirée » V3 ci-dessous). Mêmes sons, mêmes volumes.

## Variantes
| Variante | Où | Détail |
|---|---|---|
| V1 Chiffre + amorce | 9:16 : au-dessus de la tête ou sous le menton (`sous-menton`). 16:9 : à gauche ou à droite de la tête | `.ms-titre` (Anton), style `titre-916` (420 px max) / `titre-169` (350 px max), `braise` (`.ms-titre--braise`) ; amorce `.ms-amorce` collée à droite sur 1 ou 2 lignes |
| V2 Derrière la personne | derrière la tête et les épaules | un titre (`.ms-titre`), un logo ou une image, ou 2 à 4 objets (`.ms-objet` : fond `fonte`, trait `trait-objet` `acier`, arrondi `radius-md`). Le texte d’amorce reste devant. |
| V3 Sélection tirée (= V4 sélection agrandie du sous-titre) | arrivée au-dessus de la tête, jamais dessus (16:9 : à gauche ou à droite de la tête) | `.ms-tire` (avec `--dx` / `--dy` = coin de départ − place d’arrivée) qui contient le mot (`.ms-titre`, déjà complet) et son cadre `.ms-selection` (`trait-selection` `os`, sans arrondi, 4 poignées `.ms-poignee` `braise`) ; un curseur `.ms-curseur` (`--cx` / `--cy`) sur la poignée bas-droite. Le cadre compte comme l’élément braise de l’image. Validée le 2026-11-06. |

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
.nom{position:absolute;left:40px;bottom:64px;margin:0;font-family:var(--font-accent);font-weight:400;font-size:68px;line-height:1;letter-spacing:0;color:var(--os);max-width:440px}
.tag{position:absolute;left:40px;bottom:36px;margin:0;font-family:var(--font-text);font-weight:500;font-size:14px;color:var(--brume);max-width:440px}
</style></head>
<body><div class="c">
<svg aria-hidden="true" width="960" height="300" viewBox="0 0 960 300" style="position:absolute;left:0;top:0">
<!-- blocs : braise (300×300 qui déborde en haut), fonte 160×180, graphite 160×100, os 80×80 (radius-md 6px)
     disposition : une dalle braise haute avec satellites, à droite de x 480
     motif : grille de points, pas de 24 px
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
"lastChange":{"by":"Wanzt Koffi","at":now,"via":"Claude Code","note":"8 novembre 2026, depuis les deux labos de l’atelier : trio Arial / Anton / Inter (Doto retiré), le croquis du sous-titre en 4 variantes (sélection, punch, machine à écrire, sélection agrandie) avec leurs sons, taille et place selon le plan, règle 16:9 (texte à côté de la tête ou derrière toi), zones Shorts et YouTube, titres et chiffres en Anton, carré du logo en braise. Guides : règle d’or du son (jamais plus fort que la voix) et gains remesurés ; alternance des variantes."}}
w('design-system.json',json.dumps(idx,ensure_ascii=False,indent=1))
print('ok')
