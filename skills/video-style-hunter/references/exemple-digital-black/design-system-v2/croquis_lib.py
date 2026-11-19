# ---------- Le croquis de Wanzt (8 novembre 2026, Labo du sous-titre de l'atelier) ----------
# Amorce Arial 400 à gauche du mot clé, mot clé Anton braise, mot de fin Inter 400 dessous à droite.
# 4 variantes d'animation : V1 sélection, V2 punch, V3 machine à écrire, V4 sélection agrandie.
# exec dans gen3.py avant planche_c.py : redéfinit duo2() pour que toutes les scènes prennent le croquis.

css+='''
/* ===== Croquis de sous-titre (Labo du sous-titre, 8 novembre 2026) ===== */
.ms-croquis{display:grid;grid-template-columns:auto auto;column-gap:var(--ecart-croquis);align-items:center;transform:scale(var(--ech,1));transform-origin:50% 100%}
.ms-croquis .ms-amorce{grid-area:1/1;justify-self:end;margin-bottom:0.6em;white-space:nowrap}
.ms-cle{grid-area:1/2;position:relative;padding:8px 18px}
.ms-cle .ms-motcle{display:block;position:relative}
.ms-croquis .ms-motcle{color:var(--braise)}
.ms-croquis .ms-fin{grid-area:2/2;justify-self:end;margin:-8px 18px 0 0}
.ms-croquis--dessus{grid-template-columns:auto}
.ms-croquis--dessus .ms-amorce{grid-area:1/1;justify-self:start;margin:0 0 0 18px}
.ms-croquis--dessus .ms-cle{grid-area:2/1}
.ms-croquis--dessus .ms-fin{grid-area:3/1}
/* placement : 9:16 sous le menton (ms-bloc--916), 16:9 à côté de la tête ou derrière toi */
.ms-bloc--cote{top:var(--y,520px);bottom:auto;transform:translateY(-50%)}
.ms-bloc--gauche{left:var(--col-169-marge);right:auto;width:calc(var(--tete-g,760px) - var(--tete-ecart) - var(--col-169-marge));align-items:flex-end;text-align:right}
.ms-bloc--droite{left:calc(var(--tete-d,950px) + var(--tete-ecart));right:var(--col-169-marge);align-items:flex-start;text-align:left}
.ms-bloc--derriere{left:var(--bloc-169-marge);right:var(--bloc-169-marge)}
.ms-bloc--gauche .ms-croquis{transform-origin:100% 50%}
.ms-bloc--droite .ms-croquis{transform-origin:0% 50%}
.ms-bloc--derriere .ms-croquis,.ms-bloc--haut .ms-croquis{transform-origin:50% 0%}
.ms-bloc--haut{top:var(--haut,250px);bottom:auto}
/* poignées et curseur des sélections */
.ms-cle .ms-poignee,.ms-agrandie .ms-poignee{width:var(--poignee);height:var(--poignee);background:var(--os);border:3px solid var(--braise);box-sizing:border-box}
.ms-cle .ms-poignee--hg{left:-9px;top:-9px}.ms-cle .ms-poignee--hd{right:-9px;top:-9px}.ms-cle .ms-poignee--bg{left:-9px;bottom:-9px}.ms-cle .ms-poignee--bd{right:-9px;bottom:-9px}
.ms-fleche{position:absolute;width:0;height:0;z-index:2}
.ms-fleche > span{position:absolute;left:0;top:0;opacity:0}
.ms-fleche svg{display:block;width:64px;height:78px;transform-origin:1px 1px}
/* V1 · sélection : mot os, cadre braise tracé, poignées, curseur, clic → noir sur braise */
.ms-v1 .ms-motcle{color:var(--os);animation:ms-entree-mot var(--dur-mot) var(--ease-out) both,ms-noircit 120ms linear both;animation-delay:var(--t,0ms),calc(var(--t,0ms) + var(--v1-clic) + 20ms)}
.ms-v1 .ms-cle{animation:ms-remplit 120ms linear both;animation-delay:calc(var(--t,0ms) + var(--v1-clic) + 20ms)}
.ms-v1 .ms-cadre{position:absolute;inset:0;border:var(--trait-selection) solid var(--braise);animation:ms-trace var(--dur-cadre) var(--ease-out) both;animation-delay:calc(var(--t,0ms) + 450ms)}
.ms-v1 .ms-poignee{animation:ms-poignee-in 160ms var(--ease-out) both;animation-delay:calc(var(--t,0ms) + 750ms)}
.ms-v1 .ms-fleche{right:-24px;bottom:-40px}
.ms-v1 .ms-fleche > span{animation:ms-fleche 420ms var(--ease-out) both;animation-delay:calc(var(--t,0ms) + 850ms)}
.ms-v1 .ms-fleche svg{animation:ms-clic-fleche 160ms ease-out both;animation-delay:calc(var(--t,0ms) + var(--v1-clic))}
/* V2 · punch : le mot clé tombe trop grand puis se pose */
.ms-v2 .ms-motcle{transform-origin:50% 60%;animation:ms-punch var(--dur-punch) var(--ease-out) both;animation-delay:var(--t,0ms)}
/* V3 · machine à écrire : chaque lettre a son --t */
.ms-v3 .ms-amorce,.ms-v3 .ms-fin,.ms-v3 .ms-motcle{display:flex;align-items:flex-end}
.ms-frappe{display:inline-block;overflow:hidden;white-space:pre;animation:ms-frappe 10ms steps(1,end) both;animation-delay:var(--t,0ms)}
/* V4 · sélection agrandie : petit (40 %), sélectionné, tiré et agrandi jusqu’à sa place */
.ms-agrandie{position:relative;transform-origin:50% 50%;animation:ms-agrandie var(--dur-agrandie) var(--ease-in-out) both;animation-delay:var(--drag,0ms)}
.ms-agrandie .ms-cadre{position:absolute;inset:-18px;border:5px solid var(--braise);animation:ms-trace var(--dur-cadre) var(--ease-out) both,ms-efface 200ms var(--ease-in) both;animation-delay:var(--cadre,0ms),calc(var(--lache,0ms) + 100ms)}
.ms-agrandie .ms-poignee{width:24px;height:24px;border-width:4px;animation:ms-poignee-in 160ms var(--ease-out) both,ms-efface 200ms var(--ease-in) both;animation-delay:calc(var(--cadre,0ms) + 300ms),calc(var(--lache,0ms) + 100ms)}
.ms-agrandie .ms-poignee--hg{left:-30px;top:-30px}.ms-agrandie .ms-poignee--hd{right:-30px;top:-30px}.ms-agrandie .ms-poignee--bg{left:-30px;bottom:-30px}.ms-agrandie .ms-poignee--bd{right:-30px;bottom:-30px}
.ms-agrandie .ms-fleche{right:-30px;bottom:-30px;transform-origin:0 0;animation:ms-contre var(--dur-agrandie) var(--ease-in-out) both,ms-efface 200ms var(--ease-in) both;animation-delay:var(--drag,0ms),calc(var(--lache,0ms) + 150ms)}
.ms-agrandie .ms-fleche > span{left:-4px;top:-4px;animation:ms-fleche 420ms var(--ease-out) both;animation-delay:calc(var(--cadre,0ms) + 350ms)}
.ms-agrandie .ms-fleche svg{animation:ms-clic-fleche 160ms ease-out both;animation-delay:var(--clic,0ms)}
.ms-v4 .ms-motcle{color:var(--os);animation:ms-entree-mot var(--dur-mot) var(--ease-out) both,ms-braise 160ms linear both;animation-delay:var(--t,0ms),var(--lache,0ms)}
/* derrière toi (16:9) : ton détourage par-dessus le texte */
.ms-detour-169{position:absolute;left:0;top:0;width:100%;height:100%;object-fit:cover;pointer-events:none}
@keyframes ms-noircit{to{color:var(--abysse);text-shadow:none}}
@keyframes ms-remplit{to{background:var(--braise)}}
@keyframes ms-braise{to{color:var(--braise)}}
@keyframes ms-trace{from{clip-path:inset(0 100% 100% 0)}to{clip-path:inset(0 0 0 0)}}
@keyframes ms-poignee-in{from{opacity:0;transform:scale(0)}to{opacity:1;transform:scale(1)}}
@keyframes ms-fleche{0%{opacity:0;transform:translate(220px,180px)}25%{opacity:1}100%{opacity:1;transform:translate(0,0)}}
@keyframes ms-clic-fleche{0%,100%{transform:scale(1)}50%{transform:scale(0.8)}}
@keyframes ms-punch{0%{opacity:0;transform:scale(1.7)}55%{opacity:1;transform:scale(0.93)}78%{transform:scale(1.03)}100%{opacity:1;transform:scale(1)}}
@keyframes ms-frappe{from{max-width:0;opacity:0}to{max-width:1.4em;opacity:1}}
@keyframes ms-agrandie{from{transform:translate(var(--dx,0px),var(--dy,0px)) scale(0.4)}to{transform:translate(0,0) scale(1)}}
@keyframes ms-contre{from{transform:scale(2.5)}to{transform:scale(1)}}
@keyframes ms-efface{from{opacity:1}to{opacity:0}}
'''

FLECHE = ('<svg aria-hidden="true" viewBox="0 0 14 17"><path d="M1 1 L1 14 L4.5 10.8 L7 16 L9.4 15 L6.9 9.9 L11.6 9.9 Z" '
          'fill="#efefef" stroke="#0a0a0a" stroke-width="1"></path></svg>')
POIG = ''.join(f'<span class="ms-poignee ms-poignee--{c}"></span>' for c in ('hg', 'hd', 'bg', 'bd'))

def cap(t):
    t = t.lower()
    for i, c in enumerate(t):
        if c.isalpha():
            return t[:i] + c.upper() + t[i + 1:]
    return t

def mots_t(txt, t0, pas):
    out, t = [], t0
    for m in txt.split():
        out.append(f'<span class="ms-mot" style="--t:{t}ms">{html.escape(m)}</span>')
        t += pas
    return ' '.join(out), t

def frappe(txt, t0):
    out, t = [], t0
    for c in txt:
        out.append(f'<span class="ms-frappe" style="--t:{t}ms">{"&#160;" if c == " " else html.escape(c)}</span>')
        t += 55
    return ''.join(out), t

def croquis(v, am, mc, fin='', t0=0, dessus=False, dx=180, dy=160):
    """Le croquis en HTML, le temps (ms) du dernier élément, et les temps clés pour le son."""
    am, mc, fin = cap(am), cap(mc), fin.lower()
    cls = f'ms-croquis ms-{v}' + (' ms-croquis--dessus' if dessus else '')
    sons = {}
    if v == 'v3':
        a, t = frappe(am, t0 + 150); tk = t + 120
        k, t = frappe(mc, tk); t += 150
        f, t = frappe(fin, t) if fin else ('', t)
        sons = {'mot clé': tk}
        inner = (f'<span class="ms-amorce">{a}</span><span class="ms-cle"><span class="ms-motcle">{k}</span></span>'
                 + (f'<span class="ms-fin">{f}</span>' if fin else ''))
        return f'<div class="{cls}">{inner}</div>', t, sons
    if v == 'v4':
        a, t = mots_t(am, t0 + 100, 100); tk = t + 50
        f, tf = mots_t(fin, tk + 150, 100) if fin else ('', tk + 150)
        cadre = tf + 250; clic = cadre + 850; drag = clic + 80; lache = drag + 700
        sons = {'cadre': cadre, 'clic': clic, 'posé': lache}
        inner = (f'<span class="ms-amorce">{a}</span><span class="ms-cle" style="--t:{tk}ms"><span class="ms-motcle">{html.escape(mc)}</span></span>'
                 + (f'<span class="ms-fin">{f}</span>' if fin else ''))
        return (f'<div class="ms-agrandie" style="--dx:{dx}px;--dy:{dy}px;--cadre:{cadre}ms;--clic:{clic}ms;--drag:{drag}ms;--lache:{lache}ms">'
                f'<div class="{cls}">{inner}</div><span class="ms-cadre"></span>{POIG}<span class="ms-fleche"><span>{FLECHE}</span></span></div>'), lache + 300, sons
    a, t = mots_t(am, t0 + 100, 180); tk = t + 120 if am else t0 + 200
    if v == 'v1':
        clic = tk + 1300
        f, tf = mots_t(fin, clic + 250, 160) if fin else ('', clic)
        dernier = tf - 160 + 350 if fin else clic + 350
        sons = {'cadre': tk + 450, 'clic': clic}
        cle = f'<span class="ms-cle" style="--t:{tk}ms"><span class="ms-cadre"></span>{POIG}<span class="ms-fleche"><span>{FLECHE}</span></span><span class="ms-motcle">{html.escape(mc)}</span></span>'
    else:
        f, tf = mots_t(fin, tk + 450, 160) if fin else ('', tk + 450)
        dernier = tf - 160 + 400 if fin else tk + 450
        sons = {'mot clé': tk}
        cle = f'<span class="ms-cle" style="--t:{tk}ms"><span class="ms-motcle">{html.escape(mc)}</span></span>'
    inner = f'<span class="ms-amorce">{a}</span>{cle}' + (f'<span class="ms-fin">{f}</span>' if fin else '')
    return f'<div class="{cls}">{inner}</div>', dernier, sons

def bloc_croquis(v, am, mc, fin='', fmt='916', place='bas', bas=1560, haut=250, y=520, ech=1, t0=0, dessus=False,
                 tete_g=760, tete_d=950, dx=180, dy=160, tenue=1000):
    h, dernier, _ = croquis(v, am, mc, fin, t0, dessus, dx, dy)
    sortie = dernier + tenue
    if fmt == '916':
        cls = 'ms-bloc ms-bloc--916' + (' ms-bloc--haut' if place == 'haut' else '')
        st = f'--bas:{bas}px' if place != 'haut' else f'--haut:{haut}px'
    else:
        cls = f'ms-bloc ms-bloc--169 ms-bloc--cote ms-bloc--{place}'
        st = f'--y:{y}px;--tete-g:{tete_g}px;--tete-d:{tete_d}px'
    return f'<div class="{cls}" style="{st};--ech:{ech};--sortie:{sortie}ms">{h}</div>', sortie
