# Planche « Labo des textes » (8 novembre) : les textes du design system hors sous-titre
# (titre d'accroche, mot géant, scène texte plein écran, étiquettes et chiffres, logo),
# testés avec le trio Arial / Anton / Inter avant la mise à jour du design system.
import os, json, importlib.util, io, contextlib

ICI = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("g", os.path.join(ICI, "gen.py"))
g = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(g)

W, H = 1720, 1420
FOND169 = "/_blob/dd6937f0aa6191cc2aa5331f48d3a914"

SCRIPT = f"var SONS = {json.dumps(g.SONS, ensure_ascii=False)};\n" + r"""
var FORMATS = {
  '916': { n: '9:16 · Shorts', w: 1080, h: 1920, f: 1, utile: 920, img: '__FOND916__', vue: 0.5, vueW: 540, vueH: 960 },
  '169': { n: '16:9 · YouTube', w: 1920, h: 1080, f: 150 / 180, utile: 1600, img: '__FOND169__', vue: 0.28125, vueW: 540, vueH: 304 }
};
var POL = {
  anton: { n: 'Anton', f: "'Anton', sans-serif", w: 400, ls: '0em', lh: 1 },
  doto: { n: 'Doto 900 (actuel)', f: "'Doto', monospace", w: 900, ls: '-0.04em', lh: 0.9 },
  arial4: { n: 'Arial 400', f: 'Arial, Arimo, sans-serif', w: 400, ls: '0em', lh: 1.1 },
  arial7: { n: 'Arial 700', f: 'Arial, Arimo, sans-serif', w: 700, ls: '0em', lh: 1.1 },
  inter8: { n: 'Inter 800 (actuel)', f: 'Inter, sans-serif', w: 800, ls: '-0.02em', lh: 1.05 },
  inter6: { n: 'Inter 600', f: 'Inter, sans-serif', w: 600, ls: '0.06em', lh: 1.2 },
  jet: { n: 'JetBrains Mono 600 (actuel)', f: "'JetBrains Mono', monospace", w: 600, ls: '0.08em', lh: 1.2 },
  bs: { n: 'Big Shoulders 900 (actuel)', f: "'Big Shoulders Display', sans-serif", w: 900, ls: '0.01em', lh: 0.95 }
};
var ELEMENTS = [
  { id: 'accroche', n: 'Titre d’accroche' }, { id: 'motgeant', n: 'Mot géant seul' }, { id: 'scene', n: 'Scène texte plein écran' },
  { id: 'etiq', n: 'Étiquettes et chiffres' }, { id: 'logo', n: 'Logo et titres de partie' }
];
var DEFAUTS = {
  accroche: { amorce: 'Les erreurs qui coûtent', titre: '5', police: 'anton', couleur: 'braise', taille: 420, pos: 'haut', h: 140, pos169: 'gauche', h169: 480, anim: 'punch' },
  motgeant: { titre: 'Contrôle', police: 'anton', couleur: 'braise', taille: 240, pos: 'bas', h: 420, pos169: 'droite', h169: 500, anim: 'agrandie' },
  scene: { avant: 'Le montage qui', mot: 'Explose', apres: 'tes vues', policePh: 'arial7', taillePh: 110, policeMot: 'anton', tailleMot: 260, fond: 'noir' },
  etiq: { titre: 'Ventes · novembre', chiffre: '+240 %', policeEt: 'jet', tailleEt: 28, policeCh: 'anton', couleurCh: 'braise', tailleCh: 240 },
  logo: { police: 'bs', carre: 'nouvelle', taille: 120, fond: 'noir' }
};
var CHOIX = {
  police: ['anton', 'doto'], policeMot: ['anton', 'doto'], policePh: ['arial4', 'arial7', 'inter8'], policeEt: ['jet', 'inter6', 'arial7'],
  policeCh: ['anton', 'doto', 'arial7'], policeLogo: ['bs', 'anton']
};
var ANIMS = [ { id: 'punch', n: 'Punch (comme V2)' }, { id: 'selection', n: 'Sélection (comme V1)' }, { id: 'machine', n: 'Machine à écrire (comme V3)' }, { id: 'agrandie', n: 'Sélection puis agrandie (comme V4)' } ];
var COULEURS = [ { id: 'braise', n: 'Braise' }, { id: 'os', n: 'Os' } ];
var POSITIONS = [ { id: 'haut', n: 'Au-dessus de la tête' }, { id: 'bas', n: 'Sous le menton' } ];
var POSITIONS169 = [ { id: 'gauche', n: 'À gauche de la tête' }, { id: 'droite', n: 'À droite de la tête' }, { id: 'derriere', n: 'Derrière toi' } ];
/* ta tête sur le plan 16:9 (mesurée sur ton détourage) et la colonne libre de chaque côté */
var TETE = { x: 855, demi: 95 };
function colonne169(pos) {
  if (pos === 'gauche') { return { x0: 100, x1: TETE.x - TETE.demi - 50 }; }
  if (pos === 'droite') { return { x0: TETE.x + TETE.demi + 50, x1: 1820 }; }
  return { x0: 160, x1: 1760 };
}
var FONDS = [ { id: 'noir', n: 'Fond noir' }, { id: 'blanc', n: 'Fond blanc' } ];
var CARRES = [ { id: 'ancienne', n: 'Carré #FF4D00 (actuel)', c: '#FF4D00' }, { id: 'nouvelle', n: 'Carré braise #FF7033', c: '#FF7033' } ];
var EASE = 'cubic-bezier(0.16, 1, 0.3, 1)';
var HALO = '0 0 36px rgba(10,10,10,0.8), 0 2px 6px rgba(10,10,10,0.6)';

function casse(txt) { var t = txt.toLowerCase(), i = t.search(/[a-zà-ÿ]/i); return i >= 0 ? t.slice(0, i) + t.charAt(i).toUpperCase() + t.slice(i + 1) : t; }
function an(nom, ms, t, ease) { return nom + ' ' + ms + 'ms ' + (ease || EASE) + ' ' + Math.round(t * 1000) + 'ms both'; }
function pill(on) { return { bg: on ? '#FF7033' : '#1E1E1E', fg: on ? '#0A0A0A' : '#EFEFEF', bd: on ? '#FF7033' : '#3A3A3A' }; }
function nomDe(liste, id) { for (var i = 0; i < liste.length; i++) { if (liste[i].id === id) { return liste[i].n; } } return id; }
function mots(txt) { return txt.split(/\s+/).filter(function (x) { return x; }); }
var _cv = null;
function largeur(txt, P, t) {
  try {
    if (!_cv) { _cv = document.createElement('canvas').getContext('2d'); }
    _cv.font = P.w + ' ' + t + 'px ' + P.f;
    return _cv.measureText(txt).width + (parseFloat(P.ls) || 0) * t * txt.length;
  } catch (e) { return txt.length * t * 0.5; }
}
function lettres(txt, t, liste, sons, son) {
  for (var k = 0; k < txt.length; k++) {
    var ch = txt.charAt(k);
    liste.push({ t: ch, anim: an('asLettre', 10, t, 'steps(1, end)'), m: '0' });
    if (son && ch !== ' ') { sons.push({ id: son.id, t: t, vol: son.vol }); }
    t += 0.055;
  }
  return t;
}
function motsEnFlou(txt, t0, pas, liste, sons, son) {
  mots(txt).forEach(function (m, i) {
    liste.push({ t: m, anim: an('asFlouIn', 350, t0 + i * pas), m: '0 0.14em' });
    if (son) { sons.push({ id: son.id, t: t0 + i * pas, vol: son.vol }); }
  });
  return t0 + mots(txt).length * pas;
}
/* titre d'accroche et mot géant : les sons de tes 3 variantes du sous-titre */
function planRush(o, avecAmorce) {
  var r = { am: [], ti: [], sons: [], sel: o.anim === 'selection' };
  var amTxt = avecAmorce ? casse(o.amorce) : '', tiTxt = casse(o.titre);
  if (o.anim === 'agrandie') {
    var ms_ = function (x) { return Math.round(x * 1000); };
    var tK2 = amTxt ? motsEnFlou(amTxt, 0.1, 0.1, r.am, r.sons, { id: 'short-shutter-click', vol: 0.3 }) + 0.05 : 0.15;
    r.ti.push({ t: tiTxt, anim: an('asFlouIn', 300, tK2), m: '0' });
    var tC = tK2 + 0.4, tCl = tC + 0.85, tD = tCl + 0.08, tR = tD + 0.7, eff = 'asEfface 200ms ease-in ' + ms_(tR + 0.1) + 'ms both';
    r.agr = true; r.agrCadre = an('asCadre', 300, tC) + ', ' + eff; r.agrPoignee = an('asPoignee', 160, tC + 0.3) + ', ' + eff;
    r.curseurVie = an('asCurseur', 420, tC + 0.35); r.curseurClic = an('asClic', 160, tCl, 'ease-out');
    r.agrAnim = 'asAgrandit 700ms cubic-bezier(0.65, 0, 0.35, 1) ' + ms_(tD) + 'ms both';
    r.agrContre = r.agrAnim + ', asEfface 200ms ease-in ' + ms_(tR + 0.15) + 'ms both';
    r.braise = o.couleur === 'braise' ? 'asBraiseMot 160ms linear ' + ms_(tR) + 'ms both' : 'none';
    r.sons.push({ id: 'gear-turn-click', t: tC, vol: 0.4, dur: 0.3 }, { id: 'mouse-click', t: tCl, vol: 0.6 }, { id: 'camera-shutter', t: tR, vol: 0.35 });
    r.dernier = tR + 0.3;
  } else if (o.anim === 'machine') {
    var t = amTxt ? lettres(amTxt, 0.15, r.am, r.sons, { id: 'gear-single-click', vol: 0.25 }) + 0.12 : 0.2;
    r.sons.push({ id: 'camera-shutter', t: t, vol: 0.35 });
    r.dernier = lettres(tiTxt, t, r.ti, r.sons, null);
  } else {
    var tK = amTxt ? motsEnFlou(amTxt, 0.1, 0.18, r.am, r.sons, { id: 'short-shutter-click', vol: 0.3 }) + 0.12 : 0.2;
    if (o.anim === 'punch') {
      r.ti.push({ t: tiTxt, anim: an('asPunch', 420, tK), m: '0' });
      r.sons.push({ id: 'mouse-click', t: tK, vol: 0.45 });
      r.dernier = tK + 0.45;
    } else {
      r.ti.push({ t: tiTxt, anim: an('asFlouIn', 350, tK), m: '0' });
      var tClic = tK + 1.3;
      r.cadre = an('asCadre', 300, tK + 0.45); r.poignee = an('asPoignee', 160, tK + 0.75);
      r.curseurVie = an('asCurseur', 420, tK + 0.85); r.curseurClic = an('asClic', 160, tClic, 'ease-out');
      r.remplit = 'asRemplitFond 120ms linear ' + Math.round((tClic + 0.02) * 1000) + 'ms both';
      r.noircit = 'asNoircitMot 120ms linear ' + Math.round((tClic + 0.02) * 1000) + 'ms both';
      r.sons.push({ id: 'gear-turn-click', t: tK + 0.45, vol: 0.4, dur: 0.3 }, { id: 'mouse-click', t: tClic, vol: 0.6 });
      r.dernier = tClic + 0.4;
    }
  }
  r.fin = r.dernier + 1.6;
  r.sortie = an('asFlouOut', 300, r.dernier + 1.2, 'ease-in');
  return r;
}
function planScene(o) {
  var r = { av: [], mo: [], ap: [], sons: [] }, son = { id: 'short-shutter-click', vol: 0.3 };
  var tK = motsEnFlou(o.avant, 0.15, 0.2, r.av, r.sons, son) + 0.1;
  r.mo.push({ t: casse(o.mot), anim: an('asPunch', 420, tK), m: '0' });
  r.sons.push({ id: 'mouse-click', t: tK, vol: 0.45 });
  var tA = motsEnFlou(o.apres, tK + 0.5, 0.2, r.ap, r.sons, son);
  r.dernier = o.apres ? tA + 0.2 : tK + 0.45;
  r.fin = r.dernier + 1.6;
  return r;
}
function planEtiq() {
  var r = { sons: [], barres: [] };
  [0.35, 0.5, 0.42, 0.7, 1].forEach(function (v, i) {
    r.barres.push({ hp: Math.round(v * 100), anim: an('asBarre', 420, 0.35 + i * 0.09), c: i === 4 ? '#FF7033' : '#5A5A5A', lab: 'S' + (i + 1) });
    r.sons.push({ id: 'gear-single-click', t: 0.35 + i * 0.09, vol: 0.25 });
  });
  r.titre = an('asFlouIn', 350, 0.1); r.chiffre = an('asPunch', 420, 0.95);
  r.sons.push({ id: 'mouse-click', t: 0.95, vol: 0.45 });
  r.fin = 3; return r;
}
function planLogo() { return { mot: an('asFlouIn', 400, 0.2), carre: an('asPoignee', 200, 0.6), sons: [{ id: 'short-shutter-click', t: 0.6, vol: 0.3 }], fin: 2.5 }; }

class Component extends DCLogic {
  constructor(props) {
    super(props);
    var self = this;
    this.state = { el: 'accroche', fmt: '916', run: true, joue: false, err: '', copie: '', polices: 0, E: JSON.parse(JSON.stringify(DEFAUTS)) };
    try {
      if (document.fonts && document.fonts.load) {
        Promise.all(['400 200px Anton', '900 200px Doto', '400 54px Arimo', '700 54px Arimo'].map(function (f) { return document.fonts.load(f); }))
          .then(function () { self.setState({ polices: 1 }); }, function () {});
      }
    } catch (e) {}
  }
""" + g.MOTEUR + r"""
  plan() {
    var st = this.state, o = st.E[st.el];
    if (st.el === 'accroche') { return planRush(o, true); }
    if (st.el === 'motgeant') { return planRush(o, false); }
    if (st.el === 'scene') { return planScene(o); }
    if (st.el === 'etiq') { return planEtiq(); }
    return planLogo();
  }
  lancer() {
    var self = this, p = this.plan();
    this.couper(); this.ac();
    var ids = p.sons.map(function (s) { return s.id; }).filter(function (x, i, l) { return l.indexOf(x) === i; });
    Promise.all(ids.map(function (id) { return self.buf(id); })).then(function () {
      self.setState({ run: false, err: '' });
      self._tm.push(setTimeout(function () {
        var t0 = self.ac().currentTime + 0.03;
        self.setState({ run: true, joue: true });
        p.sons.forEach(function (s) { self.jouer(s.id, t0 + s.t, s.vol, s.dur); });
        self._tm.push(setTimeout(function () { self.setState({ joue: false }); }, p.fin * 1000));
      }, 40));
    }).catch(function (e) { self.setState({ err: 'Le son ne se charge pas : ' + e.message }); });
  }
  regler(cle, val) {
    var E = JSON.parse(JSON.stringify(this.state.E)); E[this.state.el][cle] = val;
    this.setState({ E: E, copie: '' });
  }
  recette() {
    var E = this.state.E, a = E.accroche, m = E.motgeant, s = E.scene, e = E.etiq, l = E.logo;
    var px = function (v, f) { return Math.round(v * f) + ' px'; };
    var f169 = FORMATS['169'].f;
    var rush = function (o) {
      return POL[o.police].n.replace(' (actuel)', '') + ', ' + px(o.taille, 1) + ' en 9:16 (' + px(o.taille, f169) + ' en 16:9), ' + nomDe(COULEURS, o.couleur).toLowerCase() +
        ', en 9:16 ' + nomDe(POSITIONS, o.pos).toLowerCase() + ' (' + o.h + ' px du ' + (o.pos === 'haut' ? 'haut' : 'bas') + '), en 16:9 ' + nomDe(POSITIONS169, o.pos169).toLowerCase() + ' (centre à ' + o.h169 + ' px du haut), animation ' + nomDe(ANIMS, o.anim);
    };
    return [
      'Titre d’accroche — amorce Arial 400, 54 px, au-dessus du titre · titre ' + rush(a),
      'Mot géant seul — ' + rush(m),
      'Scène texte plein écran — phrase ' + POL[s.policePh].n.replace(' (actuel)', '') + ', ' + px(s.taillePh, 1) + ' · mot mis en valeur ' + POL[s.policeMot].n.replace(' (actuel)', '') + ', ' + px(s.tailleMot, 1) + ', braise · ' + nomDe(FONDS, s.fond).toLowerCase(),
      'Étiquettes — ' + POL[e.policeEt].n.replace(' (actuel)', '') + ', ' + px(e.tailleEt, 1) + ' en 9:16, MAJUSCULES · chiffres ' + POL[e.policeCh].n.replace(' (actuel)', '') + ', ' + px(e.tailleCh, 1) + ', ' + nomDe(COULEURS, e.couleurCh).toLowerCase(),
      'Règle 16:9 — tout texte posé sur toi va à gauche ou à droite de ta tête, ou derrière toi (détourage) ; jamais sur le visage',
      'Logo — DIGITAL BLACK en ' + POL[l.police].n.replace(' (actuel)', '') + ', ' + nomDe(CARRES, l.carre).replace('Carré', 'carré') + ', ' + px(l.taille, 1) + ' en carton plein écran'
    ].join('\n\n');
  }
  copier() {
    var self = this, t = this.recette(), ok = false, MANUEL = 'Pas copié : clique dans le cadre, Cmd+A puis Cmd+C';
    try { if (this._ta) { this._ta.focus(); this._ta.select(); ok = document.execCommand('copy'); } } catch (e) { ok = false; }
    if (ok) { this.setState({ copie: 'Copié' }); return; }
    try { navigator.clipboard.writeText(t).then(function () { self.setState({ copie: 'Copié' }); }, function () { self.setState({ copie: MANUEL }); }); } catch (e) { this.setState({ copie: MANUEL }); }
  }
  controles() {
    var self = this, st = this.state, o = st.E[st.el];
    var pills = function (titre, cle, liste) {
      return { titre: titre, estPills: true, estSlider: false, estTexte: false, pills: liste.map(function (x) {
        var s = pill(x.id === o[cle]); return { label: x.n, bg: s.bg, fg: s.fg, bd: s.bd, pick: function () { self.regler(cle, x.id); } };
      }) };
    };
    var polices = function (titre, cle, ids) { return pills(titre, cle, ids.map(function (id) { return { id: id, n: POL[id].n }; })); };
    var slider = function (titre, cle, mn, mx, pas, unite) {
      return { titre: titre, estPills: false, estSlider: true, estTexte: false, mn: mn, mx: mx, pas: pas, val: o[cle], txt: o[cle] + ' ' + unite,
        on: function (ev) { self.regler(cle, Number(ev.target.value)); } };
    };
    var texte = function (titre, cle) {
      return { titre: titre, estPills: false, estSlider: false, estTexte: true, val: o[cle], on: function (ev) { self.regler(cle, ev.target.value); } };
    };
    if (st.el === 'accroche' || st.el === 'motgeant') {
      var l = st.el === 'accroche' ? [texte('Amorce (au-dessus)', 'amorce'), texte('Titre : un chiffre ou un mot', 'titre')] : [texte('Le mot', 'titre')];
      return l.concat([polices('Police du titre', 'police', CHOIX.police), pills('Couleur', 'couleur', COULEURS),
        slider('Taille (9:16)', 'taille', st.el === 'accroche' ? 200 : 140, st.el === 'accroche' ? 560 : 400, 10, 'px'),
        st.fmt === '169' ? pills('Place (16:9)', 'pos169', POSITIONS169) : pills('Place (9:16)', 'pos', POSITIONS),
        st.fmt === '169' ? slider('Hauteur du centre (16:9)', 'h169', 120, 960, 10, 'px') : slider('Hauteur (9:16)', 'h', 60, 900, 10, 'px'),
        pills('Animation et sons', 'anim', ANIMS)]);
    }
    if (st.el === 'scene') {
      return [texte('Avant le mot', 'avant'), texte('Mot mis en valeur', 'mot'), texte('Après le mot', 'apres'),
        polices('Police de la phrase', 'policePh', CHOIX.policePh), slider('Taille de la phrase (9:16)', 'taillePh', 70, 150, 5, 'px'),
        polices('Police du mot mis en valeur', 'policeMot', CHOIX.policeMot), slider('Taille du mot (9:16)', 'tailleMot', 160, 360, 10, 'px'), pills('Fond', 'fond', FONDS)];
    }
    if (st.el === 'etiq') {
      return [texte('Étiquette', 'titre'), texte('Chiffre', 'chiffre'), polices('Police des étiquettes', 'policeEt', CHOIX.policeEt),
        slider('Taille des étiquettes (9:16)', 'tailleEt', 18, 44, 1, 'px'), polices('Police du chiffre', 'policeCh', CHOIX.policeCh),
        pills('Couleur du chiffre', 'couleurCh', COULEURS), slider('Taille du chiffre (9:16)', 'tailleCh', 120, 340, 10, 'px')];
    }
    return [polices('Police du logo', 'police', CHOIX.policeLogo), pills('Couleur du carré', 'carre', CARRES), slider('Taille (carton plein écran)', 'taille', 40, 220, 5, 'px'), pills('Fond', 'fond', FONDS)];
  }
  renderVals() {
    var self = this, st = this.state, Fo = FORMATS[st.fmt], f = Fo.f, o = st.E[st.el], p = this.plan();
    var rush = st.el === 'accroche' || st.el === 'motgeant', alertes = [], infos = [];
    var v = {
      run: st.run, boutonTxt: st.joue ? 'Rejouer' : 'Jouer avec le son', onPlay: function () { self.lancer(); }, err: st.err, aErr: !!st.err,
      vueW: Fo.vueW, vueH: Fo.vueH, vue: Fo.vue, cw: Fo.w, ch: Fo.h, imgSrc: Fo.img, marge: (Fo.w - Fo.utile) / 2,
      aRush: rush, aScene: st.el === 'scene', aEtiq: st.el === 'etiq', aLogo: st.el === 'logo', aFond: !rush,
      fondC: (st.el === 'scene' || st.el === 'logo') && o.fond === 'blanc' ? '#EFEFEF' : '#0A0A0A',
      grilleC: (st.el === 'scene' || st.el === 'logo') && o.fond === 'blanc' ? 'rgba(10,10,10,0.07)' : 'rgba(239,239,239,0.06)',
      encre: (st.el === 'scene' || st.el === 'logo') && o.fond === 'blanc' ? '#0A0A0A' : '#EFEFEF'
    };
    if (rush) {
      var P = POL[o.police], t = Math.round(o.taille * f), tiTxt = casse(o.titre);
      var lw = largeur(tiTxt, P, t) + 44, h169 = st.fmt === '169', pos = h169 ? o.pos169 : o.pos;
      var col = h169 ? colonne169(pos) : { x0: (Fo.w - Fo.utile) / 2, x1: (Fo.w + Fo.utile) / 2 }, U = col.x1 - col.x0;
      var amW = st.el === 'accroche' && o.amorce ? largeur(casse(o.amorce), POL.arial4, Math.round(54 * f)) + mots(o.amorce).length * 0.28 * 54 * f : 0;
      var bw = Math.max(lw, amW), bh = t * P.lh + 12 + (amW ? 54 * f * 1.1 : 0), fx, fy;
      if (h169) { fy = o.h169; fx = pos === 'gauche' ? col.x1 - bw / 2 : (pos === 'droite' ? col.x0 + bw / 2 : (col.x0 + col.x1) / 2); }
      else { fx = Fo.w / 2; fy = pos === 'haut' ? o.h + bh / 2 : Fo.h - o.h - bh / 2; }
      var sx = h169 ? 960 : fx + 180, sy = h169 ? 820 : fy + 160;
      if (lw > U) { alertes.push('Le titre dépasse la place (' + U + ' px' + (h169 && pos !== 'derriere' ? ' à côté de ta tête' : '') + ') : à ' + t + ' px il fait ' + Math.round(lw) + ' px. Taille max qui tient : ' + Math.floor(o.taille * U / lw) + ' px.'); }
      else { var tmx = Math.floor(o.taille * U / lw); infos.push(tmx > 560 ? 'Ce titre tient même à la taille maximum' : 'Taille max qui tient pour ce titre : ' + tmx + ' px (9:16)'); }
      if (st.el === 'accroche' && mots(o.amorce).length > 4) { alertes.push('Amorce : ' + mots(o.amorce).length + ' mots, 4 au plus (même règle que le sous-titre).'); }
      infos.push('À l’écran : titre ' + t + ' px' + (st.el === 'accroche' ? ' · amorce ' + Math.round(54 * f) + ' px' : ''));
      Object.assign(v, {
        rTop: h169 ? o.h169 + 'px' : (pos === 'haut' ? o.h + 'px' : 'auto'), rBas: !h169 && pos === 'bas' ? o.h + 'px' : 'auto',
        rG: col.x0, rL: U, rTr: h169 ? 'translateY(-50%)' : 'none', rAlign: h169 && pos === 'gauche' ? 'flex-end' : (h169 && pos === 'droite' ? 'flex-start' : 'center'),
        rTexte: h169 && pos === 'gauche' ? 'right' : (h169 && pos === 'droite' ? 'left' : 'center'), aDetour: h169 && pos === 'derriere',
        aAgr: !!p.agr, agrTr: p.agr ? 'translate(' + Math.round(sx - fx) + 'px, ' + Math.round(sy - fy) + 'px) scale(0.4)' : 'none', agrAnim: p.agrAnim || 'none',
        agrCadre: p.agrCadre || 'none', agrPoignee: p.agrPoignee || 'none', agrContre: p.agrContre || 'none',
        sortie: p.sortie, aAmorce: st.el === 'accroche' && !!o.amorce, amT: Math.round(54 * f), amTokens: p.am,
        tiF: P.f, tiW: P.w, tiLs: P.ls, tiLh: P.lh, tiT: t, tiTokens: p.ti, tiC: p.sel || p.agr ? '#EFEFEF' : (o.couleur === 'braise' ? '#FF7033' : '#EFEFEF'),
        aSel: p.sel, cadre: p.cadre || 'none', poignee: p.poignee || 'none', curseurVie: p.curseurVie || 'none', curseurClic: p.curseurClic || 'none',
        tire: p.remplit || 'none', noircit: p.noircit || p.braise || 'none', curseurT: Math.round(64 * f)
      });
    }
    if (st.el === 'scene') {
      var Ph = POL[o.policePh], Mo = POL[o.policeMot], tp = Math.round(o.taillePh * f), tm = Math.round(o.tailleMot * f);
      var plusLarge = Math.max(largeur(o.avant, Ph, tp), largeur(o.apres, Ph, tp), largeur(casse(o.mot), Mo, tm));
      if (plusLarge > Fo.utile) { alertes.push('Une ligne dépasse la largeur utile (' + Fo.utile + ' px) : réduis la taille ou raccourcis.'); }
      var nb = mots(o.avant).length + 1 + mots(o.apres).length;
      if (nb > 6) { alertes.push('La scène texte compte ' + nb + ' mots : 6 au plus.'); }
      infos.push('À l’écran : phrase ' + tp + ' px · mot ' + tm + ' px · ' + nb + ' mots');
      Object.assign(v, { phF: Ph.f, phW: Ph.w, phLs: Ph.ls, phT: tp, moF: Mo.f, moW: Mo.w, moLs: Mo.ls, moLh: Mo.lh, moT: tm, avTokens: p.av, moTokens: p.mo, apTokens: p.ap, aApres: !!o.apres });
    }
    if (st.el === 'etiq') {
      var Et = POL[o.policeEt], Ch = POL[o.policeCh];
      infos.push('À l’écran : étiquettes ' + Math.round(o.tailleEt * f) + ' px · chiffre ' + Math.round(o.tailleCh * f) + ' px');
      Object.assign(v, { etF: Et.f, etW: Et.w, etLs: Et.ls, etT: Math.round(o.tailleEt * f), etTitre: o.titre.toUpperCase(), chF: Ch.f, chW: Ch.w, chLs: Ch.ls, chLh: Ch.lh,
        chT: Math.round(o.tailleCh * f), chTxt: o.chiffre, chC: o.couleurCh === 'braise' ? '#FF7033' : '#EFEFEF', barres: p.barres, etAnim: p.titre, chAnim: p.chiffre,
        carteW: st.fmt === '169' ? 1100 : 860, barreH: st.fmt === '169' ? 300 : 420 });
    }
    if (st.el === 'logo') {
      var Lg = POL[o.police];
      Object.assign(v, { lgF: Lg.f, lgW: Lg.w, lgLs: Lg.ls, lgT: Math.round(o.taille * f), carreC: o.carre === 'ancienne' ? '#FF4D00' : '#FF7033', carreT: Math.round(o.taille * f * 0.3),
        lgAnim: p.mot, carreAnim: p.carre });
      if (o.carre === 'ancienne') { alertes.push('Le carré est encore dans l’ancienne braise #FF4D00 : le reste du style est en #FF7033.'); }
    }
    return Object.assign(v, {
      elements: ELEMENTS.map(function (x) { var s = pill(x.id === st.el); return { label: x.n, bg: s.bg, fg: s.fg, bd: s.bd, pick: function () { self.couper(); self.setState({ el: x.id, copie: '' }); } }; }),
      formats: ['916', '169'].map(function (id) { var s = pill(id === st.fmt); return { label: FORMATS[id].n, bg: s.bg, fg: s.fg, bd: s.bd, pick: function () { self.setState({ fmt: id }); } }; }),
      controles: this.controles(), alertes: alertes.map(function (t) { return { t: t }; }), sansAlerte: alertes.length === 0, infos: infos.map(function (t) { return { t: t }; }),
      recette: this.recette(), copie: st.copie, aCopie: !!st.copie, setTa: function (el) { self._ta = el; }, onCopier: function () { self.copier(); }
    });
  }
}
"""

PILLS = ('<div style="display: flex; flex-wrap: wrap; gap: 6px"><sc-for list="{{LISTE}}" as="p" hint-placeholder-count="4">'
         '<button type="button" onClick="{{p.pick}}" style="padding: 6px 11px; min-height: 32px; border-radius: 999px; border: 1px solid {{p.bd}}; '
         'background: {{p.bg}}; color: {{p.fg}}; font-family: Inter, sans-serif; font-weight: 700; font-size: 13px; cursor: pointer">{{p.label}}</button></sc-for></div>')
def pills(liste): return PILLS.replace("LISTE", liste)

TOKENS = ('<sc-for list="{{LISTE}}" as="x" hint-placeholder-count="2"><span style="display: inline-block; overflow: hidden; white-space: pre; '
          'margin: {{x.m}}; animation: {{x.anim}}">{{x.t}}</span></sc-for>')
def tokens(liste): return TOKENS.replace("LISTE", liste)

POIGNEES = "".join(
    f'<span style="position: absolute; {pos}; width: 18px; height: 18px; background: #EFEFEF; border: 3px solid #FF7033; box-sizing: border-box; animation: {{{{poignee}}}}"></span>'
    for pos in ["left: -9px; top: -9px", "right: -9px; top: -9px", "left: -9px; bottom: -9px", "right: -9px; bottom: -9px"])
HALO = "text-shadow: 0 0 36px rgba(10,10,10,0.8), 0 2px 6px rgba(10,10,10,0.6)"

RUSH = f"""<sc-if value="{{{{aRush}}}}" hint-placeholder-val="{{{{ true }}}}">
<img src="{{{{imgSrc}}}}" alt="Image de ton rush" style="position: absolute; inset: 0; width: {{{{cw}}}}px; height: {{{{ch}}}}px; object-fit: cover; display: block">
<sc-if value="{{{{run}}}}" hint-placeholder-val="{{{{ true }}}}">
<div style="position: absolute; left: {{{{rG}}}}px; width: {{{{rL}}}}px; top: {{{{rTop}}}}; bottom: {{{{rBas}}}}; transform: {{{{rTr}}}}; display: flex; flex-direction: column; align-items: {{{{rAlign}}}}; text-align: {{{{rTexte}}}}; animation: {{{{sortie}}}}">
<div style="position: relative; display: flex; flex-direction: column; align-items: {{{{rAlign}}}}; transform-origin: 50% 50%; transform: {{{{agrTr}}}}; animation: {{{{agrAnim}}}}">
<sc-if value="{{{{aAmorce}}}}" hint-placeholder-val="{{{{ true }}}}"><div style="display: flex; align-items: flex-end; white-space: nowrap; font-family: Arial, Arimo, sans-serif; font-weight: 400; font-size: {{{{amT}}}}px; line-height: 1.1; color: #EFEFEF; {HALO}">{tokens("amTokens")}</div></sc-if>
<div style="position: relative; padding: 6px 22px; animation: {{{{tire}}}}">
<sc-if value="{{{{aSel}}}}" hint-placeholder-val="{{{{ false }}}}"><span style="position: absolute; inset: 0; border: 3px solid #FF7033; animation: {{{{cadre}}}}"></span>{POIGNEES}<span style="position: absolute; right: -24px; bottom: -40px; width: 0; height: 0; z-index: 2"><span style="position: absolute; left: 0; top: 0; opacity: 0; animation: {{{{curseurVie}}}}"><svg aria-hidden="true" width="64" height="78" viewBox="0 0 14 17" style="display: block; transform-origin: 1px 1px; animation: {{{{curseurClic}}}}"><path d="M1 1 L1 14 L4.5 10.8 L7 16 L9.4 15 L6.9 9.9 L11.6 9.9 Z" fill="#EFEFEF" stroke="#0A0A0A" stroke-width="1"></path></svg></span></span></sc-if>
<div style="position: relative; display: flex; align-items: flex-end; white-space: nowrap; font-family: {{{{tiF}}}}; font-weight: {{{{tiW}}}}; font-size: {{{{tiT}}}}px; line-height: {{{{tiLh}}}}; letter-spacing: {{{{tiLs}}}}; color: {{{{tiC}}}}; {HALO}; animation: {{{{noircit}}}}">{tokens("tiTokens")}</div>
</div>
<sc-if value="{{{{aAgr}}}}" hint-placeholder-val="{{{{ false }}}}"><span style="position: absolute; inset: -18px; border: 5px solid #FF7033; animation: {{{{agrCadre}}}}"></span><span style="position: absolute; left: -30px; top: -30px; width: 24px; height: 24px; background: #EFEFEF; border: 4px solid #FF7033; box-sizing: border-box; animation: {{{{agrPoignee}}}}"></span><span style="position: absolute; right: -30px; top: -30px; width: 24px; height: 24px; background: #EFEFEF; border: 4px solid #FF7033; box-sizing: border-box; animation: {{{{agrPoignee}}}}"></span><span style="position: absolute; left: -30px; bottom: -30px; width: 24px; height: 24px; background: #EFEFEF; border: 4px solid #FF7033; box-sizing: border-box; animation: {{{{agrPoignee}}}}"></span><span style="position: absolute; right: -30px; bottom: -30px; width: 24px; height: 24px; background: #EFEFEF; border: 4px solid #FF7033; box-sizing: border-box; animation: {{{{agrPoignee}}}}"></span><span style="position: absolute; right: -30px; bottom: -30px; width: 0; height: 0; z-index: 3; transform-origin: 0 0; transform: scale(2.5); animation: {{{{agrContre}}}}"><span style="position: absolute; left: -4px; top: -4px; opacity: 0; animation: {{{{curseurVie}}}}"><svg aria-hidden="true" width="64" height="78" viewBox="0 0 14 17" style="display: block; transform-origin: 1px 1px; animation: {{{{curseurClic}}}}"><path d="M1 1 L1 14 L4.5 10.8 L7 16 L9.4 15 L6.9 9.9 L11.6 9.9 Z" fill="#EFEFEF" stroke="#0A0A0A" stroke-width="1"></path></svg></span></span></sc-if>
</div>
</div>
</sc-if>
<sc-if value="{{{{aDetour}}}}" hint-placeholder-val="{{{{ false }}}}"><img src="__DETOUR169__" alt="" aria-hidden="true" style="position: absolute; inset: 0; width: {{{{cw}}}}px; height: {{{{ch}}}}px; display: block"></sc-if>
</sc-if>"""

FOND = """<sc-if value="{{aFond}}" hint-placeholder-val="{{ false }}"><div style="position: absolute; inset: 0; background-color: {{fondC}}; background-image: linear-gradient({{grilleC}} 2px, transparent 2px), linear-gradient(90deg, {{grilleC}} 2px, transparent 2px); background-size: 60px 60px"></div></sc-if>"""

SCENE_TXT = f"""<sc-if value="{{{{aScene}}}}" hint-placeholder-val="{{{{ false }}}}"><sc-if value="{{{{run}}}}" hint-placeholder-val="{{{{ true }}}}">
<div style="position: absolute; inset: 0; padding: 0 {{{{marge}}}}px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; color: {{{{encre}}}}">
<div style="display: flex; flex-wrap: wrap; justify-content: center; font-family: {{{{phF}}}}; font-weight: {{{{phW}}}}; font-size: {{{{phT}}}}px; line-height: 1.05; letter-spacing: {{{{phLs}}}}">{tokens("avTokens")}</div>
<div style="display: flex; white-space: nowrap; font-family: {{{{moF}}}}; font-weight: {{{{moW}}}}; font-size: {{{{moT}}}}px; line-height: {{{{moLh}}}}; letter-spacing: {{{{moLs}}}}; color: #FF7033; margin: 10px 0">{tokens("moTokens")}</div>
<sc-if value="{{{{aApres}}}}" hint-placeholder-val="{{{{ true }}}}"><div style="display: flex; flex-wrap: wrap; justify-content: center; font-family: {{{{phF}}}}; font-weight: {{{{phW}}}}; font-size: {{{{phT}}}}px; line-height: 1.05; letter-spacing: {{{{phLs}}}}">{tokens("apTokens")}</div></sc-if>
</div>
</sc-if></sc-if>"""

ETIQ = """<sc-if value="{{aEtiq}}" hint-placeholder-val="{{ false }}"><sc-if value="{{run}}" hint-placeholder-val="{{ true }}">
<div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center">
<div style="width: {{carteW}}px; box-sizing: border-box; padding: 48px; border-radius: 16px; background: #161616; border: 2px solid #2E2E2E; display: flex; flex-direction: column; gap: 20px">
<div style="font-family: {{etF}}; font-weight: {{etW}}; font-size: {{etT}}px; letter-spacing: {{etLs}}; color: #A3A3A3; animation: {{etAnim}}">{{etTitre}}</div>
<div style="font-family: {{chF}}; font-weight: {{chW}}; font-size: {{chT}}px; line-height: {{chLh}}; letter-spacing: {{chLs}}; color: {{chC}}; white-space: nowrap; animation: {{chAnim}}">{{chTxt}}</div>
<div style="display: flex; align-items: flex-end; gap: 24px; height: {{barreH}}px">
<sc-for list="{{barres}}" as="b" hint-placeholder-count="5"><div style="flex: 1; height: 100%; display: flex; flex-direction: column; justify-content: flex-end; align-items: stretch; gap: 12px"><div style="height: {{b.hp}}%; background: {{b.c}}; border-radius: 6px 6px 0 0; transform-origin: 50% 100%; animation: {{b.anim}}"></div><div style="text-align: center; font-family: {{etF}}; font-weight: {{etW}}; font-size: {{etT}}px; letter-spacing: {{etLs}}; color: #A3A3A3">{{b.lab}}</div></div></sc-for>
</div>
</div>
</div>
</sc-if></sc-if>"""

LOGO = """<sc-if value="{{aLogo}}" hint-placeholder-val="{{ false }}"><sc-if value="{{run}}" hint-placeholder-val="{{ true }}">
<div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center">
<div style="display: flex; align-items: center; gap: 0.18em; font-family: {{lgF}}; font-weight: {{lgW}}; font-size: {{lgT}}px; line-height: 1; letter-spacing: {{lgLs}}; color: {{encre}}; white-space: nowrap"><span style="animation: {{lgAnim}}">DIGITAL BLACK</span><span style="display: inline-block; width: {{carreT}}px; height: {{carreT}}px; background: {{carreC}}; animation: {{carreAnim}}"></span></div>
</div>
</sc-if></sc-if>"""

VUE = f"""<div style="position: relative; width: {{{{vueW}}}}px; height: {{{{vueH}}}}px; overflow: hidden; border-radius: 8px; border: 2px solid #3A3A3A; box-sizing: content-box; background: #1A1A1A">
<div style="position: absolute; left: 0; top: 0; width: {{{{cw}}}}px; height: {{{{ch}}}}px; transform: scale({{{{vue}}}}); transform-origin: 0 0; overflow: hidden">
{FOND}{RUSH}{SCENE_TXT}{ETIQ}{LOGO}
</div>
</div>"""

CONTROLES = """<sc-for list="{{controles}}" as="x" hint-placeholder-count="6"><div style="display: flex; flex-direction: column; gap: 10px; padding: 14px 16px; border: 1px solid #2E2E2E; border-radius: 8px; background: #161616">
<div style="font-size: 15px; font-weight: 800; color: #EFEFEF">{{x.titre}}</div>
<sc-if value="{{x.estPills}}" hint-placeholder-val="{{ true }}"><div style="display: flex; flex-wrap: wrap; gap: 6px"><sc-for list="{{x.pills}}" as="p" hint-placeholder-count="3"><button type="button" onClick="{{p.pick}}" style="padding: 6px 11px; min-height: 32px; border-radius: 999px; border: 1px solid {{p.bd}}; background: {{p.bg}}; color: {{p.fg}}; font-family: Inter, sans-serif; font-weight: 700; font-size: 13px; cursor: pointer">{{p.label}}</button></sc-for></div></sc-if>
<sc-if value="{{x.estSlider}}" hint-placeholder-val="{{ false }}"><label style="display: flex; align-items: center; gap: 12px"><input type="range" min="{{x.mn}}" max="{{x.mx}}" step="{{x.pas}}" value="{{x.val}}" onChange="{{x.on}}" aria-label="{{x.titre}}" style="flex: 1; accent-color: #FF7033"><span style="width: 70px; text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 13px; color: #EFEFEF">{{x.txt}}</span></label></sc-if>
<sc-if value="{{x.estTexte}}" hint-placeholder-val="{{ false }}"><input type="text" value="{{x.val}}" onChange="{{x.on}}" aria-label="{{x.titre}}" style="min-width: 0; min-height: 36px; padding: 6px 10px; border: 1px solid #3A3A3A; border-radius: 6px; background: #0A0A0A; color: #EFEFEF; font-family: Inter, sans-serif; font-size: 15px; font-weight: 700"></sc-if>
</div></sc-for>"""

RECETTE = """<div style="grid-column: 1 / -1; display: flex; flex-direction: column; gap: 8px; padding: 14px 16px; border-radius: 8px; background: #EFEFEF; color: #0A0A0A">
<div style="display: flex; align-items: center; justify-content: space-between; gap: 12px">
<div style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #5A5A5A">Ta recette des textes · copie-la et envoie-la-moi</div>
<div style="display: flex; align-items: center; gap: 10px">
<sc-if value="{{aCopie}}" hint-placeholder-val="{{ false }}"><span style="font-size: 13px; font-weight: 700; color: #5A5A5A">{{copie}}</span></sc-if>
<button type="button" onClick="{{onCopier}}" style="min-height: 36px; padding: 6px 14px; border: 0; border-radius: 6px; background: #0A0A0A; color: #EFEFEF; font-family: Inter, sans-serif; font-weight: 800; font-size: 13px; cursor: pointer">Copier la recette</button>
</div>
</div>
<textarea readonly="readonly" ref="{{setTa}}" value="{{recette}}" aria-label="Ta recette des textes" rows="10" style="width: 100%; box-sizing: border-box; resize: none; padding: 8px 10px; border: 1px solid #BDBDBD; border-radius: 6px; background: #FFFFFF; color: #0A0A0A; font-family: Inter, sans-serif; font-size: 14px; line-height: 1.45; font-weight: 700"></textarea>
</div>"""

corps = f"""<div style="width: {W}px; height: {H}px; box-sizing: border-box; padding: 44px 48px; background: #121212; color: #EFEFEF; font-family: Inter, sans-serif; display: flex; flex-direction: column; gap: 24px; overflow: hidden">
<div style="display: flex; flex-direction: column; gap: 10px">
<div style="display: flex; align-items: center; gap: 12px"><span style="display: inline-block; width: 14px; height: 14px; background: #FF7033"></span><span style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 15px; letter-spacing: 0.08em; text-transform: uppercase; color: #A3A3A3">Animation caption et son · labo des textes · 9:16 et 16:9</span></div>
<h1 style="margin: 0; font-family: 'Big Shoulders Display', sans-serif; font-weight: 900; font-size: 60px; line-height: 0.95; letter-spacing: 0.01em; text-transform: uppercase">Labo des textes</h1>
<p style="margin: 0; max-width: 1500px; font-size: 18px; line-height: 1.45; font-weight: 500; color: #A3A3A3">Les autres textes du design system, essayés avec ton trio Arial / Anton / Inter. « (actuel) » = la police d’aujourd’hui, pour comparer. Les animations et les sons reprennent tes 4 variantes du sous-titre. En 16:9, le texte va à gauche ou à droite de ta tête, ou derrière toi.</p>
</div>
<div style="display: flex; gap: 36px; align-items: flex-start">
<div style="display: flex; flex-direction: column; gap: 12px; width: 544px; flex-shrink: 0">
{pills("formats")}
{VUE}
<button type="button" onClick="{{{{onPlay}}}}" style="display: flex; align-items: center; justify-content: center; gap: 12px; min-height: 56px; border: 0; border-radius: 8px; background: #FF7033; color: #0A0A0A; font-family: Inter, sans-serif; font-weight: 800; font-size: 18px; cursor: pointer"><svg aria-hidden="true" width="16" height="18" viewBox="0 0 16 18"><path d="M1 1 L15 9 L1 17 Z" fill="#0A0A0A"></path></svg>{{{{boutonTxt}}}}</button>
<sc-if value="{{{{aErr}}}}" hint-placeholder-val="{{{{ false }}}}"><p style="margin: 0; font-size: 14px; color: #FF7033">{{{{err}}}}</p></sc-if>
<div style="display: flex; flex-direction: column; gap: 8px; padding: 14px 16px; border-radius: 8px; background: #161616; border: 1px solid #2E2E2E">
<div style="font-size: 16px; font-weight: 800; color: #EFEFEF">Contrôles</div>
<sc-if value="{{{{sansAlerte}}}}" hint-placeholder-val="{{{{ true }}}}"><div style="font-size: 14px; font-weight: 700; color: #EFEFEF">Tout tient dans la largeur.</div></sc-if>
<sc-for list="{{{{alertes}}}}" as="x" hint-placeholder-count="1"><div style="display: flex; gap: 8px; align-items: flex-start; font-size: 14px; line-height: 1.4; font-weight: 700; color: #FF7033"><span aria-hidden="true">▲</span><span>{{{{x.t}}}}</span></div></sc-for>
<sc-for list="{{{{infos}}}}" as="x" hint-placeholder-count="2"><div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; line-height: 1.5; color: #A3A3A3">{{{{x.t}}}}</div></sc-for>
</div>
</div>
<div style="flex: 1; min-width: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; align-items: start">
<div style="grid-column: 1 / -1; display: flex; flex-direction: column; gap: 10px; padding: 14px 16px; border: 2px solid #FF7033; border-radius: 8px; background: #1A120E"><div style="font-size: 16px; font-weight: 800; color: #EFEFEF">Le texte à tester</div>{pills("elements")}</div>
{CONTROLES}
{RECETTE}
</div>
</div>
</div>"""

DETOUR169 = "/_blob/8044d9952f1361ea9b673f1c6c5ce21f"
SCRIPT = SCRIPT.replace("__FOND916__", g.FOND).replace("__FOND169__", FOND169)
corps = corps.replace("__DETOUR169__", DETOUR169)
doc = g.doc("Labo des textes", corps, SCRIPT, W, H)
doc = doc.replace("@keyframes asFlouIn",
                  "@keyframes asRemplitFond{to{background:#FF7033}}\n@keyframes asNoircitMot{to{color:#0A0A0A;text-shadow:none}}\n"
                  "@keyframes asEfface{from{opacity:1}to{opacity:0}}\n@keyframes asAgrandit{to{transform:none}}\n@keyframes asBraiseMot{to{color:#FF7033}}\n@keyframes asBarre{from{transform:scaleY(0)}to{transform:scaleY(1)}}\n@keyframes asFlouIn", 1)
doc = doc.replace("&amp;family=Google+Sans+Flex:wght@800&amp;display=swap",
                  "&amp;family=Google+Sans+Flex:wght@800&amp;family=Anton&amp;family=Arimo:wght@400;700&amp;family=Doto:wght@900&amp;display=swap", 1)
doc = doc.replace("family=Inter:wght@500;700;800", "family=Inter:wght@400;500;600;700;800", 1)
assert "family=Doto" in doc and "family=Anton" in doc
open(os.path.join(ICI, "project", "AS-Textes.dc.html"), "w").write(doc)
loc = (doc.replace('<script src="./support.js"></script>', '').replace(g.FOND, "fond-8.jpg").replace(FOND169, "fond-169.jpg").replace(DETOUR169, "detour-169.png")
       .replace("/_blob/113612acc014ae1a0af417b8f8c1c679", "redaction-50-latin-400-italic.woff2").replace("</body>", '<script src="mini-dc.js?v=3"></script></body>'))
open(os.path.join(ICI, "test-textes.html"), "w").write(loc)
print("ok", len(doc))
