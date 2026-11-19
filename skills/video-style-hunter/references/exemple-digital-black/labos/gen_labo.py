# Planche « Labo du sous-titre » : on y règle ensemble police, composition, casse et animation,
# avec les 11 sons gardés, avant de reporter le résultat partout.
# v2 (8 novembre) : le croquis de Wanzt — amorce Arial à gauche, mot clé Anton braise,
# mot de fin Inter dessous à droite, cadre de sélection au choix.
import os, json, importlib.util, io, contextlib

ICI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("g", os.path.join(ICI, "gen.py"))
g = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(g)

W, H = 1720, 2440

DATA = f"""var SONS = {json.dumps(g.SONS, ensure_ascii=False)};
var TOUS = {json.dumps(g.TOUS)};
"""

SCRIPT = DATA + r"""
var AMORCES = [
  { n: 'Arial 400 · croquis', f: 'Arial, Arimo, sans-serif', w: 400, ls: '0em', t: 54 },
  { n: 'Arial 700', f: 'Arial, Arimo, sans-serif', w: 700, ls: '0em', t: 58 },
  { n: 'JetBrains Mono 500', f: "'JetBrains Mono', monospace", w: 500, ls: '-0.02em', t: 50 },
  { n: 'JetBrains Mono 700', f: "'JetBrains Mono', monospace", w: 700, ls: '-0.02em', t: 50 },
  { n: 'Inter 500', f: 'Inter, sans-serif', w: 500, ls: '-0.01em', t: 58 },
  { n: 'Inter 800', f: 'Inter, sans-serif', w: 800, ls: '-0.01em', t: 56 }
];
var MOTS = [
  { n: 'Anton · croquis', f: "'Anton', sans-serif", w: 400, s: 'normal', ls: '0em', t: 180 },
  { n: 'Google Sans Flex 800', f: "'Google Sans Flex', sans-serif", w: 800, s: 'normal', ls: '-0.03em', t: 170 },
  { n: 'Redaction 50 Italic', f: "'Redaction 50', serif", w: 400, s: 'italic', ls: '-0.01em', t: 200 },
  { n: 'Unbounded 900', f: "'Unbounded', sans-serif", w: 900, s: 'normal', ls: '-0.03em', t: 124 },
  { n: 'Space Mono 700 Italic', f: "'Space Mono', monospace", w: 700, s: 'italic', ls: '-0.04em', t: 160 },
  { n: 'Sixtyfour', f: "'Sixtyfour', monospace", w: 400, s: 'normal', ls: '-0.04em', t: 110 }
];
var FINS = [
  { n: 'Inter 400 · croquis', f: 'Inter, sans-serif', w: 400, ls: '0em', t: 54 },
  { n: 'Inter 500', f: 'Inter, sans-serif', w: 500, ls: '-0.01em', t: 58 },
  { n: 'Arial 400', f: 'Arial, Arimo, sans-serif', w: 400, ls: '0em', t: 60 },
  { n: 'JetBrains Mono 500', f: "'JetBrains Mono', monospace", w: 500, ls: '-0.02em', t: 50 }
];
var CASSES_MOT = [ { id: 'cap', n: 'Capitale + minuscules' }, { id: 'maj', n: 'MAJUSCULES' }, { id: 'min', n: 'minuscules' } ];
var CASSES_AM = [ { id: 'cap', n: 'Capitale + minuscules' }, { id: 'min', n: 'minuscules' }, { id: 'maj', n: 'MAJUSCULES' } ];
var COMPOS = [
  { id: 'croix', n: 'Croquis : amorce à gauche, fin dessous' }, { id: 'empile', n: 'Empilé centré' }, { id: 'dessus', n: 'Mot clé au-dessus' },
  { id: 'ligne', n: 'En ligne' }, { id: 'escalier', n: 'Escalier' }, { id: 'gauche', n: 'Aligné à gauche' }
];
var CADRES = [ { id: 'oui', n: 'Cadre gardé' }, { id: 'non', n: 'Cadre retiré après le clic' } ];
var COULEURS = [ { id: 'braise', n: 'Mot clé braise', c: '#FF7033' }, { id: 'os', n: 'Mot clé os', c: '#EFEFEF' } ];
var ANIMS = [
  { id: 'agrandie', n: 'Sélection puis agrandie' }, { id: 'tiree', n: 'Sélection tirée' }, { id: 'mot', n: 'Mot par mot + punch' }, { id: 'claque', n: 'Le mot qui claque' }, { id: 'glisse', n: 'Glisse du bas' },
  { id: 'surligne', n: 'Surligneur braise' }, { id: 'machine', n: 'Machine à écrire' }, { id: 'fondu', n: 'Fondu simple' }
];
var EASE = 'cubic-bezier(0.16, 1, 0.3, 1)';
var FORMATS = {
  '916': { n: '9:16 · Shorts', w: 1080, h: 1920, f: 1, utile: 920, zone: 360, zoneN: 'Interface des Shorts : titre, chaîne, musique', zoneF: 40, origine: '530px 1000px', img: '__FOND916__', vue: 0.5, vueW: 540, vueH: 960 },
  '169': { n: '16:9 · YouTube', w: 1920, h: 1080, f: 150 / 180, utile: 1600, zone: 100, zoneN: 'Barre de lecture YouTube', zoneF: 52, origine: '860px 560px', img: '__FOND169__', vue: 0.28125, vueW: 540, vueH: 304 }
};
var SORTIES = [ { id: 'flou', n: 'Flou rapide (0,3 s)' }, { id: 'coupe', n: 'Coupe sèche' }, { id: 'descend', n: 'Descend et s’efface' } ];
var MAX_AM = [3, 4, 5], MAX_FIN = [2, 3, 4];
var _cv = null;
function largeur(txt, P, t) {
  try {
    if (!_cv) { _cv = document.createElement('canvas').getContext('2d'); }
    _cv.font = (P.s && P.s !== 'normal' ? P.s + ' ' : '') + P.w + ' ' + t + 'px ' + P.f;
    return _cv.measureText(txt).width + (parseFloat(P.ls) || 0) * t * txt.length;
  } catch (e) { return txt.length * t * 0.5; }
}
/* ta tête sur le plan 16:9 de référence (1920 × 1080, mesurée sur ton détourage) */
var TETE = { x: 855, y: 525, demi: 95, haut: 425, menton: 625 };
function tete(k) { var ox = 860, oy = 560; return { x: ox + (TETE.x - ox) * k, demi: TETE.demi * k, haut: oy + (TETE.haut - oy) * k, menton: oy + (TETE.menton - oy) * k, y: oy + (TETE.y - oy) * k }; }
/* la colonne où vit le bloc : en 16:9, à gauche ou à droite de la tête, ou derrière toi */
function colonne(fmt, pos, k) {
  var Fo = FORMATS[fmt];
  if (fmt !== '169') { return { x0: (Fo.w - Fo.utile) / 2, x1: (Fo.w + Fo.utile) / 2 }; }
  var T = tete(k), g = 50;
  if (pos === 'gauche') { return { x0: 100, x1: Math.max(260, Math.round(T.x - T.demi - g)) }; }
  if (pos === 'droite') { return { x0: Math.min(1660, Math.round(T.x + T.demi + g)), x1: 1820 }; }
  return { x0: 160, x1: 1760 };
}
function nbMots(txt) { return txt.split(/\s+/).filter(function (x) { return x; }).length; }
/* la largeur du croquis : si le mot clé ne tient pas, il rétrécit jusqu'à 140 px (pour 180 px), puis l'alerte s'allume */
function mesure(st, fmt, ech, utile) {
  var A = AMORCES[st.fa], M = MOTS[st.fm], F = FINS[st.ff], mach = st.anim === 'machine';
  var amTxt = casse(st.amorce, st.casseAm), motTxt = casse(st.mot, st.casseMot), finTxt = st.fin.toLowerCase();
  var amW = largeur(amTxt, A, st.ta) + (mach ? 0 : nbMots(amTxt) * 0.28 * st.ta);
  var finW = finTxt ? largeur(finTxt, F, st.tf) + (mach ? 0 : nbMots(finTxt) * 0.28 * st.tf) + 18 : 0;
  var motNu = largeur(motTxt, M, st.tm);
  var S = FORMATS[fmt].f * ech / 100, dispo = (utile || FORMATS[fmt].utile) / S;
  var reste = dispo - amW - st.ecart - 36;
  /* croquis : si le mot clé ne tient pas à côté de l'amorce, l'amorce passe au-dessus, calée à gauche */
  var dessus = st.compo === 'croix' && amTxt && motNu > reste;
  var place = dessus ? dispo - 36 : reste;
  var tmMin = Math.round(st.tm * 140 / 180), tmEff = st.tm;
  if (motNu > place) { tmEff = Math.max(tmMin, Math.floor(st.tm * place / motNu)); }
  var motW = motNu * tmEff / st.tm + 36;
  var total = dessus ? Math.max(amW + 18, motW, finW) : amW + st.ecart + Math.max(motW, finW);
  var amH = amTxt ? st.ta * 1.1 : 0, motH = tmEff + 16, finH = finTxt ? st.tf * 0.95 : 0;
  return { tmEff: tmEff, tmMin: tmMin, reduit: tmEff < st.tm, dessus: dessus, trop: total > dispo + 1, largeur: total, hauteur: (dessus ? amH + motH : Math.max(amH, motH)) + finH,
    finTrop: finW > motW && (dessus ? finW : amW + st.ecart + finW) > dispo + 1, S: S };
}

function casse(txt, mode) {
  if (mode === 'maj') { return txt.toUpperCase(); }
  var t = txt.toLowerCase();
  if (mode === 'cap') { var i = t.search(/[a-zà-ÿ]/i); if (i >= 0) { t = t.slice(0, i) + t.charAt(i).toUpperCase() + t.slice(i + 1); } }
  return t;
}
function an(nom, ms, t, ease) { return nom + ' ' + ms + 'ms ' + (ease || EASE) + ' ' + Math.round(t * 1000) + 'ms both'; }
function nom(liste, id) { for (var i = 0; i < liste.length; i++) { if (liste[i].id === id) { return liste[i].n; } } return id; }
function pct(v) { return Math.round(v) + ' %'; }
function pill(on) { return { bg: on ? '#FF7033' : '#1E1E1E', fg: on ? '#0A0A0A' : '#EFEFEF', bd: on ? '#FF7033' : '#3A3A3A' }; }

/* le minutage : ce que fait chaque élément, et quand les sons partent */
function plan(st) {
  var a = st.anim;
  var amTxt = casse(st.amorce, st.casseAm), motTxt = casse(st.mot, st.casseMot), finTxt = st.fin.toLowerCase();
  var res = { am: [], mk: [], fn: [], tAm: [], tFin: [], tK: 0, fin: 0, scene: '', barre: 'none', noircit: '', masque: 'visible', lettres: a === 'machine' };
  function lettres(txt, t, liste, temps) {
    for (var k = 0; k < txt.length; k++) {
      var ch = txt.charAt(k);
      liste.push({ t: ch === ' ' ? ' ' : ch, anim: an('asLettre', 10, t, 'steps(1, end)'), m: '0' });
      if (temps && ch !== ' ') { temps.push(t); }
      t += 0.055;
    }
    return t;
  }
  function mots(txt, t0, pas, liste, temps) {
    var ms = txt.split(/\s+/).filter(function (x) { return x; });
    ms.forEach(function (m, i) {
      var t = t0 + i * pas;
      var anim = a === 'glisse' ? an('asMonte', 380, t) : (a === 'fondu' ? an('asFlouIn', 400, t) : an('asFlouIn', 350, t));
      liste.push({ t: m, anim: anim, m: '0 0.14em' });
      if (pas > 0 || i === 0) { temps.push(t); }
    });
    return t0 + ms.length * pas;
  }
  res.tire = '';
  if (a === 'agrandie') {
    /* V4 : le texte arrive petit, il est sélectionné, puis tiré et agrandi jusqu'à sa place */
    var ms_ = function (t) { return Math.round(t * 1000); };
    res.tK = mots(amTxt, 0.1, 0.1, res.am, res.tAm) + 0.05;
    res.mk.push({ t: motTxt.replace(/ /g, ' '), anim: an('asFlouIn', 300, res.tK) });
    var tF3 = finTxt ? mots(finTxt, res.tK + 0.15, 0.1, res.fn, res.tFin) : res.tK + 0.15;
    res.tCadre = tF3 + 0.25; res.tClic = res.tCadre + 0.85; res.tDrag = res.tClic + 0.08; res.tRel = res.tDrag + 0.7;
    var efface = 'asEfface 200ms ease-in ' + ms_(res.tRel + 0.1) + 'ms both';
    res.agr = true;
    res.agrCadre = an('asCadre', 300, res.tCadre) + ', ' + efface;
    res.agrPoignee = an('asPoignee', 160, res.tCadre + 0.3) + ', ' + efface;
    res.curseurVie = an('asCurseur', 420, res.tCadre + 0.35);
    res.curseurClic = an('asClic', 160, res.tClic, 'ease-out');
    res.agrAnim = 'asAgrandit 700ms cubic-bezier(0.65, 0, 0.35, 1) ' + ms_(res.tDrag) + 'ms both';
    res.agrContre = 'asAgrandit 700ms cubic-bezier(0.65, 0, 0.35, 1) ' + ms_(res.tDrag) + 'ms both, asEfface 200ms ease-in ' + ms_(res.tRel + 0.15) + 'ms both';
    res.braise = 'asBraiseMot 160ms linear ' + ms_(res.tRel) + 'ms both';
    res.dernier = res.tRel + 0.3;
    return sortie(res, st);
  }
  if (a === 'tiree') {
    var finAm2 = mots(amTxt, 0.1, 0.18, res.am, res.tAm);
    res.tK = finAm2 + 0.12;
    res.mk.push({ t: motTxt.replace(/ /g, ' '), anim: an('asFlouIn', 350, res.tK) });
    res.tCadre = res.tK + 0.45;
    res.tClic = res.tK + 1.3;
    res.curseurVie = an('asCurseur', 420, res.tK + 0.85);
    res.curseurClic = an('asClic', 160, res.tClic, 'ease-out');
    res.remplit = 'asRemplitFond 120ms linear ' + Math.round((res.tClic + 0.02) * 1000) + 'ms both';
    res.noircit = 'asNoircitMot 120ms linear ' + Math.round((res.tClic + 0.02) * 1000) + 'ms both';
    res.efface = 'asEfface 240ms ease-in ' + Math.round((res.tClic + 0.35) * 1000) + 'ms both';
    res.dernier = finTxt ? mots(finTxt, res.tClic + 0.25, 0.16, res.fn, res.tFin) - 0.16 + 0.35 : res.tClic + 0.35;
    return sortie(res, st);
  }
  if (a === 'machine') {
    var t = lettres(amTxt, 0.15, res.am, res.tAm) + 0.12;
    res.tK = t;
    t = lettres(motTxt, t, res.mk, null) + 0.15;
    if (finTxt) { t = lettres(finTxt, t, res.fn, res.tFin); }
    res.dernier = t;
  } else {
    var finAm = mots(amTxt, 0.1, a === 'mot' ? 0.18 : 0, res.am, res.tAm);
    res.tK = a === 'mot' ? finAm + 0.12 : (a === 'claque' ? 0.6 : (a === 'glisse' ? 0.3 : (a === 'fondu' ? 0.1 : 0.15)));
    var animK = a === 'glisse' ? an('asMonte', 420, res.tK) : (a === 'fondu' ? an('asFlouIn', 400, res.tK) : (a === 'surligne' ? an('asFlouIn', 350, res.tK) : an('asPunch', a === 'claque' ? 380 : 420, res.tK)));
    res.mk.push({ t: motTxt.replace(/ /g, ' '), anim: animK });
    if (a === 'claque') { res.scene = an('asTremble', 260, res.tK + 0.06, 'linear'); }
    if (a === 'glisse') { res.masque = 'hidden'; }
    if (a === 'surligne') { res.barre = 'block'; res.tK += 0.4; res.noircit = an('asNoircit', 120, res.tK + 0.17, 'linear'); }
    var tF = res.tK + (a === 'fondu' ? 0 : 0.45);
    var pasF = a === 'mot' ? 0.16 : 0;
    res.dernier = finTxt ? mots(finTxt, tF, pasF, res.fn, res.tFin) - pasF + 0.4 : res.tK + 0.45;
  }
  res.tCadre = res.tK + (a === 'machine' ? 0.1 : 0.3);
  return sortie(res, st);
}
/* la sortie : le bloc reste « tenue » secondes après le dernier mot, puis part */
function sortie(res, st) {
  var tenue = st.tenue == null ? 1 : st.tenue;
  res.tSortie = res.dernier + tenue;
  var ms = Math.round(res.tSortie * 1000);
  res.sortieAnim = st.sortie === 'coupe' ? 'asEfface 1ms linear ' + ms + 'ms both' :
    (st.sortie === 'descend' ? 'asDescend 380ms ease-in ' + ms + 'ms both' : 'asFlouOut 300ms ease-in ' + ms + 'ms both');
  res.fin = res.tSortie + 0.45;
  return res;
}

var CLES = ['amorce', 'mot', 'fin', 'fa', 'ta', 'fm', 'tm', 'ff', 'tf', 'casseMot', 'casseAm', 'cadre', 'compo', 'ecart', 'bas', 'couleur', 'anim',
  'sonAm', 'volAm', 'sonMot', 'volMot', 'sonCadre', 'volCadre', 'sonClic', 'volClic', 'tenue', 'sortie'];
var VARIANTES = [
  { nom: 'V1 · Croquis + sélection', amorce: 'Ton montage', mot: '1 heure', fin: 'par vidéo',
    fa: 0, ta: 54, fm: 0, tm: 180, ff: 0, tf: 54, casseMot: 'cap', casseAm: 'cap', cadre: 'oui',
    compo: 'croix', ecart: 10, bas: 340, couleur: 'braise', anim: 'tiree',
    sonAm: 'short-shutter-click', volAm: 30, sonMot: '', volMot: 45, sonCadre: 'gear-turn-click', volCadre: 40, sonClic: 'mouse-click', volClic: 60, tenue: 1, sortie: 'flou' },
  { nom: 'V2 · Croquis + punch', amorce: 'Et la première', mot: 'coûte', fin: 'très cher',
    fa: 0, ta: 54, fm: 0, tm: 180, ff: 0, tf: 54, casseMot: 'cap', casseAm: 'cap', cadre: 'non',
    compo: 'croix', ecart: 10, bas: 340, couleur: 'braise', anim: 'mot',
    sonAm: 'short-shutter-click', volAm: 30, sonMot: 'mouse-click', volMot: 45, sonCadre: '', volCadre: 40, sonClic: '', volClic: 60, tenue: 1, sortie: 'flou' },
  { nom: 'V3 · Croquis + machine à écrire', amorce: 'Garde le', mot: 'contrôle', fin: 'sur ton rythme',
    fa: 0, ta: 54, fm: 0, tm: 180, ff: 0, tf: 54, casseMot: 'cap', casseAm: 'cap', cadre: 'non',
    compo: 'croix', ecart: 10, bas: 340, couleur: 'braise', anim: 'machine',
    sonAm: 'gear-single-click', volAm: 25, sonMot: 'camera-shutter', volMot: 35, sonCadre: '', volCadre: 40, sonClic: '', volClic: 60, tenue: 1, sortie: 'flou' },
  { nom: 'V4 · Croquis + sélection agrandie', amorce: 'Le secret', mot: 'simple', fin: 'le rythme',
    fa: 0, ta: 54, fm: 0, tm: 180, ff: 0, tf: 54, casseMot: 'cap', casseAm: 'cap', cadre: 'non',
    compo: 'croix', ecart: 10, bas: 340, couleur: 'braise', anim: 'agrandie',
    sonAm: 'short-shutter-click', volAm: 30, sonMot: 'camera-shutter', volMot: 35, sonCadre: 'gear-turn-click', volCadre: 40, sonClic: 'mouse-click', volClic: 60, tenue: 1, sortie: 'flou' }
];
var PLANS = [
  { id: 'gros', n: 'Gros plan (visage)', img: { '916': 1.7, '169': 2.6 }, d: { '916': { ech: 80, pos: 'haut', h: 250 }, '169': { ech: 80, pos: 'gauche', h: 470 } } },
  { id: 'rapproche', n: 'Plan rapproché (poitrine)', img: { '916': 1, '169': 1.8 }, d: { '916': { ech: 100, pos: 'bas', h: 360 }, '169': { ech: 100, pos: 'gauche', h: 500 } } },
  { id: 'moyen', n: 'Plan moyen (taille)', img: { '916': 0.78, '169': 1.3 }, d: { '916': { ech: 105, pos: 'bas', h: 380 }, '169': { ech: 100, pos: 'droite', h: 510 } } },
  { id: 'large', n: 'Plan large (en pied)', img: { '916': 0.55, '169': 1 }, d: { '916': { ech: 108, pos: 'bas', h: 400 }, '169': { ech: 100, pos: 'derriere', h: 400 } } }
];
var POSITIONS = { '916': [ { id: 'bas', n: 'Sous le menton' }, { id: 'haut', n: 'Au-dessus de la tête' } ],
  '169': [ { id: 'gauche', n: 'À gauche de la tête' }, { id: 'droite', n: 'À droite de la tête' }, { id: 'derriere', n: 'Derrière toi' } ] };
function placeTxt(fmt, r) {
  if (fmt === '169') { return nom(POSITIONS['169'], r.pos).toLowerCase() + ', centre du bloc à ' + r.h + ' px du haut'; }
  return (r.pos === 'haut' ? 'au-dessus de la tête, haut du bloc à ' : 'sous le menton, bas du bloc à ') + r.h + ' px du ' + (r.pos === 'haut' ? 'haut' : 'bas');
}
function planDe(id) { for (var i = 0; i < PLANS.length; i++) { if (PLANS[i].id === id) { return PLANS[i]; } } return PLANS[1]; }
function copie(o) { var r = {}; CLES.forEach(function (k) { r[k] = o[k]; }); return r; }
function recetteDe(st) {
  var A = AMORCES[st.fa], M = MOTS[st.fm], F = FINS[st.ff];
  var net = function (n) { return n.replace(' · croquis', ''); };
  return 'Amorce : ' + net(A.n) + ', ' + st.ta + ' px, ' + nom(CASSES_AM, st.casseAm) +
    '  ·  Mot clé : ' + net(M.n) + ', ' + st.tm + ' px, ' + nom(CASSES_MOT, st.casseMot) + ', ' + (st.anim === 'tiree' ? 'blanc, puis noir sur fond braise au clic' : st.anim === 'agrandie' ? 'blanc, puis braise une fois posé' : (st.couleur === 'braise' ? 'braise' : 'os')) + ', ' + (st.cadre === 'oui' ? 'avec cadre de sélection' : 'sans cadre') +
    '  ·  Mot de fin : ' + (st.fin ? net(F.n) + ', ' + st.tf + ' px, minuscules' : 'aucun') +
    '  ·  Composition : ' + nom(COMPOS, st.compo) + ', écart ' + st.ecart + ' px' +
    '  ·  Animation : ' + nom(ANIMS, st.anim) +
    '  ·  Sons : amorce et fin ' + (st.sonAm ? SONS[st.sonAm].n + ' à ' + pct(st.volAm) : 'aucun') + ', ' + (st.anim === 'agrandie' ? 'mot posé ' : 'mot clé ') + (st.sonMot ? SONS[st.sonMot].n + ' à ' + pct(st.volMot) : 'aucun') +
    ((st.cadre === 'oui' || st.anim === 'tiree' || st.anim === 'agrandie') ? ', cadre ' + (st.sonCadre ? SONS[st.sonCadre].n + ' à ' + pct(st.volCadre) : 'aucun') : '') +
    (st.anim === 'tiree' || st.anim === 'agrandie' ? ', clic ' + (st.sonClic ? SONS[st.sonClic].n + ' à ' + pct(st.volClic) : 'aucun') : '') +
    '  ·  Sortie : ' + nom(SORTIES, st.sortie).toLowerCase() + ', ' + String(st.tenue).replace('.', ',') + ' s après le dernier mot';
}
class Component extends DCLogic {
  constructor(props) {
    super(props);
    var reg = { '916': {}, '169': {} }, self = this;
    PLANS.forEach(function (p) { ['916', '169'].forEach(function (f) { reg[f][p.id] = JSON.parse(JSON.stringify(p.d[f])); }); });
    this.state = Object.assign({ run: true, joue: false, err: '', copie: '', v: 0, suite: false, plan: 'rapproche', reg: reg,
      fmt: '916', zones: true, maxAm: 4, maxFin: 3, polices: 0, vars: VARIANTES.map(copie) }, copie(VARIANTES[0]));
    try {
      if (document.fonts && document.fonts.load) {
        Promise.all(['400 180px Anton', '400 54px Arimo', '400 54px Inter'].map(function (f) { return document.fonts.load(f); }))
          .then(function () { self.setState({ polices: 1 }); }, function () {});
      }
    } catch (e) {}
  }
  instantane() { var vars = this.state.vars.slice(); vars[this.state.v] = copie(this.state); return vars; }
  choisirVariante(i) {
    this.arreterSuite();
    var vars = this.instantane();
    this.setState(Object.assign({ vars: vars, v: i, copie: '' }, vars[i]));
  }
  arreterSuite() { (this._suite || []).forEach(function (t) { clearTimeout(t); }); this._suite = []; if (this.state.suite) { this.setState({ suite: false }); } }
  jouerSuite() {
    var self = this, vars = this.instantane(), attente = 0;
    this.arreterSuite();
    this.setState({ suite: true });
    vars.forEach(function (o, i) {
      self._suite.push(setTimeout(function () {
        self.setState(Object.assign({ vars: vars, v: i, copie: '' }, o));
        self._suite.push(setTimeout(function () { self.lancer(true); }, 80));
      }, attente));
      attente += (plan(o).fin + 0.6) * 1000;
    });
    self._suite.push(setTimeout(function () { self.setState({ suite: false }); }, attente));
  }
""" + g.MOTEUR + r"""
  lancer(depuisSuite) {
    var self = this, st = this.state;
    if (!depuisSuite) { this.arreterSuite(); }
    this.couper();
    this.ac();
    var p = plan(st);
    var sel = st.anim === 'tiree' || st.anim === 'agrandie', avecCadre = st.cadre === 'oui' || sel;
    var ids = [st.sonAm, st.sonMot, avecCadre ? st.sonCadre : '', sel ? st.sonClic : ''].filter(function (x, i, l) { return x && l.indexOf(x) === i; });
    Promise.all(ids.map(function (id) { return self.buf(id); })).then(function () {
      self.setState({ run: false, err: '' });
      self._tm.push(setTimeout(function () {
        var t0 = self.ac().currentTime + 0.03;
        self.setState({ run: true, joue: true });
        if (st.sonAm) { p.tAm.concat(p.tFin).forEach(function (t) { self.jouer(st.sonAm, t0 + t, st.volAm / 100); }); }
        if (st.sonMot) { self.jouer(st.sonMot, t0 + (st.anim === 'agrandie' ? p.tRel : p.tK), st.volMot / 100); }
        if (avecCadre && st.sonCadre) { self.jouer(st.sonCadre, t0 + p.tCadre, st.volCadre / 100, 0.3); }
        if (sel && st.sonClic) { self.jouer(st.sonClic, t0 + p.tClic, st.volClic / 100); }
        self._tm.push(setTimeout(function () { self.setState({ joue: false }); }, p.fin * 1000 + 100));
      }, 40));
    }).catch(function (e) { self.setState({ err: 'Le son ne se charge pas : ' + e.message }); });
  }
  regler(cle, val) {
    var reg = JSON.parse(JSON.stringify(this.state.reg)); reg[this.state.fmt][this.state.plan][cle] = val;
    this.setState({ reg: reg, copie: '' });
  }
  ecouter(id, vol) { if (id) { this.couper(); this.jouer(id, this.ac().currentTime + 0.02, vol / 100).catch(function () {}); } }
  recette() {
    var vars = this.instantane();
    var reg = this.state.reg;
    var st = this.state;
    var plans = ['916', '169'].map(function (f) {
      return 'Taille et place selon le plan, ' + FORMATS[f].n + ' — ' + PLANS.map(function (p) {
        var r = reg[f][p.id];
        return p.n + ' : ' + r.ech + ' % (mot clé ' + Math.round(180 * FORMATS[f].f * r.ech / 100) + ' px), ' + placeTxt(f, r);
      }).join('  ·  ');
    }).join('\n\n');
    var regles = 'Règles du texte — amorce : ' + st.maxAm + ' mots au plus  ·  mot clé : 1 ou 2 mots ; s’il ne tient pas à côté de l’amorce, l’amorce passe au-dessus, calée à gauche ; s’il ne tient toujours pas, il rétrécit jusqu’à 140 px (pour 180 px), sinon on change de mot  ·  mot de fin : ' + st.maxFin + ' mots au plus  ·  largeur utile : 920 px en 9:16 ; en 16:9, le texte est à gauche ou à droite de la tête (jamais dessus), ou derrière toi grâce au détourage  ·  zones interdites : 360 px du bas en 9:16 (interface des Shorts), 100 px du bas en 16:9 (barre de lecture)';
    return plans + '\n\n' + regles + '\n\n' + vars.map(function (o, i) { return 'Variante ' + (i + 1) + ' (' + VARIANTES[i].nom.split(' · ')[1] + ') — ' + recetteDe(o); }).join('\n\n');
  }
  copier() {
    var self = this, t = this.recette(), ok = false;
    var MANUEL = 'Pas copié : clique dans le cadre, Cmd+A puis Cmd+C';
    try { if (this._ta) { this._ta.focus(); this._ta.select(); ok = document.execCommand('copy'); } } catch (e) { ok = false; }
    if (ok) { this.setState({ copie: 'Copié' }); return; }
    try { navigator.clipboard.writeText(t).then(function () { self.setState({ copie: 'Copié' }); }, function () { self.setState({ copie: MANUEL }); }); }
    catch (e) { this.setState({ copie: MANUEL }); }
  }
  renderVals() {
    var self = this, st = this.state, A = AMORCES[st.fa], M = MOTS[st.fm], F = FINS[st.ff], p = plan(st);
    var c = st.compo, croix = c === 'croix';
    var Fo = FORMATS[st.fmt], R = st.reg[st.fmt][st.plan], k = planDe(st.plan).img[st.fmt], col = colonne(st.fmt, R.pos, k);
    var m = mesure(st, st.fmt, R.ech, col.x1 - col.x0), tmE = m.tmEff, T = tete(k), h169 = st.fmt === '169';
    var vw = m.largeur * m.S, vh = m.hauteur * m.S, fx, fy;
    if (h169) { fy = R.h; fx = R.pos === 'gauche' ? col.x1 - vw / 2 : (R.pos === 'droite' ? col.x0 + vw / 2 : (col.x0 + col.x1) / 2); }
    else { fx = Fo.w / 2; fy = R.pos === 'bas' ? Fo.h - R.h - vh / 2 : R.h + vh / 2; }
    var sx = h169 ? 960 : fx + 180, sy = h169 ? 820 : fy + 160;
    var alertes = [], nAm = nbMots(st.amorce), nMot = nbMots(st.mot), nFin = nbMots(st.fin);
    if (R.pos === 'bas' && R.h < Fo.zone) { alertes.push('Le bas du bloc est à ' + R.h + ' px du bas : il entre dans la zone « ' + Fo.zoneN.split(' :')[0] + ' ». Monte-le à ' + Fo.zone + ' px au moins.'); }
    if (h169 && R.pos !== 'derriere' && col.x1 - col.x0 < 420) { alertes.push('Il reste ' + (col.x1 - col.x0) + ' px ' + (R.pos === 'gauche' ? 'à gauche' : 'à droite') + ' de ta tête sur ce plan : prends l’autre côté, derrière toi, ou réduis la taille.'); }
    if (h169 && fy + vh / 2 > Fo.h - Fo.zone) { alertes.push('Le bas du bloc entre dans la barre de lecture YouTube : monte-le.'); }
    if (m.trop) { alertes.push(m.finTrop ? 'Le mot de fin est trop long pour la largeur : raccourcis-le.' : 'Le mot clé ne tient pas, même réduit à ' + Math.round(m.tmMin * m.S) + ' px : coupe-le ou change de mot.'); }
    if (nAm > st.maxAm) { alertes.push('Amorce : ' + nAm + ' mots, ' + st.maxAm + ' au plus.'); }
    if (nMot > 2) { alertes.push('Mot clé : ' + nMot + ' mots, 2 au plus.'); }
    if (nFin > st.maxFin) { alertes.push('Mot de fin : ' + nFin + ' mots, ' + st.maxFin + ' au plus.'); }
    var infos = ['Tailles à l’écran : amorce ' + Math.round(st.ta * m.S) + ' px · mot clé ' + Math.round(tmE * m.S) + ' px' + (m.reduit ? ' (réduit pour tenir)' : '') + ' · fin ' + Math.round(st.tf * m.S) + ' px',
      (m.dessus ? 'Amorce au-dessus : le mot clé ne tient pas à côté' : 'Amorce à gauche du mot clé') + (h169 ? ' · place disponible : ' + (col.x1 - col.x0) + ' px' : ''),
      'Mots : amorce ' + nAm + ' / ' + st.maxAm + ' · mot clé ' + nMot + ' / 2 · fin ' + nFin + ' / ' + st.maxFin];
    var dir = c === 'dessus' ? 'column-reverse' : (c === 'ligne' ? 'row' : 'column');
    var align = c === 'gauche' ? 'flex-start' : (c === 'escalier' ? 'stretch' : (c === 'ligne' ? 'baseline' : 'center'));
    var liste = function (l, cur, cle, parIndex) {
      return l.map(function (x, i) {
        var v = parIndex ? i : x.id, s = pill(v === cur);
        return { label: x.n, bg: s.bg, fg: s.fg, bd: s.bd, pick: function () {
          var o = {}; o[cle] = v; o.copie = '';
          if (cle === 'fa') { o.ta = AMORCES[i].t; }
          if (cle === 'fm') { o.tm = MOTS[i].t; }
          if (cle === 'ff') { o.tf = FINS[i].t; }
          self.setState(o);
        } };
      });
    };
    var sons = function (cur, cleSon, cleVol) {
      return [''].concat(TOUS).map(function (id) {
        var s = pill(id === cur);
        return { label: id ? SONS[id].n : 'Aucun', bg: s.bg, fg: s.fg, bd: s.bd,
          pick: function () { var o = {}; o[cleSon] = id; o.copie = ''; self.setState(o); self.ecouter(id, self.state[cleVol]); } };
      });
    };
    var slider = function (cle) { return function (ev) { var o = {}; o[cle] = Number(ev.target.value); o.copie = ''; self.setState(o); }; };
    var texte = function (cle) { return function (ev) { var o = {}; o[cle] = ev.target.value; o.copie = ''; self.setState(o); }; };
    return {
      run: st.run, boutonTxt: st.joue ? 'Rejouer' : 'Jouer avec le son', onPlay: function () { self.lancer(); },
      err: st.err, aErr: !!st.err,
      /* scène */
      sceneAnim: p.scene || 'none', blocAnim: p.sortieAnim,
      vueW: Fo.vueW, vueH: Fo.vueH, vue: Fo.vue, cw: Fo.w, ch: Fo.h, imgSrc: Fo.img, imgOrigine: Fo.origine, marge: (Fo.w - Fo.utile) / 2,
      zonesOn: st.zones, zoneH: Fo.zone, zoneN: Fo.zoneN, zoneF: Fo.zoneF,
      alertes: alertes.map(function (t) { return { t: t }; }), aAlertes: alertes.length > 0, sansAlerte: alertes.length === 0,
      infos: infos.map(function (t) { return { t: t }; }),
      blocDisplay: croix ? 'grid' : 'flex', blocCols: croix ? (m.dessus ? 'auto' : 'auto auto') : 'none',
      blocDir: dir, blocAlign: croix ? 'center' : align, blocBas: !h169 && R.pos === 'bas' ? R.h + 'px' : 'auto', blocHaut: h169 || R.pos === 'haut' ? R.h + 'px' : 'auto',
      blocTr: (h169 ? 'translateY(-50%) ' : '') + 'scale(' + m.S + ')', blocG: col.x0, blocL: col.x1 - col.x0,
      blocOrigine: h169 ? (R.pos === 'gauche' ? '100% 50%' : (R.pos === 'droite' ? '0% 50%' : '50% 50%')) : (R.pos === 'haut' ? '50% 0%' : '50% 100%'),
      blocAligneV: h169 ? 'center' : (R.pos === 'haut' ? 'flex-start' : 'flex-end'), blocJust: h169 && R.pos === 'gauche' ? 'flex-end' : (h169 && R.pos === 'droite' ? 'flex-start' : 'center'),
      aDetour: h169 && R.pos === 'derriere', aTete: h169 && st.zones, teteG: Math.round(T.x - T.demi), teteH: Math.round(T.haut), teteL: Math.round(2 * T.demi), teteHt: Math.round(T.menton - T.haut),
      aAgr: !!p.agr, agrTr: p.agr ? 'translate(' + Math.round((sx - fx) / m.S) + 'px, ' + Math.round((sy - fy) / m.S) + 'px) scale(0.4)' : 'none', agrAnim: p.agrAnim || 'none',
      agrCadre: p.agrCadre || 'none', agrPoignee: p.agrPoignee || 'none', agrContre: p.agrContre || 'none', imgEch: planDe(st.plan).img[st.fmt], blocEcart: st.ecart, blocTexte: c === 'gauche' ? 'left' : 'center',
      blocWrap: c === 'ligne' ? 'wrap' : 'nowrap', blocJustify: c === 'ligne' || croix ? 'center' : 'flex-start',
      amSelf: c === 'escalier' ? 'flex-start' : (croix ? (m.dessus ? 'end' : 'center') : 'auto'), amMarge: c === 'escalier' ? '40px' : (m.dessus ? '18px' : '0'), amJustifySelf: m.dessus ? 'start' : 'auto', amJustify: c === 'gauche' || c === 'escalier' ? 'flex-start' : 'center',
      amArea: croix ? '1 / 1' : 'auto', amBas: croix && !m.dessus ? Math.round(tmE * 0.18) : 0,
      mkSelf: c === 'escalier' ? 'flex-end' : 'auto', mkMarge: c === 'escalier' ? '40px' : '0', mkArea: croix ? (m.dessus ? '2 / 1' : '1 / 2') : 'auto',
      fnArea: croix ? (m.dessus ? '3 / 1' : '2 / 2') : 'auto', fnSelf: croix || c === 'escalier' ? 'flex-end' : (c === 'gauche' ? 'flex-start' : 'center'), fnJustifySelf: croix ? 'end' : 'auto',
      fnHaut: croix ? -Math.round(st.tf * 0.15) : 0,
      amF: A.f, amW: A.w, amT: st.ta, amLs: A.ls,
      mkF: M.f, mkW: M.w, mkS: M.s, mkT: tmE, mkLs: M.ls, mkC: st.anim === 'tiree' || st.anim === 'agrandie' ? '#EFEFEF' : (st.couleur === 'braise' ? '#FF7033' : '#EFEFEF'),
      fnF: F.f, fnW: F.w, fnT: st.tf, fnLs: F.ls, aFin: !!st.fin,
      amTokens: p.am, mkTokens: p.mk, fnTokens: p.fn, lettresAm: p.lettres ? 'flex-end' : 'baseline',
      masque: p.masque, barre: p.barre, noircit: p.noircit || p.braise || 'none', xs: Math.round(p.tK * 1000),
      aCadre: st.cadre === 'oui' || st.anim === 'tiree',
      cadreAnim: st.anim === 'tiree' ? an('asCadre', 300, p.tCadre) + (st.cadre === 'oui' ? '' : ', ' + p.efface) : an('asCadre', 300, p.tCadre),
      poigneeAnim: st.anim === 'tiree' ? an('asPoignee', 160, p.tCadre + 0.3) + (st.cadre === 'oui' ? '' : ', ' + p.efface) : an('asPoignee', 160, p.tCadre + 0.25),
      aCurseur: st.anim === 'tiree', tire: p.remplit || 'none', contre: 'none', curseurVie: p.curseurVie || 'none', curseurClic: p.curseurClic || 'none',
      /* réglages */
      amorce: st.amorce, mot: st.mot, fin: st.fin, onAmorce: texte('amorce'), onMot: texte('mot'), onFin: texte('fin'),
      policesAm: liste(AMORCES, st.fa, 'fa', true), policesMot: liste(MOTS, st.fm, 'fm', true), policesFin: liste(FINS, st.ff, 'ff', true),
      cassesAm: liste(CASSES_AM, st.casseAm, 'casseAm'), cassesMot: liste(CASSES_MOT, st.casseMot, 'casseMot'),
      compos: liste(COMPOS, st.compo, 'compo'), couleurs: liste(COULEURS, st.couleur, 'couleur'), anims: liste(ANIMS, st.anim, 'anim'), cadres: liste(CADRES, st.cadre, 'cadre'),
      ta: st.ta, tm: st.tm, tf: st.tf, ecart: st.ecart, bas: st.bas, volAm: st.volAm, volMot: st.volMot, volCadre: st.volCadre,
      taTxt: st.ta + ' px', tmTxt: st.tm + ' px', tfTxt: st.tf + ' px', ecartTxt: st.ecart + ' px', basTxt: st.bas + ' px',
      volAmTxt: pct(st.volAm), volMotTxt: pct(st.volMot), volCadreTxt: pct(st.volCadre),
      onTa: slider('ta'), onTm: slider('tm'), onTf: slider('tf'), onEcart: slider('ecart'), onBas: slider('bas'),
      onVolAm: slider('volAm'), onVolMot: slider('volMot'), onVolCadre: slider('volCadre'), onVolClic: slider('volClic'), volClic: st.volClic, volClicTxt: pct(st.volClic), sonsClic: sons(st.sonClic, 'sonClic', 'volClic'),
      sonsAm: sons(st.sonAm, 'sonAm', 'volAm'), sonsMot: sons(st.sonMot, 'sonMot', 'volMot'), sonsCadre: sons(st.sonCadre, 'sonCadre', 'volCadre'),
      recette: this.recette(), copie: st.copie, aCopie: !!st.copie,
      plans: PLANS.map(function (x) { var p2 = pill(x.id === st.plan); return { label: x.n, bg: p2.bg, fg: p2.fg, bd: p2.bd, pick: function () { self.setState({ plan: x.id, copie: '' }); } }; }),
      positions: POSITIONS[st.fmt].map(function (x) { var p2 = pill(x.id === R.pos); return { label: x.n, bg: p2.bg, fg: p2.fg, bd: p2.bd, pick: function () { self.regler('pos', x.id); } }; }),
      ech: R.ech, echTxt: R.ech + ' %', onEch: function (ev) { self.regler('ech', Number(ev.target.value)); },
      hauteur: R.h, hauteurTxt: R.h + ' px', onHauteur: function (ev) { self.regler('h', Number(ev.target.value)); },
      hauteurLabel: h169 ? 'Centre (haut)' : (R.pos === 'haut' ? 'Depuis le haut' : 'Depuis le bas'), aCadreSons: st.anim === 'tiree' || st.anim === 'agrandie',
      formats: ['916', '169'].map(function (f) { var p2 = pill(f === st.fmt); return { label: FORMATS[f].n, bg: p2.bg, fg: p2.fg, bd: p2.bd, pick: function () { self.setState({ fmt: f, copie: '' }); } }; }),
      zonesPills: [true, false].map(function (z) { var p2 = pill(z === st.zones); return { label: z ? 'Zones à éviter : affichées' : 'masquées', bg: p2.bg, fg: p2.fg, bd: p2.bd, pick: function () { self.setState({ zones: z }); } }; }),
      sorties: liste(SORTIES, st.sortie, 'sortie'), tenue: Math.round(st.tenue * 10), tenueTxt: String(st.tenue).replace('.', ',') + ' s',
      onTenue: function (ev) { self.setState({ tenue: Number(ev.target.value) / 10, copie: '' }); },
      maxAms: MAX_AM.map(function (n) { var p2 = pill(n === st.maxAm); return { label: n + ' mots', bg: p2.bg, fg: p2.fg, bd: p2.bd, pick: function () { self.setState({ maxAm: n, copie: '' }); } }; }),
      maxFins: MAX_FIN.map(function (n) { var p2 = pill(n === st.maxFin); return { label: n + ' mots', bg: p2.bg, fg: p2.fg, bd: p2.bd, pick: function () { self.setState({ maxFin: n, copie: '' }); } }; }),
      variantes: VARIANTES.map(function (x, i) { var p2 = pill(i === st.v); return { label: x.nom, bg: p2.bg, fg: p2.fg, bd: p2.bd, pick: function () { self.choisirVariante(i); } }; }),
      suiteTxt: st.suite ? 'Arrêter l’enchaînement' : 'Jouer les 4 à la suite',
      onSuite: function () { if (self.state.suite) { self.arreterSuite(); self.couper(); } else { self.jouerSuite(); } },
      varNom: VARIANTES[st.v].nom,
      setTa: function (el) { self._ta = el; }, onCopier: function () { self.copier(); }
    };
  }
}
"""

def pills(liste):
    return (f'<div style="display: flex; flex-wrap: wrap; gap: 6px"><sc-for list="{{{{{liste}}}}}" as="p" hint-placeholder-count="5">'
            '<button type="button" onClick="{{p.pick}}" style="padding: 6px 11px; min-height: 32px; border-radius: 999px; border: 1px solid {{p.bd}}; '
            'background: {{p.bg}}; color: {{p.fg}}; font-family: Inter, sans-serif; font-weight: 700; font-size: 13px; cursor: pointer">{{p.label}}</button></sc-for></div>')

def curseur(label, val, txt, on, mn, mx, pas):
    return (f'<label style="display: flex; align-items: center; gap: 12px; font-size: 13px; font-weight: 700; color: #A3A3A3"><span style="width: 92px">{label}</span>'
            f'<input type="range" min="{mn}" max="{mx}" step="{pas}" value="{{{{{val}}}}}" onChange="{{{{{on}}}}}" style="flex: 1; accent-color: #FF7033">'
            f'<span style="width: 60px; text-align: right; font-family: \'JetBrains Mono\', monospace; color: #EFEFEF">{{{{{txt}}}}}</span></label>')

def carte(titre, contenu, accent=False):
    bord = "#FF7033" if accent else "#2E2E2E"
    return (f'<div style="display: flex; flex-direction: column; gap: 10px; padding: 14px 16px; border: 1px solid {bord}; border-radius: 8px; background: #161616">'
            f'<div style="font-size: 16px; font-weight: 800; color: #EFEFEF">{titre}</div>{contenu}</div>')

def champ(label, val, on):
    return (f'<label style="display: flex; align-items: center; gap: 12px; font-size: 13px; font-weight: 700; color: #A3A3A3"><span style="width: 92px">{label}</span>'
            f'<input type="text" value="{{{{{val}}}}}" onChange="{{{{{on}}}}}" style="flex: 1; min-width: 0; min-height: 36px; padding: 6px 10px; border: 1px solid #3A3A3A; border-radius: 6px; '
            'background: #0A0A0A; color: #EFEFEF; font-family: Inter, sans-serif; font-size: 15px; font-weight: 700"></label>')

HALO = "text-shadow: 0 0 36px rgba(10,10,10,0.8), 0 2px 6px rgba(10,10,10,0.6)"
POIGNEES = "".join(
    f'<span style="position: absolute; {pos}; width: 18px; height: 18px; background: #EFEFEF; border: 3px solid #FF7033; box-sizing: border-box; animation: {{{{poigneeAnim}}}}"></span>'
    for pos in ["left: -9px; top: -9px", "right: -9px; top: -9px", "left: -9px; bottom: -9px", "right: -9px; bottom: -9px"])

SCENE = f"""<div style="position: relative; width: {{{{vueW}}}}px; height: {{{{vueH}}}}px; overflow: hidden; border-radius: 8px; border: 2px solid #3A3A3A; box-sizing: content-box; background: #1A1A1A">
<div style="position: absolute; left: 0; top: 0; width: {{{{cw}}}}px; height: {{{{ch}}}}px; transform: scale({{{{vue}}}}); transform-origin: 0 0">
<div style="position: absolute; inset: 0; animation: {{{{sceneAnim}}}}">
<img src="{{{{imgSrc}}}}" alt="" aria-hidden="true" style="position: absolute; inset: 0; width: {{{{cw}}}}px; height: {{{{ch}}}}px; object-fit: cover; display: block; filter: blur(40px) brightness(0.55); transform: scale(1.2)"><img src="{{{{imgSrc}}}}" alt="Image de ton rush, cadrée selon le plan choisi" style="position: absolute; inset: 0; width: {{{{cw}}}}px; height: {{{{ch}}}}px; object-fit: cover; display: block; transform-origin: {{{{imgOrigine}}}}; transform: scale({{{{imgEch}}}})">
<sc-if value="{{{{run}}}}" hint-placeholder-val="{{{{ true }}}}">
<div style="position: absolute; left: {{{{blocG}}}}px; width: {{{{blocL}}}}px; bottom: {{{{blocBas}}}}; top: {{{{blocHaut}}}}; transform: {{{{blocTr}}}}; transform-origin: {{{{blocOrigine}}}}; display: flex; justify-content: {{{{blocJust}}}}; align-items: {{{{blocAligneV}}}}">
<div style="position: relative; transform-origin: 50% 50%; transform: {{{{agrTr}}}}; animation: {{{{agrAnim}}}}">
<div style="display: {{{{blocDisplay}}}}; grid-template-columns: {{{{blocCols}}}}; flex-direction: {{{{blocDir}}}}; align-items: {{{{blocAlign}}}}; justify-content: {{{{blocJustify}}}}; flex-wrap: {{{{blocWrap}}}}; gap: 0 {{{{blocEcart}}}}px; text-align: {{{{blocTexte}}}}; animation: {{{{blocAnim}}}}">
<div style="grid-area: {{{{amArea}}}}; align-self: {{{{amSelf}}}}; justify-self: {{{{amJustifySelf}}}}; margin-left: {{{{amMarge}}}}; margin-bottom: {{{{amBas}}}}px; overflow: {{{{masque}}}}; display: flex; flex-wrap: nowrap; justify-content: {{{{amJustify}}}}; align-items: {{{{lettresAm}}}}; white-space: nowrap; font-family: {{{{amF}}}}; font-weight: {{{{amW}}}}; font-size: {{{{amT}}}}px; line-height: 1.1; letter-spacing: {{{{amLs}}}}; color: #EFEFEF; {HALO}">
<sc-for list="{{{{amTokens}}}}" as="x" hint-placeholder-count="3"><span style="display: inline-block; overflow: hidden; white-space: pre; margin: {{{{x.m}}}}; animation: {{{{x.anim}}}}">{{{{x.t}}}}</span></sc-for>
</div>
<div style="grid-area: {{{{mkArea}}}}; align-self: {{{{mkSelf}}}}; margin-right: {{{{mkMarge}}}}; position: relative; overflow: {{{{masque}}}}; padding: 8px 18px; transform-origin: 0 0; animation: {{{{tire}}}}">
<span style="display: {{{{barre}}}}; position: absolute; inset: 0; background: #FF7033; transform-origin: 0 50%; animation: asSurligne 320ms cubic-bezier(0.65, 0, 0.35, 1) {{{{xs}}}}ms both"></span>
<sc-if value="{{{{aCadre}}}}" hint-placeholder-val="{{{{ true }}}}"><span style="position: absolute; inset: 0; border: 3px solid #FF7033; animation: {{{{cadreAnim}}}}"></span>{POIGNEES}</sc-if>
<sc-if value="{{{{aCurseur}}}}" hint-placeholder-val="{{{{ false }}}}"><span style="position: absolute; right: -24px; bottom: -40px; width: 0; height: 0; z-index: 2"><span style="position: absolute; left: 0; top: 0; opacity: 0; animation: {{{{curseurVie}}}}"><svg aria-hidden="true" width="64" height="78" viewBox="0 0 14 17" style="display: block; transform-origin: 1px 1px; animation: {{{{curseurClic}}}}"><path d="M1 1 L1 14 L4.5 10.8 L7 16 L9.4 15 L6.9 9.9 L11.6 9.9 Z" fill="#EFEFEF" stroke="#0A0A0A" stroke-width="1"></path></svg></span></span></sc-if>
<div style="position: relative; display: flex; align-items: flex-end; font-family: {{{{mkF}}}}; font-weight: {{{{mkW}}}}; font-style: {{{{mkS}}}}; font-size: {{{{mkT}}}}px; line-height: 1; letter-spacing: {{{{mkLs}}}}; color: {{{{mkC}}}}; {HALO}; white-space: nowrap; animation: {{{{noircit}}}}">
<sc-for list="{{{{mkTokens}}}}" as="x" hint-placeholder-count="1"><span style="display: inline-block; overflow: hidden; white-space: pre; animation: {{{{x.anim}}}}">{{{{x.t}}}}</span></sc-for>
</div>
</div>
<sc-if value="{{{{aFin}}}}" hint-placeholder-val="{{{{ true }}}}">
<div style="grid-area: {{{{fnArea}}}}; align-self: {{{{fnSelf}}}}; justify-self: {{{{fnJustifySelf}}}}; margin-top: {{{{fnHaut}}}}px; margin-right: 18px; overflow: {{{{masque}}}}; display: flex; flex-wrap: nowrap; align-items: {{{{lettresAm}}}}; white-space: nowrap; font-family: {{{{fnF}}}}; font-weight: {{{{fnW}}}}; font-size: {{{{fnT}}}}px; line-height: 1.1; letter-spacing: {{{{fnLs}}}}; color: #EFEFEF; {HALO}">
<sc-for list="{{{{fnTokens}}}}" as="x" hint-placeholder-count="2"><span style="display: inline-block; overflow: hidden; white-space: pre; margin: {{{{x.m}}}}; animation: {{{{x.anim}}}}">{{{{x.t}}}}</span></sc-for>
</div>
</sc-if>
</div>
<sc-if value="{{{{aAgr}}}}" hint-placeholder-val="{{{{ false }}}}"><span style="position: absolute; inset: -18px; border: 5px solid #FF7033; animation: {{{{agrCadre}}}}"></span><span style="position: absolute; left: -30px; top: -30px; width: 24px; height: 24px; background: #EFEFEF; border: 4px solid #FF7033; box-sizing: border-box; animation: {{{{agrPoignee}}}}"></span><span style="position: absolute; right: -30px; top: -30px; width: 24px; height: 24px; background: #EFEFEF; border: 4px solid #FF7033; box-sizing: border-box; animation: {{{{agrPoignee}}}}"></span><span style="position: absolute; left: -30px; bottom: -30px; width: 24px; height: 24px; background: #EFEFEF; border: 4px solid #FF7033; box-sizing: border-box; animation: {{{{agrPoignee}}}}"></span><span style="position: absolute; right: -30px; bottom: -30px; width: 24px; height: 24px; background: #EFEFEF; border: 4px solid #FF7033; box-sizing: border-box; animation: {{{{agrPoignee}}}}"></span><span style="position: absolute; right: -30px; bottom: -30px; width: 0; height: 0; z-index: 3; transform-origin: 0 0; transform: scale(2.5); animation: {{{{agrContre}}}}"><span style="position: absolute; left: -4px; top: -4px; opacity: 0; animation: {{{{curseurVie}}}}"><svg aria-hidden="true" width="64" height="78" viewBox="0 0 14 17" style="display: block; transform-origin: 1px 1px; animation: {{{{curseurClic}}}}"><path d="M1 1 L1 14 L4.5 10.8 L7 16 L9.4 15 L6.9 9.9 L11.6 9.9 Z" fill="#EFEFEF" stroke="#0A0A0A" stroke-width="1"></path></svg></span></span></sc-if>
</div>
</div>
</sc-if>
<sc-if value="{{{{aDetour}}}}" hint-placeholder-val="{{{{ false }}}}"><img src="__DETOUR169__" alt="" aria-hidden="true" style="position: absolute; inset: 0; width: {{{{cw}}}}px; height: {{{{ch}}}}px; display: block; transform-origin: {{{{imgOrigine}}}}; transform: scale({{{{imgEch}}}})"></sc-if>
<sc-if value="{{{{aTete}}}}" hint-placeholder-val="{{{{ false }}}}"><div style="position: absolute; left: {{{{teteG}}}}px; top: {{{{teteH}}}}px; width: {{{{teteL}}}}px; height: {{{{teteHt}}}}px; box-sizing: border-box; border: 4px dashed rgba(239,239,239,0.7); border-radius: 45%; display: flex; align-items: flex-start; justify-content: center"><span style="margin-top: -46px; font: 800 30px Inter, sans-serif; color: #EFEFEF; text-shadow: 0 2px 8px rgba(10,10,10,0.8)">ta tête</span></div></sc-if>
<sc-if value="{{{{zonesOn}}}}" hint-placeholder-val="{{{{ true }}}}"><div style="position: absolute; left: 0; right: 0; bottom: 0; height: {{{{zoneH}}}}px; box-sizing: border-box; border-top: 4px dashed #EFEFEF; background: repeating-linear-gradient(45deg, rgba(239,239,239,0.22) 0 16px, rgba(239,239,239,0.06) 16px 32px); display: flex; align-items: center; justify-content: center; padding: 0 40px; text-align: center; font-family: Inter, sans-serif; font-weight: 800; font-size: {{{{zoneF}}}}px; line-height: 1.1; color: #EFEFEF; text-shadow: 0 2px 8px rgba(10,10,10,0.8)">{{{{zoneN}}}}</div></sc-if>
</div>
</div>
</div>"""

VARIANTES_CARTE = (
    '<div style="grid-column: 1 / -1; display: flex; flex-direction: column; gap: 10px; padding: 14px 16px; border: 2px solid #FF7033; border-radius: 8px; background: #1A120E">'
    '<div style="display: flex; align-items: center; justify-content: space-between; gap: 12px"><div style="font-size: 16px; font-weight: 800; color: #EFEFEF">Variantes à alterner dans la vidéo</div>'
    '<button type="button" onClick="{{onSuite}}" style="min-height: 36px; padding: 6px 14px; border: 0; border-radius: 6px; background: #FF7033; color: #0A0A0A; font-family: Inter, sans-serif; font-weight: 800; font-size: 13px; cursor: pointer">{{suiteTxt}}</button></div>'
    + pills("variantes") +
    '<div style="font-size: 13px; line-height: 1.45; color: #A3A3A3">Même croquis, même trio de polices et mêmes couleurs ; seule l’animation change. Les réglages ci-dessous modifient la variante choisie.</div></div>')
PLAN_CARTE = (
    '<div style="grid-column: 1 / -1; display: flex; flex-direction: column; gap: 10px; padding: 14px 16px; border: 1px solid #FF7033; border-radius: 8px; background: #161616">'
    '<div style="font-size: 16px; font-weight: 800; color: #EFEFEF">Le plan et la taille du sous-titre</div>'
    + pills("formats") + pills("plans") + pills("positions")
    + curseur("Taille", "ech", "echTxt", "onEch", 50, 150, 5)
    + '<label style="display: flex; align-items: center; gap: 12px; font-size: 13px; font-weight: 700; color: #A3A3A3"><span style="width: 92px">{{hauteurLabel}}</span>'
      '<input type="range" min="80" max="1000" step="10" value="{{hauteur}}" onChange="{{onHauteur}}" style="flex: 1; accent-color: #FF7033">'
      '<span style="width: 60px; text-align: right; font-family: \'JetBrains Mono\', monospace; color: #EFEFEF">{{hauteurTxt}}</span></label>'
    + '<div style="font-size: 13px; line-height: 1.45; color: #A3A3A3">Chaque format et chaque plan gardent leur taille et leur place, pour les 4 variantes. En 16:9, le texte va à gauche ou à droite de ta tête, ou derrière toi. 100 % = la recette (9:16 : amorce 54 px, mot clé 180 px ; 16:9 : 45 et 150 px). L’image est recadrée pour simuler le plan.</div></div>')
DROITE = "".join([
    VARIANTES_CARTE,
    PLAN_CARTE,
    carte("Le texte", champ("Amorce", "amorce", "onAmorce") + champ("Mot clé", "mot", "onMot") + champ("Mot de fin", "fin", "onFin")),
    carte("Règles du texte",
          '<div style="font-size: 13px; font-weight: 700; color: #A3A3A3">Amorce : mots au plus</div>' + pills("maxAms") +
          '<div style="font-size: 13px; font-weight: 700; color: #A3A3A3">Mot de fin : mots au plus</div>' + pills("maxFins") +
          '<div style="font-size: 13px; line-height: 1.45; color: #A3A3A3">Mot clé : 1 ou 2 mots. S’il ne tient pas à côté de l’amorce, l’amorce passe au-dessus. S’il ne tient toujours pas, il rétrécit jusqu’à 140 px (pour 180 px) ; au-delà, l’alerte s’allume.</div>'),
    carte("La sortie (variante choisie)", pills("sorties") + curseur("Tenue", "tenue", "tenueTxt", "onTenue", 4, 40, 1) +
          '<div style="font-size: 13px; line-height: 1.45; color: #A3A3A3">Tenue = temps à l’écran après le dernier mot. Dans la vidéo, le sous-titre part plus tôt si la phrase suivante commence.</div>'),
    carte("Son de l’amorce et du mot de fin", pills("sonsAm") + curseur("Volume", "volAm", "volAmTxt", "onVolAm", 0, 100, 5)),
    carte("Son du mot clé (V4 : quand il se pose)", pills("sonsMot") + curseur("Volume", "volMot", "volMotTxt", "onVolMot", 0, 100, 5)),
    '<sc-if value="{{aCadreSons}}" hint-placeholder-val="{{ true }}">' +
    carte("Son du cadre de sélection (V1, V4)", pills("sonsCadre") + curseur("Volume", "volCadre", "volCadreTxt", "onVolCadre", 0, 100, 5)) +
    carte("Son du clic (V1, V4)", pills("sonsClic") + curseur("Volume", "volClic", "volClicTxt", "onVolClic", 0, 100, 5)) +
    '</sc-if>',
])

RECETTE = """<div style="display: flex; flex-direction: column; gap: 8px; padding: 14px 16px; border-radius: 8px; background: #EFEFEF; color: #0A0A0A">
<div style="display: flex; align-items: center; justify-content: space-between; gap: 12px">
<div style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #5A5A5A">Ta recette · copie-la et envoie-la-moi</div>
<div style="display: flex; align-items: center; gap: 10px">
<sc-if value="{{aCopie}}" hint-placeholder-val="{{ false }}"><span style="font-size: 13px; font-weight: 700; color: #5A5A5A">{{copie}}</span></sc-if>
<button type="button" onClick="{{onCopier}}" style="min-height: 36px; padding: 6px 14px; border: 0; border-radius: 6px; background: #0A0A0A; color: #EFEFEF; font-family: Inter, sans-serif; font-weight: 800; font-size: 13px; cursor: pointer">Copier la recette</button>
</div>
</div>
<textarea readonly="readonly" ref="{{setTa}}" value="{{recette}}" aria-label="Ta recette de sous-titre" rows="25" style="width: 100%; box-sizing: border-box; resize: none; padding: 8px 10px; border: 1px solid #BDBDBD; border-radius: 6px; background: #FFFFFF; color: #0A0A0A; font-family: Inter, sans-serif; font-size: 14px; line-height: 1.45; font-weight: 700"></textarea>
</div>"""

corps = f"""<div style="width: {W}px; height: {H}px; box-sizing: border-box; padding: 44px 48px; background: #121212; color: #EFEFEF; font-family: Inter, sans-serif; display: flex; flex-direction: column; gap: 24px; overflow: hidden">
<div style="display: flex; flex-direction: column; gap: 10px">
<div style="display: flex; align-items: center; gap: 12px"><span style="display: inline-block; width: 14px; height: 14px; background: #FF7033"></span><span style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 15px; letter-spacing: 0.08em; text-transform: uppercase; color: #A3A3A3">Animation caption et son · labo · 9:16 et 16:9</span></div>
<h1 style="margin: 0; font-family: 'Big Shoulders Display', sans-serif; font-weight: 900; font-size: 60px; line-height: 0.95; letter-spacing: 0.01em; text-transform: uppercase">Labo du sous-titre</h1>
<p style="margin: 0; max-width: 1500px; font-size: 18px; line-height: 1.45; font-weight: 500; color: #A3A3A3">Ta recette : Arial / Anton / Inter dans ton croquis, en quatre variantes à alterner (V1 sélection, V2 punch, V3 machine à écrire, V4 sélection agrandie). Choisis le plan pour régler la taille et la place du sous-titre, puis copie la recette.</p>
</div>
<div style="display: flex; gap: 36px; align-items: flex-start">
<div style="display: flex; flex-direction: column; gap: 12px; width: 544px; flex-shrink: 0">
{SCENE}
<button type="button" onClick="{{{{onPlay}}}}" style="display: flex; align-items: center; justify-content: center; gap: 12px; min-height: 56px; border: 0; border-radius: 8px; background: #FF7033; color: #0A0A0A; font-family: Inter, sans-serif; font-weight: 800; font-size: 18px; cursor: pointer"><svg aria-hidden="true" width="16" height="18" viewBox="0 0 16 18"><path d="M1 1 L15 9 L1 17 Z" fill="#0A0A0A"></path></svg>{{{{boutonTxt}}}}</button>
<sc-if value="{{{{aErr}}}}" hint-placeholder-val="{{{{ false }}}}"><p style="margin: 0; font-size: 14px; color: #FF7033">{{{{err}}}}</p></sc-if>
<div style="display: flex; flex-direction: column; gap: 8px; padding: 14px 16px; border-radius: 8px; background: #161616; border: 1px solid #2E2E2E">
<div style="font-size: 16px; font-weight: 800; color: #EFEFEF">Contrôles</div>
{pills("zonesPills")}
<sc-if value="{{{{sansAlerte}}}}" hint-placeholder-val="{{{{ true }}}}"><div style="font-size: 14px; font-weight: 700; color: #EFEFEF">Tout tient : zones, largeur et nombre de mots.</div></sc-if>
<sc-for list="{{{{alertes}}}}" as="x" hint-placeholder-count="1"><div style="display: flex; gap: 8px; align-items: flex-start; font-size: 14px; line-height: 1.4; font-weight: 700; color: #FF7033"><span aria-hidden="true">▲</span><span>{{{{x.t}}}}</span></div></sc-for>
<sc-for list="{{{{infos}}}}" as="x" hint-placeholder-count="2"><div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; line-height: 1.5; color: #A3A3A3">{{{{x.t}}}}</div></sc-for>
</div>
</div>
<div style="flex: 1; min-width: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; align-items: start">
{DROITE}
<div style="grid-column: 1 / -1">{RECETTE}</div>
</div>
</div>
</div>"""

def kf_tirage(dx=-230, dy=-1000, s0=0.3, pas=20):
    def e(t):
        return 4 * t ** 3 if t < 0.5 else 1 - (-2 * t + 2) ** 3 / 2
    tire, contre = [], []
    for i in range(pas + 1):
        t = i / pas; v = e(t); s_ = s0 + (1 - s0) * v
        tire.append(f"{t*100:.1f}%{{transform:translate({dx*(1-v):.1f}px,{dy*(1-v):.1f}px) scale({s_:.4f})}}")
        contre.append(f"{t*100:.1f}%{{transform:scale({1/s_:.4f})}}")
    return ("@keyframes asTire{" + "".join(tire) + "}\n@keyframes asContre{" + "".join(contre) + "}\n"
            "@keyframes asAgrandit{to{transform:none}}\n@keyframes asBraiseMot{to{color:#FF7033}}\n@keyframes asDescend{to{opacity:0;transform:translateY(70px)}}\n@keyframes asApparait{from{opacity:0}to{opacity:1}}\n@keyframes asEfface{from{opacity:1}to{opacity:0}}\n"
            "@keyframes asCurseurVie{0%{opacity:0}8%{opacity:1}85%{opacity:1}100%{opacity:0}}\n"
            "@keyframes asRemplitFond{to{background:#FF7033}}\n@keyframes asNoircitMot{to{color:#0A0A0A;text-shadow:none}}\n")

FOND169 = "/_blob/dd6937f0aa6191cc2aa5331f48d3a914"
DETOUR169 = "/_blob/8044d9952f1361ea9b673f1c6c5ce21f"
SCRIPT = SCRIPT.replace("__FOND916__", g.FOND).replace("__FOND169__", FOND169)
corps = corps.replace("__DETOUR169__", DETOUR169)
doc = g.doc("Labo du sous-titre", corps, SCRIPT, W, H)
doc = doc.replace("@keyframes asFlouIn", kf_tirage() + "@keyframes asFlouIn", 1)
# polices du croquis : Anton, Arimo (le double libre d'Arial), Inter 400
doc = doc.replace("&amp;family=Google+Sans+Flex:wght@800&amp;display=swap",
                  "&amp;family=Google+Sans+Flex:wght@800&amp;family=Anton&amp;family=Arimo:wght@400;700&amp;display=swap", 1).replace("family=Inter:wght@500;700;800", "family=Inter:wght@400;500;700;800", 1)
assert "family=Anton" in doc
open(os.path.join(ICI, "project", "AS-Labo.dc.html"), "w").write(doc)
loc = (doc.replace('<script src="./support.js"></script>', '').replace(g.FOND, "fond-8.jpg").replace(FOND169, "fond-169.jpg").replace(DETOUR169, "detour-169.png")
       .replace("/_blob/113612acc014ae1a0af417b8f8c1c679", "redaction-50-latin-400-italic.woff2").replace("</body>", '<script src="mini-dc.js?v=3"></script></body>'))
open(os.path.join(ICI, "test-labo.html"), "w").write(loc)
print("ok", len(doc))
