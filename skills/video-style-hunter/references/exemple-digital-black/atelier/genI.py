import json, math, os, sys
R=os.path.dirname(os.path.abspath(__file__))
OUT=sys.argv[1] if len(sys.argv)>1 else f'{R}/atelier/project'
os.makedirs(OUT,exist_ok=True)
fav=json.load(open(f'{R}/favoris.json'))
for i,e in enumerate(fav,1): e['n']=i; e['url']='/_blob/'+e['blob']; e['gif']=e['local'].endswith('.gif')
# n: (légende, renvoi composant)
CAP={
1:('Mot clé géant, 2e police, sous le visage','A · SousTitreDuo'),2:('Même scène, autre instant','A · SousTitreDuo'),
3:('Mot clé géant en couleur sous le visage','A · SousTitreDuo'),4:('Gros mot posé sur le buste','A · SousTitreDuo'),
5:('Mot dans un cadre de sélection','A · TitreChoc sélection'),6:('Sous-titres seuls, plan net (extrait)','C1'),
7:('Trois étapes numérotées sous le titre','K-C2 · points d’étape'),8:('Widgets en verre autour d’elle','K-C2'),
9:('Mot sélectionné + barre d’outils du logiciel','K-C2'),10:('Palette de couleurs façon logiciel','K-C2'),
11:('Éclats dessinés derrière elle','B · derrière toi'),12:('Petite fenêtre d’appli près du visage','K-C2'),
13:('Nuancier en haut, lui en bas','K-C3'),14:('Le nuancier se remplit (extrait)','K-C3'),
15:('Jauge « effect usage » 4 / 9','K-C3'),16:('Titre au-dessus de la tête (extrait)','K-C3'),
17:('Icône d’appli géante + pastille −25 %','K-D3'),18:('Deux scores côte à côte, 53 / 53','K-C3'),
19:('Capture du logiciel en haut, lui en bas','K-C3'),20:('La jauge avance (extrait)','K-C3'),
21:('Ses plans en cartes qui tombent (extrait)','K-D2 V1'),22:('Phrase + carte qui arrive (extrait)','K-D2 V1'),
23:('Cartes de plans + phrase sur grille claire','K-D2 V1'),24:('Œil + petits widgets timeline et son','K-C4'),
25:('Logos en étiquettes autour d’une phrase','K-D1'),26:('Icône cerveau au trait sur noir','K-D3 V2'),
27:('Checklist 20 / 20 sur fond sombre','K-D4 V1'),28:('Jour 45 · 1 350 €, chiffre géant','K-D1'),
29:('Schéma deux ronds + pastille PLAN.md','K-D4 V2'),30:('Carte d’image dans un cadre braise','K-D3'),
31:('Menu d’interface sur grille claire','K-D4'),32:('Fichiers et dossier au centre','K-D3'),
33:('Deux colonnes titre + texte, photo coupée','K-D1'),34:('Pellicule photo + mot « PROMPTS »','K-D2'),
35:('Terminal claude code, étapes cochées','K-D4 V3'),36:('Carte de dépôt GitHub','K-D4'),
37:('Terminal /agents, liste à puces','K-D4 V3'),38:('Gros titre + foule en noir et blanc','K-D2'),
39:('Gros titre + touche Ctrl braise','K-D1 V3'),40:('Titre manuscrit + pastille, page claire','K-D1'),
41:('Gros titre + curseur géant','K-D1'),42:('Mot dans un cadre de sélection, page à grille','K-D1 V2'),
43:('Statue au portable sur page claire','K-D2 V2'),44:('Personnage tramé au téléphone','K-D2 V2'),
45:('Personne détourée + flèche dessinée','K-D2'),46:('Statue penseur sur noir + titre','K-D2 V2'),
47:('Crâne scanné en N&B + phrase','K-D3'),48:('Touche Ctrl géante, petit personnage','K-D3 V3'),
49:('Pince qui attrape la touche Shift','K-D3'),50:('Clé à molette + gros titre','K-D3'),
51:('Touche Ctrl sous le titre','K-D3 V3'),52:('Touche Esc noire inclinée','K-D3 V1'),
53:('Touche Esc + flèches en pointillés','K-D3 V1'),54:('Feu rouge sur grille sombre','K-D3'),
55:('Référence Joseph : main vers l’objectif (extrait)','K-B'),56:('Mot clé géant à côté de lui','K-B'),
57:('Titre en deux polices au-dessus de lui','K-B'),
}
RAYONS=[
 ('IU','Interfaces','I · rayon 1 · {n} favoris','Interfaces — un vrai logiciel à l’écran',
  "Fenêtres, widgets, terminaux, menus, fichiers. Ce qu’ils ont en commun : un seul morceau d’interface, propre, bien net, jamais une capture d’écran entière.",
  [8,9,10,12,13,14,19,24,17,27,30,31,32,35,36,37]),
 ('IG','Graphiques et chiffres','I · rayon 2 · {n} favoris','Graphiques et chiffres',
  "Un chiffre géant, une jauge, deux scores, un schéma à deux ronds, des étapes numérotées. Toujours une seule donnée à lire, en grand.",
  [28,18,15,20,29,7]),
 ('IS1','Scènes complètes — avec toi','I · rayon 3a · {n} favoris','Scènes complètes — avec toi à l’écran',
  "Le plan face caméra reste net ; le texte ou le petit élément vient près de toi, jamais sur le visage.",
  [55,56,57,1,2,3,4,5,6,11,16]),
 ('IS2','Scènes complètes — plein écran','I · rayon 3b · {n} favoris','Scènes complètes — plein écran',
  "Un gros titre et un seul objet héros : touche de clavier, statue, personne détourée, icône. Chez toi : Doto à la place de l’italique serif, fond noir ou blanc os à la place des aplats de couleur, un seul élément braise.",
  [39,48,51,52,53,49,50,54,47,26,25,41,42,38,40,33,43,44,45,46,34,21,22,23]),
]
assert sorted(sum([r[5] for r in RAYONS],[]))==list(range(1,58))
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800;900&amp;family=Doto:wght@900&amp;family=Inter:wght@500;700;800&amp;family=JetBrains+Mono:wght@600&amp;display=swap">'
BG='#121212'; OS='#EFEFEF'; BRUME='#A3A3A3'; BRAISE='#FF7033'; GRAPH='#1A1A1A'; ACIER='#3A3A3A'
MONO="font-family: 'JetBrains Mono', monospace; font-weight: 600"
def page(fichier,title,w,h,body):
    open(f'{OUT}/{fichier}','w').write(f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
body{{margin:0}}
</style>
</helmet>
<div style="width: {w}px; height: {h}px; box-sizing: border-box; padding: 48px; background: {BG}; color: {OS}; font-family: Inter, sans-serif; display: flex; flex-direction: column; gap: 28px">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
''')
def header(label,titre,texte):
    return f'''<div style="display: flex; flex-direction: column; gap: 14px">
<div style="display: flex; align-items: center; gap: 12px"><span style="display: inline-block; width: 14px; height: 14px; background: {BRAISE}"></span><span style="{MONO}; font-size: 15px; letter-spacing: 0.08em; text-transform: uppercase; color: {BRUME}">{label}</span></div>
<h1 style="margin: 0; font-family: 'Big Shoulders Display', sans-serif; font-weight: 900; font-size: 68px; line-height: 0.95; letter-spacing: 0.01em; text-transform: uppercase">{titre}</h1>
<p style="margin: 0; max-width: 1100px; font-size: 20px; line-height: 1.45; font-weight: 500; color: {BRUME}">{texte}</p>
</div>'''
TW,TH,COLS=216,384,6
def grille(ns):
    cells=[]
    for n in ns:
        e=fav[n-1]; cap,comp=CAP[n]
        badge=f'<span style="padding: 3px 7px; border-radius: 3px; background: {OS}; color: #0A0A0A; {MONO}; font-size: 11px">{e["planches"][0].split()[0]}</span>'
        if e['gif']: badge+=f'<span style="padding: 3px 7px; border-radius: 3px; background: {BRAISE}; color: #0A0A0A; {MONO}; font-size: 11px">EXTRAIT</span>'
        cells.append(f'''<figure style="margin: 0; width: {TW}px; display: flex; flex-direction: column; gap: 8px">
<div style="position: relative; width: {TW}px; height: {TH}px; box-sizing: border-box; border: 2px solid {ACIER}; border-radius: 6px; overflow: hidden; background: {GRAPH}"><img src="{e['url']}" alt="{cap}" style="width: 100%; height: 100%; object-fit: contain; display: block"><div style="position: absolute; top: 8px; left: 8px; display: flex; gap: 6px">{badge}</div></div>
<figcaption style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 14px; line-height: 1.35; font-weight: 500; color: {OS}">{cap}</span><span style="{MONO}; font-size: 12px; color: {BRUME}">→ {comp}</span></figcaption>
</figure>''')
    return f'<div style="display: grid; grid-template-columns: repeat({COLS}, {TW}px); gap: 32px 24px">\n'+'\n'.join(cells)+'\n</div>'
W=48*2+COLS*TW+(COLS-1)*24
def haut(n,head=171): rows=math.ceil(n/COLS); return 48+head+28+rows*(TH+8+57)+(rows-1)*32+48
boards={}
for code,court,label,titre,texte,ns in RAYONS:
    f=f'PI-{code}.dc.html'; h=haut(len(ns))
    page(f,f'I — {court}',W,h,header(label.format(n=len(ns)),titre,texte)+'\n'+grille(ns)); boards[f]=(W,h,f'I — {court}')
json.dump(boards,open(f'{R}/boards-I.json','w'),ensure_ascii=False)
print(boards)
