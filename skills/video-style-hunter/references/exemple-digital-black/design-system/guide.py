# ---------- Guide d'utilisation : sections + carte GuideVisuel (exec dans gen3.py après marque.py) ----------
w('01-guide-utilisation.md',open('01-guide-utilisation.md').read())
w('02-guide-son.md',open('02-guide-son.md').read())

def sous(am,mc,t0=0,bas=1450,braise=False,size=200):
    b,_=duo2(am,mc,t0,bas,braise=braise,size=size); return b
SC=0.14
def mini(inner,leg): return ap('916',inner,leg,sc=SC,plan=False)
f1=serre(P916,'50%','45%')+titre_sel('3 erreurs',110,300,860,250,190)
f2=plan_img('916')+sous('et la première coûte','cher',0,braise=True,size=240)
f3=plan_img('916')+sous('erreur','une',0)+etapes(700,1,1490)
s4,_=mots('tu coupes au hasard',700)
f4=plan_img('916','ms-plan--bas')+f'<div class="ms-bande" style="--t:0ms">{fond("916","ambiance",False)}{carte(140,160,800,440,200,"MONTAGE.PRJ")}</div><div class="ms-jointure"></div><div class="ms-bloc ms-bloc--916" style="top:800px;bottom:auto;--sortie:3200ms"><div class="ms-amorce">{s4}</div></div>'
l1,t=phrase('un plan',200,120); l2,t=phrase('prend',t,120); k,_=doto('10 min',t+120,200,True,';margin-top:18px')
f5=fond('916','ambiance',True)+bloc(l1+l2+k,'left:90px;right:90px;top:640px;display:flex;flex-direction:column;gap:12px',True)
l1,t=phrase('appuie sur',1300,96); k,_=doto('Échap',t+120,200)
f6=fond('916','ambiance',False)+touche('Esc',300,520,480,'braise',200)+bloc(l1+k,'left:70px;right:70px;top:1220px;display:flex;flex-direction:column;align-items:center;gap:14px;text-shadow:var(--halo-sombre)')
f7=plan_img('916')+sous('garde le','contrôle',0)
q,_=mots('abonne-toi pour la suite',200)
f8=plan_img('916')+abo(60,1180,960)+f'<div class="ms-bloc ms-bloc--916" style="--bas:1110px;--sortie:3200ms"><div class="ms-amorce">{q}</div></div>'
frise=[(f1,'0 s · Accroche'),(f2,'3 s · Sous-titres'),(f3,'6 s · C2 étape'),(f4,'10 s · C3 bande'),(f5,'15 s · C4 texte'),(f6,'24 s · C4 objet'),(f7,'34 s · Sous-titres'),(f8,'38 s · S’abonner')]
# barre du temps : largeur proportionnelle à la durée de chaque moment
durees=[(3,'Accroche','braise'),(3,'1','os'),(4,'2','os'),(5,'3','os'),(5,'4','os'),(4,'2','os'),(6,'4','os'),(4,'2','os'),(4,'1','os'),(4,'Fin','brume')]
tot=sum(d for d,_,_ in durees)
barre='<div style="display:flex;gap:4px;padding:0 24px 24px;width:1424px;box-sizing:border-box">'+''.join(f'<div style="flex:{d};height:28px;border-radius:3px;background:var(--{c});display:flex;align-items:center;justify-content:center;font-family:var(--font-mono);font-weight:600;font-size:12px;letter-spacing:0.08em;color:var(--abysse)">{l}</div>' for d,l,c in durees)+'</div>'
prev=card('Edit for Digital B',500,1500,'Un reel de 42 s, « 3 erreurs qui tuent ton montage », monté avec le système : un exemple de chaque moment, puis la frise des types de scène (1 sous-titres, 2 pendant que tu parles, 3 écran partagé, 4 plein écran)',
 lab('Le déroulé, image par image')+rang(*[mini(f,l) for f,l in frise])+lab('La frise du temps : quel type de scène, combien de temps')+barre)
w('components/GuideVisuel/preview.html',prev)
w('components/GuideVisuel/README.md','''# GuideVisuel — un reel monté de bout en bout

L’exemple de **Edit for Digital B** (le guide d’utilisation) en images : un reel de 42 s (« 3 erreurs qui tuent ton montage »), avec un moment de chaque sorte, dans l’ordre où ils passent. Ce n’est pas un élément à poser : c’est le modèle de rythme à suivre.

| Moment | Composant |
|---|---|
| 0 s · accroche | **Accroche** V1 |
| 3 s · face caméra | **SousTitreDuo**, mot clé braise |
| 6 s · étape | **SceneC2** V1 (la même petite interface revient à chaque partie) |
| 10 s · écran partagé | **SceneC3**, bande noire + fenêtre du logiciel |
| 15 s · plein écran, une idée | **SceneC4** + **AnimTexte** |
| 24 s · plein écran, un objet | **SceneC4** + **AnimObjet** |
| 34 s · face caméra | **SousTitreDuo** |
| 38 s · fin | **Abonnement**, puis **Logo** |

La frise sous les images donne la durée de chaque type de scène. Le plan complet, ligne par ligne, avec les sons, est dans la section **Edit for Digital B**.
''')
