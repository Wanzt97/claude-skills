import sys, json, html
src=open(__file__.replace('compB.py','compC2.py')).read().split('boards={}')[0]
exec(src)
boards={}
a=Anim('b_')
pc=lambda v: f'{100*v/CYCLE:.3f}%'
EIO='cubic-bezier(0.65, 0, 0.35, 1)'
T_TITRE=300; T_SORT=1600; T_SOUS=1700
def plan_punch(src,W,H,origin):
    # plan serré dès la 1re image (×1,12), petit coup de zoom au moment du geste (×1,16), retour
    n=a.n+1; a.n=n; nm=f'b_p{n}'
    a.css.append(f'@keyframes {nm}{{0%{{transform:scale(1.12)}}{pc(200)}{{transform:scale(1.12);animation-timing-function:{EOUT}}}{pc(320)}{{transform:scale(1.16)}}{pc(560)}{{transform:scale(1.12)}}100%{{transform:scale(1.12)}}}}')
    return f'<div style="position: absolute; inset: 0; overflow: hidden"><img src="{src}" alt="Ton plan face caméra" style="width: {W}px; height: {H}px; object-fit: cover; display: block; transform-origin: {origin}; animation: {nm} {CYCLE}ms linear infinite"></div>'
def geste(x,y):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; padding: 10px 18px; border-radius: 3px; background: rgba(10,10,10,0.75); border: 2px dashed {BRUME}; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 26px; letter-spacing: 0.08em; color: {BRUME}; {a.kf(150,120,700,blur_in=0)}">ICI : TA MAIN VERS L’OBJECTIF</div>'
def titre_sel(txt,left,top,w,h,fs):
    k,tk=lettres(a,txt,T_TITRE,ex=T_SORT)
    hd=''.join(f'<span style="position: absolute; {p}; width: 16px; height: 16px; background: {BRAISE}"></span>' for p in ('left: -10px; top: -10px','right: -10px; top: -10px','left: -10px; bottom: -10px','right: -10px; bottom: -10px'))
    cadre=f'<div style="position: absolute; left: {left}px; top: {top}px; width: {w}px; height: {h}px; box-sizing: border-box; border: 3px solid {OS}; {a.kf(tk+120,240,T_SORT,blur_in=0,extra_in=";transform:scale(1.03)",extra_on=";transform:scale(1)")}">{hd}</div>'
    return f'<div style="position: absolute; left: {left}px; top: {top}px; width: {w}px; height: {h}px; display: flex; align-items: center; justify-content: center; {MC}; font-size: {fs}px; color: {OS}; text-shadow: {HALO}">{k}</div>'+cadre
def chiffre_amorce(ch,l1,l2,left,top,fs=420,am=56):
    k,tk=lettres(a,ch,T_TITRE,ex=T_SORT)
    m1,t=mots(a,l1,tk,ex=T_SORT); m2,_=mots(a,l2,t,ex=T_SORT)
    return f'<div style="position: absolute; left: {left}px; top: {top}px; display: flex; align-items: center; gap: 28px; text-shadow: {HALO}"><span style="{MC}; font-size: {fs}px; line-height: 0.8; color: {BRAISE}">{k}</span><span style="display: flex; flex-direction: column; {AM}; font-size: {am}px; color: {OS}"><span>{m1}</span><span>{m2}</span></span></div>'
# 9:16 · V1 : titre en sélection au-dessus de la tête
v1=apercu(plan_punch(F916,1080,1920,'50% 45%')+geste(240,1180)+titre_sel('3 erreurs',110,300,860,250,190)+duo(a,'qui tuent ton','montage',T_SOUS,bas=1450,size=200),'B · 9:16 · V1 · Titre en sélection au-dessus de la tête')
# 9:16 · V2 : chiffre + amorce sous le menton
v2=apercu(plan_punch(F916,1080,1920,'50% 45%')+geste(240,560)+chiffre_amorce('3','erreurs qui','tuent ton montage',90,1190,360,52)+duo(a,'et la première','coûte',T_SOUS,bas=1450,size=200),'B · 9:16 · V2 · Chiffre + amorce sous le menton')
def duo169(am,mc,t0):
    m,t=mots(a,am,t0); k,_=lettres(a,mc,t+120)
    return f'<div style="position: absolute; left: 160px; right: 160px; bottom: 120px; display: flex; flex-direction: column; align-items: center; text-align: center; text-shadow: {HALO}"><div style="{AM}; font-size: 44px; color: {OS}">{m}</div><div style="{MC}; font-size: 200px; color: {OS}; margin-top: -6px">{k}</div></div>'
# 16:9 · V3 : titre à côté du visage
w3=apercu(plan_punch(F169,1920,1080,'45% 45%')+geste(1180,150)+chiffre_amorce('3','erreurs qui','tuent ton montage',1120,330,300,44)+duo169('qui tuent ton','montage',T_SOUS),'B · 16:9 · V3 · Titre à côté du visage',W=1920,H=1080,sc=0.22)

# ---------- Ajouts : derrière toi, zoom out / zoom in, texte qui s'écrit à côté ----------
D916='/_blob/ae657ad6d99d57dc27cfcc3eefbca4dc'; D169='/_blob/a7f225e0fd5957222c63ba2401980e69'
def zoom(depart,arrivee,t=0,dur=600):
    n=a.n+1; a.n=n; nm=f'b_z{n}'
    a.css.append(f'@keyframes {nm}{{0%{{transform:scale({depart})}}{pc(t)}{{transform:scale({depart});animation-timing-function:{EIO}}}{pc(t+dur)}{{transform:scale({arrivee})}}100%{{transform:scale({arrivee})}}}}')
    return f'animation: {nm} {CYCLE}ms linear infinite'
def calque(src,W,H,origin,anim,alt):
    return f'<div style="position: absolute; inset: 0; overflow: hidden; pointer-events: none"><img src="{src}" alt="{alt}" style="width: {W}px; height: {H}px; object-fit: cover; display: block; transform-origin: {origin}; {anim}"></div>'
def monte(inner,left,top,t=300):
    return f'<div style="position: absolute; left: {left}px; top: {top}px; {a.kf(t,600,T_SORT,blur_in=0,extra_in=";transform:translateY(700px)",extra_on=";transform:translateY(0px)")}">{inner}</div>'
def derriere(fmt,depart,arrivee,element,sous):
    W,H,P,D,o=(1080,1920,F916,D916,'440px 925px') if fmt=='916' else (1920,1080,F169,D169,'857px 520px')
    an=zoom(depart,arrivee)
    return calque(P,W,H,o,an,'Ton plan face caméra')+element+calque(D,W,H,o,an,'Toi détouré, devant l’élément')+sous
mot_derriere=lambda fs: f'<span style="{MC}; font-size: {fs}px; line-height: 0.85; color: {OS}; white-space: nowrap">MONTAGE</span>'
logo_rond=lambda d: f'<div style="width: {d}px; height: {d}px; border-radius: 50%; background: {BRAISE}; display: flex; align-items: center; justify-content: center; box-shadow: 0 30px 60px rgba(0,0,0,0.45)"><svg aria-hidden="true" width="{int(d*0.5)}" height="{int(d*0.5)}" viewBox="0 0 24 24"><path d="M12 2v20M2 12h20M4.9 4.9l14.2 14.2M19.1 4.9L4.9 19.1" stroke="#0A0A0A" stroke-width="2.4" stroke-linecap="round"></path></svg></div>'
v3=apercu(derriere('916',1.35,1.0,monte(mot_derriere(260),30,640),duo(a,'monte tes vidéos','plus vite',T_SOUS,bas=1450,size=200)),'B · 9:16 · V3 · Plan serré → zoom out, texte qui sort derrière toi')
v4=apercu(derriere('916',1.0,1.3,monte(logo_rond(560),260,330),duo(a,'avec un seul','outil',T_SOUS,bas=1450,size=200)),'B · 9:16 · V4 · Plan large → zoom in, image qui sort derrière toi')
w5=apercu(derriere('169',1.35,1.0,monte(mot_derriere(340),290,300),duo169('monte tes vidéos','vite',T_SOUS)),'B · 16:9 · V5 · Serré → zoom out, texte derrière toi',W=1920,H=1080,sc=0.22)
w6=apercu(derriere('169',1.0,1.3,monte(logo_rond(520),600,120),duo169('avec un seul','outil',T_SOUS)),'B · 16:9 · V6 · Large → zoom in, logo derrière toi',W=1920,H=1080,sc=0.22)
def ecrit(txt,t0,ecart=45):
    o=''.join(f'<span style="{a.kf(t0+i*ecart,30,T_SORT,blur_in=0)}">{html.escape(c) if c!=" " else "&nbsp;"}</span>' for i,c in enumerate(txt))
    return o,t0+len(txt)*ecart
e1,t=ecrit('le montage le plus',400); e2,t2=ecrit('rapide',t+80)
curseur=f'<span style="display: inline-block; width: 18px; height: 120px; margin-left: 10px; background: {BRAISE}; vertical-align: -10px; {a.kf(t2,60,T_SORT,blur_in=0)}"></span>'
w7=apercu(plan_punch(F169,1920,1080,'45% 45%')+f'<div style="position: absolute; left: 1120px; top: 300px; width: 760px; text-shadow: {HALO}"><div style="{AM}; font-size: 60px; color: {OS}">{e1}</div><div style="{MC}; font-size: 170px; color: {OS}; margin-top: 8px; white-space: nowrap">{e2}{curseur}</div></div>','B · 16:9 · V7 · Texte qui s’écrit à côté de toi (droite ou gauche)',W=1920,H=1080,sc=0.22)

# ---------- Plan large qui se resserre sur un objet du décor, avec un texte ----------
def vers_objet(src,W,H,ox,oy,s_fin,tx,ty,t=300,dur=1200):
    n=a.n+1; a.n=n; nm=f'b_o{n}'
    fin=f'translate({tx}px,{ty}px) scale({s_fin})'
    a.css.append(f'@keyframes {nm}{{0%{{transform:translate(0px,0px) scale(1)}}{pc(t)}{{transform:translate(0px,0px) scale(1);animation-timing-function:{EIO}}}{pc(t+dur)}{{transform:{fin}}}{pc(EXIT)}{{transform:{fin}}}100%{{transform:{fin}}}}}')
    return f'<div style="position: absolute; inset: 0; overflow: hidden"><img src="{src}" alt="Ton plan, qui se resserre sur un objet" style="width: {W}px; height: {H}px; object-fit: cover; display: block; transform-origin: {ox}px {oy}px; animation: {nm} {CYCLE}ms linear infinite"></div>'
v5=apercu(vers_objet(F916,1080,1920,905,555,2.6,-280,205)+duo(a,'tout est parti de','ce livre',1500,bas=1450,size=200),'B · 9:16 · V5 · Plan large qui se resserre sur un objet, avec un texte')
def texte_cote(x,t0,am,mc,fs=180):
    m,t=mots(a,am,t0); k,_=lettres(a,mc,t+120)
    return f'<div style="position: absolute; left: {x}px; top: 380px; display: flex; flex-direction: column; align-items: flex-start; text-shadow: {HALO}"><div style="{AM}; font-size: 56px; color: {OS}">{m}</div><div style="{MC}; font-size: {fs}px; color: {OS}; margin-top: 4px; white-space: nowrap">{k}</div></div>'
w8=apercu(vers_objet(F169,1920,1080,1125,310,3.0,175,230)+texte_cote(110,1500,'tout est parti de','ce livre'),'B · 16:9 · V8 · Plan large qui se resserre sur un objet, avec un texte',W=1920,H=1080,sc=0.4)
# frise des 3 premières secondes
marques=[(0,'0 s','Plan serré dès la 1re image'),(200,'0,2 s','Ton geste vers l’objectif'),(300,'0,3 s','Le titre arrive pendant le geste'),(1600,'1,6 s','Le titre sort'),(1700,'1,7 s','1er sous-titre'),(3000,'3 s','Fin de l’accroche')]
fr=''.join(f'<div style="flex: 1; display: flex; flex-direction: column; gap: 8px; padding-top: 14px; border-top: 3px solid {BRAISE if t in (200,300) else ACIER}"><span style="font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 16px; letter-spacing: 0.08em; color: {OS}">{lab}</span><span style="font-size: 15px; line-height: 1.35; color: {BRUME}">{txt}</span></div>' for t,lab,txt in marques)
frise=f'<div style="display: flex; gap: 16px; width: 100%">{fr}</div>'
spec=tableau([
 ['Principe','Les 3 premières secondes : tu es déjà là, en plan serré, et tu parles à la caméra. Le titre-choc arrive pendant ton geste, puis le 1er sous-titre prend le relais.'],
 ['Cadrage','Plan serré dès la 1re image (zoom ×1,12 sur ton plan). Au moment du geste, un petit coup de zoom (×1,16 en 120 ms, retour en 240 ms).'],
 ['Geste','À filmer : ta main vers l’objectif (ou un objet tendu vers la caméra) dans la 1re seconde. Le montage ne l’invente pas.'],
 ['Ouverture : zoom','Deux départs possibles : plan serré puis zoom out (×1,35 → ×1, 600 ms, ease-in-out), ou plan large puis zoom in (×1 → ×1,3). Ton détourage suit exactement le même zoom.'],
 ['Resserré sur un objet (9:16 et 16:9)','On part du plan large et la caméra se resserre lentement (1,2 s, ease-in-out) sur un objet du décor : un livre, l’horloge, une plante. Le texte arrive quand le zoom s’arrête (amorce + mot clé Doto), sous l’objet en 9:16, à côté en 16:9.'],
 ['Derrière toi (9:16 et 16:9)','Un mot géant en Doto, une image ou un logo sort de derrière toi, du bas vers le haut (600 ms, ease-out), grâce à ton détourage posé par-dessus. Il sort à 1,6 s.'],
 ['À côté de toi (16:9)','Un texte qui s’écrit lettre après lettre (45 ms par signe) à droite ou à gauche de toi, l’amorce en Inter, le mot clé en Doto, un curseur braise à la fin. Ou le titre-choc posé à côté (V3).'],
 ['Titre','Composant TitreChoc (planche A) : V3 sélection au-dessus de la tête, ou V1 chiffre + amorce sous le menton (9:16) / à côté du visage (16:9). Il entre à 0,3 s, sort à 1,6 s.'],
 ['Sous-titres','SousTitreDuo à partir de 1,7 s, jamais en même temps que le titre.'],
 ['Gardés, pas favoris','Le mot géant seul, sans toi ni geste : à éviter en ouverture.'],
],['Élément','Règle'])
body=header('Planche B · composant Accroche','B — L’accroche',"Tu parles à la caméra et tends la main vers l’objectif ; on ouvre en plan serré qui recule, ou en plan large qui avance ; le titre arrive pendant le geste (sélection, chiffre, derrière toi ou à côté), puis le sous-titre.")+f'<div style="display: flex; gap: 40px; align-items: flex-start">{v1}{v2}{v3}{v4}</div><div style="display: flex; gap: 40px; align-items: flex-start">{w3}{w5}{w6}{w7}</div><div style="display: flex; gap: 40px; align-items: flex-start">{v5}{w8}</div>'+frise+spec
page('K-B.dc.html','Accroche',1960,2980,body,a.style()); boards['K-B.dc.html']=(1960,2980,'B — L’accroche')
json.dump(boards,open(f'{R}/boards-B.json','w'),ensure_ascii=False); print('ok')
