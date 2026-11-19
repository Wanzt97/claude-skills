python3 - <<'PY'
import json,os,shutil
t=json.load(open('out4/project/tokens.json'))
v=[]
for cat in ('color','spacing','radius','shadow','stroke','duration','easing','blur'):
    for x in t[cat]['tokens']: v.append(f"--{x['name']}:{x['value']}")
for k,f in t['type']['families'].items(): v.append(f"--font-{k}:{f}")
open('test4/tokens.css','w').write(':root{'+';'.join(v)+'}')
shutil.copy('out4/project/components/bundle.css','test4/bundle.css')
for c in os.listdir('out4/project/components'):
    p=f'out4/project/components/{c}/preview.html'
    if not os.path.exists(p): continue
    s=open(p).read().replace('<meta charset="utf-8">','<meta charset="utf-8"><link rel="stylesheet" href="tokens.css"><link rel="stylesheet" href="bundle.css">',1).replace('/_blob/','_blob/')
    open(f'test4/{c}.html','w').write(s)
print('ok')
PY
