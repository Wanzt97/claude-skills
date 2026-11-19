#!/usr/bin/env python3
"""rythmize.py — zooms, punch-ins, secousses, transitions et whoosh sur un montage face caméra HyperFrames.

Lancer depuis le dossier du projet, avec python3 -I :
  python3 -I rythmize.py analyze                 -> plans (temps vidéo), chapitres, mots joués, coupes
  python3 -I rythmize.py apply plan.json         -> écrit la caméra, la scène de transitions et les whoosh

apply est rejouable : il remplace ce qu'un apply précédent a écrit (balises marquées rythmize).
"""
import glob, html, json, os, re, sys

def attr(tag, k):
    m = re.search(r'\s' + re.escape(k) + r'="([^"]*)"', tag)
    return html.unescape(m.group(1)) if m else None

def root_duration(s):
    m = re.search(r'data-composition-id="main"[^>]*?data-duration="([\d.]+)"', s) or \
        re.search(r'data-duration="([\d.]+)"[^>]*?data-composition-id="main"', s)
    return float(m.group(1))

def root_size(s):
    m = re.search(r'<div\b[^>]*data-composition-id="main"[^>]*>', s)
    tag = m.group(0) if m else ''
    return int(attr(tag, 'data-width') or 1920), int(attr(tag, 'data-height') or 1080)

def video_clips(s):
    out = []
    for tag in re.findall(r'<video\b[^>]*>', s):
        if attr(tag, 'data-start') is None: continue
        out.append(dict(id=attr(tag, 'id'), start=float(attr(tag, 'data-start')), dur=float(attr(tag, 'data-duration') or 0),
                        ms=float(attr(tag, 'data-media-start') or 0), src=attr(tag, 'src'), label=attr(tag, 'data-label') or ''))
    return sorted(out, key=lambda c: c['start'])

def transcripts():
    t = {}
    for f in glob.glob('.hyperframes/transcripts/*.json'):
        try: d = json.load(open(f, encoding='utf-8'))
        except Exception: continue
        if isinstance(d, dict) and d.get('src') and d.get('words'): t[d['src']] = d['words']
    return t

def analyze():
    s = open('index.html', encoding='utf-8').read()
    clips, tr = video_clips(s), transcripts()
    out = {"duration": root_duration(s), "clips": [], "chapterStarts": [], "imagesAndOverlays": []}
    prev = None
    for c in clips:
        ws = [w for w in tr.get(c['src'], []) if c['ms'] <= (w['start'] + w['end']) / 2 < c['ms'] + c['dur']]
        chap = c['label'][:2]
        if chap != prev: out["chapterStarts"].append({"t": round(c['start'], 3), "label": c['label']})
        prev = chap
        out["clips"].append({"id": c['id'], "t": round(c['start'], 3), "dur": round(c['dur'], 3), "label": c['label'],
                             "words": " ".join(f"{w['text']}@{c['start'] + w['start'] - c['ms']:.2f}" for w in ws)})
    for tag in re.findall(r'<img\b[^>]*>', s):
        if attr(tag, 'data-start'):
            out["imagesAndOverlays"].append({"id": attr(tag, 'id'), "t": float(attr(tag, 'data-start')), "dur": float(attr(tag, 'data-duration') or 3)})
    print(json.dumps(out, ensure_ascii=False, indent=1))

# ---------- transitions scene ----------
CELLS = '<i class="cell"></i>' * 144
GRID = [(9, 16)]  # [lignes, colonnes] ; (16, 9) en vertical
def fx_parts(i, tr):
    k, at = tr['type'], float(tr['at'])
    n = f"fx-{k}-{i}"
    if k == 'flash':
        st = at - 0.16
        el = f'<div id="{n}" class="clip fx flash" data-start="{st:.3f}" data-duration="0.45" data-track-index="{i%3}" data-label="Flash"></div>'
        js = (f'tl.fromTo("#{n}", {{opacity:0}}, {{opacity:0.9, duration:0.15, ease:"power2.in"}}, {st+0.01:.3f});\n'
              f'    tl.to("#{n}", {{opacity:0, duration:0.26, ease:"power2.out"}}, {at:.3f});')
    elif k in ('grid', 'grid-center'):
        center = k == 'grid-center'
        st = at - (0.36 if center else 0.44)
        g = GRID[0]
        frm = ('{grid:[%d,%d], from:"center", amount:%%s}' % g) if center else ('{grid:[%d,%d], axis:"x", from:"start", amount:%%s}' % g)
        el = f'<div id="{n}" class="clip fx grid" data-start="{st:.3f}" data-duration="{0.85 if center else 1.0}" data-track-index="{i%3}" data-label="Grille pixelisée">{CELLS}</div>'
        js = (f'tl.fromTo("#{n} .cell", {{scale:0}}, {{scale:1.02, duration:{0.18 if center else 0.2}, ease:"power2.in", stagger:{frm % (0.17 if center else 0.23)}}}, {st+0.01:.3f});\n'
              f'    tl.to("#{n} .cell", {{scale:0, duration:{0.22 if center else 0.24}, ease:"power2.out", stagger:{frm % (0.22 if center else 0.26)}}}, {at+0.005:.3f});')
    elif k == 'iris':
        el = f'<div id="{n}" class="clip fx" data-start="{at:.3f}" data-duration="0.6" data-track-index="{i%3}" data-label="Iris"><div id="{n}-mask" class="iris-mask"></div></div>'
        js = f'tl.fromTo("#{n}-mask", {{"--r":"0px"}}, {{"--r":"1400px", duration:0.5, ease:"power2.inOut"}}, {at:.3f});'
    elif k == 'leak':
        st = at - 0.2
        el = (f'<div id="{n}" class="clip fx" data-start="{st:.3f}" data-duration="1.3" data-track-index="{i%3}" data-label="Light leak" data-layout-allow-overflow>'
              f'<div id="{n}-glow" class="leak-glow"><div class="leak amber"></div><div class="leak red"></div><div class="leak gold"></div></div></div>')
        js = (f'tl.fromTo("#{n}-glow", {{opacity:0}}, {{opacity:0.85, duration:0.3, ease:"sine.out"}}, {st:.3f});\n'
              f'    tl.to("#{n}-glow", {{opacity:0, duration:0.65, ease:"sine.in"}}, {st+0.35:.3f});\n'
              f'    tl.fromTo("#{n}-glow .amber", {{xPercent:-20, scale:0.92}}, {{xPercent:18, scale:1.1, duration:1.25, ease:"sine.inOut"}}, {st:.3f});\n'
              f'    tl.fromTo("#{n}-glow .red", {{xPercent:20, yPercent:-8}}, {{xPercent:-16, yPercent:8, duration:1.25, ease:"sine.inOut"}}, {st:.3f});\n'
              f'    tl.fromTo("#{n}-glow .gold", {{xPercent:-28}}, {{xPercent:24, duration:1.25, ease:"sine.inOut"}}, {st:.3f});')
    elif k == 'glitch':
        st = at - 0.1
        el = (f'<div id="{n}" class="clip fx" data-start="{st:.3f}" data-duration="0.26" data-track-index="{i%3}" data-label="Glitch">'
              + "".join(f'<div id="{n}-{b}" class="bar g{b}"></div>' for b in "abcd") + '</div>')
        steps = [dict(a=(1,0),b=(0,0),c=(1,0),d=(0,0)), dict(a=(1,140),b=(1,-60),c=(0,0),d=(1,80)), dict(a=(0,0),b=(1,210),c=(1,-120),d=(0,0)),
                 dict(a=(1,-90),b=(0,0),c=(0,0),d=(1,-200)), dict(a=(0,0),b=(1,40),c=(1,60),d=(0,0)), dict(a=(0,0),b=(0,0),c=(0,0),d=(0,0))]
        js = "\n    ".join(f'tl.set("#{n}-{b}", {{opacity:{o}, y:{y}}}, {st + j*0.04:.3f});' for j, stp in enumerate(steps) for b, (o, y) in stp.items())
    else:
        raise SystemExit(f"type de transition inconnu : {k} (flash, grid, grid-center, iris, leak, glitch)")
    return el, js

def scene(plan, dur, W=1920, H=1080):
    ox, oy = plan.get('origin', [W // 2, H // 2])
    rows, cols = GRID[0]
    k = H / 1080
    els, jss = [], []
    for i, tr in enumerate(sorted(plan.get('transitions', []), key=lambda t: t['at'])):
        e, j = fx_parts(i, tr); els.append('    ' + e); jss.append('    ' + j)
    return f'''<template>
  <!-- rythmize : scène générée, relancer rythmize.py apply pour la modifier -->
  <style>
    #transitions {{ position: absolute; inset: 0; pointer-events: none; }}
    #transitions .fx {{ position: absolute; inset: 0; }}
    #transitions .flash {{ background: #EFEFEF; opacity: 0; }}
    #transitions .grid {{ display: grid; grid-template-columns: repeat({cols}, 1fr); grid-template-rows: repeat({rows}, 1fr); }}
    #transitions .grid .cell {{ display: block; background: {plan.get('gridColor', '#121212')}; }}
    #transitions .iris-mask {{ position: absolute; inset: 0; --r: 0px;
      background: radial-gradient(circle at {ox}px {oy}px, transparent var(--r), {plan.get('gridColor', '#121212')} calc(var(--r) + 2px)); }}
    #transitions .leak-glow {{ position: absolute; inset: -16%; opacity: 0; mix-blend-mode: screen; overflow: hidden; }}
    #transitions .leak {{ position: absolute; inset: -20%; }}
    #transitions .amber {{ background: radial-gradient(ellipse 52% 110% at 10% 58%, rgb(255 241 197 / 92%), transparent 45%), radial-gradient(ellipse 72% 120% at 24% 54%, rgb(255 126 57 / 78%), transparent 66%); filter: blur(2.8vmin); }}
    #transitions .red {{ background: radial-gradient(ellipse 58% 105% at 78% 34%, rgb(255 79 61 / 72%), rgb(255 44 92 / 28%) 48%, transparent 76%); filter: blur(4vmin); }}
    #transitions .gold {{ background: linear-gradient(104deg, transparent 24%, rgb(255 144 62 / 30%) 40%, rgb(255 247 205 / 72%) 51%, rgb(255 124 48 / 22%) 62%, transparent 78%); filter: blur(2vmin); }}
    #transitions .bar {{ position: absolute; left: 0; width: {W}px; opacity: 0; }}
    #transitions .ga {{ top: {round(180*k)}px; height: {round(46*k)}px; background: #FF4D00; mix-blend-mode: screen; }}
    #transitions .gb {{ top: {round(520*k)}px; height: {round(22*k)}px; background: #EFEFEF; mix-blend-mode: difference; }}
    #transitions .gc {{ top: {round(760*k)}px; height: {round(70*k)}px; background: #0A0A0A; }}
    #transitions .gd {{ top: {round(360*k)}px; height: {round(12*k)}px; background: #FF4D00; }}
  </style>
  <div id="transitions" data-composition-id="transitions" data-width="{W}" data-height="{H}">
{chr(10).join(els)}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
{chr(10).join(jss)}
    window.__timelines["transitions"] = tl;
  </script>
</template>
'''

CAM_SCRIPT = r'''  <script data-rythmize="camera">
    // rythmize : plan caméra lu dans #rhythm-plan ; il suit les coupes si on les retouche dans Studio.
    const DUR = Number(document.getElementById("root").getAttribute("data-duration"));
    const P = JSON.parse(document.getElementById("rhythm-plan").textContent);
    const tl = gsap.timeline({ paused: true });
    tl.to({ v: 0 }, { v: 1, duration: DUR, ease: "none" }, 0);
    const TIGHT = P.tight || 1.12, PUSH = P.push || 1.05, PUSH_MIN = P.pushMin || 2.8;
    const EMPHASIS = P.emphasis || [], ZT = P.zoomThrough || [];
    const chapOf = v => (P.chapters || {})[(v.dataset.label || "").slice(0, 2)] ?? (v.dataset.label || "").slice(0, 2);
    const clips = [...document.querySelectorAll("#shake > video.clip")]
      .map(v => ({ start: +v.dataset.start, dur: +v.dataset.duration, chap: chapOf(v) }))
      .sort((a, b) => a.start - b.start);
    const near = (a, b) => Math.abs(a - b) < 0.02;
    let prevChap = null, k = 0, cur = 1;
    // Hook : zoom d'ouverture (from -> to en "in" s, puis poussée lente jusqu'à "end" à la fin du hook), petits punch-ins aux coupes
    const HK = P.hook, hookChap = clips.length ? clips[0].chap : null;
    const hookEnd = HK ? Math.max(...clips.filter(c => c.chap === hookChap).map(c => c.start + c.dur)) : 0;
    // HK.at : le plan reste serré (from) jusqu'à "at", puis recule jusqu'à "to" en "in" s (zoom out), puis glisse vers "end"
    const AT = HK && HK.at != null ? HK.at : null;
    const hookAt = t => AT === null
      ? (t <= HK.in ? HK.to : HK.to + (HK.end - HK.to) * (t - HK.in) / Math.max(0.01, hookEnd - HK.in))
      : (t < AT ? HK.from : t < AT + HK.in ? HK.to : HK.to + (HK.end - HK.to) * (t - AT - HK.in) / Math.max(0.01, hookEnd - AT - HK.in));
    clips.forEach((c, i) => {
      const end = c.start + c.dur;
      if (HK && AT !== null && c.chap === hookChap) {
        if (i > 0) k += 1;
        const P1 = HK.punch || 1.06, serre = end <= AT + 0.001;
        const f = k % 2 ? (serre ? 1 / P1 : P1) : 1;
        if (serre) tl.set("#cam", { scale: HK.from * f }, c.start);
        else if (c.start < AT + HK.in) {
          const t0 = Math.max(AT, c.start);
          tl.set("#cam", { scale: HK.from * f }, c.start);
          tl.to("#cam", { scale: HK.to * f, duration: AT + HK.in - t0, ease: "power2.inOut" }, t0);
          tl.to("#cam", { scale: hookAt(end) * f, duration: Math.max(0.01, end - AT - HK.in), ease: "none" }, AT + HK.in);
        } else {
          tl.set("#cam", { scale: hookAt(c.start) * f }, c.start);
          tl.to("#cam", { scale: hookAt(end) * f, duration: c.dur, ease: "none" }, c.start);
        }
        prevChap = c.chap; return;
      }
      if (HK && c.chap === hookChap) {
        if (i === 0) {
          tl.fromTo("#cam", { scale: HK.from || 1 }, { scale: HK.to, duration: HK.in, ease: "power2.out", immediateRender: false }, c.start);
          tl.to("#cam", { scale: hookAt(end), duration: Math.max(0.01, end - c.start - HK.in), ease: "none" }, c.start + HK.in);
        } else {
          k += 1; const f = k % 2 ? (HK.punch || 1.06) : 1;
          tl.set("#cam", { scale: hookAt(c.start) * f }, c.start);
          tl.to("#cam", { scale: hookAt(end) * f, duration: c.dur, ease: "none" }, c.start);
        }
        prevChap = c.chap; return;
      }
      let s;
      if (c.chap !== prevChap) { k = 0; s = 1; }
      else if (c.dur < 0.3) { s = cur; }
      else { k += 1; s = k % 2 ? TIGHT : 1; }
      prevChap = c.chap; cur = s;
      const emph = EMPHASIS.find(e => e.t >= c.start && e.t < end);
      const zIn = ZT.some(t => near(t, c.start));
      const next = clips[i + 1];
      const zOut = next && ZT.some(t => near(t, next.start));
      const outAt = zOut ? end - 0.2 : end;
      if (zIn) tl.fromTo("#cam", { scale: 1.4 }, { scale: s, duration: 0.45, ease: "power3.out", immediateRender: false }, c.start);
      else tl.set("#cam", { scale: s }, c.start);
      const t0 = zIn ? c.start + 0.45 : c.start;
      if (emph) { tl.set("#cam", { scale: emph.scale }, emph.t); s = emph.scale; }
      else if (c.dur >= PUSH_MIN && outAt - t0 > 1) { tl.to("#cam", { scale: s * PUSH, duration: outAt - t0, ease: "sine.inOut" }, t0); s *= PUSH; }
      if (zOut) tl.to("#cam", { scale: s * 1.35, duration: 0.2, ease: "power2.in" }, end - 0.2);
    });
    const SHAKE = [[16, -9, 0.7], [-13, 7, -0.6], [10, 6, 0.45], [-7, -5, -0.3], [4, 3, 0.15], [-2, -1, 0], [0, 0, 0]];
    (P.shake || []).forEach(t0 => SHAKE.forEach(([x, y, r], i) => tl.to("#shake", { x, y, rotation: r, duration: 0.045, ease: "none" }, t0 + i * 0.045)));
    (P.transitions || []).filter(t => t.type === "glitch").forEach(t =>
      [[-28, 0], [22, 0], [-12, 0], [0, 0]].forEach(([x, y], i) => tl.set("#shake", { x, y }, t.at - 0.06 + i * 0.034)));
    window.__timelines = window.__timelines || {};
    window.__timelines["main"] = tl;
  </script>'''

def apply(plan_path):
    plan = json.load(open(plan_path, encoding='utf-8'))
    p = 'index.html'; s = open(p, encoding='utf-8').read()
    dur = root_duration(s)
    W, H = root_size(s)
    GRID[0] = (16, 9) if H > W else (9, 16)
    ox, oy = plan.get('origin', [W // 2, H // 2])
    # 1. caméra : envelopper les <video> du rush (une seule fois)
    if 'id="cam"' not in s:
        m = re.search(r'(<div\b[^>]*data-composition-id="main"[^>]*>)(.*?)(\n  </div>\n)', s, re.S)
        if not m: raise SystemExit("racine introuvable : envelopper les vidéos à la main dans <div id=\"cam\"><div id=\"shake\">")
        inner = m.group(2)
        vids = re.findall(r'[ \t]*<video\b[^>]*>\s*</video>', inner)
        if not vids: raise SystemExit("aucune <video> à la racine")
        rest = inner
        for v in vids: rest = rest.replace(v, '', 1)
        cam = ('\n    <!-- rythmize : caméra (zooms, punch-ins, secousses) -->\n    <div id="cam" data-layout-allow-overflow><div id="shake">\n'
               + '\n'.join('  ' + v.strip() for v in vids) + '\n    </div></div>')
        s = s[:m.start(2)] + cam + rest + s[m.end(2):]
    css = f'    #cam, #shake {{ position:absolute; inset:0; transform-origin: {ox}px {oy}px; }}\n    #cam {{ z-index:1; overflow:hidden; }}\n'
    if '#cam, #shake' in s: s = re.sub(r'    #cam, #shake \{[^}]*\}\n    #cam \{[^}]*\}\n', css, s)
    else: s = s.replace('</style>', css + '  </style>', 1)
    # 2. hôte de la scène de transitions + whoosh (remplacés à chaque apply)
    s = re.sub(r'\n    <!-- rythmize:fx -->.*?<!-- /rythmize:fx -->', '', s, flags=re.S)
    # anciennes versions écrites à la main (Studio peut avoir ajouté des data-hf-id)
    s = re.sub(r'\n[ \t]*<!-- (Transitions de chapitre|Whoosh \(CC0\))[^\n]*-->', '', s)
    s = re.sub(r'\n[ \t]*<div\b[^>]*\sid="transitions"[^>]*>\s*</div>', '', s)
    s = re.sub(r'\n[ \t]*<audio\b[^>]*\sid="whoosh-[^"]*"[^>]*>\s*</audio>', '', s)
    fx = ['    <!-- rythmize:fx -->',
          f'    <div id="transitions" data-composition-id="transitions" data-composition-src="compositions/transitions.html" data-start="0" data-duration="{dur}" data-track-index="2" data-track-kind="graphics" data-width="{W}" data-height="{H}" data-label="Transitions" style="z-index:5"></div>']
    for i, w in enumerate(plan.get('whoosh', [])):
        st = max(0.0, float(w['at']) - float(w.get('peakOffset', 0)))
        fx.append(f'    <audio id="whoosh-{i+1}" class="clip" src="{html.escape(w["file"])}" data-start="{st:.3f}" data-duration="{w.get("duration", 0.6)}" '
                  f'data-track-index="{3 + i % 2}" data-volume="{w.get("volume", 0.6)}" data-label="{html.escape(w.get("label", "Whoosh"))}"></audio>')
    fx.append('    <!-- /rythmize:fx -->')
    # insérer juste avant la fermeture de la racine (la ligne "  </div>" qui suit le bloc caméra)
    idx = s.find('\n  </div>', s.find('</div></div>', s.find('id="cam"')) + 12)
    s = s[:idx] + '\n' + '\n'.join(fx) + s[idx:]
    # 3. plan + script caméra
    planjson = json.dumps({k: plan[k] for k in ('chapters', 'hook', 'tight', 'push', 'pushMin', 'emphasis', 'zoomThrough', 'shake', 'transitions') if k in plan}, ensure_ascii=False)
    s = re.sub(r'  <script id="rhythm-plan" type="application/json">.*?</script>\n', '', s, flags=re.S)
    s = re.sub(r'  <script data-rythmize="camera">.*?</script>', '', s, flags=re.S)
    s = re.sub(r'  <script>\n    // Plan caméra calculé.*?</script>', '', s, flags=re.S)
    s = re.sub(r'  <script>\n    const tl = gsap\.timeline\(\{ paused: true \}\);\n    const clock.*?</script>', '', s, flags=re.S)
    block = f'  <script id="rhythm-plan" type="application/json">{planjson}</script>\n' + CAM_SCRIPT
    s = s.replace('</body>', block + '\n</body>', 1)
    s = re.sub(r'\n\s*\n(\s*<script id="rhythm-plan")', r'\n\1', s)
    open(p, 'w', encoding='utf-8').write(s)
    os.makedirs('compositions', exist_ok=True)
    open('compositions/transitions.html', 'w', encoding='utf-8').write(scene(plan, dur, W, H))
    print(json.dumps({"ok": True, "transitions": len(plan.get('transitions', [])), "whoosh": len(plan.get('whoosh', [])),
                      "emphasis": len(plan.get('emphasis', [])), "shake": len(plan.get('shake', []))}))

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] not in ('analyze', 'apply'): raise SystemExit(__doc__)
    analyze() if a[0] == 'analyze' else apply(a[1])
