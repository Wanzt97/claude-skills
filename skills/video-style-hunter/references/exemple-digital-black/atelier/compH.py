import sys, json, html
src=open(__file__.replace('compH.py','compC2.py')).read().split('boards={}')[0]
exec(src)
boards={}
a=Anim('h_')
pc=lambda v: f'{100*v/CYCLE:.3f}%'
def plan_fx(filt,t=500,dur=400):
    n=a.n+1; a.n=n; nm=f'h_p{n}'
    a.css.append(f'@keyframes {nm}{{0%{{filter:none}}{pc(t)}{{filter:none;animation-timing-function:{EOUT}}}{pc(t+dur)}{{filter:{filt}}}{pc(EXIT)}{{filter:{filt};animation-timing-function:{EIN}}}{pc(EXIT+240)}{{filter:none}}100%{{filter:none}}}}')
    return f'<div style="position: absolute; inset: 0; animation: {nm} {CYCLE}ms linear infinite">{plan()}</div>'
def grande_carte(y,t):
    lig=''.join(f'<div style="height: 22px; width: {w}%; border-radius: 3px; background: #3a3a3a"></div>' for w in (90,70,84,56))
    return f'<div style="position: absolute; left: 60px; right: 60px; top: {y}px; height: 360px; box-sizing: border-box; border-radius: 6px; background: {FONTE}; border: 2px solid {ACIER}; overflow: hidden; {objet_kf(a,t)}"><div style="height: 64px; display: flex; align-items: center; gap: 12px; padding: 0 24px; border-bottom: 2px solid {ACIER}"><span style="width: 16px; height: 16px; border: 2px solid {BRUME}"></span><span style="width: 16px; height: 16px; border: 2px solid {BRUME}"></span><span style="width: 16px; height: 16px; background: {BRAISE}"></span><span style="margin-left: 14px; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 28px; letter-spacing: 0.08em; color: {BRUME}">SCRIPT.TXT</span></div><div style="padding: 32px 28px; display: flex; flex-direction: column; gap: 22px">{lig}</div></div>'
# Plan net dans les trois cas : seul le placement change
def puce(x,y,t,txt,icone):
    return f'<div style="position: absolute; left: {x}px; top: {y}px; display: flex; align-items: center; gap: 14px; padding: 16px 24px; border-radius: 6px; background: rgba(35,35,35,0.92); border: 2px solid {ACIER}; {objet_kf(a,t,scale=0.92)}"><span style="width: 18px; height: 18px; background: {icone}"></span><span style="font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 30px; letter-spacing: 0.06em; color: {OS}">{txt}</span></div>'
v1=apercu(plan()+carte_logiciel(a,260,150,560,380,300,'SCRIPT.TXT')+duo(a,'mon script','s’écrit',700,bas=1450,size=220),'H · V1 · Au-dessus de la tête')
autour=puce(60,640,300,'COUPES',BRAISE)+puce(700,560,420,'HOOKS',BRUME)+puce(720,1000,540,'B-ROLL',BRUME)
v2=apercu(plan()+autour+duo(a,'il fait','tout',900,bas=1450,size=220),'H · V2 · Autour de toi (3 éléments au plus)')
v3=apercu(plan()+grande_carte(1470,500)+duo(a,'mon script','s’écrit',700,bas=1440,size=200),'H · V3 · En bas de l’écran')
spec=tableau([
 ['Choix de Wanzt','A, plan net : quand une animation apparaît pendant que tu parles, ton plan ne change pas (ni assombri, ni flouté). Tu restes le sujet.'],
 ['V1 Au-dessus de la tête','Une carte, une fenêtre ou une icône dans l’espace au-dessus de ta tête, sans la toucher. C’est le placement par défaut.'],
 ['V2 Autour de toi','1 à 3 petits éléments (pastilles, widgets) posés autour de toi, à gauche et à droite, jamais sur le visage. Un seul en braise.'],
 ['V3 En bas de l’écran','Une carte large dans le bas de l’écran ; les sous-titres passent juste au-dessus, toujours sous ton menton. À éviter quand ton visage est bas dans le cadre.'],
 ['Mouvement','Les éléments arrivent un par un (montée 48 px ou échelle 0,92 → 1 + fondu, 400 ms, 120 ms d’écart) ; ils sortent avec le bloc de sous-titres (140 ms).'],
 ['Écartés','B (plan assombri et flouté) et C (plan juste assombri). Pas d’effet sur le décor ni sur toi.'],
],['Élément','Règle'])

# ---------- 16:9 ----------
EIO='cubic-bezier(0.65, 0, 0.35, 1)'
def kf_custom(debut,fin,t,dur,ease=EIO,sortie=240):
    n=a.n+1; a.n=n; nm=f'h_z{n}'
    a.css.append(f'@keyframes {nm}{{0%{{{debut}}}{pc(t)}{{{debut};animation-timing-function:{ease}}}{pc(t+dur)}{{{fin}}}{pc(EXIT)}{{{fin};animation-timing-function:{ease}}}{pc(EXIT+sortie)}{{{debut}}}100%{{{debut}}}}}')
    return f'animation: {nm} {CYCLE}ms linear infinite'
def plan169(style_anim,origin='857px 520px'):
    return f'<div style="position: absolute; inset: 0; background: {BG}"></div><div style="position: absolute; inset: 0; transform-origin: {origin}; {style_anim}"><img src="{F169}" alt="Ton plan face caméra" style="width: 1920px; height: 1080px; object-fit: cover; display: block"></div>'
def carte169(t):
    lig=''.join(f'<div style="height: 22px; width: {w}%; border-radius: 3px; background: #3a3a3a"></div>' for w in (90,70,84,56))
    return f'<div style="position: absolute; left: 560px; top: 250px; width: 800px; height: 520px; box-sizing: border-box; border-radius: 6px; background: {FONTE}; border: 2px solid {ACIER}; overflow: hidden; {objet_kf(a,t,scale=0.92)}"><div style="height: 64px; display: flex; align-items: center; gap: 12px; padding: 0 24px; border-bottom: 2px solid {ACIER}"><span style="width: 16px; height: 16px; border: 2px solid {BRUME}"></span><span style="width: 16px; height: 16px; border: 2px solid {BRUME}"></span><span style="width: 16px; height: 16px; background: {BRAISE}"></span><span style="margin-left: 14px; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 28px; letter-spacing: 0.08em; color: {BRUME}">SCRIPT.TXT</span></div><div style="padding: 36px 32px; display: flex; flex-direction: column; gap: 26px">{lig}</div></div>'
def zone(cote,t):
    # la zone du contenu n'est pas floutée : elle est juste noircie en dégradé vers le bord
    sens='to right' if cote=='gauche' else 'to left'
    return f'<div style="position: absolute; inset: 0; background: linear-gradient({sens}, rgba(10,10,10,0.85) 0%, rgba(10,10,10,0.62) 38%, rgba(10,10,10,0) 60%); {a.kf(t,400,EXIT,blur_in=0)}"></div>'
def texte169(x,t0,am,mc):
    m,t=mots(a,am,t0); k,_=lettres(a,mc,t+120)
    return f'<div style="position: absolute; left: {x}px; width: 760px; top: 360px; display: flex; flex-direction: column; align-items: flex-start; text-shadow: {HALO}"><div style="{AM}; font-size: 64px; color: {OS}">{m}</div><div style="{MC}; font-size: 190px; color: {BRAISE}; margin-top: 4px">{k}</div></div>'
# V4 : plan flouté, l'animation passe dessus, pas de sous-titres
w4=apercu(plan169(kf_custom('filter:none','filter:blur(16px) brightness(0.75)',300,400,EOUT))+carte169(600),'H · 16:9 · V4 · Plan flouté, animation dessus',W=1920,H=1080,sc=0.22)
# V5 : zoom sur toi à droite, la gauche floutée porte l'animation ou le texte
w5=apercu(plan169(kf_custom('transform:translateX(0px) scale(1)','transform:translateX(743px) scale(1.9)',300,600))+zone('gauche',800)+texte169(110,1100,'trois','étapes'),'H · 16:9 · V5 · Toi collé à droite, zone noircie à gauche',W=1920,H=1080,sc=0.22)
# V6 : zoom sur toi à gauche, la droite floutée porte l'animation ou le texte
w6=apercu(plan169(kf_custom('transform:translateX(0px) scale(1)','transform:translateX(-537px) scale(1.9)',300,600))+zone('droite',800)+texte169(1110,1100,'trois','étapes'),'H · 16:9 · V6 · Toi collé à gauche, zone noircie à droite',W=1920,H=1080,sc=0.22)
spec169=tableau([
 ['16:9 · V4 Plan flouté','Ton plan se floute (16 px, un peu assombri) en 400 ms et l’animation passe par-dessus, au centre. Pas de sous-titres pendant ce temps : l’animation parle. Le flou repart en 240 ms quand elle sort.'],
 ['16:9 · V5 Toi collé à droite','La caméra zoome sur toi (×1,9, 600 ms, ease-in-out) et te colle au bord droit de l’écran. Le côté gauche n’est pas flouté : il est noirci en dégradé (85 % au bord, 62 % au tiers, rien au milieu) pour faire ressortir l’animation ou le texte (amorce Inter + mot clé Doto).'],
 ['16:9 · V6 Toi collé à gauche','Même principe en miroir : tu es collé au bord gauche, le côté droit noirci porte l’animation ou le texte.'],
 ['Ordre','Le zoom d’abord, puis le noircissement (400 ms), puis le contenu. Retour : tout repart ensemble en 240 ms.'],
],['Élément','Règle'])
body=header('Planche H · fusionnée avec C2','H — Pendant que tu parles',"9:16 : ton plan reste net, l’animation se place au-dessus de ta tête, autour de toi ou en bas de l’écran. 16:9 : ton plan se floute, ou la caméra te colle à un bord et l’autre côté, noirci, porte l’animation.")+f'<div style="display: flex; gap: 40px">{v1}{v2}{v3}</div>'+spec+f'<div style="font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 15px; letter-spacing: 0.08em; text-transform: uppercase; color: {BRUME}; margin-top: 12px">16:9 · pendant que tu parles</div><div style="display: flex; gap: 40px">{w4}{w5}{w6}</div>'+spec169
page('K-H.dc.html','PendantQueTuParles',1480,2320,body,a.style()); boards['K-H.dc.html']=(1480,2320,'H — Pendant que tu parles · plan net')
json.dump(boards,open(f'{R}/boards-H.json','w'),ensure_ascii=False); print('ok')
