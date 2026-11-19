python3 gen3.py out3 >/dev/null && python3 - <<'PY'
import json,os,shutil
t=json.load(open('out3/project/tokens.json'))
v=[]
for cat in ('color','spacing','radius','shadow','stroke','duration','easing','blur'):
    for x in t[cat]['tokens']: v.append(f"--{x['name']}:{x['value']}")
for k,f in t['type']['families'].items(): v.append(f"--font-{k}:{f}")
open('test3/tokens.css','w').write(':root{'+';'.join(v)+'}')
shutil.copy('out3/project/components/bundle.css','test3/bundle.css')
for c in os.listdir('out3/project/components'):
    p=f'out3/project/components/{c}/preview.html'
    if not os.path.exists(p): continue
    s=open(p).read().replace('<meta charset="utf-8">','<meta charset="utf-8"><link rel="stylesheet" href="tokens.css"><link rel="stylesheet" href="bundle.css">',1).replace('/_blob/','_blob/')
    open(f'test3/{c}.html','w').write(s)
print('ok')
PY
