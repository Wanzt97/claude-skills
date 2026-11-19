import json, sys, html, datetime
R=sys.argv[1]; P=sys.argv[2] if len(sys.argv)>2 else f'{R}/root/project'
F916='/_blob/fd576d89845f397ad5f03570548aced9'; F169='/_blob/ff226d0130ccf5606081be5b13d4519c'
if len(sys.argv)>4: F916, F169 = sys.argv[3], sys.argv[4]
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800;900&amp;family=Doto:wght@900&amp;family=Inter:wght@500;700;800&amp;family=JetBrains+Mono:wght@600&amp;display=swap">'
BG='#121212'; OS='#EFEFEF'; BRUME='#A3A3A3'; BRAISE='#FF7033'; GRAPH='#1A1A1A'; FONTE='#232323'; ACIER='#3A3A3A'; ABYSSE='#0A0A0A'
PAPIER='#F1EFEC'; ENCRE='#121212'; ENCRE2='#5C5A55'; BRAISE_P='#C2410C'
HALO='0 0 36px rgba(10,10,10,0.8), 0 2px 6px rgba(10,10,10,0.6)'
OMBRE_P='0 18px 40px rgba(18,18,18,0.12), 0 2px 6px rgba(18,18,18,0.08)'
EOUT='cubic-bezier(0.16, 1, 0.3, 1)'; EIN='cubic-bezier(0.7, 0, 0.84, 0)'
CYCLE=4000; EXIT=3600
class Anim:
    def __init__(s,p): s.p=p; s.css=[]; s.n=0
    def kf(s,start,dur,exit_at,exit_dur=140,blur_in=12,blur_out=8,extra_in='',extra_on='',exit_extra=''):
        s.n+=1; name=f'{s.p}{s.n}'; pc=lambda t: f'{100*t/CYCLE:.3f}%'
        s.css.append(f'@keyframes {name}{{0%{{opacity:0;filter:blur({blur_in}px){extra_in}}}{pc(start)}{{opacity:0;filter:blur({blur_in}px){extra_in};animation-timing-function:{EOUT}}}{pc(start+dur)}{{opacity:1;filter:blur(0px){extra_on}}}{pc(exit_at)}{{opacity:1;filter:blur(0px){extra_on};animation-timing-function:{EIN}}}{pc(exit_at+exit_dur)}{{opacity:0;filter:blur({blur_out}px){extra_on}{exit_extra}}}100%{{opacity:0}}}}')
        return f'animation: {name} {CYCLE}ms linear infinite'
    def style(s): return '\n'.join(s.css)
def mots(a,t,t0,ec=150,ex=EXIT):
    o=[]
    for w in t.split(' '): o.append(f'<span style="display: inline-block; {a.kf(t0,120,ex,blur_in=6)}">{html.escape(w)}</span>'); t0+=ec
    return ' '.join(o),t0
def lettres(a,t,t0,ex=EXIT):
    return ''.join('<span style="display: inline-block; width: 0.5em"></span>' if c==' ' else f'<span style="display: inline-block; {a.kf(t0+i*30,240,ex)}">{html.escape(c)}</span>' for i,c in enumerate(t)), t0+(len(t)-1)*30+240
AM="font-family: Inter, sans-serif; font-weight: 800; font-size: 56px; line-height: 1.05; letter-spacing: -0.01em"
MC="font-family: Doto, monospace; font-weight: 900; font-size: 240px; line-height: 0.9; letter-spacing: -0.04em"
def duo(a,am,mc,t0,color=OS,mccolor=None,halo=True,bas=None,top=None,left=80,right=80,size=240):
    m,t=mots(a,am,t0); k,_=lettres(a,mc,t+120)
    sh=f'text-shadow: {HALO};' if halo else ''
    pos=f'bottom: {1920-bas}px;' if bas else f'top: {top}px;'
    return f'<div style="position: absolute; left: {left}px; right: {right}px; {pos} display: flex; flex-direction: column; align-items: center; text-align: center"><div style="{AM}; color: {color}; {sh}">{m}</div><div style="{MC}; font-size: {size}px; color: {mccolor or color}; {sh} margin-top: -6px; white-space: nowrap">{k}</div></div>'
def apercu(inner,leg,W=1080,H=1920,sc=0.4):
    return f'<figure style="margin: 0; display: flex; flex-direction: column; gap: 12px"><div style="position: relative; width: {int(W*sc)}px; height: {int(H*sc)}px; overflow: hidden; border-radius: 6px; border: 2px solid {ACIER}; background: {GRAPH}"><div style="position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; transform: scale({sc}); transform-origin: 0 0">{inner}</div></div><figcaption style="font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 13px; letter-spacing: 0.08em; text-transform: uppercase; color: {BRUME}">{leg}</figcaption></figure>'
def plan(src=F916,top=0,h=1920,posy='50%'):
    return f'<img src="{src}" alt="Plan face caméra" style="position: absolute; left: 0; top: {top}px; width: 1080px; height: {h}px; object-fit: cover; object-position: 50% {posy}">'
def page(f,title,w,h,body,css):
    open(f'{P}/{f}','w').write(f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
body{{margin:0}}
{css}
</style>
</helmet>
<div style="width: {w}px; height: {h}px; box-sizing: border-box; padding: 48px; background: {BG}; color: {OS}; font-family: Inter, sans-serif; display: flex; flex-direction: column; gap: 32px">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
''')
def header(label,titre,texte):
    return f'''<div style="display: flex; flex-direction: column; gap: 14px"><div style="display: flex; align-items: center; gap: 12px"><span style="display: inline-block; width: 14px; height: 14px; background: {BRAISE}"></span><span style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 15px; letter-spacing: 0.08em; text-transform: uppercase; color: {BRUME}">{label}</span></div><h1 style="margin: 0; font-family: 'Big Shoulders Display', sans-serif; font-weight: 900; font-size: 68px; line-height: 0.95; letter-spacing: 0.01em; text-transform: uppercase">{titre}</h1><p style="margin: 0; max-width: 1280px; font-size: 20px; line-height: 1.45; font-weight: 500; color: {BRUME}">{texte}</p></div>'''
def tableau(lignes,ent):
    th=''.join(f'<th style="text-align: left; padding: 12px 16px; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 13px; letter-spacing: 0.08em; text-transform: uppercase; color: {BRUME}; border-bottom: 2px solid {ACIER}">{e}</th>' for e in ent)
    tr=''.join('<tr>'+''.join(f'<td style="padding: 12px 16px; font-size: 17px; line-height: 1.4; font-weight: 500; vertical-align: top; border-bottom: 2px solid {GRAPH}">{c}</td>' for c in l)+'</tr>' for l in lignes)
    return f'<table style="border-collapse: collapse; width: 100%"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'
def objet_kf(a,t,ex=EXIT,dy=48,scale=None):
    tin=f';transform:translateY({dy}px)' if scale is None else f';transform:scale({scale})'
    ton=';transform:translateY(0px)' if scale is None else ';transform:scale(1)'
    return a.kf(t,400,ex,blur_in=0,extra_in=tin,extra_on=ton)
def carte_logiciel(a,x,y,w,h,t,titre,clair=False):
    fond=PAPIER if clair else FONTE; bord='rgba(18,18,18,0.10)' if clair else ACIER; ink=ENCRE if clair else OS; sub=ENCRE2 if clair else BRUME
    sh=f'box-shadow: {OMBRE_P};' if clair else ''
    lignes=''.join(f'<div style="height: 18px; width: {wd}%; border-radius: 3px; background: {"rgba(18,18,18,0.12)" if clair else "#3a3a3a"}"></div>' for wd in (86,64,92,48))
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; box-sizing: border-box; border-radius: 6px; background: {fond}; border: 2px solid {bord}; {sh} overflow: hidden; {objet_kf(a,t)}"><div style="height: 56px; display: flex; align-items: center; gap: 10px; padding: 0 20px; border-bottom: 2px solid {bord}"><span style="width: 14px; height: 14px; border: 2px solid {sub}"></span><span style="width: 14px; height: 14px; border: 2px solid {sub}"></span><span style="width: 14px; height: 14px; background: {BRAISE}"></span><span style="margin-left: 12px; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 24px; letter-spacing: 0.08em; color: {sub}">{titre}</span></div><div style="padding: 28px 24px; display: flex; flex-direction: column; gap: 18px">{lignes}</div></div>'
boards={}

# ---------- C2 : petite animation ----------
a=Anim('c2_')
# V1 points d'étape sous le sous-titre
def points(a,t,active=1,top=1500):
    o=[]
    for i in range(3):
        on=(i+1)==active
        st=f'background: {BRAISE}; color: {ABYSSE}; border-color: {BRAISE};' if on else f'background: transparent; color: {OS}; border-color: {OS};'
        o.append(f'<span style="width: 64px; height: 64px; box-sizing: border-box; border: 3px solid; {st} display: flex; align-items: center; justify-content: center; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 28px; {a.kf(t+i*120,240,EXIT,blur_in=0,extra_in=";transform:scale(0.6)",extra_on=";transform:scale(1)")}">{i+1}</span>')
        if i<2: o.append(f'<span style="width: 72px; height: 3px; background: {OS}; opacity: 0.6; {a.kf(t+i*120+60,240,EXIT,blur_in=0)}"></span>')
    return f'<div style="position: absolute; left: 0; right: 0; top: {top}px; display: flex; align-items: center; justify-content: center; filter: drop-shadow(0 0 18px rgba(10,10,10,0.7))">{"".join(o)}</div>'
v1=apercu(plan()+duo(a,'ces trois','erreurs',0,bas=1450,size=200)+points(a,900,1,1490),'C2 · V1 · Points d’étape sous le sous-titre')
v2=apercu(plan()+carte_logiciel(a,90,260,560,380,300,'SCRIPT.TXT',clair=False)+duo(a,'mon script','s’écrit',700,bas=1450,size=220),'C2 · V2 · Fenêtre logiciel (sombre)')
v3=apercu(plan()+carte_logiciel(a,430,240,560,380,300,'L’IDÉE',clair=True)+duo(a,'une seule','idée',700,bas=1450),'C2 · V3 · Carte idée (papier)')
spec=tableau([
 ['Principe','Toi en plein cadre, toujours le sujet. UN seul petit élément d’interface, près de toi, jamais sur le visage.'],
 ['V1 Points d’étape','3 cases carrées 64 px (trait 3 px os), reliées par un trait ; l’étape en cours en braise pleine, chiffre abysse. Sous le bloc de sous-titres. Entrée : chaque case s’ouvre (échelle 0,6 → 1, 240 ms), 120 ms d’écart.'],
 ['V2 Fenêtre logiciel','Pour montrer un logiciel : carte sombre (fonte, trait acier 2 px, arrondi 6), barre de titre mono avec 2 carrés creux + 1 carré braise. 560 × 380 en 9:16, au-dessus ou à côté de la tête.'],
 ['V3 Carte idée','Pour expliquer une idée : même carte en papier clair avec l’ombre douce du papier.'],
 ['Mouvement','Monte de 48 px + fondu, 400 ms, ease-out ; sort avec le bloc (140 ms). Aucun effet sur le décor ni sur le visage.'],
],['Élément','Règle'])
body=header('Planche C · composant ScèneC2','Sous-titres + petite animation',"Ce que ton tri a gardé : un seul petit élément qui ressemble à un vrai logiciel, près de toi. Fond sombre pour un logiciel, papier pour une idée.")+f'<div style="display: flex; gap: 40px">{v1}{v2}{v3}</div>'+spec
page('K-C2.dc.html','ScèneC2',1480,1660,body,a.style()); boards['K-C2.dc.html']=(1480,1660,'Composant C2 — Petite animation')

# ---------- C3 : écran partagé ----------
a=Anim('c3_')
BANDE=760
def bande(a,clair,inner):
    fond=PAPIER if clair else BG
    return f'<div style="position: absolute; left: 0; top: 0; width: 1080px; height: {BANDE}px; background: {fond}; overflow: hidden; {a.kf(0,400,EXIT,blur_in=0,extra_in=";transform:translateY(-100%)",extra_on=";transform:translateY(0%)",exit_dur=240)}">{inner}</div>'
def swatches(a):
    c=[(ENCRE,'ENCRE'),(OS,'OS'),(BRAISE,'BRAISE')]
    o=''.join(f'<div style="display: flex; flex-direction: column; align-items: center; gap: 16px; {objet_kf(a,240+i*120,scale=0.92)}"><div style="width: 200px; height: 200px; border-radius: 6px; background: {col}; box-shadow: {OMBRE_P}; border: 2px solid rgba(18,18,18,0.08)"></div><span style="font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 22px; letter-spacing: 0.08em; color: {ENCRE2}">{lab}</span></div>' for i,(col,lab) in enumerate(c))
    return f'<div style="position: absolute; left: 0; right: 0; top: 230px; display: flex; justify-content: center; gap: 56px">{o}</div>'
def phrase_papier(a,am,mc,t0):
    m,t=mots(a,am,t0); k,_=lettres(a,mc,t+120)
    return f'<div style="position: absolute; left: 80px; right: 80px; top: 80px; display: flex; align-items: baseline; justify-content: center; gap: 18px"><span style="{AM}; font-size: 48px; color: {ENCRE}">{m}</span><span style="{MC}; font-size: 120px; color: {BRAISE_P}">{k}</span></div>'
term_lines=['> /montage lance','✓ rushs triés · 12','✓ script calé','› export en cours']
def terminal(a):
    l=''.join(f'<div style="font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 30px; color: {BRAISE if i==3 else OS}; {a.kf(300+i*200,240,EXIT,blur_in=0)}">{html.escape(x)}</div>' for i,x in enumerate(term_lines))
    return f'<div style="position: absolute; left: 140px; top: 160px; width: 800px; height: 440px; box-sizing: border-box; border-radius: 6px; background: {FONTE}; border: 2px solid {ACIER}; padding: 32px; display: flex; flex-direction: column; gap: 22px; {objet_kf(a,200,scale=0.92)}">{l}</div>'
pied=plan(top=BANDE,h=1920-BANDE,posy='50%')+f'<div style="position: absolute; left: 0; top: {BANDE-1}px; width: 1080px; height: 2px; background: rgba(10,10,10,0.6)"></div>'
v1=apercu(pied+bande(a,True,phrase_papier(a,'trois','couleurs',500)+swatches(a))+duo(a,'pas plus de','trois',900,top=BANDE+24,size=200),'C3 · V1 · Bande papier (idée)')
v2=apercu(pied+bande(a,False,terminal(a))+duo(a,'il monte','seul',900,top=BANDE+24,size=200),'C3 · V2 · Bande sombre (logiciel)')
# 16:9 côte à côte
a169=a
pan=f'<img src="{F169}" alt="Plan face caméra" style="position: absolute; left: 820px; top: 0; width: 1100px; height: 1080px; object-fit: cover; object-position: 55% 50%">'
panneau=f'<div style="position: absolute; left: 0; top: 0; width: 820px; height: 1080px; background: {PAPIER}; {a.kf(0,400,EXIT,blur_in=0,extra_in=";transform:translateX(-100%)",extra_on=";transform:translateX(0%)",exit_dur=240)}"><div style="position: absolute; left: 0; right: 0; top: 330px; display: flex; justify-content: center; gap: 40px">'+''.join(f'<div style="width: 170px; height: 170px; border-radius: 6px; background: {c}; box-shadow: {OMBRE_P}; {objet_kf(a,240+i*120,scale=0.92)}"></div>' for i,c in enumerate([ENCRE,OS,BRAISE]))+'</div></div>'
sub169=f'<div style="position: absolute; left: 860px; right: 40px; bottom: 140px; text-align: center"><div style="{AM}; font-size: 44px; color: {OS}; text-shadow: {HALO}">{mots(a,"pas plus de",900)[0]}</div></div>'
v3=apercu(pan+panneau+sub169,'C3 · 16:9 · V3 · Panneau papier à gauche',W=1920,H=1080,sc=0.25)
# V4 : A-roll qui se rétracte dans un coin (incrustation)
EIO='cubic-bezier(0.65, 0, 0.35, 1)'
pc=lambda t: f'{100*t/CYCLE:.3f}%'
S0,S1,G0,G1=400,1000,3200,3800   # rétraction 600 ms (dur-lg), retour 600 ms
PIP=0.3; M=56
a.css.append(f'@keyframes c3pip{{0%{{transform:translate(0px,0px) scale(1);border-radius:0px}}{pc(S0)}{{transform:translate(0px,0px) scale(1);border-radius:0px;animation-timing-function:{EIO}}}{pc(S1)}{{transform:translate(-{M}px,-{M}px) scale({PIP});border-radius:20px}}{pc(G0)}{{transform:translate(-{M}px,-{M}px) scale({PIP});border-radius:20px;animation-timing-function:{EIO}}}{pc(G1)}{{transform:translate(0px,0px) scale(1);border-radius:0px}}100%{{transform:translate(0px,0px) scale(1);border-radius:0px}}}}')
a.css.append(f'@keyframes c3pipb{{0%{{opacity:0}}{pc(S1-120)}{{opacity:0}}{pc(S1)}{{opacity:1}}{pc(G0)}{{opacity:1}}{pc(G0+120)}{{opacity:0}}100%{{opacity:0}}}}')
fond_pip=f'<div style="position: absolute; inset: 0; background: {BG}"></div>'+terminal(a).replace('left: 140px; top: 160px; width: 800px; height: 440px','left: 300px; top: 210px; width: 900px; height: 480px').replace(f'animation: c3_','animation: c3_')
ex_t=lambda t: t  # objets du fond : après la rétraction
pip=f'<div style="position: absolute; inset: 0; transform-origin: 100% 100%; overflow: hidden; animation: c3pip {CYCLE}ms linear infinite"><img src="{F169}" alt="Plan face caméra" style="width: 100%; height: 100%; object-fit: cover"><div style="position: absolute; inset: 0; border: 7px solid {ACIER}; border-radius: inherit; animation: c3pipb {CYCLE}ms linear infinite"></div></div>'
mp,_=mots(a,'et pendant ce temps',S1+200)
sub_pip=f'<div style="position: absolute; left: 300px; width: 900px; top: 780px; text-align: center; {AM}; font-size: 44px; color: {OS}; text-shadow: {HALO}">{mp}</div>'
v4=apercu(fond_pip+sub_pip+pip,'C3 · 16:9 · V4 · A-roll rétracté dans un coin',W=1920,H=1080,sc=0.25)
spec=tableau([
 ['9:16','Bande du haut : 760 px (40 %), papier #F1EFEC pour une idée, noir #121212 pour un logiciel. Toi en bas, plan recadré pour que ta tête reste dans la partie basse. Coupe nette à la jointure.'],
 ['16:9','Panneau à gauche : 820 px (≈ 43 %), même règle papier / noir. Toi à droite.'],
 ['Contenu de la bande','UN seul objet ou groupe centré (palette, carte, icône, terminal), une phrase courte au-dessus : amorce en encre #121212, mot clé en Doto. Sur papier, le mot clé est en braise foncée #C2410C (la braise #FF7033 n’a que 2,4:1 sur le papier, trop peu pour du texte).'],
 ['16:9 · V4 Incrustation','Ton plan (A-roll) se rétracte dans un coin (bas-droite, 30 % de la taille, marge 56 px, coins arrondis, cadre acier) et le graphique prend tout l’écran derrière. Rétraction et retour : 600 ms, ease-in-out, sans coupe. Pendant l’incrustation, tes sous-titres passent dans la zone du graphique. Jamais de texte sous l’incrustation.'],
 ['Sous-titres','Juste sous la jointure, entre la jointure et le haut de ta tête (9:16) ; en bas de ton côté (16:9). Halo sombre.'],
 ['Mouvement','La bande glisse depuis le haut (le panneau depuis la gauche), 400 ms, ease-out ; l’objet arrive 240 ms après (échelle 0,92 → 1 + fondu, 400 ms), les éléments d’un groupe à 120 ms d’écart. Sortie : la bande repart, 240 ms, ease-in.'],
 ['Ombre','Sur papier seulement : ombre douce sous les cartes (0 18px 40px noir 12 % + 0 2px 6px noir 8 %). À valider : c’est une nouvelle ombre dans le système.'],
],['Élément','Règle'])
body=header('Planche C · composant ScèneC3','Écran partagé',"Ton favori : la bande claire en haut avec un seul objet, toi en bas. Papier pour une idée, noir pour un logiciel.")+f'<div style="display: flex; flex-wrap: wrap; gap: 40px; align-items: flex-start">{v1}{v2}{v3}{v4}</div>'+spec
page('K-C3.dc.html','ScèneC3',1480,2160,body,a.style()); boards['K-C3.dc.html']=(1480,2160,'Composant C3 — Écran partagé')

# ---------- C4 : plein écran ----------
a=Anim('c4_')
def carte_video(a,x,y,w,h,t):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; border-radius: 6px; overflow: hidden; box-shadow: {OMBRE_P}; border: 2px solid rgba(18,18,18,0.08); {objet_kf(a,t,scale=0.92)}"><img src="{F916}" alt="" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 45%"></div>'
p1=f'<div style="position: absolute; inset: 0; background: {PAPIER}"></div>'+phrase_papier(a,'un seul objet,','beaucoup',300).replace('top: 80px','top: 330px')+carte_video(a,300,700,480,760,200)+f'<div style="position: absolute; left: 0; right: 0; top: 1540px; text-align: center; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 26px; letter-spacing: 0.08em; color: {ENCRE2}; {a.kf(900,240,EXIT,blur_in=0)}">DE VIDE AUTOUR</div>'
v1=apercu(p1,'C4 · V1 · Papier : une idée, un objet')
p2=f'<div style="position: absolute; inset: 0; background: {BG}"></div>'+terminal(a).replace('left: 140px; top: 160px; width: 800px; height: 440px','left: 100px; top: 620px; width: 880px; height: 520px')+duo(a,'ça tourne','seul',1200,top=1260,size=220)
v2=apercu(p2,'C4 · V2 · Noir : un logiciel, un terminal')
p3=f'<div style="position: absolute; inset: 0; background: {PAPIER}"></div>'+f'<div style="position: absolute; left: 0; right: 0; top: 640px; text-align: center; {MC}; font-size: 300px; color: {ENCRE}">{lettres(a,"200 €",200)[0]}</div>'+f'<div style="position: absolute; left: 0; right: 0; top: 960px; text-align: center; {AM}; font-size: 48px; color: {ENCRE2}">{mots(a,"par mois, pour un outil",600)[0]}</div>'
v3=apercu(p3,'C4 · V3 · Papier : un chiffre')
spec=tableau([
 ['Fond','Papier #F1EFEC pour expliquer une idée ; noir #121212 pour montrer un logiciel, un terminal, une interface. Un seul fond par plan.'],
 ['Composition','UN objet au centre (carte, icône, chiffre, terminal), beaucoup de vide autour. Une phrase courte au-dessus ou en dessous : amorce + mot clé (planche A). Une étiquette mono au plus.'],
 ['Couleurs sur papier','Texte en encre #121212, secondaire #5C5A55, mot clé en encre ou braise foncée #C2410C. La braise #FF7033 seulement en aplat (case, pastille, poignée), jamais en texte.'],
 ['Couleurs sur noir','Comme la planche A : os #EFEFEF, braise #FF7033 pour l’unique accent.'],
 ['Mouvement','Coupe franche vers le fond. L’objet arrive 200 ms après (échelle 0,92 → 1 + fondu, 400 ms, ease-out) ; la phrase suit le rythme de la voix (planche A). Sortie : coupe franche ou fondu 140 ms.'],
 ['À éviter','Affiche chargée, capture d’écran entière, grille d’avatars, gros titre plaqué sur une capture, plusieurs objets qui se battent.'],
],['Élément','Règle'])
body=header('Planche C · composant ScèneC4','Plein écran',"On ne te voit plus : un seul objet au centre, beaucoup de vide. Papier pour une idée, noir pour un logiciel.")+f'<div style="display: flex; gap: 40px">{v1}{v2}{v3}</div>'+spec
page('K-C4.dc.html','ScèneC4',1480,1720,body,a.style()); boards['K-C4.dc.html']=(1480,1720,'Composant C4 — Plein écran')

json.dump(boards,open(f'{R}/boards-composants.json','w'),ensure_ascii=False)
print('ok',boards)
