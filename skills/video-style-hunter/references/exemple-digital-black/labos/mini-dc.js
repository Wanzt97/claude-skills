// Mini rendu local d'une planche .dc.html (sc-for, sc-if, trous {{x}}, onClick/onChange) pour vérifier la mise en page.
(function () {
  const tpl = document.querySelector('x-dc');
  const helmet = tpl.querySelector('helmet');
  if (helmet) { document.head.insertAdjacentHTML('beforeend', helmet.innerHTML); helmet.remove(); }
  const src = document.querySelector('script[data-dc-script]').textContent;
  class DCLogic { constructor(p) { this.props = p || {}; } setState(o) { Object.assign(this.state, typeof o === 'function' ? o(this.state) : o); planifier(); } }
  const C = new Function('DCLogic', src + '\nreturn Component;')(DCLogic);
  const comp = new C({});
  const modele = tpl.innerHTML; tpl.innerHTML = '';
  const racine = document.createElement('div'); tpl.after(racine);
  const get = (sc, p) => { p = p.trim(); if (p === 'true') return true; if (p === 'false') return false; return p.split('.').reduce((o, k) => o == null ? undefined : o[k], sc); };
  function rendre(node, sc, out) {
    if (node.nodeType === 3) { out.appendChild(document.createTextNode(node.textContent.replace(/{{([^}]+)}}/g, (m, p) => { const v = get(sc, p); return v == null ? '' : v; }))); return; }
    if (node.nodeType !== 1) return;
    const tag = node.tagName.toLowerCase();
    if (tag === 'sc-for') { const l = get(sc, node.getAttribute('list').replace(/[{}]/g, '')) || []; const as = node.getAttribute('as'); l.forEach((it, i) => { const s2 = Object.assign({}, sc, { [as]: it, $index: i }); node.childNodes.forEach(c => rendre(c, s2, out)); }); return; }
    if (tag === 'sc-if') { if (get(sc, node.getAttribute('value').replace(/[{}]/g, ''))) node.childNodes.forEach(c => rendre(c, sc, out)); return; }
    const el = document.createElementNS(node.namespaceURI, node.localName);
    for (const a of node.attributes) {
      const m = a.value.match(/^{{([^}]+)}}$/);
      if (/^on[A-Z]/.test(a.name) || /^on[a-z]/.test(a.name) && m) { const f = get(sc, m[1]); const ev = a.name.slice(2).toLowerCase(); el.addEventListener(ev === 'change' ? 'input' : ev, f); continue; }
      if (a.name === 'ref' && m) { const f = get(sc, m[1]); setTimeout(() => f && f(el)); continue; }
      const v = a.value.replace(/{{([^}]+)}}/g, (mm, p) => { const x = get(sc, p); return x == null ? '' : x; });
      if (a.name === 'value') { el.value = v; }
      el.setAttribute(a.name, v);
    }
    node.childNodes.forEach(c => rendre(c, sc, el));
    out.appendChild(el);
  }
  let prevu = false;
  function planifier() { if (prevu) return; prevu = true; setTimeout(() => { prevu = false; dessiner(); }, 0); }
  function dessiner() { const t = document.createElement('template'); t.innerHTML = modele; racine.innerHTML = ''; t.content.childNodes.forEach(c => rendre(c, comp.renderVals(), racine)); }
  dessiner();
  window.__comp = comp;
})();
