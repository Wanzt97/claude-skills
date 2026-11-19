import json, math, sys, datetime
R=sys.argv[1]
blob={l.split()[0]:l.split()[1] for l in open(f'{R}/uploads.txt')}
sel=json.load(open(f'{R}/sel.json'))
for i,e in enumerate(sel,1): e['url']='/_blob/'+blob[f'{i:03d}']; e['n']=i
CAP={1:'Petite amorce, mot géant qui la chevauche',2:'Même plan, 0,2 s plus tard',3:'Mot clé géant en couleur',4:'Petit, géant, petit',5:'Mot géant encadré de petits mots',
6:'Titre dans une boîte sur fond blanc',7:'Petit mot seul',8:'Face caméra sans texte',9:'Petit « The » au-dessus de la tête',
10:'Sous-titre + petits points 1-2-3 juste dessous',11:'Même plan, image fixe',12:'Widgets en verre autour de la personne',13:'Texte sélectionné à l’écran, poignées',14:'Palette de couleurs façon logiciel',15:'Pastille de chat en haut',16:'Capture d’app avec une fenêtre qui s’ouvre',
17:'Bandeaux « breaking » autour du visage',18:'Titres de journaux en fond',19:'Petite carte en bas à droite',20:'Titre encadré sur fond blanc',21:'Personnage illustré en haut',22:'Mots sur plaques de couleur',23:'Checklist sur fond flouté',24:'Carte « problème » en haut',25:'Graphique en haut, personne en bas',
26:'Paillettes et halo autour de la tête',27:'Visage qui se brise en éclats',28:'Décor remplacé + créature',
29:'Bande claire en haut (palette), visage en bas',30:'La bande claire s’allume pendant qu’il parle',31:'Curseur d’interface en haut, sous-titre à la jointure',32:'Les pastilles arrivent une à une',33:'Une icône d’app seule en haut',34:'Deux scores face à face en haut',35:'Capture d’écran en haut, visage en bas',36:'Passage face caméra → écran partagé',
37:'Carte plan + logo en haut',38:'Fenêtres de code en haut',39:'Boutons en pastilles + personne en bas',
40:'Papier clair : phrase + carte vidéo',41:'La phrase arrive, la carte monte',42:'Grandes icônes sur papier',43:'Un objet central (œil) + petites cartes UI',44:'Logos de marques posés en cercle',45:'Illustration seule sur fond sombre',46:'Checklist sombre, numéro en couleur',47:'Chiffre géant sur papier, légende fine',48:'Schéma aller-retour sur papier',49:'Deux cartes qui travaillent ensemble',50:'Interface sur grille, mot géant',51:'Objet (dossier) au centre d’un aplat',52:'Avant / après sur papier',53:'Pellicule d’images',54:'Terminal propre sur fond sombre',55:'Fiche dépôt GitHub sombre',56:'Liste d’agents en terminal',
57:'Texte seul, police éditoriale',58:'Texte seul, deux tailles',59:'Mot-titre + image d’écran',60:'Mot-titre + illustration',61:'Carte d’app sur fond sombre',62:'Titre + image + frise de progression',63:'Même frise, étape suivante',64:'Même frise, étape suivante',65:'Chiffre géant (2 500 étoiles)',66:'Appel à l’action en grosses lettres',67:'Deux logos face à face',68:'Écran de téléphone au centre',69:'Mise en page magazine',
70:'Affiche de soirée chargée',71:'Photo de profil + gros texte',72:'Mots géants sur capture',73:'Gros titre « Animated captions »',74:'Page GitHub claire',75:'Capture d’interface entière',76:'Grille d’avatars ronds',77:'Page web entière'}
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800;900&amp;family=Doto:wght@900&amp;family=Inter:wght@500;700;800&amp;family=JetBrains+Mono:wght@600&amp;display=swap">'
BG='#121212'; OS='#EFEFEF'; BRUME='#A3A3A3'; BRAISE='#FF7033'; GRAPH='#1A1A1A'; ACIER='#3A3A3A'
def page(fichier,title,w,h,body):
    open(f'{R}/root/project/{fichier}','w').write(f'''<!doctype html>
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
<div style="display: flex; align-items: center; gap: 12px"><span style="display: inline-block; width: 14px; height: 14px; background: {BRAISE}"></span><span style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 15px; letter-spacing: 0.08em; text-transform: uppercase; color: {BRUME}">{label}</span></div>
<h1 style="margin: 0; font-family: 'Big Shoulders Display', sans-serif; font-weight: 900; font-size: 68px; line-height: 0.95; letter-spacing: 0.01em; text-transform: uppercase">{titre}</h1>
<p style="margin: 0; max-width: 1100px; font-size: 20px; line-height: 1.45; font-weight: 500; color: {BRUME}">{texte}</p>
</div>'''
def grille(items,tw=216,th=384,cols=5):
    cells=[]
    for e in items:
        badge=''
        if e['out'].endswith('.gif'): badge+=f'<span style="padding: 3px 7px; border-radius: 3px; background: {BRAISE}; color: #0A0A0A; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 11px">EXTRAIT</span>'
        if e['fav']: badge+=f'<span style="padding: 3px 7px; border-radius: 3px; background: {OS}; color: #0A0A0A; font-family: \'JetBrains Mono\', monospace; font-weight: 600; font-size: 11px">++</span>'
        bord=f'border: 2px solid {ACIER};' if not e['rej'] else 'border: 2px solid #5A2A1A; opacity: 0.85;'
        cells.append(f'''<figure style="margin: 0; width: {tw}px; display: flex; flex-direction: column; gap: 8px">
<div style="position: relative; width: {tw}px; height: {th}px; box-sizing: border-box; {bord} border-radius: 6px; overflow: hidden; background: {GRAPH}"><img src="{e['url']}" alt="{CAP[e['n']]}" style="width: 100%; height: 100%; object-fit: cover; display: block"><div style="position: absolute; top: 8px; left: 8px; display: flex; gap: 6px">{badge}</div></div>
<figcaption style="font-size: 14px; line-height: 1.35; font-weight: 500; color: {BRUME}">{CAP[e['n']]}</figcaption>
</figure>''')
    return f'<div style="display: grid; grid-template-columns: repeat({cols}, {tw}px); gap: 32px 24px">\n'+'\n'.join(cells)+'\n</div>'
W=1240
def haut(n,cols=5,th=384,head=260):
    rows=math.ceil(n/cols); return 48+head+28+rows*(th+8+58)+(rows-1)*32+48
boards={}
def add(f,title,label,titre,texte,items,**kw):
    cols=kw.get('cols',5); th=kw.get('th',384)
    body=header(label,titre,texte)+'\n'+grille(items,**kw)
    h=haut(len(items),cols,th); page(f,title,W,h,body); boards[f]=(W,h,title)
G=lambda code,rej=False,fav=None: [e for e in sel if e['code']==code and e['rej']==rej and (fav is None or e['fav']==fav)]
add('C1.dc.html','C1 — Sous-titres seuls','C1 · gardé · 17 (5 montrés)','Sous-titres seuls',"Toi face caméra, rien d’autre que le bloc de sous-titres. Déjà réglé par la planche A : le duo petite amorce + mot géant. Tes refus le confirment : pas de petit texte seul, pas de titre dans une boîte sur fond blanc.",G('C1')+G('C1',True))
add('C2.dc.html','C2 — Sous-titres + petite animation','C2 · gardé · 16 (7 ++)','Sous-titres + petite animation',"Tu restes le sujet, plein cadre. Un seul petit élément d’interface apparaît près de toi : des points d’étape sous le sous-titre, une fenêtre d’app, une palette, des poignées de sélection, des widgets en verre. Il ressemble à un vrai logiciel. Refusé : les effets sur le décor ou sur le visage (paillettes, éclats, décor remplacé).",G('C2',fav=True)+G('C2',fav=False)+G('C2',True))
add('C3.dc.html','C3 — Écran partagé','C3 · gardé · 11 (8 ++) · aucun refus','Écran partagé',"Ton favori net : le montage de référence. Une bande claire en haut (papier blanc cassé, légère texture), environ 40 % de la hauteur, avec UN seul objet d’interface au centre (palette, curseur, icône, deux scores). Toi en bas, coupé net à la jointure. Le sous-titre se pose juste sous la jointure, sur ton plan.",G('C3',fav=True)+G('C3',fav=False))
add('C4a.dc.html','C4 — Plein écran : tes favoris','C4 · 17 favoris sur 40 gardés','Plein écran — tes favoris',"Deux familles. 1) Le papier clair : fond blanc cassé, un seul objet au centre (carte vidéo, icônes, œil, logos, chiffre), une phrase courte en petit avec un mot mis en avant, des ombres douces sous les cartes. 2) L’interface sombre et propre : terminal, fiche GitHub, liste d’agents, checklist. Toujours une seule idée par image, beaucoup de vide.",G('C4',fav=True))
add('C4b.dc.html','C4 — Plein écran : gardés et refusés','C4 · 13 autres gardés + 8 refusés (sur 15)','Plein écran — le reste',"Gardés sans être favoris : le texte seul en police éditoriale, les frises d’étapes, les chiffres géants, les écrans de téléphone. Refusés (cadre rouge) : les affiches chargées, les captures d’écran entières, les grilles d’avatars, les gros titres plaqués sur une capture.",G('C4',fav=False)+G('C4',True))
REF=G('C2',True)+G('C1',True)
cover_body=header('Planche C · types de scène · 2026-11-06','Types de scène — moodboard',"Ton tri des anciennes inspirations : 84 gardés (37 favoris), 22 refusés. Une planche par type de scène, puis deux pour le plein écran.")+f'''
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px">
<section style="background: {GRAPH}; border: 2px solid {ACIER}; border-radius: 6px; padding: 28px; display: flex; flex-direction: column; gap: 12px">
<h2 style="margin: 0; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 15px; letter-spacing: 0.08em; text-transform: uppercase; color: {BRAISE}">Ce qui revient</h2>
<p style="margin: 0; font-size: 19px; line-height: 1.55; font-weight: 500">C1 : réglé par la planche A.<br>C2 : un seul petit élément d’interface près de toi, qui ressemble à un vrai logiciel.<br>C3 : bande claire en haut (≈ 40 %) avec un seul objet, toi en bas, coupe nette.<br>C4 : un seul objet au centre et beaucoup de vide, sur papier clair ou sur interface sombre propre.</p>
</section>
<section style="background: {GRAPH}; border: 2px solid {ACIER}; border-radius: 6px; padding: 28px; display: flex; flex-direction: column; gap: 12px">
<h2 style="margin: 0; font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 15px; letter-spacing: 0.08em; text-transform: uppercase; color: {BRUME}">La question à trancher</h2>
<p style="margin: 0; font-size: 19px; line-height: 1.55; font-weight: 500">Tes favoris en écran partagé et en plein écran sont surtout sur <b>papier clair</b> (blanc cassé), alors que ton design system est sur <b>noir</b> (#121212). Trois options : 1) papier clair pour les plans graphiques, noir ailleurs ; 2) tout en noir, en reprenant seulement la composition ; 3) les deux, papier pour expliquer, noir pour les interfaces.</p>
</section>
</div>'''
page('Main.dc.html','Types de scène — moodboard',W,860,cover_body); boards['Main.dc.html']=(W,860,'Couverture')
order=['Main.dc.html','C1.dc.html','C2.dc.html','C3.dc.html','C4a.dc.html','C4b.dc.html']
xs=[0,W+80]; y=[0,0]; pos={}
for n in order:
    c=0 if y[0]<=y[1] else 1
    w,h,t=boards[n]; pos[n]=dict(x=xs[c],y=y[c],w=w,h=h,title=t); y[c]+=h+120
now=datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')
json.dump({"v":3,"createdOnFiles":{"v":1,"at":now},"title":"Moodboard — Planche C · Types de scène","launch":{"view":"canvas"},"pages":[],"boards":pos,"order":order,"notes":{},"designSystems":[]},open(f'{R}/root/project/canvas.json','w'),ensure_ascii=False,indent=1)
for n in order: print(n,pos[n])
