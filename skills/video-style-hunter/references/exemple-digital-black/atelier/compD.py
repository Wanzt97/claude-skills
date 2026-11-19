import sys, json, html
# Réutilise les aides de compC2.py (tout ce qui précède « boards={} »)
src=open(__file__.replace('compD.py','compC2.py')).read().split('boards={}')[0]
exec(src)
boards={}
term_lines=['> /montage lance','✓ rushs triés · 12','✓ script calé','› export en cours']
def terminal(a):
    l=''.join(f'<div style="font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 30px; color: {BRAISE if i==3 else OS}; {a.kf(300+i*200,240,EXIT,blur_in=0)}">{html.escape(x)}</div>' for i,x in enumerate(term_lines))
    return f'<div style="position: absolute; left: 140px; top: 160px; width: 800px; height: 440px; box-sizing: border-box; border-radius: 6px; background: {FONTE}; border: 2px solid {ACIER}; padding: 32px; display: flex; flex-direction: column; gap: 22px; {objet_kf(a,200,scale=0.92)}">{l}</div>'
def keycap(label,x,y,s=300,theme='clair',t=0,a=None,fs=None):
    # touche de clavier en volume (CSS), entrée : tombe + se pose, puis pression
    if theme=='clair': face='linear-gradient(160deg,#FFFFFF 0%,#E4E4E4 100%)'; bord='#BDBDBD'; ink=ENCRE; ombre='0 30px 60px rgba(18,18,18,0.22)'
    elif theme=='noir': face='linear-gradient(160deg,#3A3A3A 0%,#232323 100%)'; bord='#0A0A0A'; ink=OS; ombre='0 30px 60px rgba(0,0,0,0.6)'
    else: face='linear-gradient(160deg,#FF8A55 0%,#FF7033 100%)'; bord='#C2410C'; ink=ABYSSE; ombre='0 30px 60px rgba(0,0,0,0.5)'
    n=a.n+1; a.n=n; nm=f'{a.p}k{n}'; pc=lambda v: f'{100*v/CYCLE:.3f}%'
    a.css.append(f'@keyframes {nm}{{0%{{opacity:0;transform:translateY(-120px) rotate(-8deg) scale(0.9)}}{pc(t)}{{opacity:0;transform:translateY(-120px) rotate(-8deg) scale(0.9);animation-timing-function:{EOUT}}}{pc(t+400)}{{opacity:1;transform:translateY(0) rotate(-8deg) scale(1)}}{pc(t+900)}{{opacity:1;transform:translateY(0) rotate(-8deg) scale(1);animation-timing-function:{EIN}}}{pc(t+1020)}{{opacity:1;transform:translateY(14px) rotate(-8deg) scale(0.97)}}{pc(t+1240)}{{opacity:1;transform:translateY(0) rotate(-8deg) scale(1);animation-timing-function:{EOUT}}}{pc(EXIT)}{{opacity:1;transform:translateY(0) rotate(-8deg) scale(1);animation-timing-function:{EIN}}}{pc(EXIT+140)}{{opacity:0;transform:translateY(0) rotate(-8deg) scale(1)}}100%{{opacity:0}}}}')
    fs=fs or int(s*0.2)
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {s}px; height: {s}px; border-radius: {int(s*0.13)}px; background: {face}; box-shadow: inset 0 -{int(s*0.06)}px 0 {bord}, inset 0 2px 0 rgba(255,255,255,0.5), {ombre}; animation: {nm} {CYCLE}ms linear infinite"><span style="position: absolute; left: {int(s*0.13)}px; top: {int(s*0.11)}px; font-family: Inter, sans-serif; font-weight: 600; font-size: {fs}px; color: {ink}">{label}</span></div>'
def selection(a,x,y,w,h,t,clair=False):
    trait=ENCRE if clair else OS
    hd=''.join(f'<span style="position: absolute; {p}; width: 16px; height: 16px; background: {BRAISE}"></span>' for p in ('left: -10px; top: -10px','right: -10px; top: -10px','left: -10px; bottom: -10px','right: -10px; bottom: -10px'))
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; box-sizing: border-box; border: 3px solid {trait}; {a.kf(t,240,EXIT,blur_in=0,extra_in=";transform:scale(1.03)",extra_on=";transform:scale(1)")}">{hd}</div>'
def texte(a,txt,t0,size,color,weight=800,ec=150,font='Inter, sans-serif',ls='-0.02em'):
    m,t=mots(a,txt,t0,ec); return f'<span style="font-family: {font}; font-weight: {weight}; font-size: {size}px; line-height: 0.95; letter-spacing: {ls}; color: {color}">{m}</span>',t
def doto(a,txt,t0,size,color):
    k,t=lettres(a,txt,t0); return f'<span style="font-family: Doto, monospace; font-weight: 900; font-size: {size}px; line-height: 0.9; letter-spacing: -0.04em; color: {color}; white-space: nowrap">{k}</span>',t

# ---------- D1 : centrée sur le texte ----------
a=Anim('d1_')
l1,t=texte(a,'le montage',200,120,ENCRE); l2,t=texte(a,'prend',t,120,ENCRE); k,_=doto(a,'1 heure',t+120,190,BRAISE_P)
v1=apercu(grille(True)+f'<div style="position: absolute; left: 90px; right: 90px; top: 640px; display: flex; flex-direction: column; gap: 12px">{l1}{l2}<div style="margin-top: 18px">{k}</div></div>','D1 · V1 · Blanc : phrase énorme + mot Doto')
l1,t=texte(a,'tu n’as pas besoin de',200,64,OS); k,tk=doto(a,'temps',t+120,230,OS)
v2=apercu(grille(False)+f'<div style="position: absolute; left: 90px; right: 90px; top: 700px; display: flex; flex-direction: column; gap: 26px; align-items: flex-start">{l1}<div style="position: relative; padding: 4px 22px">{k}</div></div>'+selection(a,90,792,700,240,tk+120)+f'<div style="position: absolute; left: 90px; top: 1100px">{texte(a,"tu as besoin d’un plan.",tk+600,64,BRUME)[0]}</div>','D1 · V2 · Noir : un mot dans le cadre de sélection')
l1,t=texte(a,'tout est sous',700,96,ENCRE); k,_=doto(a,'contrôle',t+120,170,ENCRE)
v3=apercu(grille(True)+keycap('Ctrl',350,420,380,'clair',0,a,fs=72)+f'<div style="position: absolute; left: 70px; right: 70px; top: 1060px; display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center">{l1}{k}</div>','D1 · V3 · Blanc : texte énorme + un objet d’appui')

# V4 : texte au milieu, puis un graphique qui se construit dessous
l1,t=texte(a,'tes vues ont',200,96,OS); k,tk=doto(a,'doublé',t+120,200,OS)
hauteurs=[150,210,190,290,420]
barres=''.join(f'<div style="width: 96px; height: {h}px; border-radius: 6px 6px 0 0; background: {BRAISE if i==4 else ACIER}; transform-origin: 50% 100%; {a.kf(tk+300+i*120,400,EXIT,blur_in=0,extra_in=";transform:scaleY(0)",extra_on=";transform:scaleY(1)")}"></div>' for i,h in enumerate(hauteurs))
axe=f'<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 3px; background: {BRUME}; {a.kf(tk+200,240,EXIT,blur_in=0)}"></div>'
etiq=f'<div style="position: absolute; left: 0; right: 0; bottom: -56px; display: flex; justify-content: space-between; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 26px; letter-spacing: 0.08em; color: {BRUME}; {a.kf(tk+900,240,EXIT,blur_in=0)}"><span>JAN</span><span>MAI</span></div>'
graph=f'<div style="position: absolute; left: 140px; right: 140px; top: 1000px; height: 440px; display: flex; align-items: flex-end; justify-content: space-between; text-shadow: none">{barres}{axe}{etiq}</div>'
v4=apercu(grille(False)+f'<div style="position: absolute; left: 70px; right: 70px; top: 560px; display: flex; flex-direction: column; align-items: center; gap: 10px; text-align: center; text-shadow: {HALO}">{l1}{k}</div>'+graph,'D1 · V4 · Noir : texte au milieu, puis un graphique')
spec=tableau([
 ['Principe','Le texte est la star : 3 à 6 mots énormes, UN mot mis en valeur. Au plus un objet d’appui. Beaucoup de vide.'],
 ['Polices','La phrase en Inter 800 (96 à 120 px en 9:16, approche −0,02 em). Le mot mis en valeur en Doto 900 (170 à 230 px) : jamais de serif, jamais d’italique.'],
 ['Mise en valeur (une seule)','plus grand en Doto ; ou braise (braise foncée sur fond blanc) ; ou dans un cadre de sélection (trait 3 px, 4 poignées braise), comme dans un logiciel.'],
 ['V4 Texte puis graphique','La phrase au milieu de l’écran ; dès qu’elle est dite, un graphique simple se construit dessous (5 barres qui montent une à une, la dernière en braise ; axe et 2 étiquettes mono). Le graphique appuie le texte, il ne le remplace pas.'],
 ['16:9','La phrase passe sur une ou deux lignes, alignée à gauche, avec plus de vide à droite. Le graphique ou l’objet d’appui se place à côté du texte au lieu d’en dessous.'],
 ['Fond','Blanc os ou noir du pack (grille gommée). Jamais d’aplat de couleur.'],
 ['Mouvement','Mots un par un au rythme de la voix (120 ms, fondu + flou), le mot Doto lettre par lettre (240 ms, 30 ms d’écart), le cadre 120 ms après sa dernière lettre (240 ms). L’objet d’appui arrive en premier. Sortie : tout d’un coup, 140 ms.'],
],['Élément','Règle'])
body=header('Planche D · composant AnimTexte','D1 — Centrée sur le texte',"Tes favoris : un texte énorme en grotesque grasse avec un seul mot mis en valeur. L’italique serif des inspirations devient le mot géant en Doto.")+f'<div style="display: flex; gap: 40px">{v1}{v2}{v3}{v4}</div>'+spec
S1=0.3
l1,t=texte(a,'le montage prend',200,120,ENCRE); k,_=doto(a,'1 heure',t+120,260,BRAISE_P)
w5=ap169(grille(True)+f'<div style="position: absolute; left: 160px; right: 160px; top: 330px; display: flex; flex-direction: column; gap: 24px">{l1}{k}</div>','D1 · 16:9 · V5 · Blanc : phrase énorme alignée à gauche',sc=S1)
l1,t=texte(a,'tes vues ont',200,96,OS); k,tk=doto(a,'doublé',t+120,200,OS)
hb=[150,210,190,290,420]
barres=''.join(f'<div style="width: 110px; height: {h}px; border-radius: 6px 6px 0 0; background: {BRAISE if i==4 else ACIER}; transform-origin: 50% 100%; {a.kf(tk+300+i*120,400,EXIT,blur_in=0,extra_in=";transform:scaleY(0)",extra_on=";transform:scaleY(1)")}"></div>' for i,h in enumerate(hb))
axe=f'<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 3px; background: {BRUME}; {a.kf(tk+200,240,EXIT,blur_in=0)}"></div>'
etiq=f'<div style="position: absolute; left: 0; right: 0; bottom: -56px; display: flex; justify-content: space-between; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 26px; letter-spacing: 0.08em; color: {BRUME}; {a.kf(tk+900,240,EXIT,blur_in=0)}"><span>JAN</span><span>MAI</span></div>'
graph=f'<div style="position: absolute; left: 1060px; right: 160px; top: 240px; height: 480px; display: flex; align-items: flex-end; justify-content: space-between">{barres}{axe}{etiq}</div>'
w6=ap169(grille(False)+f'<div style="position: absolute; left: 160px; top: 330px; display: flex; flex-direction: column; gap: 10px; text-shadow: {HALO}">{l1}{k}</div>'+graph,'D1 · 16:9 · V6 · Noir : texte à gauche, graphique à droite',sc=S1)
l1,t=texte(a,'tout est sous',700,96,ENCRE); k,_=doto(a,'contrôle',t+120,170,ENCRE)
w7=ap169(grille(True)+keycap('Ctrl',260,300,440,'clair',0,a,fs=84)+f'<div style="position: absolute; left: 900px; right: 100px; top: 380px; display: flex; flex-direction: column; gap: 16px">{l1}{k}</div>','D1 · 16:9 · V7 · Blanc : l’objet à gauche, le texte à droite',sc=S1)
body=header('Planche D · composant AnimTexte','D1 — Centrée sur le texte',"Tes favoris : un texte énorme en grotesque grasse avec un seul mot mis en valeur. L’italique serif des inspirations devient le mot géant en Doto.")+L916+f'<div style="display: flex; gap: 40px">{v1}{v2}{v3}{v4}</div>'+L169+rangee(w5,w6,w7)+spec
page('K-D1.dc.html','AnimTexte',1960,2080,body,a.style()); boards['K-D1.dc.html']=(1960,2080,'D1 — Centrée sur le texte')

# ---------- D2 : centrée sur une personne ----------
a=Anim('d2_')
def carte_plan(a,x,y,w,h,t,rot,clair=True):
    sh='box-shadow: 0 18px 40px rgba(18,18,18,0.18), 0 2px 6px rgba(18,18,18,0.10);' if clair else 'box-shadow: 0 18px 40px rgba(0,0,0,0.6);'
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; border-radius: 12px; overflow: hidden; border: 6px solid {CARTE_C if clair else FONTE}; {sh} transform: rotate({rot}deg)"><div style="width: 100%; height: 100%; {a.kf(t,400,EXIT,blur_in=0,extra_in=";transform:translateY(48px)",extra_on=";transform:translateY(0px)")}"><img src="{F916}" alt="Ton plan face caméra" style="width: 100%; height: 100%; object-fit: cover; object-position: 50% 40%"></div></div>'
l1,t=texte(a,'3 vidéos',900,96,ENCRE); k,_=doto(a,'gagnantes',t+120,150,BRAISE_P)
v1=apercu(grille(True)+carte_plan(a,110,260,400,620,200,-6)+carte_plan(a,560,420,400,620,320,5)+f'<div style="position: absolute; left: 80px; right: 80px; top: 1240px; display: flex; flex-direction: column; gap: 10px">{l1}{k}</div>','D2 · V1 · Blanc : tes plans posés en cartes')
trame='background-image: radial-gradient(rgba(10,10,10,0.55) 1.6px, transparent 1.8px); background-size: 7px 7px;'
pers=f'<div style="position: absolute; left: 380px; top: 520px; width: 700px; height: 1400px; overflow: hidden; {a.kf(0,400,EXIT,blur_in=0)}"><img src="{F916}" alt="Personne en noir et blanc" style="position: absolute; left: -190px; top: -420px; width: 1080px; height: 1920px; object-fit: cover; filter: grayscale(1) contrast(1.35) brightness(1.05); -webkit-mask-image: radial-gradient(ellipse 48% 42% at 50% 44%, #000 60%, transparent 72%); mask-image: radial-gradient(ellipse 48% 42% at 50% 44%, #000 60%, transparent 72%)"><div style="position: absolute; inset: 0; {trame} mix-blend-mode: multiply; opacity: 0.5"></div></div>'
l1,t=texte(a,'ce qui',300,110,OS); l2,t=texte(a,'change',t,110,OS); k,_=doto(a,'tout',t+120,220,BRAISE)
v2=apercu(grille(False)+pers+f'<div style="position: absolute; left: 70px; top: 300px; display: flex; flex-direction: column; gap: 6px; text-shadow: {HALO}">{l1}{l2}{k}</div>','D2 · V2 · Noir : personne en noir et blanc, titre à côté')
spec=tableau([
 ['Principe','La personne porte l’idée. Le titre est à côté, jamais sur le visage.'],
 ['V1 Tes plans en cartes','Sur fond blanc os à grille : 1 à 3 cartes de tes plans (bord blanc 6 px, arrondi 12, légère rotation −6° / +5°, ombre claire). Le texte en dessous ou à côté.'],
 ['V2 Personne en noir et blanc','Sur fond noir : une personne (toi, une statue, une photo) en noir et blanc contrasté, avec une trame de points légère ; bords effacés (ou détourage). Titre à gauche avec le halo sombre, mot fort en Doto braise.'],
 ['16:9','Les cartes de tes plans se mettent en ligne (3 au plus), le texte dessous sur une ligne. La personne passe d’un côté, le titre de l’autre.'],
 ['Mouvement','Les cartes montent de 48 px + fondu (400 ms), 120 ms d’écart ; la personne apparaît en fondu (400 ms) ; le texte suit la voix (planche A).'],
 ['À éviter','Texte sur le visage, couleurs vives sur la personne, plus de 3 cartes.'],
],['Élément','Règle'])
body=header('Planche D · composant AnimPersonne','D2 — Centrée sur une personne',"Tes favoris : tes propres plans posés en cartes sur fond clair, ou une personne détourée en noir et blanc, le titre à côté.")+f'<div style="display: flex; gap: 40px">{v1}{v2}</div>'+spec
def carte169(x,y,w,h,t,rot):
    return carte_plan(a,x,y,w,h,t,rot).replace(F916,F169).replace('object-position: 50% 40%','object-position: 50% 50%')
l1,t=texte(a,'3 vidéos',900,96,ENCRE); k,_=doto(a,'gagnantes',t+120,150,BRAISE_P)
w3=ap169(grille(True)+carte169(140,200,520,292,200,-5)+carte169(700,280,520,292,320,3)+carte169(1260,210,520,292,440,-2)+f'<div style="position: absolute; left: 0; right: 0; top: 700px; display: flex; align-items: baseline; justify-content: center; gap: 28px">{l1}{k}</div>','D2 · 16:9 · V3 · Blanc : tes plans en cartes, en ligne')
pers169=f'<div style="position: absolute; left: 900px; top: 0; width: 1020px; height: 1080px; overflow: hidden; {a.kf(0,400,EXIT,blur_in=0)}"><img src="{F169}" alt="Personne en noir et blanc" style="position: absolute; left: -861px; top: -362px; width: 3072px; height: 1728px; object-fit: cover; filter: grayscale(1) contrast(1.35) brightness(1.05); -webkit-mask-image: radial-gradient(ellipse 17% 34% at 44% 52%, #000 40%, transparent 78%); mask-image: radial-gradient(ellipse 17% 34% at 44% 52%, #000 40%, transparent 78%)"><div style="position: absolute; inset: 0; {trame} mix-blend-mode: multiply; opacity: 0.5"></div></div>'
l1,t=texte(a,'ce qui',300,110,OS); l2,t=texte(a,'change',t,110,OS); k,_=doto(a,'tout',t+120,220,BRAISE)
w4=ap169(grille(False)+pers169+f'<div style="position: absolute; left: 160px; top: 260px; display: flex; flex-direction: column; gap: 6px; text-shadow: {HALO}">{l1}{l2}{k}</div>','D2 · 16:9 · V4 · Noir : la personne à droite, le titre à gauche')
body=header('Planche D · composant AnimPersonne','D2 — Centrée sur une personne',"Tes favoris : tes propres plans posés en cartes sur fond clair, ou une personne détourée en noir et blanc, le titre à côté.")+L916+f'<div style="display: flex; gap: 40px">{v1}{v2}</div>'+L169+rangee(w3,w4)+spec
page('K-D2.dc.html','AnimPersonne',1480,1992,body,a.style()); boards['K-D2.dc.html']=(1480,1992,'D2 — Centrée sur une personne')

# ---------- D3 : centrée sur un objet ----------
a=Anim('d3_')
l1,t=texte(a,'appuie sur',1300,96,OS); k,_=doto(a,'Échap',t+120,200,BRAISE)
v1=apercu(grille(False)+keycap('Esc',300,520,480,'braise',200,a,fs=96)+f'<div style="position: absolute; left: 70px; right: 70px; top: 1220px; display: flex; flex-direction: column; align-items: center; gap: 14px; text-shadow: {HALO}">{l1}{k}</div>','D3 · V1 · Noir : une touche braise')
ico='<svg aria-hidden="true" width="420" height="420" viewBox="0 0 64 64"><path d="M6 32 C 16 16, 48 16, 58 32 C 48 48, 16 48, 6 32 Z" fill="none" stroke="#121212" stroke-width="2.4" stroke-linejoin="round"></path><circle cx="32" cy="32" r="10" fill="none" stroke="#121212" stroke-width="2.4"></circle><circle cx="32" cy="32" r="4.5" fill="#C2410C"></circle></svg>'
l1,t=texte(a,'ce que ton',700,90,ENCRE); k,_=doto(a,'œil voit',t+120,190,ENCRE)
v2=apercu(grille(True)+f'<div style="position: absolute; left: 330px; top: 460px; {objet_kf(a,200,scale=0.92)}">{ico}</div>'+f'<div style="position: absolute; left: 70px; right: 70px; top: 1060px; display: flex; flex-direction: column; align-items: center; gap: 14px">{l1}{k}</div>','D3 · V2 · Blanc : une icône au trait (un œil)')
l1,t=texte(a,'garde le',1300,96,ENCRE); k,_=doto(a,'contrôle',t+120,170,BRAISE_P)
v3=apercu(grille(True)+keycap('Ctrl',300,520,480,'clair',200,a,fs=96)+f'<div style="position: absolute; left: 70px; right: 70px; top: 1220px; display: flex; flex-direction: column; align-items: center; gap: 14px">{l1}{k}</div>','D3 · V3 · Blanc : une touche claire')
spec=tableau([
 ['Principe','UN objet héros au centre, en volume, net, avec beaucoup de vide ; un titre court l’explique. Jamais plusieurs objets qui se battent.'],
 ['Objets','Touches de clavier (Ctrl, Esc, Shift, Entrée…) : ton motif de signature. Aussi une clé, un feu, un œil, une icône au trait (trait 2,4 en encre ou os, détail en braise).'],
 ['Touche','Carré arrondi (13 % du côté), face en dégradé doux, bord bas plus sombre (6 % du côté), ombre portée sous la touche, inclinaison −8°. Trois teintes : claire (sur blanc), noire (sur noir), braise (l’accent, une seule à l’écran).'],
 ['Fond','Blanc os ou noir du pack. L’aplat de couleur des inspirations est remplacé par la touche braise sur fond noir.'],
 ['16:9','La touche se pose d’un côté (environ un tiers de l’écran), le titre de l’autre, aligné à gauche. Avec la touche braise, le titre reste en os : un seul élément braise.'],
 ['Mouvement','La touche tombe et se pose (400 ms, ease-out), puis est pressée une fois (descend de 14 px en 120 ms, remonte en 220 ms). Le titre arrive après la pression, au rythme de la voix.'],
],['Élément','Règle'])
body=header('Planche D · composant AnimObjet','D3 — Centrée sur un objet',"Tes favoris : un objet héros, surtout des touches de clavier en volume. Chez toi, il se pose sur fond noir ou blanc os, et la couleur vient de la touche braise.")+f'<div style="display: flex; gap: 40px">{v1}{v2}{v3}</div>'+spec
l1,t=texte(a,'appuie sur',1300,96,OS); k,_=doto(a,'Échap',t+120,200,OS)
w4=ap169(grille(False)+keycap('Esc',300,280,460,'braise',200,a,fs=92)+f'<div style="position: absolute; left: 980px; right: 100px; top: 380px; display: flex; flex-direction: column; gap: 14px; text-shadow: {HALO}">{l1}{k}</div>','D3 · 16:9 · V4 · Noir : la touche braise à gauche')
l1,t=texte(a,'garde le',1300,96,ENCRE); k,_=doto(a,'contrôle',t+120,170,BRAISE_P)
w5=ap169(grille(True)+keycap('Ctrl',1180,280,460,'clair',200,a,fs=92)+f'<div style="position: absolute; left: 160px; right: 860px; top: 380px; display: flex; flex-direction: column; gap: 14px">{l1}{k}</div>','D3 · 16:9 · V5 · Blanc : la touche à droite')
body=header('Planche D · composant AnimObjet','D3 — Centrée sur un objet',"Tes favoris : un objet héros, surtout des touches de clavier en volume. Chez toi, il se pose sur fond noir ou blanc os, et la couleur vient de la touche braise.")+L916+f'<div style="display: flex; gap: 40px">{v1}{v2}{v3}</div>'+L169+rangee(w4,w5)+spec
page('K-D3.dc.html','AnimObjet',1480,2068,body,a.style()); boards['K-D3.dc.html']=(1480,2068,'D3 — Centrée sur un objet')

# ---------- D4 : centrée sur un graphique ----------
a=Anim('d4_')
items=['Coupes','Sous-titres','Accroches','B-roll','Musique','Export']
rows=''.join(f'<div style="display: flex; align-items: center; gap: 22px; {a.kf(600+i*200,240,EXIT,blur_in=0)}"><span style="width: 40px; height: 40px; box-sizing: border-box; border-radius: 6px; border: 3px solid {OS}; display: flex; align-items: center; justify-content: center"><svg aria-hidden="true" width="26" height="26" viewBox="0 0 24 24"><path d="M5 12l5 5 9-10" fill="none" stroke="#EFEFEF" stroke-width="3"></path></svg></span><span style="font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 38px; color: {OS}">{x}</span></div>' for i,x in enumerate(items))
k,_=doto(a,'6/6',200,200,BRAISE)
v1=apercu(grille(False)+f'<div style="position: absolute; left: 110px; top: 330px; display: flex; flex-direction: column; gap: 30px">{k}<span style="font-family: Inter, sans-serif; font-weight: 800; font-size: 54px; color: {OS}">{mots(a,"faits par Claude.",500)[0]}</span><div style="margin-top: 30px; display: flex; flex-direction: column; gap: 26px">{rows}</div></div>','D4 · V1 · Noir : checklist qui se coche')
def logo_rond(x,y,t,inner):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: 260px; height: 260px; border-radius: 50%; background: {CARTE_C}; box-shadow: 0 18px 40px rgba(18,18,18,0.12), 0 2px 6px rgba(18,18,18,0.08); display: flex; align-items: center; justify-content: center; {objet_kf(a,t,scale=0.92)}">{inner}</div>'
star='<svg aria-hidden="true" width="130" height="130" viewBox="0 0 24 24"><path d="M12 2v20M2 12h20M4.9 4.9l14.2 14.2M19.1 4.9L4.9 19.1" stroke="#121212" stroke-width="2.2" stroke-linecap="round"></path></svg>'
film='<svg aria-hidden="true" width="120" height="120" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="#121212" stroke-width="1.8"></rect><path d="M10 9l5 3-5 3z" fill="#121212"></path></svg>'
lien=f'<svg aria-hidden="true" width="1080" height="1920" viewBox="0 0 1080 1920" style="position: absolute; left: 0; top: 0"><path d="M300 820 C 420 700, 660 700, 780 820" fill="none" stroke="#5C5A55" stroke-width="4" stroke-dasharray="10 12" style="{a.kf(500,400,EXIT,blur_in=0)}"></path></svg>'
pill=f'<div style="position: absolute; left: 430px; top: 690px; padding: 14px 26px; border-radius: 40px; background: {BRAISE}; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 34px; color: {ABYSSE}; {objet_kf(a,800,scale=0.92)}">PLAN.md</div>'
labs=f'<div style="position: absolute; left: 0; right: 0; top: 560px; display: flex; justify-content: space-between; padding: 0 110px; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 30px; letter-spacing: 0.08em; color: {ENCRE2}"><span>SCRIPT</span><span>MONTAGE</span></div>'
l1,t=texte(a,'du script au',1100,96,ENCRE); k,_=doto(a,'montage',t+120,170,ENCRE)
v2=apercu(grille(True)+labs+logo_rond(170,690,200,star)+logo_rond(650,690,320,film)+lien+pill+f'<div style="position: absolute; left: 70px; right: 70px; top: 1180px; display: flex; flex-direction: column; align-items: center; gap: 14px">{l1}{k}</div>','D4 · V2 · Blanc : schéma, deux éléments reliés')
v3=apercu(grille(False)+terminal(a).replace('left: 140px; top: 160px; width: 800px; height: 440px','left: 100px; top: 640px; width: 880px; height: 520px')+f'<div style="position: absolute; left: 0; right: 0; top: 1260px; text-align: center; {AM}; font-size: 56px; color: {OS}; text-shadow: {HALO}">{mots(a,"il fait tout seul",1200)[0]}</div>','D4 · V3 · Noir : terminal propre')
spec=tableau([
 ['Principe','Une interface qui fait comprendre en un coup d’œil. Peu de texte : les chiffres et l’interface parlent.'],
 ['V1 Checklist','Sur fond noir : un chiffre en Doto braise (6/6), une phrase courte, puis une liste mono (38 px) dont chaque ligne se coche (case 40 px, trait 3 px os, coche os). Seul le chiffre est en braise : un seul élément braise à l’écran.'],
 ['V2 Schéma','Sur fond blanc : deux éléments ronds (blanc pur, ombre claire) reliés par un trait pointillé gris, une pastille braise au milieu (mono, abysse). Étiquettes mono en encre secondaire. La pastille est le seul élément braise.'],
 ['V3 Terminal','Sur fond noir : fenêtre fonte, trait acier, police mono 30 px, la ligne en cours en braise.'],
 ['16:9','Le chiffre ou le titre à gauche, la liste à droite ; le schéma s’étale en largeur, la phrase dessous sur une ligne. Le terminal en 16:9 : voir C4 V5.'],
 ['Mouvement','Les éléments arrivent un par un (échelle 0,92 → 1 + fondu, 400 ms) ; les lignes de liste ou de terminal toutes les 200 ms (240 ms) ; le trait du schéma après ses deux bouts.'],
],['Élément','Règle'])
body=header('Planche D · composant AnimGraphique','D4 — Centrée sur un graphique',"Tes favoris : une interface sombre et propre (checklist, terminal, liste d’agents) ou un schéma simple qui relie deux éléments.")+f'<div style="display: flex; gap: 40px">{v1}{v2}{v3}</div>'+spec
rows169=''.join(f'<div style="display: flex; align-items: center; gap: 22px; {a.kf(600+i*200,240,EXIT,blur_in=0)}"><span style="width: 40px; height: 40px; box-sizing: border-box; border-radius: 6px; border: 3px solid {OS}; display: flex; align-items: center; justify-content: center"><svg aria-hidden="true" width="26" height="26" viewBox="0 0 24 24"><path d="M5 12l5 5 9-10" fill="none" stroke="#EFEFEF" stroke-width="3"></path></svg></span><span style="font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 38px; color: {OS}">{x}</span></div>' for i,x in enumerate(items))
k,_=doto(a,'6/6',200,240,BRAISE)
w4=ap169(grille(False)+f'<div style="position: absolute; left: 180px; top: 330px; display: flex; flex-direction: column; gap: 24px">{k}<span style="font-family: Inter, sans-serif; font-weight: 800; font-size: 54px; color: {OS}">{mots(a,"faits par Claude.",500)[0]}</span></div><div style="position: absolute; left: 1080px; top: 230px; display: flex; flex-direction: column; gap: 26px">{rows169}</div>','D4 · 16:9 · V4 · Noir : le chiffre à gauche, la liste à droite')
def rond169(x,y,t,inner): return logo_rond(x,y,t,inner)
lien169=f'<svg aria-hidden="true" width="1920" height="1080" viewBox="0 0 1920 1080" style="position: absolute; left: 0; top: 0"><path d="M720 430 C 860 300, 1060 300, 1200 430" fill="none" stroke="#5C5A55" stroke-width="4" stroke-dasharray="10 12" style="{a.kf(500,400,EXIT,blur_in=0)}"></path></svg>'
pill169=f'<div style="position: absolute; left: 840px; top: 300px; padding: 14px 26px; border-radius: 40px; background: {BRAISE}; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 34px; color: {ABYSSE}; {objet_kf(a,800,scale=0.92)}">PLAN.md</div>'
labs169=f'<div style="position: absolute; left: 460px; width: 1000px; top: 220px; display: flex; justify-content: space-between; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 30px; letter-spacing: 0.08em; color: {ENCRE2}"><span style="width: 260px; text-align: center">SCRIPT</span><span style="width: 260px; text-align: center">MONTAGE</span></div>'
l1,t=texte(a,'du script au',1100,96,ENCRE); k,_=doto(a,'montage',t+120,170,ENCRE)
w5=ap169(grille(True)+labs169+rond169(460,300,200,star)+rond169(1200,300,320,film)+lien169+pill169+f'<div style="position: absolute; left: 0; right: 0; top: 690px; display: flex; align-items: baseline; justify-content: center; gap: 28px">{l1}{k}</div>','D4 · 16:9 · V5 · Blanc : le schéma s’étale en largeur')
body=header('Planche D · composant AnimGraphique','D4 — Centrée sur un graphique',"Tes favoris : une interface sombre et propre (checklist, terminal, liste d’agents) ou un schéma simple qui relie deux éléments.")+L916+f'<div style="display: flex; gap: 40px">{v1}{v2}{v3}</div>'+L169+rangee(w4,w5)+spec
page('K-D4.dc.html','AnimGraphique',1480,2016,body,a.style()); boards['K-D4.dc.html']=(1480,2016,'D4 — Centrée sur un graphique')
json.dump(boards,open(f'{R}/boards-D-composants.json','w'),ensure_ascii=False)
print('ok',boards)
