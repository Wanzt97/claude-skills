import json,hashlib,os,sys
S=sys.argv[1]
def up(p):
    m={}
    for l in open(p):
        t=l.split()
        if len(t)>=2: m[t[0]]=t[1]
    return m
out=[];seen={}
def add(planche,code,src,f,blob,local):
    h=hashlib.md5(open(src,'rb').read()).hexdigest() if os.path.exists(src) else f
    if h in seen:
        seen[h]['planches'].append(planche+' '+code); return
    e=dict(planche=planche,code=code,f=f,src=src,blob=blob,local=local,planches=[planche+' '+code])
    seen[h]=e; out.append(e)
# C
uc=up(S+'/moodC/uploads-atelier.txt')
for x in json.load(open(S+'/moodC/sel.json')):
    if x['fav'] and not x['rej']:
        k=x['out'].split('.')[0]
        add('C',x['code'],x['src'],x['f'],uc[k],S+'/moodC/img/'+x['out'])
ud=up(S+'/lotDG/uploads-D.txt')
for x in json.load(open(S+'/lotDG/sel.json')):
    if x['fav']:
        k='%02d'%x['n']
        add('D',x['code'],x['src'],x['f'],ud[k],S+'/lotDG/'+x['out'])
ub=up(S+'/lotB/uploads-D.txt')
for i,x in enumerate(json.load(open(S+'/lotB/sel.json'))):
    if x['fav']:
        k=x.get('out','').split('/')[-1].split('.')[0] or '%02d'%(i+1)
        add('B',x['code'],x['src'],x['f'],ub.get(k) or ub.get('%02d'%(i+1)),S+'/lotB/'+x.get('out',''))
json.dump(out,open(S+'/lotI/favoris.json','w'),ensure_ascii=False,indent=1)
for i,e in enumerate(out,1): print(i,' / '.join(e['planches']),e['f'][:50],os.path.exists(e['local']),e['blob'])
