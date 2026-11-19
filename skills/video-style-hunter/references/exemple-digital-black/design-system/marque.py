# ---------- Marque : logo Digital Black + bouton S'abonner (exec dans gen3.py après planche_suite.py) ----------
AVATAR='/_blob/6639195c6e2cec95195711876ce30bf8'
tokens['color']['tokens']+=[
 T("braise-logo","#ff4d00","Le carré du logo Digital Black : l’orange d’origine de la marque, gardé tel quel (comme les cases orange des fonds). Seulement dans le logo.")]
tokens['type']['families']['display']='"Big Shoulders Display", Anton, Impact, sans-serif'
tokens['type']['groups'].append({"name":"Logo","family":"display","styles":[
 {"name":"logo-916","fontSize":"52px","lineHeight":1,"fontWeight":900,"letterSpacing":"0.01em","sample":"DIGITAL BLACK","usage":"Le logo, tel qu’il est dans les fonds de la marque. MAJUSCULES. Seulement pour le logo."},
 {"name":"logo-carte","fontSize":"40px","lineHeight":1,"fontWeight":900,"letterSpacing":"0.01em","sample":"DIGITAL BLACK","usage":"Le nom de la chaîne dans le bouton S’abonner."}]})
tokens['spacing']['tokens']+=[T("logo-carre","16px","Côté du carré du logo.")]
tokens['duration']['tokens']+=[T("dur-clic","120ms","Le bouton S’abonner s’enfonce sous le clic.")]
w('tokens.json',json.dumps(tokens,ensure_ascii=False,indent=1))

css=css.replace('family=Doto:wght@900','family=Big+Shoulders+Display:wght@900&family=Doto:wght@900',1)
css+='''
/* ===== Marque · logo Digital Black ===== */
.ms-logo{position:absolute;display:flex;align-items:center;gap:var(--logo-carre);font-family:var(--font-display);font-weight:900;font-size:52px;line-height:1;letter-spacing:0.01em;text-transform:uppercase;color:var(--os);white-space:nowrap}
.ms-logo::after{content:"";display:block;width:var(--logo-carre);height:var(--logo-carre);background:var(--braise-logo)}
.ms-clair .ms-logo,.ms-logo--encre{color:var(--noir-digital)}
.ms-logo.ms-pose{animation:ms-apparition var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}
/* ===== Marque · bouton S’abonner (proposition) ===== */
.ms-abo{position:absolute;display:flex;align-items:center;gap:24px;padding:20px 20px 20px 20px;box-sizing:border-box;border-radius:var(--radius-md);background:var(--fonte);border:var(--trait-objet) solid var(--acier);box-shadow:0 0 36px rgba(10,10,10,0.6);animation:ms-entree-objet var(--dur-objet) var(--ease-out) both;animation-delay:var(--t,0ms)}
.ms-abo.ms-sortie{animation:ms-entree-objet var(--dur-objet) var(--ease-out) both,ms-sortie var(--dur-sortie) var(--ease-in) forwards;animation-delay:var(--t,0ms),var(--sortie)}
.ms-abo-avatar{width:112px;height:112px;border-radius:50%;object-fit:cover;flex:none}
.ms-abo-texte{display:flex;flex-direction:column;gap:10px;flex:1}
.ms-abo-nom{font-family:var(--font-display);font-weight:900;font-size:40px;line-height:1;letter-spacing:0.01em;text-transform:uppercase;color:var(--os);display:flex;align-items:center;gap:12px}
.ms-abo-nom::after{content:"";display:block;width:12px;height:12px;background:var(--braise-logo)}
.ms-abo-sous{font-family:var(--font-mono);font-weight:600;font-size:22px;letter-spacing:0.08em;color:var(--brume)}
.ms-abo-bouton{position:relative;flex:none;height:84px;padding:0 32px;border-radius:var(--radius-md);display:flex;align-items:center;justify-content:center;font-family:var(--font-mono);font-weight:600;font-size:28px;letter-spacing:0.08em;text-transform:uppercase;animation:ms-clic-bouton var(--dur-clic) linear both;animation-delay:var(--clic,1200ms)}
.ms-abo-bouton span{position:absolute;inset:0;border-radius:inherit;display:flex;align-items:center;justify-content:center;gap:12px}
.ms-abo-bouton .avant{background:var(--braise);color:var(--abysse);animation:ms-deselection 1ms linear both;animation-delay:calc(var(--clic,1200ms) + var(--dur-clic))}
.ms-abo-bouton .apres{background:var(--acier);color:var(--os);animation:ms-apparition 1ms linear both;animation-delay:calc(var(--clic,1200ms) + var(--dur-clic))}
.ms-abo-bouton .gabarit{position:static;visibility:hidden}
.ms-abo-curseur{position:absolute;width:44px;height:56px;animation:ms-abo-curseur var(--dur-lg) var(--ease-in-out) both;animation-delay:calc(var(--clic,1200ms) - 700ms)}
.ms-abo-curseur svg{display:block;transform-origin:0 0;animation:ms-clic-curseur 600ms linear both;animation-delay:calc(var(--clic,1200ms) - 100ms)}
.ms-abo--fixe,.ms-abo--fixe *{animation:none!important}
.ms-abo--fixe .ms-abo-curseur{display:none}
.ms-abo--avant .apres{display:none}
.ms-abo--apres .avant{display:none}
@keyframes ms-clic-bouton{0%{transform:scale(1)}50%{transform:scale(0.94)}100%{transform:scale(1)}}
@keyframes ms-abo-curseur{from{opacity:0;transform:translate(var(--cx,160px),var(--cy,140px))}20%{opacity:1}to{opacity:1;transform:translate(0,0)}}
@keyframes ms-clic-curseur{0%{transform:scale(1)}20%{transform:scale(0.85)}40%{transform:scale(0.85)}60%{transform:scale(1)}100%{opacity:0;transform:scale(1)}}
'''
w('components/bundle.css',css)

CURSEUR='<svg aria-hidden="true" width="44" height="56" viewBox="0 0 22 28"><path d="M2 2 L2 22 L7.5 17 L11 25 L14.5 23.5 L11 16 L18 16 Z" fill="#efefef" stroke="#0a0a0a" stroke-width="1.6" stroke-linejoin="round"></path></svg>'
CLOCHE='<svg aria-hidden="true" width="26" height="26" viewBox="0 0 24 24"><path d="M5 12l5 5 9-10" fill="none" stroke="currentColor" stroke-width="3"></path></svg>'
def abo(x,y,w_,t=200,clic=1200,sortie=3200):
    bouton=f'<div class="ms-abo-bouton" style="--clic:{clic}ms"><span class="gabarit">S’ABONNER</span><span class="avant">S’ABONNER</span><span class="apres">{CLOCHE}ABONNÉ</span></div>'
    cur=f'<div class="ms-abo-curseur" style="right:60px;bottom:-10px;--clic:{clic}ms">{CURSEUR}</div>'
    return f'<div class="ms-abo ms-sortie" style="left:{x}px;top:{y}px;width:{w_}px;--t:{t}ms;--sortie:{sortie}ms"><img class="ms-abo-avatar" src="{AVATAR}" alt="Photo de profil Digital Black"><div class="ms-abo-texte"><div class="ms-abo-nom">Digital Black</div><div class="ms-abo-sous">VENTE · AUTOMATISATION · IA</div></div>{bouton}{cur}</div>'
def logo(x,y,t=0,clair=False,fs=None):
    s=f';font-size:{fs}px' if fs else ''
    return f'<div class="ms-logo{" ms-logo--encre" if clair else ""} ms-pose" style="left:{x}px;top:{y}px;--t:{t}ms{s}">Digital Black</div>'

# ---------- Logo ----------
l1=fond('916','ambiance',False)+logo(64,1360)
l2=fond('916','ambiance',True)+logo(64,1360,clair=True)
l3=fond('169','ambiance',False)+logo(64,960)
l4=fond('169','grappes',False)+logo(0,0,fs=120).replace('left:0px;top:0px','left:0;right:0;top:470px;justify-content:center')
prev=card('Marque',1040,1300,'Le logo Digital Black, tel qu’il est dans les fonds de la marque · noir, blanc, 16:9, carton de fin',
 lab('9:16 · reels')+rang(ap916(l1,'Sur fond noir (bas gauche, comme les fonds)'),ap916(l2,'Sur fond blanc'))+lab('16:9 · YouTube')+rang(ap169(l3,'16:9 · bas gauche'),ap169(l4,'16:9 · carton (plus grand, centré)')))
w('components/Logo/preview.html',prev)
w('components/Logo/README.md','''# Logo — Digital Black

Le logo de la chaîne : le mot **DIGITAL BLACK** en Big Shoulders Display 900, en majuscules, couleur `os`, suivi d’un **carré plein** de 16 px (`logo-carre`) en `braise-logo` (#ff4d00). C’est exactement le logo des fonds de la marque. Il n’existe pas en image : c’est du texte, on ne le redessine pas.

**Ce que tu fournis :** le fond (noir ou blanc), la place, le format.

| Élément | Classes | Règle |
|---|---|---|
| Logo | `.ms-logo` (le carré est ajouté tout seul) | `logo-916` : 52 px, approche 0,01 em. `os` sur fond noir ; `.ms-logo--encre` (ou dans `.ms-clair`) : `noir-digital` sur fond blanc. Le carré reste toujours `braise-logo`. |
| Taille | `font-size` sur `.ms-logo` | 52 px en signature ; plus grand seulement sur un carton plein écran (titre de partie, fin). |

## Où
- En signature : en bas à gauche (x 64), comme dans les fonds ; jamais sur ton visage, jamais dans les zones d’interface des Shorts.
- Dans le bouton **Abonnement**.
- La police Big Shoulders sert **seulement** au logo. Les textes de la vidéo restent en Inter, Doto et JetBrains Mono.

## À ne pas faire
Changer la couleur du carré, le mettre en braise #ff7033, écrire le logo en Doto ou en minuscules, ajouter une ombre colorée, un contour, ou un pictogramme inventé.
''')

# ---------- Abonnement ----------
q,_=mots('abonne-toi pour la suite',200)
a1=plan_img('916')+abo(60,1180,960)+f'<div class="ms-bloc ms-bloc--916" style="--bas:1110px;--sortie:3200ms"><div class="ms-amorce">{q}</div></div>'
a2=fond('916','grappes',False)+logo(0,0,fs=96).replace('left:0px;top:0px','left:0;right:0;top:640px;justify-content:center')+abo(60,880,960,600,1600)
a3=plan_img('169')+abo(64,830,880,200,1200)
a4=fond('169','grappes',False)+logo(0,0,fs=120).replace('left:0px;top:0px','left:0;right:0;top:300px;justify-content:center')+abo(520,520,880,600,1600)
def abo_fixe(etat):
    h=abo(0,0,960).replace('class="ms-abo ms-sortie"',f'class="ms-abo ms-abo--fixe ms-abo--{etat}"')
    return f'<figure class="ap" style="margin:0"><div class="cadre" style="width:614px;height:110px;background:var(--noir-digital)"><div style="position:relative;width:960px;height:152px;transform:scale(0.64);transform-origin:0 0">{h}</div></div><figcaption class="leg">{"Avant le clic : S’ABONNER" if etat=="avant" else "Après le clic : ABONNÉ"}</figcaption></figure>'
prev=card('Marque',1260,1300,'Bouton S’abonner (proposition) · en grand, avant et après le clic · puis animé en 9:16 et 16:9, sur ta vidéo ou en fin de vidéo',
 lab('Le bouton en grand')+rang(abo_fixe('avant'),abo_fixe('apres'))+lab('9:16 · reels')+rang(ap916(a1,'Sur ta vidéo, sous le menton'),ap916(a2,'Fin de vidéo, sous le logo'))+lab('16:9 · YouTube')+rang(ap169(a3,'16:9 · sur ta vidéo, bas gauche'),ap169(a4,'16:9 · fin de vidéo')))
w('components/Abonnement/preview.html',prev)
w('components/Abonnement/README.md','''# Abonnement — le bouton S’abonner (proposition à valider)

Une carte qui reprend l’en-tête de ta chaîne : ta photo de profil, le nom **DIGITAL BLACK** (logo) et le bouton. Un curseur clique : **S’ABONNER** (aplat `braise`, texte `abysse`) devient **ABONNÉ** (aplat `acier`, texte `os`, coche). Aucun fichier de bouton n’existait : il est construit avec les jetons du système. À valider par Wanzt.

**Ce que tu fournis :** le moment (la phrase « abonne-toi », ou la fin), la place, le format.

| Élément | Classes | Règle |
|---|---|---|
| Carte | `.ms-abo` (+ `.ms-sortie`, `--t`, `--sortie`) | fond `fonte`, trait `acier`, `radius-md`, halo sombre autour pour se détacher de la vidéo. 960 px de large en 9:16, 880 px en 16:9. |
| Photo | `img.ms-abo-avatar` | ta photo de profil YouTube (asset **Marque** `photo-profil-yt.png`), ronde, 112 px. |
| Nom | `.ms-abo-nom` + `.ms-abo-sous` | le logo en `logo-carte` (40 px) avec son carré `braise-logo` ; la ligne de la chaîne en mono `brume` (VENTE · AUTOMATISATION · IA, comme sur ta bannière). |
| Bouton | `.ms-abo-bouton` (`--clic` : l’instant du clic) > `.gabarit`, `.avant`, `.apres` | mono 600, 28 px, majuscules. Jamais de texte blanc sur la braise : texte `abysse`. |
| Curseur | `.ms-abo-curseur` | arrive sur le bouton (`dur-lg`, `ease-in-out`), clique, s’efface. |
| État fixe | `.ms-abo--fixe` + `.ms-abo--avant` ou `.ms-abo--apres` | le bouton sans animation, dans l’un des deux états (miniature, écran de fin figé). |

## Placement
- Sur ta vidéo : en 9:16 sous le menton, à la place du bloc de sous-titres (la phrase « abonne-toi… » passe juste au-dessus) ; en 16:9 en bas à gauche. Jamais sur le visage.
- En fin de vidéo : sur un **Fond** (grappes), sous le logo en grand.
- Une seule fois par vidéo, ou deux au plus (milieu + fin).

## Mouvement
La carte monte (`montee-objet` + fondu, `dur-objet`) ; 500 ms plus tard le curseur arrive ; au clic le bouton s’enfonce (échelle 0,94, `dur-clic`) et passe à ABONNÉ ; la carte sort d’un coup (`dur-sortie`) avec le bloc.
''')
DETOURS["photo-profil-yt.png"]={"name":"photo-profil-yt.png","blob":AVATAR[7:],"size":537734,"type":"image/png"}
