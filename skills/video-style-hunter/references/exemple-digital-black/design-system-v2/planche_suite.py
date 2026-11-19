# ---------- Planches D (+G), H (avec C2), B, F, E, I : exec dans gen3.py après planche_c.py ----------
D916='/_blob/6f714268be3a3597b08f404eb95c61d3'; D169='/_blob/4c0448b6b18c87bb4ec4020c2654b635'

# ---------------- jetons ajoutés ----------------
tokens['color']['tokens']+=[
 T("braise-claire","#ff8a55","Haut du dégradé de la touche braise (planche D). Jamais pour du texte."),
 T("touche-gris","#e4e4e4","Bas du dégradé de la touche claire (planche D)."),
 T("touche-bord","#bdbdbd","Bord bas de la touche claire (planche D)."),
 T("fonte-verre","rgba(35,35,35,0.92)","Fond des petites puces posées autour de toi sur la vidéo (planche H)."),
 T("voile-fort","rgba(10,10,10,0.85)","16:9, toi collé à un bord : le noircissement au bord de l’écran (planche H)."),
 T("voile-moyen","rgba(10,10,10,0.62)","16:9, toi collé à un bord : le noircissement au tiers de l’écran (planche H)."),
 T("trame","rgba(10,10,10,0.55)","Points de la trame sur une personne en noir et blanc (planche D2).")]
tokens['spacing']['tokens']+=[
 T("pression","14px","Planche D : course de la touche quand elle est pressée."),
 T("rotation-touche","-8deg","Planche D : inclinaison de toutes les touches."),
 T("montee-derriere","700px","Planche B : un texte, une image ou un logo qui sort de derrière toi part de 700 px plus bas."),
 T("zoom-serre","1.12","Planche B : plan serré dès la 1re image de l’accroche."),
 T("zoom-geste","1.16","Planche B : petit coup de zoom au moment de ton geste vers l’objectif."),
 T("zoom-recul","1.35","Planche B : départ du plan serré qui recule (zoom out vers ×1)."),
 T("zoom-avance","1.3","Planche B : arrivée du plan large qui avance (zoom in depuis ×1)."),
 T("zoom-bord","1.9","Planche H, 16:9 : zoom qui te colle au bord droit ou gauche."),
 T("derive","24px","Planche F : distance parcourue par un élément de profondeur sur toute la scène (20 à 30 px).")]
tokens['radius']['tokens']+=[
 T("radius-lg","12px","Seulement les cartes de tes plans (planche D2), avec leur bord blanc de 6 px."),
 T("radius-pastille","999px","Pastilles en forme de pilule (PLAN.md, EN DIRECT).")]
tokens['shadow']['tokens']+=[
 T("ombre-touche-clair","0 30px 60px rgba(18,18,18,0.22)","Ombre portée sous une touche ou un objet en volume sur fond blanc (planche D)."),
 T("ombre-touche-noir","0 30px 60px rgba(0,0,0,0.6)","Ombre portée sous une touche noire, ou un logo, sur fond noir (planches D et B)."),
 T("ombre-touche-braise","0 30px 60px rgba(0,0,0,0.5)","Ombre portée sous la touche braise (planche D).")]
tokens['shadow']['note']="Le halo sombre sur tout texte posé sur la vidéo ; l’ombre claire sous les objets posés sur un fond clair ; l’ombre portée des touches et objets en volume (planche D). Jamais d’ombre colorée ni décalée."
tokens['duration']['tokens']+=[
 T("dur-pression","120ms","Planche D : la touche descend quand elle est pressée."),
 T("dur-relache","220ms","Planche D : la touche remonte."),
 T("dur-signe","45ms","Planche B : écart entre deux signes d’un texte qui s’écrit à côté de toi."),
 T("dur-resserre","1200ms","Planche B : plan large qui se resserre lentement sur un objet du décor."),
 T("t-titre-accroche","300ms","Planche B : le titre-choc entre à 0,3 s, pendant ton geste."),
 T("t-sortie-accroche","1600ms","Planche B : le titre-choc sort à 1,6 s."),
 T("t-sous-titre-accroche","1700ms","Planche B : le 1er sous-titre arrive à 1,7 s, jamais en même temps que le titre.")]
tokens['blur']['tokens']+=[
 T("flou-plan","16px","Planche H, 16:9 : ton plan flouté (et assombri à 75 %) pendant qu’une animation passe dessus."),
 T("flou-profondeur","18px","Planche F : flou des éléments de profondeur (16 à 18 px).")]
w('tokens.json',json.dumps(tokens,ensure_ascii=False,indent=1))

# ---------------- bundle.css ajouté ----------------
EO='cubic-bezier(0.16, 1, 0.3, 1)'; EI='cubic-bezier(0.7, 0, 0.84, 0)'   # = ease-out / ease-in (dans les @keyframes, valeurs écrites en clair)
css_s=f'''
/* ===== Planche H (fusionnée avec C2) · pendant que tu parles ===== */
.ms-puce{{position:absolute;display:flex;align-items:center;gap:14px;padding:16px 24px;border-radius:var(--radius-md);background:var(--fonte-verre);border:var(--trait-objet) solid var(--acier);font-family:var(--font-mono);font-weight:600;font-size:30px;letter-spacing:0.06em;color:var(--os);animation:ms-pose var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}}
.ms-puce i{{width:18px;height:18px;background:var(--brume)}}
.ms-puce--braise i{{background:var(--braise)}}
.ms-plan-flou{{position:absolute;inset:0;animation:ms-plan-flou var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}}
.ms-plan-flou.ms-retour{{animation:ms-plan-flou var(--dur-objet) var(--ease-out) both,ms-plan-net var(--dur-bande-sortie) var(--ease-in) forwards;animation-delay:var(--t,0ms),var(--retour)}}
.ms-cadrage{{position:absolute;inset:0;transform-origin:var(--ox,50%) var(--oy,50%);animation:ms-cadrage var(--duree,var(--dur-lg)) var(--ease-in-out) both;animation-delay:var(--t,0ms)}}
.ms-cadrage.ms-retour{{animation:ms-cadrage var(--duree,var(--dur-lg)) var(--ease-in-out) both,ms-cadrage-retour var(--dur-bande-sortie) var(--ease-in-out) forwards;animation-delay:var(--t,0ms),var(--retour)}}
.ms-cadrage>img{{display:block;width:100%;height:100%;object-fit:cover}}
.ms-voile{{position:absolute;inset:0;animation:ms-apparition var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}}
.ms-voile--gauche{{background:linear-gradient(to right,var(--voile-fort) 0%,var(--voile-moyen) 38%,rgba(10,10,10,0) 60%)}}
.ms-voile--droite{{background:linear-gradient(to left,var(--voile-fort) 0%,var(--voile-moyen) 38%,rgba(10,10,10,0) 60%)}}
.ms-voile.ms-retour{{animation:ms-apparition var(--dur-objet) var(--ease-out) both,ms-deselection var(--dur-bande-sortie) var(--ease-in) forwards;animation-delay:var(--t,0ms),var(--retour)}}
@keyframes ms-plan-flou{{from{{filter:none}}to{{filter:blur(var(--flou-plan)) brightness(0.75)}}}}
@keyframes ms-plan-net{{from{{filter:blur(var(--flou-plan)) brightness(0.75)}}to{{filter:none}}}}
@keyframes ms-cadrage{{from{{transform:translate(var(--x0,0px),var(--y0,0px)) scale(var(--z0,1))}}to{{transform:translate(var(--x1,0px),var(--y1,0px)) scale(var(--z1,1))}}}}
@keyframes ms-cadrage-retour{{from{{transform:translate(var(--x1,0px),var(--y1,0px)) scale(var(--z1,1))}}to{{transform:translate(var(--x0,0px),var(--y0,0px)) scale(var(--z0,1))}}}}
/* ===== Planche D · types d’animation ===== */
.ms-phrase{{font-family:var(--font-text);font-weight:700;font-size:var(--fs,110px);line-height:1.05;letter-spacing:0;color:var(--os)}}
.ms-phrase--2{{color:var(--brume)}}
.ms-clair .ms-phrase{{color:var(--noir-digital)}}
.ms-clair .ms-phrase--2{{color:var(--encre-2)}}
.ms-touche{{position:absolute;width:var(--s);height:var(--s);border-radius:13%;background:linear-gradient(160deg,var(--blanc-carte) 0%,var(--touche-gris) 100%);box-shadow:inset 0 calc(var(--s) * -0.06) 0 var(--touche-bord),inset 0 2px 0 rgba(255,255,255,0.5),var(--ombre-touche-clair);transform:rotate(var(--rotation-touche));animation:ms-touche 1240ms linear both;animation-delay:var(--t,0ms)}}
.ms-touche--noir{{background:linear-gradient(160deg,var(--acier) 0%,var(--fonte) 100%);box-shadow:inset 0 calc(var(--s) * -0.06) 0 var(--abysse),inset 0 2px 0 rgba(255,255,255,0.5),var(--ombre-touche-noir)}}
.ms-touche--braise{{background:linear-gradient(160deg,var(--braise-claire) 0%,var(--braise) 100%);box-shadow:inset 0 calc(var(--s) * -0.06) 0 var(--braise-fonce),inset 0 2px 0 rgba(255,255,255,0.5),var(--ombre-touche-braise)}}
.ms-touche-label{{position:absolute;left:13%;top:11%;font-family:var(--font-text);font-weight:600;font-size:calc(var(--s) * 0.2);color:var(--noir-digital)}}
.ms-touche--noir .ms-touche-label{{color:var(--os)}}
.ms-touche--braise .ms-touche-label{{color:var(--abysse)}}
.ms-barres{{position:absolute;display:flex;align-items:flex-end;justify-content:space-between}}
.ms-barre{{border-radius:var(--radius-md) var(--radius-md) 0 0;background:var(--acier);transform-origin:50% 100%;animation:ms-barre var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}}
.ms-barre--braise{{background:var(--braise)}}
.ms-axe{{position:absolute;left:0;right:0;bottom:0;height:3px;background:var(--brume);animation:ms-apparition var(--dur-lettre) var(--ease-out) both;animation-delay:var(--t,0ms)}}
.ms-carte-plan{{position:absolute;border-radius:var(--radius-lg);overflow:hidden;border:6px solid var(--blanc-carte);box-shadow:var(--ombre-claire);transform:rotate(var(--r,0deg))}}
.ms-carte-plan img{{display:block;width:100%;height:100%;object-fit:cover;animation:ms-entree-objet var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}}
.ms-personne-nb{{position:absolute;inset:0;overflow:hidden;animation:ms-apparition var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}}
.ms-personne-nb img{{position:absolute;filter:grayscale(1) contrast(1.35) brightness(1.05)}}
.ms-trame{{position:absolute;background-image:radial-gradient(var(--trame) 1.6px,transparent 1.8px);background-size:7px 7px;mix-blend-mode:multiply;opacity:0.5}}
.ms-liste{{position:absolute;display:flex;flex-direction:column;gap:26px}}
.ms-liste-ligne{{display:flex;align-items:center;gap:22px;font-family:var(--font-mono);font-weight:600;font-size:38px;color:var(--os);animation:ms-apparition var(--dur-lettre) var(--ease-out) both;animation-delay:var(--t,0ms)}}
.ms-coche{{width:40px;height:40px;box-sizing:border-box;border-radius:var(--radius-md);border:3px solid var(--os);display:flex;align-items:center;justify-content:center}}
.ms-coche svg path{{fill:none;stroke:var(--os);stroke-width:3}}
.ms-rond{{position:absolute;width:260px;height:260px;border-radius:50%;background:var(--blanc-carte);box-shadow:var(--ombre-claire);display:flex;align-items:center;justify-content:center;animation:ms-pose var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}}
.ms-pastille{{position:absolute;padding:14px 26px;border-radius:var(--radius-pastille);background:var(--braise);font-family:var(--font-mono);font-weight:600;font-size:34px;color:var(--abysse);animation:ms-pose var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}}
.ms-lien{{position:absolute;left:0;top:0;animation:ms-apparition var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}}
.ms-lien path{{fill:none;stroke:var(--encre-2);stroke-width:4;stroke-dasharray:10 12}}
.ms-icone{{position:absolute;animation:ms-pose var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}}
.ms-icone .trait{{fill:none;stroke:var(--noir-digital);stroke-width:2.4;stroke-linejoin:round;stroke-linecap:round}}
.ms-icone .accent{{fill:var(--braise-fonce)}}
@keyframes ms-touche{{0%{{opacity:0;transform:translateY(-120px) rotate(var(--rotation-touche)) scale(0.9);animation-timing-function:{EO}}}32.26%{{opacity:1;transform:translateY(0) rotate(var(--rotation-touche)) scale(1)}}72.58%{{opacity:1;transform:translateY(0) rotate(var(--rotation-touche)) scale(1);animation-timing-function:{EI}}}82.26%{{opacity:1;transform:translateY(var(--pression)) rotate(var(--rotation-touche)) scale(0.97);animation-timing-function:{EO}}}100%{{opacity:1;transform:translateY(0) rotate(var(--rotation-touche)) scale(1)}}}}
@keyframes ms-barre{{from{{opacity:0;transform:scaleY(0)}}to{{opacity:1;transform:scaleY(1)}}}}
/* ===== Planche B · accroche ===== */
.ms-serre{{position:absolute;inset:0;overflow:hidden}}
.ms-serre>img{{display:block;width:100%;height:100%;object-fit:cover;transform-origin:var(--ox,50%) var(--oy,45%);transform:scale(var(--zoom-serre));animation:ms-geste 360ms linear both;animation-delay:var(--geste,200ms)}}
.ms-detour{{pointer-events:none}}
.ms-derriere{{position:absolute;animation:ms-derriere var(--dur-lg) var(--ease-out) both;animation-delay:var(--t,0ms)}}
.ms-derriere.ms-sortie{{animation:ms-derriere var(--dur-lg) var(--ease-out) both,ms-sortie var(--dur-sortie) var(--ease-in) forwards;animation-delay:var(--t,0ms),var(--sortie)}}
.ms-logo-rond{{border-radius:50%;background:var(--braise);display:flex;align-items:center;justify-content:center;box-shadow:var(--ombre-touche-noir)}}
.ms-logo-rond path{{fill:none;stroke:var(--abysse);stroke-width:2.4;stroke-linecap:round}}
.ms-signe{{animation:ms-apparition 30ms linear both;animation-delay:calc(var(--t,0ms) + var(--i,0) * var(--dur-signe))}}
.ms-curseur-texte{{display:inline-block;width:18px;height:0.7em;margin-left:10px;background:var(--braise);vertical-align:-0.06em;animation:ms-apparition 60ms linear both;animation-delay:var(--t,0ms)}}
.ms-repere{{position:absolute;padding:10px 18px;border-radius:var(--radius-sm);background:rgba(10,10,10,0.75);border:2px dashed var(--brume);font-family:var(--font-mono);font-weight:600;font-size:26px;letter-spacing:0.08em;color:var(--brume);animation:ms-repere 780ms linear both}}
@keyframes ms-geste{{0%{{transform:scale(var(--zoom-serre));animation-timing-function:{EO}}}33.3%{{transform:scale(var(--zoom-geste));animation-timing-function:{EO}}}100%{{transform:scale(var(--zoom-serre))}}}}
@keyframes ms-derriere{{from{{opacity:0;transform:translateY(var(--montee-derriere))}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes ms-repere{{0%{{opacity:0}}19%{{opacity:0}}35%{{opacity:1}}90%{{opacity:1}}100%{{opacity:0}}}}
/* ===== Planche F · composition en 4 couches ===== */
.ms-profondeur{{position:absolute;filter:blur(var(--flou-profondeur));opacity:0.85;animation:ms-derive var(--duree-scene,4000ms) linear both}}
.ms-profondeur .ms-touche{{animation:none;opacity:1}}
.ms-profondeur-carte{{position:absolute;border-radius:var(--radius-md);background:var(--fonte);border:var(--trait-objet) solid var(--acier);filter:blur(16px);opacity:0.8;animation:ms-derive var(--duree-scene,4000ms) linear both}}
.ms-fige *,.ms-fige *::before{{animation:none!important}}
.ms-couche{{position:absolute;left:24px;top:24px;padding:8px 14px;border-radius:var(--radius-sm);background:rgba(10,10,10,0.8);font-family:var(--font-mono);font-weight:600;font-size:34px;letter-spacing:0.08em;color:var(--os)}}
.ms-couche--4{{color:var(--braise)}}
@keyframes ms-derive{{from{{transform:translate(0,0)}}to{{transform:translate(var(--dx,24px),var(--dy,-16px))}}}}
'''
css+=css_s
w('components/bundle.css',css)

# ---------------- aides ----------------
def phrase(txt,t0,fs,cls=''):
    m,t=mots(txt,t0,150); return f'<span class="ms-phrase {cls}" style="--fs:{fs}px">{m}</span>',t
def doto(txt,t0,fs,braise=False,extra=''):
    txt=cap(txt)
    return f'<span class="ms-motcle{" ms-motcle--braise" if braise else ""}" style="--t:{t0}ms;font-size:{fs}px{extra}">{lettres(txt)}</span>',fin_lettres(txt,t0)
def bloc(inner,style,clair=False):
    return f'<div class="{"ms-clair" if clair else ""}" style="position:absolute;{style}">{inner}</div>'
def touche(label,x,y,s,kind,t):
    k='' if kind=='clair' else f' ms-touche--{kind}'
    return f'<div class="ms-touche{k}" style="left:{x}px;top:{y}px;--s:{s}px;--t:{t}ms"><span class="ms-touche-label">{label}</span></div>'
def selection_html(x,y,w_,h,t):
    hd=''.join(f'<span class="ms-poignee ms-poignee--{p}"></span>' for p in ('hg','hd','bg','bd'))
    return f'<div class="ms-selection" style="left:{x}px;top:{y}px;width:{w_}px;height:{h}px;box-sizing:border-box;--t:{t}ms">{hd}</div>'
def barres(x0,x1,top,h,hs,larg,t0):
    b=''.join(f'<div class="ms-barre{" ms-barre--braise" if i==len(hs)-1 else ""}" style="width:{larg}px;height:{v}px;--t:{t0+300+i*120}ms"></div>' for i,v in enumerate(hs))
    return f'<div class="ms-barres" style="left:{x0}px;right:{x1}px;top:{top}px;height:{h}px">{b}<div class="ms-axe" style="--t:{t0+200}ms"></div><div class="ms-pose" style="position:absolute;left:0;right:0;bottom:-56px;display:flex;justify-content:space-between;--t:{t0+900}ms"><span class="ms-legende">JAN</span><span class="ms-legende">MAI</span></div></div>'
def carte_plan(src,x,y,w_,h,r,t,pos='50% 40%'):
    return f'<div class="ms-carte-plan" style="left:{x}px;top:{y}px;width:{w_}px;height:{h}px;--r:{r}deg"><img src="{src}" alt="Ton plan" style="--t:{t}ms;object-position:{pos}"></div>'
def personne_nb(src,W,H,dx,t=0):
    m=f'-webkit-mask-image:url({src});mask-image:url({src});-webkit-mask-size:{W}px {H}px;mask-size:{W}px {H}px;-webkit-mask-position:{dx}px 0;mask-position:{dx}px 0;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat'
    return f'<div class="ms-personne-nb" style="--t:{t}ms"><img src="{src}" alt="Toi en noir et blanc, détouré" style="left:{dx}px;top:0;width:{W}px;height:{H}px"><div class="ms-trame" style="inset:0;{m}"></div></div>'
COCHE='<svg aria-hidden="true" width="26" height="26" viewBox="0 0 24 24"><path d="M5 12l5 5 9-10"></path></svg>'
ITEMS=['Coupes','Sous-titres','Accroches','B-roll','Musique','Export']
def liste(x,y,t0=600):
    l=''.join(f'<div class="ms-liste-ligne" style="--t:{t0+i*200}ms"><span class="ms-coche">{COCHE}</span>{s}</div>' for i,s in enumerate(ITEMS))
    return f'<div class="ms-liste" style="left:{x}px;top:{y}px">{l}</div>'
STAR='<svg aria-hidden="true" width="130" height="130" viewBox="0 0 24 24" class="ms-icone-in"><path d="M12 2v20M2 12h20M4.9 4.9l14.2 14.2M19.1 4.9L4.9 19.1" stroke="var(--noir-digital)" stroke-width="2.2" stroke-linecap="round"></path></svg>'
FILM='<svg aria-hidden="true" width="120" height="120" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="var(--noir-digital)" stroke-width="1.8"></rect><path d="M10 9l5 3-5 3z" fill="var(--noir-digital)"></path></svg>'
OEIL='<svg aria-hidden="true" width="420" height="420" viewBox="0 0 64 64"><path class="trait" d="M6 32 C 16 16, 48 16, 58 32 C 48 48, 16 48, 6 32 Z"></path><circle class="trait" cx="32" cy="32" r="10"></circle><circle class="accent" cx="32" cy="32" r="4.5"></circle></svg>'
def rond(x,y,t,inner): return f'<div class="ms-rond" style="left:{x}px;top:{y}px;--t:{t}ms">{inner}</div>'
def pastille(x,y,t,txt,fs=34,pad=''): return f'<div class="ms-pastille" style="left:{x}px;top:{y}px;--t:{t}ms;font-size:{fs}px{";padding:"+pad if pad else ""}">{txt}</div>'
def lien(W,H,d,t): return f'<svg class="ms-lien" aria-hidden="true" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="--t:{t}ms"><path d="{d}"></path></svg>'
def ap169(inner,leg,sc=0.3): return ap('169',inner,leg,sc=sc,plan=False)
def ap916(inner,leg,sc=0.25): return ap('916',inner,leg,sc=sc,plan=False)
def lab(t): return f'<div class="leg" style="padding:16px 24px 0;font-size:13px">{t}</div>'
def card(group,h,wd,sub,rows):
    return f'''<!-- @dsCard group="{group}" height={h} width={wd} subtitle="{sub}" -->
<!doctype html>
<html lang="fr"><head><meta charset="utf-8">{PREV_CSS}<style>.rang{{flex-wrap:wrap}}</style></head>
<body>{rows}{BOUCLE}</body></html>
'''
def rang(*v): return '<div class="rang">'+''.join(v)+'</div>'

# ================= Planche C4 : 16:9 ajouté =================
def carte_video169(x,y,w_,h,t): return f'<div class="ms-pose" style="position:absolute;left:{x}px;top:{y}px;width:{w_}px;height:{h}px;border-radius:6px;overflow:hidden;box-shadow:var(--ombre-claire);border:2px solid rgba(18,18,18,0.08);--t:{t}ms"><img src="{P169}" alt="" style="width:100%;height:100%;object-fit:cover"></div>'
a4,t4=mots('un seul objet,',300); k4,_=doto('du vide',t4+120,150,True)
p4=fond('169','sujet',True).replace('--sx:960px','--sx:620px').replace('--sy:600px','--sy:540px')+carte_video169(180,290,880,495,200)+bloc(f'<div class="ms-amorce" style="font-size:64px">{a4}</div>{k4}<span class="ms-legende ms-pose" style="--t:900ms;margin-top:24px">AUTOUR</span>','left:1140px;right:100px;top:360px;display:flex;flex-direction:column;align-items:flex-start;gap:8px',True)
a5,t5=mots('ça tourne',1200); k5,_=doto('seul',t5+120,200)
p5=fond('169','ambiance',False)+terminal(160,280,900,520,200)+f'<div class="ms-bloc ms-sortie" style="left:1120px;right:100px;top:400px;--sortie:3200ms"><div class="ms-amorce">{a5}</div>{k5}</div>'
prev=card('Types de scène',1040,1300,'Plein écran · rangée 1 : 9:16 (V1 blanc une idée, V2 noir un logiciel, V3 blanc un chiffre) · rangée 2 : 16:9 (V4 l’objet à gauche, V5 le terminal à gauche)',
 lab('9:16 · reels')+rang(ap('916',p1,'V1 · Blanc : une idée, un objet',plan=False),ap('916',p2,'V2 · Noir : un logiciel',plan=False),ap('916',p3,'V3 · Blanc : un chiffre',plan=False))+lab('16:9 · YouTube')+rang(ap169(p4,'16:9 · V4 · Blanc : l’objet à gauche, la phrase à droite'),ap169(p5,'16:9 · V5 · Noir : le terminal à gauche, la phrase à droite')))
w('components/SceneC4/preview.html',prev)
w('components/SceneC4/README.md','''# SceneC4 — Plein écran

On ne te voit plus : un **Fond** plein écran, un seul objet, beaucoup de vide autour. Pour le contenu de l’objet, voir les types d’animation (**AnimTexte**, **AnimPersonne**, **AnimObjet**, **AnimGraphique**) et la règle **Composition**.

**Ce que tu fournis :** l’objet (carte, icône, chiffre, terminal), la phrase et ses temps, noir ou blanc, le format.

- **Fond** : blanc pour une idée, noir pour un logiciel, un terminal, une interface. Grille gommée par défaut ; « sujet » quand l’objet est au centre ; grappes ou plan d’architecte pour changer de partie.
- **9:16** : UN objet au centre ; une phrase courte au-dessus ou en dessous (amorce + mot clé, planche A) ; une étiquette mono (`.ms-legende`) au plus.
- **16:9** : l’objet passe sur la gauche (environ la moitié de l’écran), la phrase à droite, alignée à gauche. Le vide reste autour des deux.
- **Couleurs sur fond blanc** (`.ms-clair`) : texte `noir-digital`, secondaire `encre-2`, mot clé en `noir-digital` ou `braise-fonce`. La `braise` seulement en aplat (case, pastille, poignée), jamais en texte. Ombre `ombre-claire` sous les objets.
- **Couleurs sur fond noir** : comme la planche A (`os`, `braise` pour l’unique accent, halo).

## Mouvement
Coupe franche vers le fond. L’objet arrive 200 ms après (`.ms-pose` : échelle 0,92 → 1 + fondu, `dur-objet`, `ease-out`) ; la phrase suit la voix (planche A). Sortie : coupe franche ou fondu `dur-sortie`.

## À éviter
Affiche chargée, capture d’écran entière, grille d’avatars, gros titre plaqué sur une capture, plusieurs objets qui se battent, aplat de couleur en fond.
''')

# ================= Planche C2 + H : pendant que tu parles =================
puces=f'<div class="ms-puce ms-puce--braise" style="left:60px;top:640px;--t:300ms"><i></i>COUPES</div><div class="ms-puce" style="left:700px;top:560px;--t:420ms"><i></i>HOOKS</div><div class="ms-puce" style="left:720px;top:1000px;--t:540ms"><i></i>B-ROLL</div>'
b4,_=duo2('il fait','tout',900,1450,size=220)
b5,_=duo2('mon script',"s’écrit",700,1440,size=200)
grande=carte(60,1470,960,360,500,'SCRIPT.TXT')
b6,_=duo2('mon script',"s’écrit",700,990,fmt='169',size=150)
q6=carte(1260,150,520,360,300,'SCRIPT.TXT')
q7=f'<div class="ms-plan-flou" style="--t:300ms">{plan_img("169")}</div>'+carte(560,250,800,520,600,'SCRIPT.TXT').replace('ms-carte"','ms-carte ms-pose"')
def bord(cote):
    x1='743px' if cote=='droite' else '-537px'
    a_,t_=mots('trois',1100); k_,_=doto('étapes',t_+120,190,True)
    tx=110 if cote=='droite' else 1110
    voile='gauche' if cote=='droite' else 'droite'
    return f'<div class="ms-cadrage" style="--t:300ms;--ox:857px;--oy:520px;--z1:var(--zoom-bord);--x1:{x1}">{plan_img("169")}</div><div class="ms-voile ms-voile--{voile}" style="--t:800ms"></div><div class="ms-bloc" style="left:{tx}px;width:760px;top:360px;align-items:flex-start;text-align:left;--sortie:3200ms"><div class="ms-amorce" style="font-size:64px">{a_}</div>{k_}</div>'
prev=card('Types de scène',1440,1600,'Sous-titres + petite animation, pendant que tu parles (planches C2 et H) · rangée 1 : 9:16, ton plan reste net · rangées 2 et 3 : 16:9',
 lab('9:16 · reels · ton plan reste net')+rang(ap('916',b1+etapes(900,1,1490),'V1 · Points d’étape',zone=Z916),ap('916',carte(90,260,560,380,300,'SCRIPT.TXT')+b2,'V2 · Fenêtre logiciel au-dessus de la tête',zone=Z916),ap('916',carte(430,240,560,380,300,'L’IDÉE',True)+b3,'V3 · Carte idée',zone=Z916),ap('916',puces+b4,'V4 · Autour de toi (3 au plus)',zone=Z916),ap('916',grande+b5,'V5 · En bas de l’écran',zone=Z916))
 +lab('16:9 · YouTube')+rang(ap('169',q6+b6,'16:9 · V6 · Fenêtre à côté de la tête',sc=0.3),ap169(q7,'16:9 · V7 · Plan flouté, animation dessus, sans sous-titres'))
 +rang(ap169(bord('droite'),'16:9 · V8 · Toi collé à droite, gauche noircie'),ap169(bord('gauche'),'16:9 · V9 · Toi collé à gauche, droite noircie')))
w('components/SceneC2/preview.html',prev)
w('components/SceneC2/README.md','''# SceneC2 — Pendant que tu parles (sous-titres + petite animation)

Planches C2 et H, fusionnées par Wanzt le 2026-11-07. Tu parles face caméra et une animation apparaît. Les sous-titres restent ceux de **SousTitreDuo**.

**Ce que tu fournis :** le plan face caméra, la position du visage, l’élément (étapes, logiciel, idée, puces) et son moment dans la phrase, le format.

## 9:16 : ton plan reste net
Choix de Wanzt : ton plan ne change pas (ni assombri, ni flouté). Tu restes le sujet. **Un seul** élément, ou 3 puces au plus.

| Variante | Classes | Détail |
|---|---|---|
| V1 Points d’étape | `.ms-etapes` > `.ms-etape` (+ `.ms-etape--active`), `.ms-etape-lien` | 3 cases de 64 px (trait 3 px `os`) reliées par un trait ; l’étape en cours en `braise` pleine, chiffre `abysse`. Sous le bloc de sous-titres. |
| V2 Fenêtre logiciel | `.ms-carte` > `.ms-carte-barre` (3 `<i>` + `.ms-carte-titre`), `.ms-carte-corps` > `.ms-carte-ligne` | carte `fonte`, trait `acier`, `radius-md`, barre mono avec 2 carrés creux + 1 carré braise. 560 × 380, **au-dessus de la tête** : le placement par défaut. |
| V3 Carte idée | `.ms-carte.ms-carte--claire` | la même carte en `blanc-carte`, avec `ombre-claire`. |
| V4 Autour de toi | `.ms-puce` (+ `.ms-puce--braise` pour une seule) | 1 à 3 petites puces (fond `fonte-verre`, carré + mot mono), à gauche et à droite de toi, jamais sur le visage. |
| V5 En bas de l’écran | `.ms-carte` large (960 × 360, y 1470) | les sous-titres passent juste au-dessus, toujours sous le menton (`--bas: 1440px`). À éviter quand ton visage est bas dans le cadre. |

## 16:9
| Variante | Classes | Détail |
|---|---|---|
| V6 Fenêtre à côté de la tête | `.ms-carte` (520 × 360) | plan net ; la carte se pose à côté de ta tête, du côté où il y a de la place ; le sous-titre reste sous le menton. |
| V7 Plan flouté | ton plan dans `.ms-plan-flou` (+ `.ms-retour` et `--retour`) | ton plan se floute (`flou-plan` 16 px, assombri à 75 %) en `dur-objet` ; l’animation passe dessus, au centre. **Pas de sous-titres** pendant ce temps : l’animation parle. Le flou repart en `dur-bande-sortie`. |
| V8 Toi collé à droite | ton plan dans `.ms-cadrage` (`--ox/--oy` = centre du visage, `--z1: var(--zoom-bord)`, `--x1` qui pousse le visage au bord) + `.ms-voile.ms-voile--gauche` | la caméra zoome (×1,9, `dur-lg`, `ease-in-out`) et te colle au bord droit. Le côté gauche **n’est pas flouté** : il est noirci en dégradé (`voile-fort` au bord, `voile-moyen` au tiers, rien au milieu) et porte l’animation ou le texte (amorce Arial + mot clé Anton, aligné à gauche). |
| V9 Toi collé à gauche | idem, `.ms-voile--droite` | en miroir. |

Réglage du zoom : `--x1` se calcule sur la vraie vidéo pour que le visage touche presque le bord (plan test : 743 px vers la droite, −537 px vers la gauche, visage en x 857, y 520). Ordre : le zoom, puis le noircissement (+500 ms), puis le contenu. Retour : tout repart ensemble en `dur-bande-sortie` (`.ms-retour` + `--retour`).

## Mouvement
| Élément | Entrée | Sortie |
|---|---|---|
| Carte | montée de `montee-objet` (48 px) + fondu, `dur-objet`, `ease-out`, à `--t` | avec le bloc de sous-titres |
| Étape, puce | échelle 0,6 / 0,92 → 1 + fondu, 120 ms d’écart | avec le bloc |

Aucun effet sur le décor ni sur le visage. Écartés : plan assombri ou flouté en 9:16.
''')

# ================= Planche D : AnimTexte =================
def anim_texte():
    l1,t=phrase('le montage',200,120); l2,t=phrase('prend',t,120); k,_=doto('1 heure',t+120,190,True,';margin-top:18px')
    v1=fond('916','ambiance',True)+bloc(l1+l2+k,'left:90px;right:90px;top:640px;display:flex;flex-direction:column;gap:12px',True)
    l1,t=phrase('tu n’as pas besoin de',200,64); k,tk=doto('temps',t+120,230,False,';padding:4px 22px')
    l3,_=phrase('tu as besoin d’un plan.',tk+600,64,'ms-phrase--2')
    v2=fond('916','ambiance',False)+bloc(l1+k,'left:90px;right:90px;top:700px;display:flex;flex-direction:column;gap:26px;align-items:flex-start')+selection_html(90,792,700,240,tk+120)+bloc(l3,'left:90px;top:1100px')
    l1,t=phrase('tout est sous',700,96); k,_=doto('contrôle',t+120,170)
    v3=fond('916','ambiance',True)+touche('Ctrl',350,420,380,'clair',0)+bloc(l1+k,'left:70px;right:70px;top:1060px;display:flex;flex-direction:column;align-items:center;gap:16px;text-align:center',True)
    l1,t=phrase('tes vues ont',200,96); k,tk=doto('doublé',t+120,200)
    v4=fond('916','ambiance',False)+bloc(l1+k,'left:70px;right:70px;top:560px;display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center')+barres(140,140,1000,440,[150,210,190,290,420],96,tk)
    l1,t=phrase('le montage prend',200,120); k,_=doto('1 heure',t+120,260,True)
    w5=fond('169','ambiance',True)+bloc(l1+k,'left:160px;right:160px;top:330px;display:flex;flex-direction:column;gap:24px',True)
    l1,t=phrase('tes vues ont',200,96); k,tk=doto('doublé',t+120,200)
    w6=fond('169','ambiance',False)+bloc(l1+k,'left:160px;top:330px;display:flex;flex-direction:column;gap:10px')+barres(1060,160,240,480,[150,210,190,290,420],110,tk)
    l1,t=phrase('tout est sous',700,96); k,_=doto('contrôle',t+120,170)
    w7=fond('169','ambiance',True)+touche('Ctrl',260,300,440,'clair',0)+bloc(l1+k,'left:900px;right:100px;top:380px;display:flex;flex-direction:column;gap:16px',True)
    return card('Types d’animation',940,1360,'D1 · Centrée sur le texte · rangée 1 : 9:16 (V1 phrase + mot Anton, V2 mot dans le cadre de sélection, V3 texte + objet d’appui, V4 texte puis graphique) · rangée 2 : 16:9 (V5, V6, V7)',
     lab('9:16 · reels')+rang(ap916(v1,'V1 · Blanc : phrase énorme + mot Anton'),ap916(v2,'V2 · Noir : mot dans le cadre de sélection'),ap916(v3,'V3 · Blanc : texte + objet d’appui'),ap916(v4,'V4 · Noir : texte, puis un graphique'))
     +lab('16:9 · YouTube')+rang(ap169(w5,'16:9 · V5 · Phrase alignée à gauche',sc=0.2),ap169(w6,'16:9 · V6 · Texte à gauche, graphique à droite',sc=0.2),ap169(w7,'16:9 · V7 · Objet à gauche, texte à droite',sc=0.2)))
w('components/AnimTexte/preview.html',anim_texte())
w('components/AnimTexte/README.md','''# AnimTexte — D1, centrée sur le texte

Le texte est la star : 3 à 6 mots énormes, **un** mot mis en valeur, au plus un objet d’appui, beaucoup de vide. Se pose sur un **Fond** (scène plein écran **SceneC4**, ou bande / panneau de **SceneC3**).

**Ce que tu fournis :** la phrase, le mot à mettre en valeur, les temps de la voix, noir ou blanc, le format.

| Élément | Classes | Règle |
|---|---|---|
| Phrase | `.ms-phrase` (`--fs` : 96 à 120 px), un `.ms-mot` par mot ; `.ms-phrase--2` pour une phrase secondaire | Arial 700 (style `phrase`, 110 px en 9:16), approche 0. `os` sur noir, `noir-digital` sur blanc (`.ms-clair`). |
| Mot mis en valeur (un seul) | `.ms-motcle` (170 à 260 px) avec `.ms-lettre` | Anton : **jamais de serif ni d’italique** (l’italique serif des inspirations est remplacé par Anton, décision de Wanzt). Soit plus grand en Anton, soit en braise (`braise-fonce` sur blanc), soit dans le cadre de sélection (`.ms-selection` + 4 `.ms-poignee`). Une seule de ces trois mises en valeur. |
| Objet d’appui (V3) | `.ms-touche` (voir **AnimObjet**) | arrive en premier. |
| Graphique (V4, V6) | `.ms-barres` > `.ms-barre` (+ `.ms-barre--braise` pour la dernière), `.ms-axe`, `.ms-legende` | la phrase au milieu ; dès qu’elle est dite, 5 barres montent une à une sous elle (en 16:9 : à côté). Le graphique appuie le texte, il ne le remplace pas. |

## 9:16 et 16:9
- 9:16 : la phrase sur 2 ou 3 lignes, au centre ou alignée à gauche ; l’objet au-dessus ou le graphique en dessous.
- 16:9 : la phrase sur une ou deux lignes, alignée à gauche, avec du vide à droite ; l’objet ou le graphique **à côté** du texte, pas en dessous.

## Mouvement
Mots un par un au rythme de la voix (`dur-mot`, fondu + flou), le mot Anton lettre par lettre (`dur-lettre`, `dur-char`), le cadre 120 ms après sa dernière lettre (`dur-lettre`). L’objet d’appui arrive en premier. Barres : `.ms-barre` (échelle verticale 0 → 1 + fondu, `dur-objet`), 120 ms d’écart, la dernière en braise. Sortie : tout d’un coup, `dur-sortie`.

## Fond
Blanc os ou noir du pack (**Fond**). Jamais d’aplat de couleur (décision de Wanzt).
''')

# ================= Planche D : AnimPersonne =================
def anim_personne():
    l1,t=phrase('3 vidéos',900,96); k,_=doto('gagnantes',t+120,150,True)
    v1=fond('916','ambiance',True)+carte_plan(P916,110,260,400,620,-6,200)+carte_plan(P916,560,420,400,620,5,320)+bloc(l1+k,'left:80px;right:80px;top:1240px;display:flex;flex-direction:column;gap:10px',True)
    l1,t=phrase('ce qui',300,110); l2,t=phrase('change',t,110); k,_=doto('tout',t+120,220,True)
    v2=fond('916','ambiance',False)+personne_nb(D916,1080,1920,300)+bloc(l1+l2+k,'left:70px;top:300px;display:flex;flex-direction:column;gap:6px;text-shadow:var(--halo-sombre)')
    l1,t=phrase('3 vidéos',900,96); k,_=doto('gagnantes',t+120,150,True)
    w3=fond('169','ambiance',True)+carte_plan(P169,140,200,520,292,-5,200,'50% 50%')+carte_plan(P169,700,280,520,292,3,320,'50% 50%')+carte_plan(P169,1260,210,520,292,-2,440,'50% 50%')+bloc(l1+k,'left:0;right:0;top:700px;display:flex;align-items:baseline;justify-content:center;gap:28px',True)
    l1,t=phrase('ce qui',300,110); l2,t=phrase('change',t,110); k,_=doto('tout',t+120,220,True)
    w4=fond('169','ambiance',False)+personne_nb(D169,1920,1080,450)+bloc(l1+l2+k,'left:160px;top:260px;display:flex;flex-direction:column;gap:6px;text-shadow:var(--halo-sombre)')
    return card('Types d’animation',1040,1300,'D2 · Centrée sur une personne · rangée 1 : 9:16 (V1 tes plans en cartes, V2 toi en noir et blanc) · rangée 2 : 16:9 (V3, V4)',
     lab('9:16 · reels')+rang(ap916(v1,'V1 · Blanc : tes plans posés en cartes'),ap916(v2,'V2 · Noir : toi en noir et blanc, titre à côté'))
     +lab('16:9 · YouTube')+rang(ap169(w3,'16:9 · V3 · Tes plans en cartes, en ligne'),ap169(w4,'16:9 · V4 · Toi à droite, titre à gauche')))
w('components/AnimPersonne/preview.html',anim_personne())
w('components/AnimPersonne/README.md','''# AnimPersonne — D2, centrée sur une personne

La personne porte l’idée ; le titre est à côté, jamais sur le visage.

**Ce que tu fournis :** tes plans (ou ton détourage), le titre et ses temps, noir ou blanc, le format.

| Variante | Classes | Règle |
|---|---|---|
| V1 / V3 Tes plans en cartes | `.ms-carte-plan` (`--r` : rotation, `--t`) > `img` | sur fond blanc os : 1 à 3 cartes de tes plans, bord `blanc-carte` 6 px, `radius-lg` (12 px, réservé à ces cartes), légère rotation (−6° à +5°), `ombre-claire`. Texte dessous ou à côté. En 16:9 : 3 cartes en ligne, le texte dessous sur une ligne. |
| V2 / V4 Toi en noir et blanc | `.ms-personne-nb` > `img` (ton **détourage**) + `.ms-trame` (masquée par le même détourage) | sur fond noir : toi (ou une statue, une photo) en noir et blanc contrasté avec une trame de points légère (`trame`). Titre de l’autre côté avec le halo sombre, mot fort en Anton braise. En 9:16 : toi décalé à droite, titre en haut à gauche. En 16:9 : toi à droite, titre à gauche. |

Détourage : `npx hyperframes remove-background <image> -o <sortie.png>` (assets **Fonds** : `detour-916.png`, `detour-169.png` pour le plan test).

## Mouvement
Les cartes montent de `montee-objet` + fondu (`dur-objet`), 120 ms d’écart ; la personne apparaît en fondu (`dur-objet`) ; le texte suit la voix (planche A).

## À éviter
Texte sur le visage, couleurs vives sur la personne, plus de 3 cartes.
''')

# ================= Planche D : AnimObjet =================
def anim_objet():
    l1,t=phrase('appuie sur',1300,96); k,_=doto('Échap',t+120,200)
    v1=fond('916','ambiance',False)+touche('Esc',300,520,480,'braise',200)+bloc(l1+k,'left:70px;right:70px;top:1220px;display:flex;flex-direction:column;align-items:center;gap:14px;text-shadow:var(--halo-sombre)')
    l1,t=phrase('ce que ton',700,90); k,_=doto('œil voit',t+120,190)
    v2=fond('916','sujet',True)+f'<div class="ms-icone ms-clair" style="left:330px;top:460px;--t:200ms">{OEIL}</div>'+bloc(l1+k,'left:70px;right:70px;top:1060px;display:flex;flex-direction:column;align-items:center;gap:14px',True)
    l1,t=phrase('garde le',1300,96); k,_=doto('contrôle',t+120,170,True)
    v3=fond('916','ambiance',True)+touche('Ctrl',300,520,480,'clair',200)+bloc(l1+k,'left:70px;right:70px;top:1220px;display:flex;flex-direction:column;align-items:center;gap:14px',True)
    l1,t=phrase('appuie sur',1300,96); k,_=doto('Échap',t+120,200)
    w4=fond('169','ambiance',False)+touche('Esc',300,280,460,'braise',200)+bloc(l1+k,'left:980px;right:100px;top:380px;display:flex;flex-direction:column;gap:14px;text-shadow:var(--halo-sombre)')
    l1,t=phrase('garde le',1300,96); k,_=doto('contrôle',t+120,170,True)
    w5=fond('169','ambiance',True)+touche('Ctrl',1180,280,460,'clair',200)+bloc(l1+k,'left:160px;right:860px;top:380px;display:flex;flex-direction:column;gap:14px',True)
    return card('Types d’animation',1040,1300,'D3 · Centrée sur un objet · rangée 1 : 9:16 (V1 touche braise sur noir, V2 icône au trait, V3 touche claire) · rangée 2 : 16:9 (V4, V5)',
     lab('9:16 · reels')+rang(ap916(v1,'V1 · Noir : une touche braise'),ap916(v2,'V2 · Blanc : une icône au trait'),ap916(v3,'V3 · Blanc : une touche claire'))
     +lab('16:9 · YouTube')+rang(ap169(w4,'16:9 · V4 · La touche braise à gauche'),ap169(w5,'16:9 · V5 · La touche à droite')))
w('components/AnimObjet/preview.html',anim_objet())
w('components/AnimObjet/README.md','''# AnimObjet — D3, centrée sur un objet

UN objet héros, en volume, net, avec beaucoup de vide ; un titre court l’explique. Jamais plusieurs objets qui se battent.

**Ce que tu fournis :** l’objet, le titre et ses temps, noir ou blanc, le format.

## Objets
- **Touches de clavier** (Ctrl, Esc, Shift, Entrée…) : ton motif de signature. `.ms-touche` (`--s` : côté, 380 à 480 px ; `--t`) > `.ms-touche-label`. Carré arrondi (13 % du côté), face en dégradé doux, bord bas plus sombre (6 % du côté), ombre portée, inclinaison `rotation-touche` (−8°).
  - `.ms-touche` : claire (`blanc-carte` → `touche-gris`, bord `touche-bord`, `ombre-touche-clair`) sur fond blanc.
  - `.ms-touche--noir` : noire (`acier` → `fonte`, `ombre-touche-noir`) sur fond noir.
  - `.ms-touche--braise` : l’accent (`braise-claire` → `braise`, bord `braise-fonce`), **une seule à l’écran** ; le titre reste alors en `os`.
- **Icônes au trait** : `.ms-icone` > svg avec `.trait` (2,4, `noir-digital`) et un détail `.accent` (`braise-fonce`). Un œil, une clé, un feu…
- L’aplat de couleur des inspirations est remplacé par la touche braise sur fond noir (décision de Wanzt : fonds noir ou blanc os seulement).

## 9:16 et 16:9
- 9:16 : l’objet au centre, le titre dessous, centré.
- 16:9 : l’objet d’un côté (environ un tiers de l’écran), le titre de l’autre, aligné à gauche.

## Mouvement
La touche tombe et se pose (`dur-objet`, `ease-out`), puis est pressée une fois : elle descend de `pression` (14 px) en `dur-pression`, remonte en `dur-relache` (classe `.ms-touche`, 1 240 ms en tout). Le titre arrive après la pression, au rythme de la voix. L’icône : `.ms-pose`.
''')

# ================= Planche D : AnimGraphique =================
def anim_graphique():
    k,_=doto('6/6',200,200,True); a_,_=mots('faits par Claude.',500)
    v1=fond('916','ambiance',False)+bloc(f'{k}<span class="ms-phrase" style="--fs:54px">{a_}</span>','left:110px;top:330px;display:flex;flex-direction:column;gap:30px')+liste(110,880)
    labs='<div class="ms-clair" style="position:absolute;left:0;right:0;top:560px;display:flex;justify-content:space-between;padding:0 110px"><span class="ms-legende" style="font-size:30px">SCRIPT</span><span class="ms-legende" style="font-size:30px">MONTAGE</span></div>'
    l1,t=phrase('du script au',1100,96); k,_=doto('montage',t+120,170)
    v2=fond('916','ambiance',True)+labs+rond(170,690,200,STAR)+rond(650,690,320,FILM)+lien(1080,1920,'M300 820 C 420 700, 660 700, 780 820',500)+pastille(430,690,800,'PLAN.md')+bloc(l1+k,'left:70px;right:70px;top:1180px;display:flex;flex-direction:column;align-items:center;gap:14px',True)
    q,_=mots('il fait tout seul',1200)
    v3=fond('916','ambiance',False)+terminal(100,640,880,520,200)+f'<div class="ms-bloc ms-bloc--916" style="top:1260px;bottom:auto;--sortie:3200ms"><div class="ms-amorce">{q}</div></div>'
    k,_=doto('6/6',200,240,True); a_,_=mots('faits par Claude.',500)
    w4=fond('169','ambiance',False)+bloc(f'{k}<span class="ms-phrase" style="--fs:54px">{a_}</span>','left:180px;top:330px;display:flex;flex-direction:column;gap:24px')+liste(1080,230)
    labs='<div class="ms-clair" style="position:absolute;left:460px;width:1000px;top:220px;display:flex;justify-content:space-between"><span class="ms-legende" style="font-size:30px;width:260px;text-align:center">SCRIPT</span><span class="ms-legende" style="font-size:30px;width:260px;text-align:center">MONTAGE</span></div>'
    l1,t=phrase('du script au',1100,96); k,_=doto('montage',t+120,170)
    w5=fond('169','ambiance',True)+labs+rond(460,300,200,STAR)+rond(1200,300,320,FILM)+lien(1920,1080,'M720 430 C 860 300, 1060 300, 1200 430',500)+pastille(840,300,800,'PLAN.md')+bloc(l1+k,'left:0;right:0;top:690px;display:flex;align-items:baseline;justify-content:center;gap:28px',True)
    return card('Types d’animation',1040,1300,'D4 · Centrée sur un graphique · rangée 1 : 9:16 (V1 checklist, V2 schéma, V3 terminal) · rangée 2 : 16:9 (V4, V5 ; terminal 16:9 : SceneC4 V5)',
     lab('9:16 · reels')+rang(ap916(v1,'V1 · Noir : checklist qui se coche'),ap916(v2,'V2 · Blanc : schéma, deux éléments reliés'),ap916(v3,'V3 · Noir : terminal propre'))
     +lab('16:9 · YouTube')+rang(ap169(w4,'16:9 · V4 · Le chiffre à gauche, la liste à droite'),ap169(w5,'16:9 · V5 · Le schéma en largeur')))
w('components/AnimGraphique/preview.html',anim_graphique())
w('components/AnimGraphique/README.md','''# AnimGraphique — D4, centrée sur un graphique

Une interface qui fait comprendre en un coup d’œil. Peu de texte : les chiffres et l’interface parlent.

**Ce que tu fournis :** le contenu (liste, deux éléments à relier, lignes de terminal), les temps, noir ou blanc, le format.

| Variante | Classes | Règle |
|---|---|---|
| V1 / V4 Checklist | `.ms-motcle.ms-motcle--braise` (le chiffre), `.ms-phrase`, `.ms-liste` > `.ms-liste-ligne` (+ `.ms-coche` avec sa coche svg) | sur fond noir : un chiffre en Anton braise (6/6), une phrase courte, puis une liste mono (38 px) dont chaque ligne se coche. Seul le chiffre est en braise. En 16:9 : le chiffre à gauche, la liste à droite. |
| V2 / V5 Schéma | `.ms-rond` (×2, svg au trait dedans), `.ms-lien` (chemin pointillé `encre-2`), `.ms-pastille` (`radius-pastille`), `.ms-legende` | sur fond blanc : deux ronds `blanc-carte` (`ombre-claire`) reliés par un pointillé, une pastille braise au milieu (mono, `abysse`) : le seul élément braise. En 16:9 : le schéma s’étale en largeur, la phrase dessous sur une ligne. |
| V3 Terminal | `.ms-terminal` > `.ms-terminal-ligne` (+ `--braise` pour la ligne en cours) | sur fond noir : fenêtre `fonte`, trait `acier`, mono 30 px. En 16:9 : voir **SceneC4** V5. |

## Mouvement
Les éléments arrivent un par un (`.ms-pose` : échelle 0,92 → 1 + fondu, `dur-objet`) ; les lignes de liste ou de terminal toutes les 200 ms (`dur-lettre`) ; le pointillé après ses deux bouts, la pastille en dernier.
''')

# ================= Planche B : Accroche =================
def serre(src,ox,oy,geste=200):
    return f'<div class="ms-serre" style="--ox:{ox};--oy:{oy};--geste:{geste}ms"><img src="{src}" alt="Ton plan face caméra"></div>'
def repere(x,y): return f'<div class="ms-repere" style="left:{x}px;top:{y}px">ICI : TA MAIN VERS L’OBJECTIF</div>'
def titre_sel(txt,L,T,W_,H_,fs):
    return f'<div class="ms-titre ms-sortie" style="left:{L}px;top:{T}px;width:{W_}px;height:{H_}px;display:flex;align-items:center;justify-content:center;font-size:{fs}px;--sortie:1600ms"><span style="--t:300ms;display:inline-block">{lettres(txt)}</span></div>'+selection_html(L,T,W_,H_,fin_lettres(txt,300)+120).replace('class="ms-selection"','class="ms-selection ms-sortie" ').replace('--t:','--sortie:1600ms;--t:')
def chiffre_amorce(ch,l1,l2,L,T,fs,am):
    a1,t=mots(l1,600,140); a2,_=mots(l2,t,140)
    return f'<div class="ms-bloc ms-sortie" style="left:{L}px;top:{T}px;flex-direction:row;align-items:center;gap:28px;text-align:left;--sortie:1600ms"><span class="ms-motcle ms-motcle--braise" style="--t:300ms;font-size:{fs}px;line-height:0.8">{lettres(ch)}</span><span style="display:flex;flex-direction:column"><span class="ms-amorce" style="font-size:{am}px">{a1}</span><span class="ms-amorce" style="font-size:{am}px">{a2}</span></span></div>'
def camera(src,z0,z1,ox,oy,alt='Ton plan face caméra',extra=''):
    return f'<div class="ms-cadrage{extra}" style="--ox:{ox};--oy:{oy};--z0:{z0};--z1:{z1};--t:0ms"><img src="{src}" alt="{alt}"></div>'
def derriere(fmt,z0,z1,element,sous):
    P,D,ox,oy=(P916,D916,'440px','925px') if fmt=='916' else (P169,D169,'857px','520px')
    return camera(P,z0,z1,ox,oy)+element+camera(D,z0,z1,ox,oy,'Toi détouré, devant l’élément',' ms-detour')+sous
MONTAGE=lambda fs: f'<span class="ms-motcle" style="font-size:{fs}px;line-height:0.85;text-shadow:none">MONTAGE</span>'
LOGO=lambda d: f'<div class="ms-logo-rond" style="width:{d}px;height:{d}px"><svg aria-hidden="true" width="{int(d*0.5)}" height="{int(d*0.5)}" viewBox="0 0 24 24"><path d="M12 2v20M2 12h20M4.9 4.9l14.2 14.2M19.1 4.9L4.9 19.1"></path></svg></div>'
def sort_derriere(inner,L,T): return f'<div class="ms-derriere ms-sortie" style="left:{L}px;top:{T}px;--t:300ms;--sortie:1600ms">{inner}</div>'
def vers_objet(src,ox,oy,zs,tx,ty): return f'<div class="ms-cadrage" style="--ox:{ox}px;--oy:{oy}px;--z1:{zs};--x1:{tx}px;--y1:{ty}px;--t:300ms;--duree:var(--dur-resserre)"><img src="{src}" alt="Ton plan, qui se resserre sur un objet"></div>'
def signes(txt,t0):
    return ''.join(f'<span class="ms-signe" style="--t:{t0}ms;--i:{i}">{html.escape(c) if c!=" " else "&nbsp;"}</span>' for i,c in enumerate(txt)), t0+len(txt)*45
def accroche():
    s1,_=duo2('qui tuent ton','montage',1700,1450,size=200)
    v1=serre(P916,'50%','45%')+repere(240,1180)+titre_sel('3 erreurs',110,300,860,250,190)+s1
    s2,_=duo2('et la première','coûte',1700,1450,size=200)
    v2=serre(P916,'50%','45%')+repere(240,560)+chiffre_amorce('3','erreurs qui','tuent ton montage',90,1190,360,52)+s2
    s3,_=duo2('monte tes vidéos','plus vite',1700,1450,size=200)
    v3=derriere('916','var(--zoom-recul)',1,sort_derriere(MONTAGE(260),30,640),s3)
    s4,_=duo2('avec un seul','outil',1700,1450,size=200)
    v4=derriere('916',1,'var(--zoom-avance)',sort_derriere(LOGO(560),260,330),s4)
    s5,_=duo2('tout est parti de','ce livre',1500,1450,size=200)
    v5=vers_objet(P916,905,555,2.6,-280,205)+s5
    t6,_=duo2('qui tuent ton','montage',1700,960,fmt='169')
    w6=serre(P169,'45%','45%')+repere(1180,150)+chiffre_amorce('3','erreurs qui','tuent ton montage',1120,330,300,44)+t6
    t7,_=duo2('monte tes vidéos','vite',1700,960,fmt='169')
    w7=derriere('169','var(--zoom-recul)',1,sort_derriere(MONTAGE(340),290,300),t7)
    t8,_=duo2('avec un seul','outil',1700,960,fmt='169')
    w8=derriere('169',1,'var(--zoom-avance)',sort_derriere(LOGO(520),600,120),t8)
    e1,t=signes('le montage le plus',400); e2,t2=signes('rapide',t+80)
    w9=serre(P169,'45%','45%')+f'<div class="ms-bloc ms-sortie" style="left:1120px;top:300px;width:760px;align-items:flex-start;text-align:left;--sortie:3200ms"><div class="ms-amorce" style="font-size:60px">{e1}</div><div class="ms-motcle" style="font-size:170px;margin-top:8px">{e2}<span class="ms-curseur-texte" style="--t:{t2}ms"></span></div></div>'
    a_,t=mots('tout est parti de',1500); k_,_=doto('ce livre',t+120,180)
    w10=vers_objet(P169,1125,310,3.0,175,230)+f'<div class="ms-bloc" style="left:110px;top:380px;align-items:flex-start;text-align:left;--sortie:3200ms"><div class="ms-amorce" style="font-size:56px">{a_}</div>{k_}</div>'
    return card('Accroche',1340,1580,'Les 3 premières secondes · rangée 1 : 9:16 (V1 sélection au-dessus de la tête, V2 chiffre + amorce, V3 serré → recul + texte derrière toi, V4 large → avance + logo derrière toi, V5 resserré sur un objet) · rangées 2 et 3 : 16:9 (V6 à V10)',
     lab('9:16 · reels')+rang(ap916(v1,'V1 · Sélection au-dessus'),ap916(v2,'V2 · Chiffre + amorce'),ap916(v3,'V3 · Recul, texte derrière'),ap916(v4,'V4 · Avance, logo derrière'),ap916(v5,'V5 · Resserré sur un objet'))
     +lab('16:9 · YouTube')+rang(ap169(w6,'16:9 · V6 · Titre à côté du visage',sc=0.25),ap169(w7,'16:9 · V7 · Serré → recul, texte derrière toi',sc=0.25),ap169(w8,'16:9 · V8 · Large → avance, logo derrière toi',sc=0.25))
     +rang(ap169(w9,'16:9 · V9 · Texte qui s’écrit à côté de toi',sc=0.25),ap169(w10,'16:9 · V10 · Resserré sur un objet du décor',sc=0.25)))
w('components/Accroche/preview.html',accroche())
w('components/Accroche/README.md','''# Accroche — les 3 premières secondes (planche B)

Tu es déjà là, tu parles à la caméra et tu tends la main vers l’objectif. On ouvre en plan serré qui recule, ou en plan large qui avance. Le titre arrive pendant le geste (en sélection, en chiffre, derrière toi ou à côté), puis le premier sous-titre.

**Ce que tu fournis :** le plan d’ouverture (avec ton geste filmé), ton détourage si un élément passe derrière toi, le titre, le format.

## Le minutage (jetons)
| Instant | Ce qui se passe |
|---|---|
| 0 s | plan serré dès la 1re image (`.ms-serre`, ×`zoom-serre`) — ou départ du recul / de l’avance (`.ms-cadrage`) |
| 0,2 s | ton geste vers l’objectif : petit coup de zoom (×`zoom-geste` en 120 ms, retour en 240 ms ; `--geste` = l’instant du geste) |
| 0,3 s (`t-titre-accroche`) | le titre arrive (**TitreChoc**, ou un élément derrière toi) |
| 1,6 s (`t-sortie-accroche`) | le titre sort (`.ms-sortie`, `--sortie: 1600ms`) |
| 1,7 s (`t-sous-titre-accroche`) | le 1er **SousTitreDuo**, jamais en même temps que le titre |

## Variantes
| Variante | Format | Classes | Détail |
|---|---|---|---|
| Sélection au-dessus de la tête | 9:16 | `.ms-serre` + `.ms-titre` + `.ms-selection` | le titre en Anton dans le cadre de sélection, au-dessus de la tête. |
| Chiffre + amorce | 9:16 / 16:9 | `.ms-bloc` en ligne : `.ms-motcle--braise` + 2 `.ms-amorce` | sous le menton en 9:16, à côté du visage en 16:9. |
| Serré → recul, derrière toi | 9:16 / 16:9 | `.ms-cadrage` (`--z0: var(--zoom-recul)`, `--z1: 1`) ×2 : ton plan, puis `.ms-detour` (ton détourage) ; entre les deux `.ms-derriere` | un mot géant en Anton sort de derrière toi, du bas vers le haut (`montee-derriere`, `dur-lg`, `ease-out`). Le détourage suit **exactement** le même zoom (mêmes `--ox/--oy/--z0/--z1`). |
| Large → avance, derrière toi | 9:16 / 16:9 | idem, `--z0: 1`, `--z1: var(--zoom-avance)` | une image ou un logo (`.ms-logo-rond`) sort de derrière toi. |
| Texte qui s’écrit à côté | 16:9 | `.ms-serre` + `.ms-signe` (`--i` par signe) + `.ms-curseur-texte` | à droite ou à gauche de toi, lettre après lettre (`dur-signe` 45 ms), amorce en Arial, mot clé en Anton, curseur braise à la fin. |
| Resserré sur un objet | 9:16 / 16:9 | `.ms-cadrage` (`--ox/--oy` = l’objet, `--z1`, `--x1/--y1`, `--duree: var(--dur-resserre)`) | on part du plan large et la caméra se resserre lentement (1,2 s, `ease-in-out`) sur un objet du décor ; le texte arrive quand le zoom s’arrête, sous l’objet en 9:16, à côté en 16:9. |

`.ms-repere` (« ici : ta main vers l’objectif ») est un repère de travail : jamais dans une vidéo livrée. Le geste se filme, le montage ne l’invente pas.

Détourage : `npx hyperframes remove-background <image> -o <sortie.png>`. Les zooms (`--x1`, `--y1`, origine) se recalent sur chaque vraie vidéo.

## À éviter
Le mot géant seul sans toi ni geste en ouverture ; le titre et le sous-titre en même temps ; un élément devant ton visage.
''')

# ================= Planche F : Composition =================
def ex1(n,anime=True):
    o=fond('916','ambiance',True)
    if n>=4:
        o+=f'<div class="ms-profondeur" style="left:-140px;top:1180px;--dx:30px;--dy:-20px">{touche("Esc",0,0,420,"clair",0)}</div><div class="ms-profondeur" style="left:820px;top:120px;--dx:-24px;--dy:16px">{touche("Shift",0,0,380,"clair",0)}</div>'
    if n>=2: o+=touche('Ctrl',300,560,480,'clair',200)
    if n>=3:
        l1,t=phrase('garde le',1300,96); k,_=doto('contrôle',t+120,170,True)
        o+=bloc(l1+k,'left:70px;right:70px;top:1220px;display:flex;flex-direction:column;align-items:center;gap:12px',True)+'<div class="ms-clair" style="position:absolute;left:0;right:0;top:330px;text-align:center"><span class="ms-legende ms-pose" style="--t:900ms;display:inline-block;font-size:30px">ÉTAPE 01</span></div>'
    return o
def ex2(n):
    o=fond('916','ambiance',False)
    if n>=4: o+='<div class="ms-profondeur-carte" style="left:-160px;top:180px;width:520px;height:340px;--dx:26px;--dy:10px"></div><div class="ms-profondeur-carte" style="left:760px;top:1420px;width:520px;height:380px;--dx:-20px;--dy:-14px"></div>'
    if n>=2: o+=terminal(100,640,880,520,200)
    if n>=3:
        q,t=mots('ça tourne',1200)
        o+=f'<div class="ms-bloc ms-bloc--916 ms-empile" style="top:1240px;bottom:auto;--sortie:3200ms"><div class="ms-amorce">{q}</div><div class="ms-motcle" style="--t:{t+120}ms;font-size:220px">{lettres("seul")}</div></div>'+pastille(100,560,900,'EN DIRECT',28,'8px 16px')
    return o
NOMS=['Fond','Sujet principal','Soutien','Profondeur']
def couche(i,inner): return f'<div class="ms-fige" style="position:absolute;inset:0">{inner}</div><div class="ms-couche{" ms-couche--4" if i==4 else ""}">{i} · {NOMS[i-1].upper()}</div>'
def ex1_169():
    o=fond('169','ambiance',True)+f'<div class="ms-profondeur" style="left:-120px;top:680px;--dx:30px;--dy:-20px">{touche("Esc",0,0,400,"clair",0)}</div><div class="ms-profondeur" style="left:1640px;top:-90px;--dx:-24px;--dy:16px">{touche("Shift",0,0,360,"clair",0)}</div>'+touche('Ctrl',320,290,440,'clair',200)
    l1,t=phrase('garde le',1300,96); k,_=doto('contrôle',t+120,170,True)
    return o+bloc('<span class="ms-legende ms-pose" style="--t:900ms;font-size:30px">ÉTAPE 01</span>'+l1+k,'left:960px;right:100px;top:300px;display:flex;flex-direction:column;gap:12px',True)
def ex2_169():
    o=fond('169','ambiance',False)+'<div class="ms-profondeur-carte" style="left:-200px;top:40px;width:520px;height:340px;--dx:26px;--dy:10px"></div><div class="ms-profondeur-carte" style="left:1580px;top:720px;width:520px;height:380px;--dx:-20px;--dy:-14px"></div>'+terminal(160,290,900,520,200)+pastille(160,210,900,'EN DIRECT',28,'8px 16px')
    q,t=mots('ça tourne',1200)
    return o+f'<div class="ms-bloc" style="left:1120px;right:100px;top:380px;--sortie:3200ms"><div class="ms-amorce">{q}</div><div class="ms-motcle" style="--t:{t+120}ms;font-size:220px">{lettres("seul")}</div></div>'
def composition():
    r1=''.join(ap916(couche(i,ex1(i)),f'Ex. 1 · couche {i} · {NOMS[i-1]}',sc=0.2) for i in (1,2,3,4))+ap916(ex1(4),'Ex. 1 · le résultat, animé',sc=0.2)
    r2=''.join(ap916(couche(i,ex2(i)),f'Ex. 2 · couche {i} · {NOMS[i-1]}',sc=0.2) for i in (1,2,3,4))+ap916(ex2(4),'Ex. 2 · le résultat, animé',sc=0.2)
    return card('Composition',1440,1340,'La règle de construction en 4 couches (planche F) · rangées 1 et 2 : 9:16, couche par couche puis le résultat · rangée 3 : 16:9',
     lab('9:16 · exemple 1 · un objet sur fond blanc')+rang(r1)+lab('9:16 · exemple 2 · une interface sur fond noir')+rang(r2)+lab('16:9 · YouTube')+rang(ap169(ex1_169(),'16:9 · Exemple 1, animé'),ap169(ex2_169(),'16:9 · Exemple 2, animé')))
w('components/Composition/preview.html',composition())
w('components/Composition/README.md','''# Composition — la scène en 4 couches (planche F)

Chaque scène graphique (**SceneC3**, **SceneC4**, types d’animation) se construit en 4 couches, de l’arrière vers l’avant. Ce n’est pas un élément à poser : c’est la règle à vérifier avant de livrer une scène.

| Couche | Règle | Classes |
|---|---|---|
| 1 · Fond | un fond du pack (**Fond**), noir ou blanc os ; il remplit le cadre et ne porte aucune information. | `.ms-fond` |
| 2 · Sujet principal | **un seul** sujet dans la zone centrale : un objet, une interface, un chiffre, ou toi. Si on hésite sur le sujet, la scène est à refaire. | `.ms-touche`, `.ms-terminal`, `.ms-carte`… |
| 3 · Soutien | 2 à 4 éléments autour du sujet, qui appuient l’idée sans lui voler la vedette : la phrase (amorce + mot clé Anton), une étiquette mono, une pastille. **Un seul élément braise à l’écran.** | `.ms-phrase`, `.ms-motcle`, `.ms-legende`, `.ms-pastille` |
| 4 · Profondeur | 1 ou 2 éléments vers les bords, coupés par le cadre, flous (`flou-profondeur`, 16 à 18 px) ou plus grands, devant ou derrière le sujet. Aucun texte à lire dedans. Ils dérivent très lentement (`derive`, 20 à 30 px sur toute la scène) pour donner du relief. | `.ms-profondeur` (`--dx`, `--dy`, `--duree-scene`), `.ms-profondeur-carte` |

## Ordre d’entrée
Le fond est déjà là ; le sujet arrive en premier ; puis le soutien au rythme de la voix ; la profondeur bouge en continu, sans jamais attirer l’œil.

## 9:16 et 16:9
Mêmes 4 couches. En 16:9, le sujet passe d’un côté (à gauche), le soutien de l’autre ; les éléments de profondeur vont dans les coins opposés (bas-gauche, haut-droite).
''')

# ---------------- assets : détourages ----------------
DETOURS={"detour-916.png":{"name":"detour-916.png","blob":D916[7:],"size":982736,"type":"image/png"},
         "detour-169.png":{"name":"detour-169.png","blob":D169[7:],"size":1443298,"type":"image/png"}}
