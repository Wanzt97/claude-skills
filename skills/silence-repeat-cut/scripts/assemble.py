#!/usr/bin/env python3
"""Assemble les morceaux du face caméra en UNE vidéo continue (aperçu fluide, coupes du son sans clic).

Après un silence/repeat cut, le rush est joué par des dizaines de <video> collés bout à bout :
l'aperçu doit sauter dans le fichier à chaque coupe (il rame) et chaque coupe nette du son claque.
Ce script fabrique un seul mp4 qui contient déjà le montage, avec un fondu de 6 ms à chaque coupe du son,
et remplace les morceaux par un seul <video>. Les balises d'origine sont gardées : --undo les remet
(l'onglet Script peut alors de nouveau couper ou remettre des mots).

À lancer depuis le dossier du projet :
  python3 -I assemble.py            # assemble (ne fait rien si c'est déjà assemblé)
  python3 -I assemble.py --dry-run  # dit ce qu'il ferait
  python3 -I assemble.py --undo     # remet les morceaux d'origine
Options : --fps 30, --fade 0.006 (s), --crf 15.
"""
import argparse, json, os, re, subprocess, sys
from collections import Counter

OUT_DIR = 'assets/facecam'
CUTS_ID = 'facecam-cuts'
CAM_OLD = 'const clips = [...document.querySelectorAll("#shake > video.clip")]\n      .map(v => ({ start: +v.dataset.start, dur: +v.dataset.duration, chap: chapOf(v) }))'
CAM_NEW = 'const clips = (document.getElementById("facecam-cuts") ? JSON.parse(document.getElementById("facecam-cuts").textContent).cuts.map(c => ({ dataset: { start: c.start, duration: c.dur, label: c.label } })) : [...document.querySelectorAll("#shake > video.clip")])\n      .map(v => ({ start: +v.dataset.start, dur: +v.dataset.duration, chap: chapOf(v) }))'


def attr(tag, k):
    m = re.search(r'\s' + re.escape(k) + r'="([^"]*)"', tag)
    return m.group(1) if m else None


def find_videos(s):
    """Les <video> du film principal (pas ceux des sous-compositions)."""
    out = []
    for m in re.finditer(r'[ \t]*<video\b[^>]*>\s*</video>[ \t]*\n?', s):
        tag = m.group(0)
        if attr(tag, 'data-start') is None:
            continue
        out.append(dict(m=m, tag=tag, src=attr(tag, 'src'), start=float(attr(tag, 'data-start')),
                        dur=float(attr(tag, 'data-duration')), ms=float(attr(tag, 'data-media-start') or 0),
                        track=attr(tag, 'data-track-index'), vol=attr(tag, 'data-volume') or '1',
                        rate=attr(tag, 'data-playback-rate'), label=attr(tag, 'data-label') or '', id=attr(tag, 'id')))
    return out


def runs_of(clips):
    """Groupes de morceaux qui se suivent sans trou et avancent dans le rush."""
    runs, cur = [], []
    for c in sorted(clips, key=lambda c: c['start']):
        if cur and (abs(cur[-1]['start'] + cur[-1]['dur'] - c['start']) > 0.002 or c['ms'] < cur[-1]['ms'] + cur[-1]['dur'] - 0.002):
            runs.append(cur); cur = []
        cur.append(c)
    if cur:
        runs.append(cur)
    return [r for r in runs if len(r) >= 2]


def build(run, src, out, fps, fade, crf):
    terms, af = [], []
    for i, r in enumerate(run):
        t0 = r['start'] - run[0]['start']
        n0, n1 = round(t0 * fps), round((t0 + r['dur']) * fps)
        off = round((r['ms'] - t0) * fps)
        terms.append(f"between(n\\,{n0 + off}\\,{n1 + off - 1})")
        a0 = r['ms'] + (n0 / fps - t0); a1 = r['ms'] + (n1 / fps - t0); d = a1 - a0
        af.append(f"[a{i}]atrim=start={a0:.6f}:end={a1:.6f},asetpts=PTS-STARTPTS,"
                  f"afade=t=in:d={fade},afade=t=out:st={max(0, d - fade):.6f}:d={fade}[b{i}]")
    n = len(run)
    fc = (f"[0:v]fps={fps},select='{'+'.join(terms)}',setpts=N/{fps}/TB[v];"
          f"[0:a]asplit={n}" + ''.join(f"[a{i}]" for i in range(n)) + ";" + ";".join(af) + ";"
          + ''.join(f"[b{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[a]")
    script = out + '.filter.txt'
    open(script, 'w').write(fc)
    try:
        subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', src, '-filter_complex_script', script,
                        '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-preset', 'slow', '-crf', str(crf),
                        '-g', '15', '-keyint_min', '15', '-sc_threshold', '0', '-pix_fmt', 'yuv420p',
                        '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-r', str(fps),
                        '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-movflags', '+faststart', out], check=True)
    finally:
        os.remove(script)


def undo(s):
    m = re.search(r'[ \t]*<script type="application/json" id="' + CUTS_ID + r'">(.*?)</script>\n?', s, re.S)
    if not m:
        sys.exit('Rien à défaire : le face caméra n\'est pas assemblé.')
    data = json.loads(m.group(1))
    groups = data['groups'] if isinstance(data, dict) else None
    if not groups:
        sys.exit('Ancien format sans les balises d\'origine : remettre les morceaux depuis l\'historique de l\'app.')
    for g in groups:
        tag = re.search(r'[ \t]*<video\b[^>]*\sid="' + re.escape(g['id']) + r'"[^>]*>\s*</video>[ \t]*\n?', s)
        if not tag:
            sys.exit(f"Vidéo assemblée {g['id']} introuvable.")
        s = s[:tag.start()] + ''.join(g['tags']) + s[tag.end():]
    m = re.search(r'[ \t]*<script type="application/json" id="' + CUTS_ID + r'">.*?</script>\n?', s, re.S)
    s = s[:m.start()] + s[m.end():]
    return s.replace(CAM_NEW, CAM_OLD), sum(len(g['tags']) for g in groups)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--undo', action='store_true'); ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--fps', type=int, default=30); ap.add_argument('--fade', type=float, default=0.006)
    ap.add_argument('--crf', type=int, default=15); ap.add_argument('--index', default='index.html')
    a = ap.parse_args()
    s = open(a.index, encoding='utf-8').read()

    if a.undo:
        s, n = undo(s)
        open(a.index, 'w', encoding='utf-8').write(s)
        print(json.dumps({'undone': True, 'clipsRestored': n})); return

    if f'id="{CUTS_ID}"' in s:
        print(json.dumps({'alreadyAssembled': True})); return
    vids = find_videos(s)
    if not vids:
        sys.exit('Aucune vidéo dans le film principal.')
    src = Counter(v['src'] for v in vids).most_common(1)[0][0]
    track = Counter(v['track'] for v in vids if v['src'] == src).most_common(1)[0][0]
    clips = [v for v in vids if v['src'] == src and v['track'] == track]
    bad = [c['id'] for c in clips if c['rate'] not in (None, '1') or c['vol'] != clips[0]['vol']]
    if bad:
        sys.exit(f'Vitesse ou volume différents sur {bad} : assemblage manuel, pas ce script.')
    runs = runs_of(clips)
    report = {'source': src, 'clips': len(clips), 'groups': [{'from': r[0]['start'], 'to': round(r[-1]['start'] + r[-1]['dur'], 3), 'clips': len(r)} for r in runs]}
    if not runs:
        print(json.dumps({**report, 'nothingToDo': True})); return
    if a.dry_run:
        print(json.dumps(report, ensure_ascii=False)); return

    os.makedirs(OUT_DIR, exist_ok=True)
    base = re.sub(r'[^a-z0-9]+', '-', os.path.splitext(os.path.basename(src))[0].lower()).strip('-') or 'face-camera'
    groups, cuts = [], []
    for gi, run in enumerate(runs):
        out = f'{OUT_DIR}/{base}-monte{"-" + str(gi + 1) if len(runs) > 1 else ""}.mp4'
        build(run, src, out, a.fps, a.fade, a.crf)
        vid = f'face-camera{"-" + str(gi + 1) if len(runs) > 1 else ""}'
        t0, end = run[0]['start'], run[-1]['start'] + run[-1]['dur']
        z = attr(run[0]['tag'], 'style') or 'z-index:1'
        new = (f'      <video id="{vid}" class="clip" src="{out}" data-start="{t0:g}" data-duration="{end - t0:.3f}" '
               f'data-track-index="{track}" data-media-start="0" preload="auto" playsinline data-has-audio="true" '
               f'data-volume="{run[0]["vol"]}" style="{z}" data-label="Face caméra ({len(run)} coupes assemblées)"></video>\n')
        groups.append({'id': vid, 'file': out, 'tags': [c['tag'] for c in run]})
        cuts += [{'start': c['start'], 'dur': c['dur'], 'label': c['label']} for c in run]
        # remplace le 1er morceau du groupe par la vidéo assemblée, retire les autres
        first = run[0]['tag']
        s = s.replace(first, new, 1)
        for c in run[1:]:
            s = s.replace(c['tag'], '', 1)
    blob = json.dumps({'cuts': cuts, 'groups': groups}, ensure_ascii=False).replace('<', '\\u003c')  # aucune balise lisible dans le JSON
    anchor = re.search(r'[ \t]*<video id="face-camera[^"]*"[^>]*></video>\n', s)
    s = s[:anchor.end()] + f'      <script type="application/json" id="{CUTS_ID}">{blob}</script>\n' + s[anchor.end():]
    cam = CAM_OLD in s
    s = s.replace(CAM_OLD, CAM_NEW)
    open(a.index, 'w', encoding='utf-8').write(s)
    json.dump({'cuts': cuts, 'groups': groups}, open(f'{OUT_DIR}/coupes.json', 'w'), ensure_ascii=False, indent=1)
    print(json.dumps({**report, 'files': [g['file'] for g in groups], 'cameraScriptPatched': cam}, ensure_ascii=False))


if __name__ == '__main__':
    main()
