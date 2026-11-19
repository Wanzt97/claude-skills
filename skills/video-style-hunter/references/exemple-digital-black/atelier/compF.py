import sys, json, html, re
src=open(__file__.replace('compF.py','compC2.py')).read().split('boards={}')[0]
exec(src)
d=open(__file__.replace('compF.py','compD.py')).read()
exec(d[d.index('def keycap'):d.index('def selection')])
c2=open(__file__.replace('compF.py','compC2.py')).read()
exec(c2[c2.index("term_lines="):c2.index("pied=")])
boards={}
a=Anim('f_')
pc=lambda v: f'{100*v/CYCLE:.3f}%'
def derive(dx,dy):
    n=a.n+1; a.n=n; nm=f'f_d{n}'
    a.css.append(f'@keyframes {nm}{{0%{{transform:translate(0px,0px)}}100%{{transform:translate({dx}px,{dy}px)}}}}')
    return f'animation: {nm} {CYCLE}ms linear infinite'
def couche_titre(n,txt):
    return f'<div style="position: absolute; left: 24px; top: 24px; padding: 8px 14px; border-radius: 3px; background: rgba(10,10,10,0.8); font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 34px; letter-spacing: 0.08em; color: {BRAISE if n==4 else OS}">{n} · {txt}</div>'
# ----- Exemple 1 : objet sur fond blanc -----
def ex1(n,anime=False):
    o=grille(True)
    if n>=4 and not anime: pass
    prof=''
    if n>=4:
        prof=(f'<div style="position: absolute; left: -140px; top: 1180px; filter: blur(18px); opacity: 0.9; {derive(30,-20) if anime else ""}">{keycap("Esc",0,0,420,"clair",0,a,fs=80).replace("animation:","data-x:")}</div>'
              f'<div style="position: absolute; left: 820px; top: 120px; filter: blur(16px); opacity: 0.85; {derive(-24,16) if anime else ""}">{keycap("Shift",0,0,380,"clair",0,a,fs=70).replace("animation:","data-x:")}</div>')
    foc=keycap('Ctrl',300,560,480,'clair',200 if anime else -2000,a,fs=96) if n>=2 else ''
    if n>=2 and not anime: foc=foc.replace('animation:','data-x:')
    sout=''
    if n>=3:
        if anime:
            l1,t=mots(a,'garde le',1300); k,_=lettres(a,'contrôle',t+120)
        else:
            l1='garde le'; k='contrôle'
        sout=(f'<div style="position: absolute; left: 70px; right: 70px; top: 1220px; display: flex; flex-direction: column; align-items: center; gap: 12px"><span style="{AM}; font-size: 96px; color: {ENCRE}">{l1}</span><span style="{MC}; font-size: 170px; color: {BRAISE_P}">{k}</span></div>'
              f'<div style="position: absolute; left: 0; right: 0; top: 330px; text-align: center; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 30px; letter-spacing: 0.08em; color: {ENCRE2}; {a.kf(900,240,EXIT,blur_in=0) if anime else ""}">ÉTAPE 01</div>')
    return o+prof+foc+sout
# ----- Exemple 2 : interface sur fond noir -----
def carte_floue(x,y,w,h,anim):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {w}px; height: {h}px; border-radius: 6px; background: {FONTE}; border: 2px solid {ACIER}; filter: blur(16px); opacity: 0.8; {anim}"></div>'
def ex2(n,anime=False):
    o=grille(False); prof=''; foc=''; sout=''
    if n>=4:
        prof=carte_floue(-160,180,520,340,derive(26,10) if anime else '')+carte_floue(760,1420,520,380,derive(-20,-14) if anime else '')
    if n>=2:
        foc=terminal(a).replace('left: 140px; top: 160px; width: 800px; height: 440px','left: 100px; top: 640px; width: 880px; height: 520px')
        if not anime: foc=re.sub(r'animation: [^;"]*','animation: none',foc)
    if n>=3:
        if anime:
            l1,t=mots(a,'ça tourne',1200); k,_=lettres(a,'seul',t+120)
        else: l1='ça tourne'; k='seul'
        sout=(f'<div style="position: absolute; left: 0; right: 0; top: 1240px; display: flex; flex-direction: column; align-items: center; text-shadow: {HALO}"><span style="{AM}; color: {OS}">{l1}</span><span style="{MC}; font-size: 220px; color: {OS}">{k}</span></div>'
              f'<div style="position: absolute; left: 100px; top: 560px; padding: 8px 16px; border-radius: 40px; background: {BRAISE}; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 28px; color: {ABYSSE}; {a.kf(900,240,EXIT,blur_in=0) if anime else ""}">EN DIRECT</div>')
    return o+prof+foc+sout
noms=['Fond','Sujet principal','Soutien','Profondeur']
SC=0.235
r1=''.join(apercu(ex1(i)+couche_titre(i,noms[i-1]),f'Couche {i} · {noms[i-1]}',sc=SC) for i in (1,2,3,4))+apercu(ex1(4,True),'Le résultat, animé',sc=SC)
r2=''.join(apercu(ex2(i)+couche_titre(i,noms[i-1]),f'Couche {i} · {noms[i-1]}',sc=SC) for i in (1,2,3,4))+apercu(ex2(4,True),'Le résultat, animé',sc=SC)
lab=lambda t: f'<div style="font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 15px; letter-spacing: 0.08em; text-transform: uppercase; color: {BRUME}">{t}</div>'
spec=tableau([
 ['1 · Fond','Un fond du pack (grille gommée, grappes ou plan d’architecte), noir ou blanc os. Il remplit tout le cadre et ne porte aucune information.'],
 ['2 · Sujet principal','UN seul sujet dans la zone centrale : un objet, une interface, un chiffre, ou toi. Si on hésite sur le sujet, la scène est à refaire.'],
 ['3 · Soutien','2 à 4 éléments autour du sujet qui appuient l’idée sans lui voler la vedette : la phrase (amorce + mot clé Doto), une étiquette mono, une pastille. Un seul élément braise à l’écran.'],
 ['4 · Profondeur','1 ou 2 éléments vers les bords, coupés par le cadre, flous (16 à 18 px) ou plus grands, devant ou derrière le sujet. Aucun texte à lire dedans. Ils dérivent très lentement (20 à 30 px sur toute la scène) pour donner du relief.'],
 ['Ordre d’entrée','Le fond est déjà là ; le sujet arrive en premier ; puis le soutien au rythme de la voix ; la profondeur bouge en continu, sans jamais attirer l’œil.'],
],['Couche','Règle'])
body=header('Planche F · règle de construction','F — La composition en 4 couches',"Chaque scène graphique se construit en 4 couches, de l’arrière vers l’avant. Montré ici sur deux de tes scènes : une touche sur fond blanc (D3) et un terminal sur fond noir (D4).")+lab('Exemple 1 · un objet sur fond blanc')+f'<div style="display: flex; gap: 24px">{r1}</div>'+lab('Exemple 2 · une interface sur fond noir')+f'<div style="display: flex; gap: 24px">{r2}</div>'+spec
def ex1_169():
    o=grille(True)
    prof=(f'<div style="position: absolute; left: -120px; top: 680px; filter: blur(18px); opacity: 0.9; {derive(30,-20)}">{keycap("Esc",0,0,400,"clair",0,a,fs=76).replace("animation:","data-x:")}</div>'
          f'<div style="position: absolute; left: 1640px; top: -90px; filter: blur(16px); opacity: 0.85; {derive(-24,16)}">{keycap("Shift",0,0,360,"clair",0,a,fs=66).replace("animation:","data-x:")}</div>')
    foc=keycap('Ctrl',320,290,440,'clair',200,a,fs=88)
    l1,t=mots(a,'garde le',1300); k,_=lettres(a,'contrôle',t+120)
    sout=(f'<div style="position: absolute; left: 960px; top: 300px; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 30px; letter-spacing: 0.08em; color: {ENCRE2}; {a.kf(900,240,EXIT,blur_in=0)}">ÉTAPE 01</div>'
          f'<div style="position: absolute; left: 960px; right: 100px; top: 370px; display: flex; flex-direction: column; gap: 12px"><span style="{AM}; font-size: 96px; color: {ENCRE}">{l1}</span><span style="{MC}; font-size: 170px; color: {BRAISE_P}">{k}</span></div>')
    return o+prof+foc+sout
def ex2_169():
    o=grille(False)
    prof=carte_floue(-200,40,520,340,derive(26,10))+carte_floue(1580,720,520,380,derive(-20,-14))
    foc=terminal(a).replace('left: 140px; top: 160px; width: 800px; height: 440px','left: 160px; top: 290px; width: 900px; height: 520px')
    l1,t=mots(a,'ça tourne',1200); k,_=lettres(a,'seul',t+120)
    sout=(f'<div style="position: absolute; left: 160px; top: 210px; padding: 8px 16px; border-radius: 40px; background: {BRAISE}; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 28px; color: {ABYSSE}; {a.kf(900,240,EXIT,blur_in=0)}">EN DIRECT</div>'
          f'<div style="position: absolute; left: 1120px; right: 100px; top: 380px; display: flex; flex-direction: column; align-items: center; text-shadow: {HALO}"><span style="{AM}; color: {OS}">{l1}</span><span style="{MC}; font-size: 220px; color: {OS}">{k}</span></div>')
    return o+prof+foc+sout
r169='<div style="display: flex; gap: 40px; align-items: flex-start">'+ap169(ex1_169(),'16:9 · Exemple 1 · le résultat, animé')+ap169(ex2_169(),'16:9 · Exemple 2 · le résultat, animé')+'</div>'
spec=spec.replace('<tbody>','<tbody><tr><td style="padding: 12px 16px; font-size: 17px; line-height: 1.4; font-weight: 500; vertical-align: top; border-bottom: 2px solid #1A1A1A">16:9</td><td style="padding: 12px 16px; font-size: 17px; line-height: 1.4; font-weight: 500; vertical-align: top; border-bottom: 2px solid #1A1A1A">Mêmes 4 couches. Le sujet passe d’un côté (à gauche), le soutien de l’autre ; les éléments de profondeur vont dans les coins opposés (bas-gauche, haut-droite).</td></tr>',1)
body=header('Planche F · règle de construction','F — La composition en 4 couches',"Chaque scène graphique se construit en 4 couches, de l’arrière vers l’avant. Montré ici sur deux de tes scènes : une touche sur fond blanc (D3) et un terminal sur fond noir (D4).")+lab('9:16 · Exemple 1 · un objet sur fond blanc')+f'<div style="display: flex; gap: 24px">{r1}</div>'+lab('9:16 · Exemple 2 · une interface sur fond noir')+f'<div style="display: flex; gap: 24px">{r2}</div>'+lab('16:9 · les deux exemples, en paysage')+r169+spec
page('K-F.dc.html','Composition',1480,2348,body,a.style()); boards['K-F.dc.html']=(1480,2348,'F — La composition en 4 couches')
json.dump(boards,open(f'{R}/boards-F.json','w'),ensure_ascii=False); print('ok')
