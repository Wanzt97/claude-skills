# ---------- Planche C : types de scène, fonds, sélection tirée (exec dans gen2.py) ----------
import math
PREV_CLAIR=''
def svg_croix(col): return "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60'%3E%3Cpath d='M24 30h12M30 24v12' stroke='%23"+col+"' stroke-width='2' fill='none'/%3E%3C/svg%3E\")"
css_c='''
/* ===== Planche C · Fonds (pack retenu le 2026-11-06) ===== */
.ms-fond{position:absolute;inset:0;overflow:hidden;background:var(--noir-digital)}
.ms-fond--clair{background:var(--os)}
.ms-fond::before{content:"";position:absolute;inset:0;background-image:linear-gradient(to right,var(--grille-noir) 1px,transparent 1px),linear-gradient(to bottom,var(--grille-noir) 1px,transparent 1px);background-size:var(--case) var(--case);-webkit-mask-image:radial-gradient(ellipse 75% 75% at 50% 50%,#000 0%,#000 40%,transparent 92%);mask-image:radial-gradient(ellipse 75% 75% at 50% 50%,#000 0%,#000 40%,transparent 92%)}
.ms-fond--clair::before{background-image:linear-gradient(to right,var(--grille-clair) 1px,transparent 1px),linear-gradient(to bottom,var(--grille-clair) 1px,transparent 1px)}
.ms-fond--sujet::before{-webkit-mask-image:radial-gradient(ellipse 75% 75% at 50% 50%,#000 0%,#000 40%,transparent 92%),radial-gradient(circle at var(--sx,50%) var(--sy,52%),transparent 0,transparent 260px,#000 560px);-webkit-mask-composite:source-in;mask-image:radial-gradient(ellipse 75% 75% at 50% 50%,#000 0%,#000 40%,transparent 92%),radial-gradient(circle at var(--sx,50%) var(--sy,52%),transparent 0,transparent 260px,#000 560px);mask-composite:intersect}
.ms-fond--plan::before{background-image:CROIX_NOIR;background-size:var(--case) var(--case)}
.ms-fond--plan.ms-fond--clair::before{background-image:CROIX_CLAIR}
.ms-fond--grappes{background:radial-gradient(ellipse 50.8% 48.6% at 50% 50%,var(--fonte) 0%,#171717 45%,var(--abysse) 100%)}
.ms-fond--grappes.ms-fond--clair{background:radial-gradient(ellipse 50.8% 48.6% at 50% 50%,var(--os) 0%,var(--os) 45%,var(--bord-clair) 100%)}
.ms-fond--grappes::before{display:none}
.ms-grappes{position:absolute;inset:0;opacity:var(--vis,1)}
.ms-case{position:absolute;width:var(--case);height:var(--case);box-sizing:border-box;background:var(--case-noir)}
.ms-fond--clair .ms-case{background:var(--case-clair)}
.ms-case--vide{background:transparent;border:1px solid var(--grille-noir)}
.ms-case--pleine{background:var(--fonte);border:1px solid var(--grille-noir)}
.ms-case--trait{border:1px solid rgba(58,58,58,0.9)}
.ms-fond--clair .ms-case--vide{background:transparent;border-color:var(--grille-clair)}
.ms-fond--clair .ms-case--pleine{background:rgba(18,18,18,0.07);border-color:var(--grille-clair)}
.ms-fond--clair .ms-case--trait{border-color:rgba(18,18,18,0.22)}
.ms-case--braise,.ms-fond--clair .ms-case--braise{background:var(--case-braise);border:1px solid var(--case-braise-trait)}
/* ===== Planche C · texte posé sur un fond clair (pas de halo) ===== */
.ms-clair .ms-amorce,.ms-clair .ms-motcle,.ms-clair .ms-titre{color:var(--noir-digital);text-shadow:none}
.ms-clair .ms-motcle--braise,.ms-clair .ms-titre--braise{color:var(--braise-fonce)}
.ms-clair .ms-objet-label,.ms-clair .ms-legende{color:var(--encre-2)}
.ms-legende{font-family:var(--font-mono);font-weight:600;font-size:26px;letter-spacing:0.08em;text-transform:uppercase;color:var(--brume)}
/* ===== Planche C · objets des scènes ===== */
.ms-pose{animation:ms-pose var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-carte{position:absolute;box-sizing:border-box;border-radius:var(--radius-md);background:var(--fonte);border:var(--trait-objet) solid var(--acier);overflow:hidden;animation:ms-entree-objet var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-carte--claire{background:var(--blanc-carte);border-color:rgba(18,18,18,0.10);box-shadow:var(--ombre-claire)}
.ms-carte-barre{height:56px;display:flex;align-items:center;gap:10px;padding:0 20px;border-bottom:var(--trait-objet) solid var(--acier)}
.ms-carte--claire .ms-carte-barre{border-bottom-color:rgba(18,18,18,0.10)}
.ms-carte-barre i{width:14px;height:14px;box-sizing:border-box;border:2px solid var(--brume)}
.ms-carte-barre i:nth-child(3){border:0;background:var(--braise)}
.ms-carte--claire .ms-carte-barre i{border-color:var(--encre-2)}
.ms-carte-titre{margin-left:12px;font-family:var(--font-mono);font-weight:600;font-size:24px;letter-spacing:0.08em;color:var(--brume)}
.ms-carte--claire .ms-carte-titre{color:var(--encre-2)}
.ms-carte-corps{padding:28px 24px;display:flex;flex-direction:column;gap:18px}
.ms-carte-ligne{height:18px;border-radius:var(--radius-sm);background:var(--acier)}
.ms-carte--claire .ms-carte-ligne{background:rgba(18,18,18,0.12)}
.ms-terminal{position:absolute;box-sizing:border-box;border-radius:var(--radius-md);background:var(--fonte);border:var(--trait-objet) solid var(--acier);padding:32px;display:flex;flex-direction:column;gap:22px;animation:ms-pose var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-terminal-ligne{font-family:var(--font-mono);font-weight:600;font-size:30px;color:var(--os);animation:ms-apparition var(--dur-lettre) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-terminal-ligne--braise{color:var(--braise)}
.ms-etapes{position:absolute;left:0;right:0;display:flex;align-items:center;justify-content:center;filter:drop-shadow(0 0 18px rgba(10,10,10,0.7))}
.ms-etape{width:64px;height:64px;box-sizing:border-box;border:3px solid var(--os);color:var(--os);display:flex;align-items:center;justify-content:center;font-family:var(--font-mono);font-weight:600;font-size:28px;animation:ms-etape var(--dur-lettre) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-etape--active{background:var(--braise);border-color:var(--braise);color:var(--abysse)}
.ms-etape-lien{width:72px;height:3px;background:var(--os);opacity:0.6}
/* ===== Planche C · écran partagé ===== */
.ms-bande{position:absolute;left:0;top:0;width:1080px;height:var(--bande-916);overflow:hidden;animation:ms-bande var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-panneau{position:absolute;left:0;top:0;width:var(--panneau-169);height:1080px;overflow:hidden;animation:ms-panneau var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-bande.ms-sortie{animation:ms-bande var(--dur-objet) var(--ease-out) both,ms-bande-sortie var(--dur-bande-sortie) var(--ease-in) forwards;animation-delay:var(--t,0ms),var(--sortie)}
.ms-panneau.ms-sortie{animation:ms-panneau var(--dur-objet) var(--ease-out) both,ms-panneau-sortie var(--dur-bande-sortie) var(--ease-in) forwards;animation-delay:var(--t,0ms),var(--sortie)}
.ms-plan--bas{top:var(--bande-916);height:calc(1920px - var(--bande-916))}
.ms-plan--droite{left:var(--panneau-169);width:calc(1920px - var(--panneau-169))}
.ms-jointure{position:absolute;left:0;width:1080px;top:calc(var(--bande-916) - 1px);height:2px;background:rgba(10,10,10,0.6)}
.ms-incrust{position:absolute;inset:0;overflow:hidden;transform-origin:100% 100%;animation:ms-incrust var(--dur-lg) var(--ease-in-out) both;animation-delay:var(--t,0ms)}
.ms-incrust.ms-retour{animation:ms-incrust var(--dur-lg) var(--ease-in-out) both,ms-incrust-retour var(--dur-lg) var(--ease-in-out) forwards;animation-delay:var(--t,0ms),var(--retour)}
.ms-incrust .ms-plan{border-radius:inherit}
.ms-incrust::after{content:"";position:absolute;inset:0;border:7px solid var(--acier);border-radius:inherit;pointer-events:none}
/* ===== TitreChoc V3 : sélection tirée depuis un coin (validée le 2026-11-06) ===== */
.ms-tire{position:absolute;transform-origin:0 0;animation:ms-apparition var(--dur-mot) var(--ease-out) both,ms-tire var(--dur-lg) var(--ease-in-out) both;animation-delay:var(--t,0ms),calc(var(--t,0ms) + 320ms)}
.ms-tire.ms-sortie{animation:ms-apparition var(--dur-mot) var(--ease-out) both,ms-tire var(--dur-lg) var(--ease-in-out) both,ms-sortie var(--dur-sortie) var(--ease-in) forwards;animation-delay:var(--t,0ms),calc(var(--t,0ms) + 320ms),var(--sortie)}
.ms-tire .ms-titre{position:relative;display:block}
.ms-tire .ms-selection{animation:ms-deselection var(--dur-lettre) var(--ease-in) both;animation-delay:calc(var(--t,0ms) + 1400ms)}
.ms-curseur{position:absolute;width:44px;height:56px;animation:ms-curseur var(--dur-lg) var(--ease-in-out) both;animation-delay:calc(var(--t,0ms) + 320ms)}
.ms-curseur svg{display:block;transform-origin:0 0;animation:ms-clic 1640ms linear both;animation-delay:var(--t,0ms)}
@keyframes ms-pose{from{opacity:0;transform:scale(0.92)}to{opacity:1;transform:scale(1)}}
@keyframes ms-apparition{from{opacity:0}to{opacity:1}}
@keyframes ms-etape{from{opacity:0;transform:scale(0.6)}to{opacity:1;transform:scale(1)}}
@keyframes ms-bande{from{transform:translateY(-100%)}to{transform:translateY(0)}}
@keyframes ms-bande-sortie{from{transform:translateY(0)}to{transform:translateY(-100%)}}
@keyframes ms-panneau{from{transform:translateX(-100%)}to{transform:translateX(0)}}
@keyframes ms-panneau-sortie{from{transform:translateX(0)}to{transform:translateX(-100%)}}
@keyframes ms-incrust{from{transform:translate(0,0) scale(1);border-radius:0}to{transform:translate(calc(-1 * var(--incrust-marge)),calc(-1 * var(--incrust-marge))) scale(var(--incrust-taille));border-radius:20px}}
@keyframes ms-incrust-retour{from{transform:translate(calc(-1 * var(--incrust-marge)),calc(-1 * var(--incrust-marge))) scale(var(--incrust-taille));border-radius:20px}to{transform:translate(0,0) scale(1);border-radius:0}}
@keyframes ms-tire{from{transform:translate(var(--dx,0px),var(--dy,0px)) scale(0.3)}to{transform:translate(0,0) scale(1)}}
@keyframes ms-deselection{from{opacity:1}to{opacity:0}}
@keyframes ms-curseur{from{transform:translate(var(--cx,0px),var(--cy,0px))}to{transform:translate(0,0)}}
@keyframes ms-clic{0%{opacity:0;transform:scale(1)}12.2%{opacity:0;transform:scale(1)}15.9%{opacity:1;transform:scale(1)}19.5%{opacity:1;transform:scale(0.85)}56.1%{opacity:1;transform:scale(0.85)}62.2%{opacity:1;transform:scale(1)}85.4%{opacity:1;transform:scale(1)}100%{opacity:0;transform:scale(1)}}
'''.replace('CROIX_NOIR',svg_croix('3a3a3a')).replace('CROIX_CLAIR',svg_croix('c9c7c2'))
css+=css_c
w('components/bundle.css',css)

# ---------- aides ----------
def hsh(i,j,s):
    x=math.sin(i*127.1+j*311.7+s*74.7)*43758.5453; return x-math.floor(x)
def grappes(fmt,dens=0.4):
    cols,rows,cx0,cy0,rx,ry=(18,32,540,960,486,747) if fmt=='916' else (32,18,960,540,862,420)
    o=[];b=0
    for j in range(rows):
        for i in range(cols):
            cx=i*60+30;cy=j*60+30
            d=math.sqrt(((cx-cx0)/rx)**2+((cy-cy0)/ry)**2)
            if d+(hsh(i,j,1)-0.5)*0.5<=1-dens: continue
            c=hsh(i,j,2); cl='ms-case ms-case--vide'
            if hsh(i,j,3)<0.16: cl+=' ms-case--trait'
            if c<0.07: cl='ms-case'
            elif c<0.15:
                if b<3: cl='ms-case ms-case--braise'; b+=1
                else: cl='ms-case ms-case--pleine'
            elif c<0.33: cl='ms-case ms-case--pleine'
            o.append(f'<div class="{cl}" style="left:{i*60}px;top:{j*60}px"></div>')
    return ''.join(o)
CASES={'916':{'ambiance':[(240,480),(780,600),(600,900),(360,1140),(720,1320),(180,1500)],'ambiance_b':(480,780),'sujet':[(180,420),(840,480),(120,1380),(780,1560)],'sujet_b':(120,720),'sujet_c':('540px','1000px')},
       '169':{'ambiance':[(540,300),(1260,240),(840,660),(1440,720),(420,780),(1080,420)],'ambiance_b':(960,480),'sujet':[(300,240),(1560,300),(360,720),(1500,780)],'sujet_b':(1620,540),'sujet_c':('960px','600px')}}
def fond(fmt,kind,clair,vis=None):
    k=CASES[fmt]; cl='ms-fond'+(' ms-fond--clair' if clair else '')
    if kind=='ambiance':
        inner=''.join(f'<div class="ms-case" style="left:{x}px;top:{y}px"></div>' for x,y in k['ambiance'])+f'<div class="ms-case ms-case--braise" style="left:{k["ambiance_b"][0]}px;top:{k["ambiance_b"][1]}px"></div>'
        return f'<div class="{cl}">{inner}</div>'
    if kind=='sujet':
        inner=''.join(f'<div class="ms-case" style="left:{x}px;top:{y}px"></div>' for x,y in k['sujet'])+f'<div class="ms-case ms-case--braise" style="left:{k["sujet_b"][0]}px;top:{k["sujet_b"][1]}px"></div>'
        return f'<div class="{cl} ms-fond--sujet" style="--sx:{k["sujet_c"][0]};--sy:{k["sujet_c"][1]}">{inner}</div>'
    if kind=='grappes':
        v=vis if vis is not None else (1 if clair else 0.1)
        return f'<div class="{cl} ms-fond--grappes"><div class="ms-grappes" style="--vis:{v}">{grappes(fmt)}</div></div>'
    return f'<div class="{cl} ms-fond--plan"></div>'
def ap2(fmt,inner,leg,sc=0.25): return ap(fmt,inner,leg,sc=sc,plan=False)
def plan_img(fmt,cls=''): return f'<img class="ms-plan {cls}" src="{P916 if fmt=="916" else P169}" alt="Plan test face caméra">'

# ---------- Fond ----------
r916=''.join(ap2('916',fond('916',k,c),f'9:16 · {n} · {"blanc" if c else "noir"}',sc=0.18) for c in (False,True) for k,n in (('ambiance','ambiance'),('sujet','sujet'),('grappes','grappes'),('plan','plan')))
r169=''.join(ap2('169',fond('169',k,c),f'16:9 · {n} · {"blanc" if c else "noir"}',sc=0.15) for c in (False,True) for k,n in (('ambiance','ambiance'),('sujet','sujet'),('grappes','grappes'),('plan','plan')))
prev=f'''<!-- @dsCard group="Fonds" height=1290 width=1600 subtitle="Le pack retenu : 4 fonds, en noir et en blanc os · rangée 1 : 9:16 · rangée 2 : 16:9" -->
<!doctype html>
<html lang="fr"><head><meta charset="utf-8">{PREV_CSS}<style>.rang{{flex-wrap:wrap}}</style></head>
<body><div class="rang">{r916}</div><div class="rang">{r169}</div></body></html>
'''
w('components/Fond/preview.html',prev)
w('components/Fond/README.md','''# Fond

Le fond de tout plan graphique (écran partagé, plein écran, carton). Un pack de 4 fonds, chacun en noir et en blanc os, le même jeu en 9:16 et en 16:9. Choisi par Wanzt le 2026-11-06 à partir de ses fonds d’écran Digital Black.

**Ce que tu fournis :** le format, noir ou blanc, et le fond voulu.

## Noir ou blanc
- **Noir** (`noir-digital`) pour montrer un logiciel, un terminal, une interface.
- **Blanc** (`.ms-fond--clair`, blanc `os`) pour expliquer une idée.
- Un seul fond par plan. On ne change de fond que pour marquer une partie.

## Les 4 fonds
| Fond | Classes | Quand |
|---|---|---|
| Grille gommée · ambiance | `.ms-fond` + quelques `.ms-case` et une `.ms-case--braise` | par défaut |
| Grille gommée · sujet | `.ms-fond.ms-fond--sujet`, centre du trou `--sx` / `--sy` | un objet ou un chiffre au centre : la grille s’efface autour |
| Grappes | `.ms-fond.ms-fond--grappes` + `.ms-grappes` (cases groupées vers les bords) | ouverture de partie, carton ; le centre reste vide pour le texte |
| Plan d’architecte | `.ms-fond.ms-fond--plan` (petites croix) | une étape, un schéma |

- La grille : cases de `case` (60 px), lignes 1 px `grille-noir` / `grille-clair`, effacée vers les bords (masque radial). Elle ne bouge jamais.
- Cases : `case-noir` / `case-clair` ; au plus 3 cases `case-braise` (bordure `case-braise-trait`).
- Grappes : visibilité des carrés par `--vis` sur `.ms-grappes` (0 à 1). Réglage retenu : 0,1 en noir, 1 en blanc. Densité retenue : 0,4.
- Plan d’architecte : blocs et braise désactivés.
- L’orange des cases (`case-braise`) est celui des fonds d’origine, gardé tel quel à la demande de Wanzt.

## À ne pas faire
Fond blanc pur, papier, dégradé coloré, texture, fond qui bouge, fond plus contrasté que le sujet, logo dans le fond.
''')

# ---------- ScèneC2 ----------
def duo2(am,mc,t0,bas,fmt='916',braise=False,size=None):
    a,t=mots(am,t0); s=f';font-size:{size}px' if size else ''
    return f'<div class="ms-bloc ms-bloc--{fmt} ms-empile" style="--bas:{bas}px;--sortie:3200ms"><div class="ms-amorce">{a}</div><div class="ms-motcle{" ms-motcle--braise" if braise else ""}" style="--t:{t+120}ms{s}">{lettres(mc)}</div></div>',t
def carte(x,y,w_,h,t,titre,claire=False):
    lig=''.join(f'<div class="ms-carte-ligne" style="width:{p}%"></div>' for p in (86,64,92,48))
    return f'<div class="ms-carte{" ms-carte--claire" if claire else ""}" style="left:{x}px;top:{y}px;width:{w_}px;height:{h}px;--t:{t}ms"><div class="ms-carte-barre"><i></i><i></i><i></i><span class="ms-carte-titre">{titre}</span></div><div class="ms-carte-corps">{lig}</div></div>'
def etapes(t,active,top):
    o=[]
    for i in range(3):
        o.append(f'<span class="ms-etape{" ms-etape--active" if i+1==active else ""}" style="--t:{t+i*120}ms">{i+1}</span>')
        if i<2: o.append('<span class="ms-etape-lien"></span>')
    return f'<div class="ms-etapes" style="top:{top}px">{"".join(o)}</div>'
b1,_=duo2('ces trois','erreurs',0,1450,size=200)
b2,_=duo2('mon script',"s’écrit",700,1450,size=220)
b3,_=duo2('une seule','idée',700,1450)
prev=f'''<!-- @dsCard group="Types de scène" height=700 width=1200 subtitle="Sous-titres + petite animation · V1 points d’étape · V2 fenêtre logiciel · V3 carte idée" -->
<!doctype html>
<html lang="fr"><head><meta charset="utf-8">{PREV_CSS}</head>
<body><div class="rang">{ap('916',b1+etapes(900,1,1490),'V1 · Points d’étape',zone=Z916)}{ap('916',carte(90,260,560,380,300,'SCRIPT.TXT')+b2,'V2 · Fenêtre logiciel (noire)',zone=Z916)}{ap('916',carte(430,240,560,380,300,'L’IDÉE',True)+b3,'V3 · Carte idée (blanche)',zone=Z916)}</div>{BOUCLE}</body></html>
'''
w('components/SceneC2/preview.html',prev)
w('components/SceneC2/README.md','''# SceneC2 — Sous-titres + petite animation

Toi en plein cadre, toujours le sujet, avec **un seul** petit élément d’interface près de toi. Les sous-titres restent ceux de **SousTitreDuo**.

**Ce que tu fournis :** le plan face caméra, la position du visage, l’élément (étapes, logiciel ou idée) et son moment dans la phrase.

| Variante | Classes | Détail |
|---|---|---|
| V1 Points d’étape | `.ms-etapes` > `.ms-etape` (+ `.ms-etape--active`), `.ms-etape-lien` | 3 cases de 64 px (trait 3 px `os`) reliées par un trait ; l’étape en cours en `braise` pleine, chiffre `abysse`. Sous le bloc de sous-titres. |
| V2 Fenêtre logiciel | `.ms-carte` > `.ms-carte-barre` (3 `<i>` + `.ms-carte-titre`), `.ms-carte-corps` > `.ms-carte-ligne` | pour montrer un logiciel : carte `fonte`, trait `acier`, arrondi `radius-md`, barre mono avec 2 carrés creux + 1 carré braise. 560 × 380 en 9:16, au-dessus ou à côté de la tête. |
| V3 Carte idée | `.ms-carte.ms-carte--claire` | pour expliquer une idée : la même carte en `blanc-carte`, avec `ombre-claire`. |

## Placement
Jamais sur le visage : au-dessus de la tête ou à côté. Un seul élément à la fois.

## Mouvement
| Élément | Entrée | Sortie |
|---|---|---|
| Carte | montée de `montee-objet` (48 px) + fondu, `dur-objet` (400 ms), `ease-out`, à `--t` | avec le bloc de sous-titres |
| Étape | échelle 0,6 → 1 + fondu, `dur-lettre`, `ease-out`, 120 ms d’écart (`--t` par case) | avec le bloc |

Aucun effet sur le décor ni sur le visage.
''')

# ---------- ScèneC3 ----------
def phrase_claire(am,mc,t0,top):
    a,t=mots(am,t0)
    return f'<div class="ms-clair" style="position:absolute;left:80px;right:80px;top:{top}px;display:flex;align-items:baseline;justify-content:center;gap:18px"><span class="ms-amorce" style="font-size:48px">{a}</span><span class="ms-motcle ms-motcle--braise" style="--t:{t+120}ms;font-size:120px">{lettres(mc)}</span></div>'
def pastilles(t,top,taille=200,gap=56):
    o=''.join(f'<div class="ms-pose" style="--t:{t+i*120}ms;display:flex;flex-direction:column;align-items:center;gap:16px"><div style="width:{taille}px;height:{taille}px;border-radius:6px;background:var(--{c});box-shadow:var(--ombre-claire);border:2px solid rgba(18,18,18,0.08)"></div><span class="ms-legende" style="font-size:22px">{l}</span></div>' for i,(c,l) in enumerate([('noir-digital','ENCRE'),('os','OS'),('braise','BRAISE')]))
    return f'<div class="ms-clair" style="position:absolute;left:0;right:0;top:{top}px;display:flex;justify-content:center;gap:{gap}px">{o}</div>'
TERM=['> /montage lance','✓ rushs triés · 12','✓ script calé','› export en cours']
def terminal(x,y,w_,h,t):
    l=''.join(f'<div class="ms-terminal-ligne{" ms-terminal-ligne--braise" if i==3 else ""}" style="--t:{t+100+i*200}ms">{html.escape(s)}</div>' for i,s in enumerate(TERM))
    return f'<div class="ms-terminal" style="left:{x}px;top:{y}px;width:{w_}px;height:{h}px;--t:{t}ms">{l}</div>'
s1a,_=mots('pas plus de',900); sous1=f'<div class="ms-bloc ms-bloc--916 ms-empile" style="top:784px;bottom:auto;--sortie:3200ms"><div class="ms-amorce">{s1a}</div><div class="ms-motcle" style="--t:1500ms;font-size:200px">{lettres("trois")}</div></div>'
s2a,_=mots('il monte',900); sous2=f'<div class="ms-bloc ms-bloc--916 ms-empile" style="top:784px;bottom:auto;--sortie:3200ms"><div class="ms-amorce">{s2a}</div><div class="ms-motcle" style="--t:1300ms;font-size:200px">{lettres("seul")}</div></div>'
v1=plan_img('916','ms-plan--bas')+f'<div class="ms-bande ms-sortie" style="--t:0ms;--sortie:3400ms">{fond("916","ambiance",True)}{phrase_claire("trois","couleurs",500,80)}{pastilles(240,230)}</div><div class="ms-jointure"></div>'+sous1
v2=plan_img('916','ms-plan--bas')+f'<div class="ms-bande ms-sortie" style="--t:0ms;--sortie:3400ms">{fond("916","ambiance",False)}{terminal(140,160,800,440,200)}</div><div class="ms-jointure"></div>'+sous2
s3a,_=mots('pas plus de',900)
v3=plan_img('169','ms-plan--droite')+f'<div class="ms-panneau ms-sortie" style="--t:0ms;--sortie:3400ms">{fond("169","ambiance",True)}{pastilles(240,330,170,40)}</div><div class="ms-bloc" style="left:860px;right:40px;bottom:140px;--sortie:3200ms"><div class="ms-amorce" style="font-size:44px">{s3a}</div></div>'
s4a,_=mots('et pendant ce temps',1200)
v4=fond('169','ambiance',False)+terminal(300,210,900,480,700)+f'<div class="ms-bloc" style="left:300px;width:900px;top:780px;--sortie:3200ms"><div class="ms-amorce" style="font-size:44px">{s4a}</div></div><div class="ms-incrust ms-retour" style="--t:400ms;--retour:3200ms">{plan_img("169")}</div>'
prev=f'''<!-- @dsCard group="Types de scène" height=1000 width=1300 subtitle="Écran partagé · rangée 1 : 9:16 bande blanche (idée), bande noire (logiciel) · rangée 2 : 16:9 panneau blanc, A-roll rétracté dans un coin" -->
<!doctype html>
<html lang="fr"><head><meta charset="utf-8">{PREV_CSS}</head>
<body><div class="rang">{ap('916',v1,'9:16 · V1 · Bande blanche (idée)',plan=False)}{ap('916',v2,'9:16 · V2 · Bande noire (logiciel)',plan=False)}</div><div class="rang">{ap('169',v3,'16:9 · V3 · Panneau blanc à gauche',sc=0.3,plan=False)}{ap('169',v4,'16:9 · V4 · A-roll rétracté dans un coin',sc=0.3,plan=False)}</div>{BOUCLE}</body></html>
'''
w('components/SceneC3/preview.html',prev)
w('components/SceneC3/README.md','''# SceneC3 — Écran partagé

Une partie de l’écran pour un seul objet, l’autre pour toi. Le fond de la partie graphique vient de **Fond** : blanc pour une idée, noir pour un logiciel.

**Ce que tu fournis :** le plan face caméra, l’objet ou le groupe à montrer, la phrase et ses temps.

| Variante | Classes | Détail |
|---|---|---|
| 9:16 · Bande du haut | `.ms-bande` (hauteur `bande-916`, 760 px) ; ton plan en `.ms-plan.ms-plan--bas` ; `.ms-jointure` | toi en bas, plan recadré pour que la tête reste dans la partie basse ; coupe nette à la jointure |
| 16:9 · Panneau à gauche | `.ms-panneau` (largeur `panneau-169`, 820 px) ; ton plan en `.ms-plan.ms-plan--droite` | toi à droite |
| 16:9 · A-roll rétracté | `.ms-incrust` (+ `.ms-retour` et `--retour`) qui contient ton plan, par-dessus un **Fond** plein écran | ton plan se rétracte dans le coin bas-droite (`incrust-taille` 30 %, marge `incrust-marge` 56 px, coins arrondis, cadre `acier`), le graphique prend l’écran derrière |

## Contenu de la partie graphique
UN seul objet ou groupe centré (pastilles, carte, icône, terminal `.ms-terminal`), une phrase courte au-dessus.
- Sur fond blanc : enveloppe `.ms-clair` ; texte `noir-digital` sans halo, mot clé en `braise-fonce`, étiquettes `encre-2`, ombre `ombre-claire` sous les objets.
- Sur fond noir : comme la planche A (`os`, `braise`, halo).

## Sous-titres
9:16 : juste sous la jointure, entre la jointure et le haut de ta tête. 16:9 : en bas de ton côté. Pendant l’incrustation : dans la zone du graphique, jamais sous l’incrustation. Halo sombre sur la vidéo.

## Mouvement
| Élément | Entrée | Sortie |
|---|---|---|
| Bande / panneau | glisse depuis le haut / la gauche, `dur-objet` (400 ms), `ease-out` | repart, `dur-bande-sortie` (240 ms), `ease-in` (classe `.ms-sortie` + `--sortie`) |
| Objet | 240 ms après : `.ms-pose` (échelle 0,92 → 1 + fondu, 400 ms), 120 ms d’écart dans un groupe | avec la bande |
| A-roll rétracté | rétraction `dur-lg` (600 ms), `ease-in-out`, sans coupe | retour identique à `--retour` |
''')

# ---------- ScèneC4 ----------
def carte_video(x,y,w_,h,t): return f'<div class="ms-pose" style="position:absolute;left:{x}px;top:{y}px;width:{w_}px;height:{h}px;border-radius:6px;overflow:hidden;box-shadow:var(--ombre-claire);border:2px solid rgba(18,18,18,0.08);--t:{t}ms"><img src="{P916}" alt="" style="width:100%;height:100%;object-fit:cover;object-position:50% 45%"></div>'
p1=fond('916','sujet',True).replace('--sy:1000px','--sy:1080px')+phrase_claire('un seul objet,','beaucoup',300,330)+carte_video(300,700,480,760,200)+'<div class="ms-clair" style="position:absolute;left:0;right:0;top:1540px;text-align:center"><span class="ms-legende ms-pose" style="--t:900ms;display:inline-block">DE VIDE AUTOUR</span></div>'
q,_=mots('ça tourne',1200)
p2=fond('916','ambiance',False)+terminal(100,620,880,520,200)+f'<div class="ms-bloc ms-bloc--916 ms-empile" style="top:1260px;bottom:auto;--sortie:3200ms"><div class="ms-amorce">{q}</div><div class="ms-motcle" style="--t:1500ms;font-size:220px">{lettres("seul")}</div></div>'
q3,_=mots('par mois, pour un outil',600)
p3=fond('916','grappes',True)+f'<div class="ms-clair"><div class="ms-titre" style="left:0;right:0;top:640px;text-align:center;font-size:300px;--sortie:3200ms"><span style="--t:200ms;display:inline-block">{lettres("200 €")}</span></div><div class="ms-bloc ms-bloc--916" style="top:960px;bottom:auto;--sortie:3200ms"><div class="ms-amorce" style="font-size:48px;color:var(--encre-2)">{q3}</div></div></div>'
prev=f'''<!-- @dsCard group="Types de scène" height=700 width=1200 subtitle="Plein écran · V1 blanc : une idée, un objet · V2 noir : un logiciel · V3 blanc : un chiffre" -->
<!doctype html>
<html lang="fr"><head><meta charset="utf-8">{PREV_CSS}</head>
<body><div class="rang">{ap('916',p1,'V1 · Blanc : une idée, un objet',plan=False)}{ap('916',p2,'V2 · Noir : un logiciel',plan=False)}{ap('916',p3,'V3 · Blanc : un chiffre',plan=False)}</div>{BOUCLE}</body></html>
'''
w('components/SceneC4/preview.html',prev)
w('components/SceneC4/README.md','''# SceneC4 — Plein écran

On ne te voit plus : un **Fond** plein écran, un seul objet au centre, beaucoup de vide autour.

**Ce que tu fournis :** l’objet (carte, icône, chiffre, terminal), la phrase et ses temps, noir ou blanc.

- **Fond** : blanc pour une idée, noir pour un logiciel, un terminal, une interface. Grille gommée par défaut ; « sujet » quand l’objet est au centre ; grappes ou plan d’architecte pour changer de partie.
- **Composition** : UN objet au centre ; une phrase courte au-dessus ou en dessous (amorce + mot clé, planche A) ; une étiquette mono (`.ms-legende`) au plus.
- **Couleurs sur fond blanc** (`.ms-clair`) : texte `noir-digital`, secondaire `encre-2`, mot clé en `noir-digital` ou `braise-fonce`. La `braise` seulement en aplat (case, pastille, poignée), jamais en texte. Ombre `ombre-claire` sous les objets.
- **Couleurs sur fond noir** : comme la planche A (`os`, `braise` pour l’unique accent, halo).

## Mouvement
Coupe franche vers le fond. L’objet arrive 200 ms après (`.ms-pose` : échelle 0,92 → 1 + fondu, `dur-objet`, `ease-out`) ; la phrase suit la voix (planche A). Sortie : coupe franche ou fondu `dur-sortie`.

## À éviter
Affiche chargée, capture d’écran entière, grille d’avatars, gros titre plaqué sur une capture, plusieurs objets qui se battent.
''')

# ---------- TitreChoc V3 : sélection tirée ----------
def tiree(fmt):
    if fmt=='916':
        L,T,W,H,fs=110,330,860,240,220; amb=300; lab='9:16 · V3 · Sélection tirée (au-dessus de la tête)'
        sx,sy=60,60   # coin de départ
    else:
        L,T,W,H,fs=640,126,640,200,190; amb=110; lab='16:9 · V3 · Sélection tirée'
        sx,sy=60,60
    dx,dy=sx-L,sy-T
    # poignée bas-droite : arrivée (L+W, T+H) ; départ (sx+0.3W, sy+0.3H)
    cx,cy=(sx+0.3*W)-(L+W),(sy+0.3*H)-(T+H)
    am,_=mots('monte tes vidéos avec',1000,140)
    cur='<svg aria-hidden="true" width="44" height="56" viewBox="0 0 22 28"><path d="M2 2 L2 22 L7.5 17 L11 25 L14.5 23.5 L11 16 L18 16 Z" fill="#efefef" stroke="#0a0a0a" stroke-width="1.6" stroke-linejoin="round"></path></svg>'
    bloc=f'<div class="ms-bloc ms-bloc--{fmt}" style="--bas:{amb}px;--sortie:3200ms"><div class="ms-amorce">{am}</div></div>' if fmt=='916' else f'<div class="ms-bloc ms-bloc--169" style="--bas:{amb}px;--sortie:3200ms"><div class="ms-amorce">{am}</div></div>'
    titre=f'<div class="ms-tire ms-sortie" style="left:{L}px;top:{T}px;width:{W}px;height:{H}px;--t:0ms;--dx:{dx}px;--dy:{dy}px;--sortie:3200ms"><div class="ms-titre" style="width:{W}px;height:{H}px;display:flex;align-items:center;justify-content:center;font-size:{fs}px">Claude</div><div class="ms-selection" style="left:0;top:0;width:{W}px;height:{H}px;box-sizing:border-box"><span class="ms-poignee ms-poignee--hg"></span><span class="ms-poignee ms-poignee--hd"></span><span class="ms-poignee ms-poignee--bg"></span><span class="ms-poignee ms-poignee--bd"></span></div></div>'
    curseur=f'<div class="ms-curseur" style="left:{L+W-4}px;top:{T+H-4}px;--t:0ms;--cx:{cx:.0f}px;--cy:{cy:.0f}px">{cur}</div>'
    return bloc+titre+curseur,lab
(t9,l9),(t16,l16)=tiree('916'),tiree('169')
