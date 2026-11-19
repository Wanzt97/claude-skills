# Génère la planche « Animation caption et son » de l'atelier Digital Black.
import json, os, html

ICI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ICI, "project")
os.makedirs(OUT, exist_ok=True)

BLOBS = {
 "1-cash-register-success": "67c9df178384d18318a46ab8841383c8",
 "1-censor-beep": "7099cef9803385d357651cd3b324b36d",
 "1-clean-ding": "dd6c59d59f6ae33d47564fa8127475b7",
 "1-keyboard-typing-loop": "b9e0b1af7f49405d20c15b521bd72b07",
 "1-mouse-click": "9a9d95f64ed650270eb4a166fe708215",
 "1-new-notification-ping": "e7a9452ce84906a0d27cca90c38c0dc1",
 "1-phone-notification-ping": "f74b356d56cb44f6e69e1954ca56f484",
 "1-sent-message-ping": "d17af5513a36cc843789c30951016a85",
 "1-slow-dell-keyboard-typing": "c6d5bc3b9350d40a25de09f1832bde79",
 "1-synthetic-bubble-pop": "122466791fb7ed82e48bd0b78998bef7",
 "1-tiny-bubble-pop": "fefd896975e90da7a69b1cd4982d1830",
 "1-ui-pop-up-alert": "721cd484017dd28faaf9e528ed8496ee",
 "1-video-call-ringtone": "d5554ad5070530bca49f20d25ecc8920",
 "2-airy-short-whoosh": "9aaa7c7724d76f40b209c1570b4667d6",
 "2-deep-short-whoosh": "c41174cfb433c4b585fd75ae679905ba",
 "2-fast-suspense-riser": "cf7d2d33aaf72657f471765dfd7c4325",
 "2-long-suspense-riser": "6ddbaaedfd361406575ce448ffa2493d",
 "2-record-scratch-rewind": "e4cd3b6d9969304dd0b9e0cfe18dda1f",
 "2-record-scratch-stop": "eb8a91a15a20612b56d634f689fd723a",
 "2-sharp-bass-riser": "ea2958242e108c29a4c9649982a15f55",
 "2-short-drum-roll-sting": "81e781a1d95b9a0aa4c32b9b63ef4367",
 "2-simple-whoosh": "2b1e5ec580b849d6bdc629dd6d526d64",
 "2-taiko-hit": "afc05e217c847ec3dfc967de4dcd7fff",
 "3-camera-shutter": "68187af1d8f396998dd6c2ff7062e97e",
 "3-gear-single-click": "e4771145b08806eeb63e1f9bd252a357",
 "3-gear-turn-click": "57a954ae2e84b93c41a0e0bb3a5722c8",
 "3-glitchy-tv-signal": "6c0c858671b65f6c816dcd2562baa7fc",
 "3-light-clock-tick": "b6a075828d7b66dbf13c9753f83c2d30",
 "3-mechanical-clicking-loop": "1fc9470f241f0c88fc2ef3e7bc2ac122",
 "3-short-shutter-click": "2751f3fcac4d6f6e08e32e14d0f41471",
 "3-tv-switch-off-noise": "c6a390a2ec1ae0e935c88aa9e36dceb1",
 "3-vintage-camera-shutter": "c359a8f045a7122ea2166359fa9c5562",
 "4-anime-wow-reaction": "951b64eb3a4f5333cd018853ec958478",
 "4-awkward-crow-flyby": "4b841f37da698d964863ade9587e7957",
 "4-dramatic-thunder-roll": "57b1e66f74e01af35c0724125cad73fa",
 "4-sitcom-laugh-track": "d985cb60452f0ca43026dbe2def693c6",
 "4-vine-boom-impact": "01a478a9f75fbf003eb3ea3fdfce9e42",
}
NOMS = {
 "1-ui-pop-up-alert": "UI Pop-up Alert",
 "1-tv-switch-off-noise": "TV Switch Off Noise",
}
DUR = {}
for ligne in open(os.path.join(ICI, "durees.txt")):
    k, d = ligne.split()
    DUR[k] = round(float(d), 2)

def nom(slug):
    if slug in NOMS:
        return NOMS[slug]
    mots = slug.split("-", 1)[1].split("-")
    special = {"ui": "UI", "tv": "TV"}
    return " ".join(special.get(m, m.capitalize()) for m in mots)

FAMILLES = {"1": "UI & retours", "2": "Transitions & emphase", "3": "Appareils & textures", "4": "Réactions"}
GARDES = ["keyboard-typing-loop", "mouse-click", "slow-dell-keyboard-typing", "camera-shutter", "gear-single-click", "gear-turn-click",
          "glitchy-tv-signal", "light-clock-tick", "mechanical-clicking-loop", "short-shutter-click", "vintage-camera-shutter"]
SONS = {k[2:]: {"n": nom(k), "f": k[0], "u": "/_blob/" + v, "d": DUR[k]} for k, v in BLOBS.items() if k[2:] in GARDES}
TOUS = [k[2:] for k in sorted(BLOBS) if k[2:] in GARDES]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" '
         'href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@800;900'
         '&amp;family=Inter:wght@500;700;800&amp;family=JetBrains+Mono:wght@600;700&amp;family=Space+Grotesk:wght@700'
         '&amp;family=IBM+Plex+Mono:wght@600&amp;family=Geist:wght@800&amp;family=Martian+Mono:wght@600'
         '&amp;family=Unbounded:wght@900&amp;family=Space+Mono:ital,wght@1,700&amp;family=Sixtyfour&amp;family=Rubik+Glitch&amp;family=Major+Mono+Display&amp;family=Google+Sans+Flex:wght@800&amp;display=swap">')

KEYFRAMES = """
@font-face{font-family:'Redaction 50';src:url(/_blob/113612acc014ae1a0af417b8f8c1c679) format('woff2');font-weight:400;font-style:italic;font-display:block}
@keyframes asFlouIn{from{opacity:0;filter:blur(12px);transform:translateY(10px)}to{opacity:1;filter:blur(0);transform:none}}
@keyframes asFlouOut{from{opacity:1;filter:blur(0)}to{opacity:0;filter:blur(12px)}}
@keyframes asPunch{0%{opacity:0;transform:scale(1.7)}55%{opacity:1;transform:scale(0.93)}78%{transform:scale(1.03)}100%{opacity:1;transform:scale(1)}}
@keyframes asTremble{0%,100%{transform:none}15%{transform:translate(-10px,6px)}35%{transform:translate(9px,-6px)}55%{transform:translate(-6px,3px)}75%{transform:translate(3px,-2px)}}
@keyframes asCadre{from{clip-path:inset(0 100% 100% 0)}to{clip-path:inset(0 0 0 0)}}
@keyframes asPoignee{from{opacity:0;transform:scale(0)}to{opacity:1;transform:scale(1)}}
@keyframes asCurseur{0%{opacity:0;transform:translate(220px,180px)}25%{opacity:1}100%{opacity:1;transform:translate(0,0)}}
@keyframes asClic{0%,100%{transform:scale(1)}50%{transform:scale(0.8)}}
@keyframes asRemplit{from{background:rgba(255,112,51,0);color:#EFEFEF}to{background:#FF7033;color:#0A0A0A}}
@keyframes asLettre{from{max-width:0;opacity:0}to{max-width:1.4em;opacity:1}}
@keyframes asCaret{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes asMonte{from{transform:translateY(115%);filter:blur(8px)}to{transform:none;filter:blur(0)}}
@keyframes asTombe{0%{opacity:0;transform:translateY(-1100px);filter:blur(14px)}70%{opacity:1;transform:translateY(24px);filter:blur(0)}100%{opacity:1;transform:none}}
@keyframes asSurligne{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes asNoircit{from{color:#EFEFEF;text-shadow:0 0 36px rgba(10,10,10,0.8),0 2px 6px rgba(10,10,10,0.6)}to{color:#0A0A0A;text-shadow:none}}
"""

HALO = "text-shadow: 0 0 36px rgba(10,10,10,0.8), 0 2px 6px rgba(10,10,10,0.6)"
AMORCE = "font-family: {{pf}}; font-weight: {{pw}}; font-size: {{pt}}px; line-height: 1.05; letter-spacing: {{pls}}; text-transform: {{pc}}; color: #EFEFEF; " + HALO
MOTCLE = "font-family: {{kf}}; font-weight: {{kw}}; font-style: {{ks}}; font-size: {{k200}}px; line-height: 0.9; letter-spacing: {{kls}}; color: #FF7033; " + HALO + "; white-space: nowrap"
EASE = "cubic-bezier(0.16, 1, 0.3, 1)"

def anim(nomk, dur_ms, t, ease=EASE, extra=""):
    return f"animation: {nomk} {dur_ms}ms {ease} {int(round(t*1000))}ms both{extra}"

def bloc_bas(contenu, bottom=380):
    return (f'<div style="position: absolute; left: 60px; right: 60px; bottom: {bottom}px; display: flex; '
            f'flex-direction: column; align-items: center; text-align: center">{contenu}</div>')

FOND = "/_blob/83ff0c0731a6cc1983b7375106d54c42"

def scene(contenu, tremble=None):
    """Aperçu 9:16 : la scène 1080×1920 réduite à 405×720."""
    trem = f' animation: asTremble 260ms linear {int(tremble*1000)}ms both;' if tremble is not None else ""
    return (
        '<div style="position: relative; width: 405px; height: 720px; overflow: hidden; border-radius: 8px; '
        'border: 2px solid #3A3A3A; box-sizing: content-box; background: #1A1A1A">'
        '<div style="position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; transform: scale(0.375); transform-origin: 0 0">'
        f'<div style="position: absolute; inset: 0;{trem}">'
        f'<img src="{FOND}" alt="Image de ton rush, en plan face caméra" style="position: absolute; inset: 0; width: 1080px; height: 1920px; object-fit: cover; display: block">'
        '<sc-if value="{{run}}" hint-placeholder-val="{{ true }}">' + contenu + '</sc-if>'
        '</div></div></div>'
    )

# ---------------------------------------------------------------- les animations

def a1():
    mots = ["le", "montage", "prend"]
    am = "".join(f'<span style="display: inline-block; {anim("asFlouIn", 350, 0.10 + i*0.18)}">{m}</span>' for i, m in enumerate(mots))
    c = (f'<div style="display: flex; flex-direction: column; align-items: center; {anim("asFlouOut", 300, 2.3, "ease-in")}">'
         f'<div style="display: flex; gap: 18px; {AMORCE}">{am}</div>'
         f'<div style="{MOTCLE}; {anim("asPunch", 420, 0.75)}">1&#160;Heure</div></div>')
    return dict(
        fichier="AS-A1-MotParMot.dc.html", titre="A1 — Mot par mot",
        sous="Le bloc SousTitreDuo : l’amorce arrive mot par mot, puis le mot clé en braise, une capitale puis des minuscules. Le bloc sort en flou.",
        scene=scene(bloc_bas(c)), duree=2.9,
        events=[
            dict(id="mot", label="Chaque mot de l’amorce", quand="3 fois · 0,10 s, 0,28 s, 0,46 s", times=[0.10, 0.28, 0.46],
                 d="short-shutter-click", v=30, c=["gear-single-click", "mouse-click", "short-shutter-click", "tiny-bubble-pop", "sent-message-ping"]),
            dict(id="cle", label="Le mot clé arrive", quand="0,75 s", times=[0.75],
                 d="airy-short-whoosh", v=45, c=["airy-short-whoosh", "camera-shutter", "gear-turn-click", "mouse-click", "short-drum-roll-sting"]),
            dict(id="sortie", label="Le bloc sort", quand="2,30 s", times=[2.3],
                 d="", v=35, c=["airy-short-whoosh", "simple-whoosh", "tv-switch-off-noise", "deep-short-whoosh"]),
        ])

def a2():
    c = (f'<div style="display: flex; flex-direction: column; align-items: center">'
         f'<div style="{AMORCE}; {anim("asFlouIn", 350, 0.55)}">tes vues ont</div>'
         f'<div style="{MOTCLE}; {anim("asPunch", 380, 1.0)}">Doublé</div></div>')
    return dict(
        fichier="AS-A2-MotQuiClaque.dc.html", titre="A2 — Le mot qui claque",
        sous="Le mot clé tombe d’un coup, trop grand puis à sa taille, et l’image tremble. Une montée peut le préparer.",
        scene=scene(bloc_bas(c), tremble=1.06), duree=2.4,
        events=[
            dict(id="montee", label="Montée avant le mot", quand="de 0,06 s à 1,00 s", times=[0.06], span=0.94,
                 d="", v=40, c=["sharp-bass-riser", "fast-suspense-riser", "long-suspense-riser", "record-scratch-rewind"]),
            dict(id="amorce", label="L’amorce arrive", quand="0,55 s", times=[0.55],
                 d="", v=30, c=["short-shutter-click", "gear-single-click", "mouse-click", "airy-short-whoosh"]),
            dict(id="impact", label="Le mot tombe", quand="1,00 s", times=[1.0],
                 d="camera-shutter", v=55, c=["camera-shutter", "taiko-hit", "vine-boom-impact", "short-drum-roll-sting", "record-scratch-stop", "mouse-click"]),
        ])

def a3():
    poignees = "".join(
        f'<span style="position: absolute; {pos}; width: 22px; height: 22px; background: #EFEFEF; border: 3px solid #FF7033; box-sizing: border-box; {anim("asPoignee", 160, 0.85)}"></span>'
        for pos in ["left: -11px; top: -11px", "right: -11px; top: -11px", "left: -11px; bottom: -11px", "right: -11px; bottom: -11px"])
    curseur = ('<svg aria-hidden="true" width="70" height="86" viewBox="0 0 14 17" style="position: absolute; right: -60px; bottom: -80px; '
               f'{anim("asCurseur", 420, 0.95)}"><g style="transform-origin: 2px 2px; {anim("asClic", 160, 1.4, "ease-out")}">'
               '<path d="M1 1 L1 14 L4.5 10.8 L7 16 L9.4 15 L6.9 9.9 L11.6 9.9 Z" fill="#EFEFEF" stroke="#0A0A0A" stroke-width="1"></path></g></svg>')
    c = (f'<div style="display: flex; flex-direction: column; align-items: center; gap: 10px">'
         f'<div style="{AMORCE}; {anim("asFlouIn", 350, 0.1)}">tout commence au</div>'
         f'<div style="position: relative; {anim("asFlouIn", 350, 0.2)}">'
         f'<span style="display: inline-block; padding: 0 22px; font-family: {{{{kf}}}}; font-weight: {{{{kw}}}}; font-style: {{{{ks}}}}; font-size: {{{{k170}}}}px; line-height: 1; letter-spacing: {{{{kls}}}}; color: #EFEFEF; {HALO}; {anim("asRemplit", 120, 1.42, "linear")}">Montage</span>'
         f'<span style="position: absolute; inset: -6px; border: 4px solid #FF7033; {anim("asCadre", 300, 0.55)}"></span>'
         f'{poignees}{curseur}</div></div>')
    return dict(
        fichier="AS-A3-SelectionTiree.dc.html", titre="A3 — Sélection tirée",
        sous="Le mot arrive, un cadre de sélection se trace autour, puis le curseur clique et le mot passe en braise.",
        scene=scene(bloc_bas(c, bottom=400)), duree=2.6,
        events=[
            dict(id="mot", label="Le mot arrive", quand="0,10 s", times=[0.1],
                 d="", v=30, c=["short-shutter-click", "gear-single-click", "airy-short-whoosh", "tiny-bubble-pop"]),
            dict(id="cadre", label="Le cadre se trace", quand="0,55 s · 0,30 s de long", times=[0.55], span=0.3,
                 d="gear-turn-click", v=40, c=["gear-turn-click", "mechanical-clicking-loop", "airy-short-whoosh", "record-scratch-rewind"]),
            dict(id="clic", label="Le clic", quand="1,40 s", times=[1.4],
                 d="mouse-click", v=60, c=["mouse-click", "short-shutter-click", "gear-single-click", "camera-shutter", "vintage-camera-shutter"]),
        ])

def a4():
    texte = "j’ai cloné Precut"
    pas, t0 = 0.06, 0.15
    lettres, times = [], []
    for i, ch in enumerate(texte):
        t = t0 + i * pas
        aff = "&#160;" if ch == " " else html.escape(ch)
        if ch != " ":
            times.append(round(t, 3))
        lettres.append(f'<span style="display: inline-block; overflow: hidden; vertical-align: bottom; {anim("asLettre", 10, t, "steps(1, end)")}">{aff}</span>')
    fin = round(t0 + len(texte) * pas, 3)
    caret = f'<span style="display: inline-block; width: 8px; height: 0.9em; margin-left: 6px; background: #FF7033; vertical-align: -0.08em; animation: asCaret 700ms linear infinite"></span>'
    c = (f'<div style="display: flex; align-items: baseline; justify-content: center; {AMORCE}; font-size: 76px; white-space: nowrap">'
         f'{"".join(lettres)}{caret}</div>')
    return dict(
        fichier="AS-A4-MachineAEcrire.dc.html", titre="A4 — Machine à écrire",
        sous="Le texte s’écrit lettre par lettre derrière un curseur braise, comme un texte en cours d’édition.",
        scene=scene(bloc_bas(c, bottom=430)), duree=round(fin + 1.0, 2),
        events=[
            dict(id="lettre", label="Chaque lettre", quand=f"{len(times)} fois · une toutes les 60 ms", times=times,
                 d="gear-single-click", v=30, c=["gear-single-click", "mouse-click", "short-shutter-click", "tiny-bubble-pop"]),
            dict(id="frappe", label="Frappe en continu", quand=f"de {t0:.2f} s à {fin:.2f} s".replace(".", ","), times=[t0], span=round(fin - t0, 2),
                 d="", v=45, c=["keyboard-typing-loop", "slow-dell-keyboard-typing", "mechanical-clicking-loop", "light-clock-tick"]),
            dict(id="fin", label="Fin de la ligne", quand=f"{fin + 0.05:.2f} s".replace(".", ","), times=[round(fin + 0.05, 3)],
                 d="", v=40, c=["sent-message-ping", "mouse-click", "clean-ding", "camera-shutter"]),
        ])

def a5():
    c = (f'<div style="display: flex; flex-direction: column; align-items: center">'
         f'<div style="overflow: hidden; padding: 0 10px"><div style="{AMORCE}; {anim("asMonte", 380, 0.12)}">et la première coûte</div></div>'
         f'<div style="overflow: hidden; padding: 0 10px"><div style="{MOTCLE}; {anim("asMonte", 420, 0.30)}">Cher</div></div></div>')
    return dict(
        fichier="AS-A5-GlisseDuBas.dc.html", titre="A5 — Glisse du bas",
        sous="Chaque ligne monte de derrière un masque, avec un peu de flou de mouvement, puis se pose.",
        scene=scene(bloc_bas(c)), duree=2.2,
        events=[
            dict(id="monte", label="Le bloc monte", quand="0,10 s", times=[0.1],
                 d="airy-short-whoosh", v=40, c=["airy-short-whoosh", "simple-whoosh", "deep-short-whoosh", "record-scratch-rewind"]),
            dict(id="pose", label="Le mot clé se pose", quand="0,62 s", times=[0.62],
                 d="", v=40, c=["mouse-click", "gear-single-click", "short-shutter-click", "camera-shutter", "tiny-bubble-pop"]),
        ])

def a6():
    c = (f'<div style="font-family: {{{{kf}}}}; font-weight: {{{{kw}}}}; font-style: {{{{ks}}}}; font-size: {{{{kt}}}}px; line-height: 0.9; '
         f'letter-spacing: {{{{kls}}}}; white-space: nowrap; color: #EFEFEF; {HALO}; text-align: center; {anim("asTombe", 320, 0.9, "cubic-bezier(0.5, 0, 0.75, 0)")}">'
         f'3 erreurs<br><span style="color: #FF7033">Qui tuent</span></div>')
    haut = f'<div style="position: absolute; left: 60px; right: 60px; top: 150px; display: flex; justify-content: center">{c}</div>'
    return dict(
        fichier="AS-A6-TitreChoc.dc.html", titre="A6 — Titre-choc",
        sous="Le titre de l’accroche tombe d’en haut, au-dessus de ta tête, rebondit et fait trembler l’image.",
        scene=scene(haut, tremble=1.12), duree=2.6,
        events=[
            dict(id="montee", label="Montée avant le titre", quand="de 0,18 s à 1,12 s", times=[0.18], span=0.94,
                 d="sharp-bass-riser", v=45, c=["sharp-bass-riser", "fast-suspense-riser", "long-suspense-riser"]),
            dict(id="chute", label="Le titre tombe", quand="0,90 s", times=[0.9],
                 d="", v=40, c=["deep-short-whoosh", "simple-whoosh", "airy-short-whoosh"]),
            dict(id="impact", label="L’impact", quand="1,12 s", times=[1.12],
                 d="taiko-hit", v=55, c=["taiko-hit", "vine-boom-impact", "camera-shutter", "short-drum-roll-sting", "dramatic-thunder-roll"]),
        ])

def a7():
    c = (f'<div style="display: flex; flex-direction: column; align-items: center; gap: 8px">'
         f'<div style="{AMORCE}; {anim("asFlouIn", 350, 0.05)}">garde le</div>'
         f'<div style="position: relative; padding: 4px 26px; {anim("asFlouIn", 350, 0.15)}">'
         f'<span style="position: absolute; inset: 0; background: #FF7033; transform-origin: 0 50%; {anim("asSurligne", 320, 0.55, "cubic-bezier(0.65, 0, 0.35, 1)")}"></span>'
         f'<span style="position: relative; display: inline-block; font-family: {{{{kf}}}}; font-weight: {{{{kw}}}}; font-style: {{{{ks}}}}; font-size: {{{{k170}}}}px; line-height: 1; letter-spacing: {{{{kls}}}}; {anim("asNoircit", 120, 0.72, "linear")}">Contrôle</span>'
         f'</div></div>')
    return dict(
        fichier="AS-A7-Surligneur.dc.html", titre="A7 — Surligneur braise",
        sous="La phrase arrive, puis une bande braise passe derrière le mot clé, qui devient noir.",
        scene=scene(bloc_bas(c, bottom=400)), duree=2.3,
        events=[
            dict(id="phrase", label="La phrase arrive", quand="0,05 s", times=[0.05],
                 d="", v=30, c=["short-shutter-click", "gear-single-click", "airy-short-whoosh"]),
            dict(id="surligne", label="Le surligneur passe", quand="0,55 s · 0,32 s de long", times=[0.55], span=0.32,
                 d="airy-short-whoosh", v=40, c=["airy-short-whoosh", "record-scratch-rewind", "gear-turn-click", "mechanical-clicking-loop", "censor-beep"]),
        ])

ANIMS = [a1(), a2(), a3(), a4(), a5(), a6(), a7()]

CHOIX = {  # (animation, moment) : (son par défaut, candidats), seulement des sons gardés
 (1, "mot"): ("short-shutter-click", ["gear-single-click", "mouse-click", "short-shutter-click"]),
 (1, "cle"): ("camera-shutter", ["camera-shutter", "vintage-camera-shutter", "gear-turn-click", "mouse-click"]),
 (1, "sortie"): ("", ["glitchy-tv-signal", "gear-turn-click", "short-shutter-click"]),
 (2, "montee"): ("", ["mechanical-clicking-loop", "light-clock-tick", "keyboard-typing-loop"]),
 (2, "amorce"): ("", ["short-shutter-click", "gear-single-click", "mouse-click"]),
 (2, "impact"): ("camera-shutter", ["camera-shutter", "vintage-camera-shutter", "mouse-click", "glitchy-tv-signal"]),
 (3, "mot"): ("", ["short-shutter-click", "gear-single-click", "mouse-click"]),
 (3, "cadre"): ("gear-turn-click", ["gear-turn-click", "mechanical-clicking-loop"]),
 (3, "clic"): ("mouse-click", ["mouse-click", "short-shutter-click", "gear-single-click", "camera-shutter", "vintage-camera-shutter"]),
 (4, "lettre"): ("gear-single-click", ["gear-single-click", "mouse-click", "short-shutter-click"]),
 (4, "frappe"): ("", ["keyboard-typing-loop", "slow-dell-keyboard-typing", "mechanical-clicking-loop", "light-clock-tick"]),
 (4, "fin"): ("", ["mouse-click", "camera-shutter", "short-shutter-click"]),
 (5, "monte"): ("gear-turn-click", ["gear-turn-click", "mechanical-clicking-loop", "glitchy-tv-signal"]),
 (5, "pose"): ("", ["mouse-click", "gear-single-click", "short-shutter-click", "camera-shutter"]),
 (6, "montee"): ("", ["mechanical-clicking-loop", "light-clock-tick", "keyboard-typing-loop"]),
 (6, "chute"): ("", ["glitchy-tv-signal", "gear-turn-click"]),
 (6, "impact"): ("camera-shutter", ["camera-shutter", "vintage-camera-shutter", "glitchy-tv-signal"]),
 (7, "phrase"): ("", ["short-shutter-click", "gear-single-click"]),
 (7, "surligne"): ("gear-turn-click", ["gear-turn-click", "mechanical-clicking-loop", "glitchy-tv-signal"]),
}
for n, a in enumerate(ANIMS, 1):
    for e in a["events"]:
        d, c = CHOIX[(n, e["id"])]
        assert all(x in SONS for x in c) and (d == "" or d in SONS), (n, e["id"])
        e["d"], e["c"] = d, c

# ---------------------------------------------------------------- le moteur son (commun)

MOTEUR = r"""
ac() {
  if (!this._ac) { var AC = window.AudioContext || window.webkitAudioContext; this._ac = new AC(); }
  if (this._ac.state === 'suspended') { this._ac.resume(); }
  return this._ac;
}
buf(id) {
  this._b = this._b || {};
  if (!this._b[id]) {
    var ac = this.ac();
    this._b[id] = fetch(SONS[id].u).then(function (r) { if (!r.ok) { throw new Error('HTTP ' + r.status); } return r.arrayBuffer(); })
      .then(function (a) { return new Promise(function (res, rej) { ac.decodeAudioData(a, res, rej); }); });
  }
  return this._b[id];
}
jouer(id, quand, vol, duree) {
  var self = this, ac = this.ac();
  return this.buf(id).then(function (b) {
    var s = ac.createBufferSource(); s.buffer = b;
    var g = ac.createGain(); g.gain.value = vol;
    s.connect(g); g.connect(ac.destination);
    var t = Math.max(quand, ac.currentTime);
    s.start(t);
    if (duree) { g.gain.setValueAtTime(vol, t + Math.max(0, duree - 0.08)); g.gain.linearRampToValueAtTime(0, t + duree); s.stop(t + duree + 0.02); }
    self._srcs = self._srcs || []; self._srcs.push(s);
  });
}
couper() {
  (this._srcs || []).forEach(function (s) { try { s.stop(); } catch (e) {} });
  this._srcs = [];
  (this._tm || []).forEach(function (t) { clearTimeout(t); });
  this._tm = [];
}
componentWillUnmount() { this.couper(); }
"""

def script_anim(a):
    ev = [dict(id=e["id"], times=e["times"], span=e.get("span"), d=e["d"], v=e["v"], c=e["c"],
               label=e["label"], quand=e["quand"]) for e in a["events"]]
    data = f"var SONS = {json.dumps(SONS, ensure_ascii=False)};\nvar TOUS = {json.dumps(TOUS)};\nvar EVTS = {json.dumps(ev, ensure_ascii=False)};\nvar DUREE = {a['duree']};\n"
    return data + r"""
function pct(v) { return Math.round(v) + ' %'; }
var POLICES = [
  { n: 'Inter 800 · actuelle', f: 'Inter, sans-serif', w: 800, ls: '-0.01em', t: 56, c: 'none' },
  { n: '01 Geist 800', f: "'Geist', sans-serif", w: 800, ls: '-0.02em', t: 56, c: 'none' },
  { n: '02 Space Grotesk 700', f: "'Space Grotesk', sans-serif", w: 700, ls: '-0.01em', t: 58, c: 'none' },
  { n: '03 JetBrains Mono 700', f: "'JetBrains Mono', monospace", w: 700, ls: '-0.02em', t: 50, c: 'none' },
  { n: '04 IBM Plex Mono 600', f: "'IBM Plex Mono', monospace", w: 600, ls: '-0.01em', t: 50, c: 'none' },
  { n: '05 Martian Mono 600', f: "'Martian Mono', monospace", w: 600, ls: '-0.03em', t: 44, c: 'uppercase' }
];
var MOTS = [
  { n: 'Google Sans Flex 800 · ton choix', f: "'Google Sans Flex', sans-serif", w: 800, s: 'normal', ls: '-0.03em', z: 0.85 },
  { n: 'Redaction 50 Italic', f: "'Redaction 50', serif", w: 400, s: 'italic', ls: '-0.01em', z: 1 },
  { n: '01 Unbounded 900', f: "'Unbounded', sans-serif", w: 900, s: 'normal', ls: '-0.03em', z: 0.62 },
  { n: '02 Space Mono 700 Italic', f: "'Space Mono', monospace", w: 700, s: 'italic', ls: '-0.04em', z: 0.8 },
  { n: '03 Sixtyfour', f: "'Sixtyfour', monospace", w: 400, s: 'normal', ls: '-0.04em', z: 0.55 },
  { n: '04 Rubik Glitch', f: "'Rubik Glitch', sans-serif", w: 400, s: 'normal', ls: '-0.01em', z: 0.85 },
  { n: '05 Major Mono Display', f: "'Major Mono Display', monospace", w: 400, s: 'normal', ls: '-0.04em', z: 0.75 }
];
class Component extends DCLogic {
  constructor(props) {
    super(props);
    var picks = {}, vols = {}, tout = {};
    EVTS.forEach(function (e) { picks[e.id] = e.d; vols[e.id] = e.v; tout[e.id] = false; });
    this.state = { run: true, joue: false, picks: picks, vols: vols, tout: tout, err: '', police: 0 };
  }
""" + MOTEUR + r"""
  lancer() {
    var self = this;
    this.couper();
    this.ac();
    var ids = [];
    EVTS.forEach(function (e) { var p = self.state.picks[e.id]; if (p && ids.indexOf(p) < 0) { ids.push(p); } });
    Promise.all(ids.map(function (id) { return self.buf(id); })).then(function () {
      self.setState({ run: false, err: '' });
      self._tm.push(setTimeout(function () {
        var t0 = self.ac().currentTime + 0.03;
        self.setState({ run: true, joue: true });
        EVTS.forEach(function (e) {
          var p = self.state.picks[e.id];
          if (!p) { return; }
          e.times.forEach(function (t) { self.jouer(p, t0 + t, self.state.vols[e.id] / 100, e.span); });
        });
        self._tm.push(setTimeout(function () { self.setState({ joue: false }); }, DUREE * 1000 + 60));
      }, 40));
    }).catch(function (err) { self.setState({ err: 'Le son ne se charge pas : ' + err.message }); });
  }
  choisir(e, id) {
    var picks = Object.assign({}, this.state.picks); picks[e.id] = id;
    this.setState({ picks: picks });
    if (id) { this.couper(); this.jouer(id, this.ac().currentTime + 0.02, this.state.vols[e.id] / 100, e.span).catch(function () {}); }
  }
  renderVals() {
    var self = this, st = this.state;
    var events = EVTS.map(function (e) {
      var cur = st.picks[e.id];
      var liste = st.tout[e.id] ? TOUS.slice() : e.c.slice();
      if (cur && liste.indexOf(cur) < 0) { liste.push(cur); }
      var pills = [''].concat(liste).map(function (id) {
        var on = id === cur;
        return {
          label: id ? SONS[id].n : 'Aucun',
          bg: on ? '#FF7033' : '#1E1E1E', fg: on ? '#0A0A0A' : '#EFEFEF', bd: on ? '#FF7033' : '#3A3A3A',
          pick: function () { self.choisir(e, id); }
        };
      });
      return {
        label: e.label, quand: e.quand, pills: pills, vol: st.vols[e.id], volTxt: pct(st.vols[e.id]),
        toutTxt: st.tout[e.id] ? 'Moins de sons' : 'Tous tes sons (' + TOUS.length + ')',
        onTout: function () { var t = Object.assign({}, st.tout); t[e.id] = !t[e.id]; self.setState({ tout: t }); },
        onVol: function (ev) { var v = Object.assign({}, self.state.vols); v[e.id] = Number(ev.target.value); self.setState({ vols: v }); }
      };
    });
    var choix = EVTS.map(function (e) {
      var p = st.picks[e.id];
      return e.label + ' : ' + (p ? SONS[p].n + ' à ' + pct(st.vols[e.id]) : 'aucun son');
    }).join('  ·  ');
    var P = POLICES[3], M = MOTS[st.police];
    var polices = MOTS.map(function (p, i) {
      var on = i === st.police;
      return { label: p.n, bg: on ? '#FF7033' : '#1E1E1E', fg: on ? '#0A0A0A' : '#EFEFEF', bd: on ? '#FF7033' : '#3A3A3A',
        pick: function () { self.setState({ police: i }); } };
    });
    return {
      pf: P.f, pw: P.w, pt: P.t, pls: P.ls, pc: P.c, polices: polices, policeNom: M.n,
      kf: M.f, kw: M.w, ks: M.s, kls: M.ls, k200: Math.round(200 * M.z), k170: Math.round(170 * M.z), kt: Math.round(180 * M.z),
      run: st.run, events: events, choix: choix + '  ·  Mot clé : ' + M.n, err: st.err, aErr: !!st.err,
      boutonTxt: st.joue ? 'Rejouer' : 'Jouer avec le son',
      onPlay: function () { self.lancer(); }
    };
  }
}
"""

def page_anim(a, n):
    evts = """
<sc-for list="{{events}}" as="ev" hint-placeholder-count="3">
<div style="display: flex; flex-direction: column; gap: 10px; padding: 16px 18px; border: 1px solid #2E2E2E; border-radius: 8px; background: #161616">
<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 12px">
<div style="font-size: 19px; font-weight: 800; color: #EFEFEF">{{ev.label}}</div>
<div style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 12px; letter-spacing: 0.04em; color: #8A8A8A">{{ev.quand}}</div>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 6px">
<sc-for list="{{ev.pills}}" as="p" hint-placeholder-count="5">
<button type="button" onClick="{{p.pick}}" style="padding: 6px 11px; min-height: 32px; border-radius: 999px; border: 1px solid {{p.bd}}; background: {{p.bg}}; color: {{p.fg}}; font-family: Inter, sans-serif; font-weight: 700; font-size: 13px; cursor: pointer">{{p.label}}</button>
</sc-for>
<button type="button" onClick="{{ev.onTout}}" style="padding: 6px 11px; min-height: 32px; border-radius: 999px; border: 1px dashed #5A5A5A; background: transparent; color: #A3A3A3; font-family: Inter, sans-serif; font-weight: 700; font-size: 13px; cursor: pointer">{{ev.toutTxt}}</button>
</div>
<label style="display: flex; align-items: center; gap: 12px; font-size: 13px; font-weight: 700; color: #A3A3A3">Volume
<input type="range" min="0" max="100" step="5" value="{{ev.vol}}" onChange="{{ev.onVol}}" style="flex: 1; accent-color: #FF7033">
<span style="width: 46px; text-align: right; font-family: 'JetBrains Mono', monospace; color: #EFEFEF">{{ev.volTxt}}</span></label>
</div>
</sc-for>"""
    corps = f"""<div style="width: 1240px; height: 1240px; box-sizing: border-box; padding: 48px; background: #121212; color: #EFEFEF; font-family: Inter, sans-serif; display: flex; flex-direction: column; gap: 28px; overflow: hidden">
<div style="display: flex; flex-direction: column; gap: 12px">
<div style="display: flex; align-items: center; gap: 12px"><span style="display: inline-block; width: 14px; height: 14px; background: #FF7033"></span><span style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 15px; letter-spacing: 0.08em; text-transform: uppercase; color: #A3A3A3">Animation caption et son · A{n} · 9:16</span></div>
<h1 style="margin: 0; font-family: 'Big Shoulders Display', sans-serif; font-weight: 900; font-size: 64px; line-height: 0.95; letter-spacing: 0.01em; text-transform: uppercase">{html.escape(a['titre'].split(' — ')[1])}</h1>
<p style="margin: 0; max-width: 1100px; font-size: 19px; line-height: 1.45; font-weight: 500; color: #A3A3A3">{html.escape(a['sous'])}</p>
</div>
<div style="display: flex; gap: 40px; align-items: flex-start">
<div style="display: flex; flex-direction: column; gap: 14px; width: 409px; flex-shrink: 0">
{a['scene']}
<button type="button" onClick="{{{{onPlay}}}}" style="display: flex; align-items: center; justify-content: center; gap: 12px; min-height: 56px; border: 0; border-radius: 8px; background: #FF7033; color: #0A0A0A; font-family: Inter, sans-serif; font-weight: 800; font-size: 18px; cursor: pointer"><svg aria-hidden="true" width="16" height="18" viewBox="0 0 16 18"><path d="M1 1 L15 9 L1 17 Z" fill="#0A0A0A"></path></svg>{{{{boutonTxt}}}}</button>
<sc-if value="{{{{aErr}}}}" hint-placeholder-val="{{{{ false }}}}"><p style="margin: 0; font-size: 14px; color: #FF7033">{{{{err}}}}</p></sc-if>
<p style="margin: 0; font-size: 13px; line-height: 1.4; color: #8A8A8A">Clique un son pour l’écouter seul, puis « Jouer avec le son » pour l’entendre sur l’animation.</p>
</div>
<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 14px">
<div style="display: flex; flex-direction: column; gap: 10px; padding: 16px 18px; border: 1px solid #FF7033; border-radius: 8px; background: #161616">
<div style="display: flex; align-items: baseline; justify-content: space-between; gap: 12px">
<div style="font-size: 19px; font-weight: 800; color: #EFEFEF">Police du mot clé</div>
<div style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 12px; letter-spacing: 0.04em; color: #8A8A8A">amorce : JetBrains Mono 700</div>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 6px">
<sc-for list="{{{{polices}}}}" as="p" hint-placeholder-count="6">
<button type="button" onClick="{{{{p.pick}}}}" style="padding: 6px 11px; min-height: 32px; border-radius: 999px; border: 1px solid {{{{p.bd}}}}; background: {{{{p.bg}}}}; color: {{{{p.fg}}}}; font-family: Inter, sans-serif; font-weight: 700; font-size: 13px; cursor: pointer">{{{{p.label}}}}</button>
</sc-for>
</div>
</div>
{evts}
<div style="padding: 14px 18px; border-radius: 8px; background: #EFEFEF; color: #0A0A0A">
<div style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #5A5A5A">Ton choix</div>
<div style="margin-top: 6px; font-size: 15px; line-height: 1.45; font-weight: 700">{{{{choix}}}}</div>
</div>
</div>
</div>
</div>"""
    return doc(a["titre"], corps, script_anim(a), 1240, 1240)

def doc(titre, corps, script, w, h):
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{html.escape(titre)}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
body{{margin:0}}
{KEYFRAMES}
</style>
</helmet>
{corps}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
{script}
</script>
</body>
</html>
"""

# ---------------------------------------------------------------- la banque

def page_banque():
    data = f"var SONS = {json.dumps(SONS, ensure_ascii=False)};\nvar TOUS = {json.dumps(TOUS)};\nvar FAM = {json.dumps(FAMILLES, ensure_ascii=False)};\n"
    script = data + r"""
var CLE = 'digitalb-sons-gardes';
function lireGardes() { try { var v = window.localStorage.getItem(CLE); return v ? JSON.parse(v) : []; } catch (e) { return []; } }
function ecrireGardes(l) { try { window.localStorage.setItem(CLE, JSON.stringify(l)); } catch (e) {} }
class Component extends DCLogic {
  constructor(props) { super(props); this.state = { cur: '', vol: 70, err: '', gardes: lireGardes(), copie: '' }; }
""" + MOTEUR + r"""
  ecouter(id) {
    var self = this;
    this.couper();
    this.setState({ cur: id, err: '' });
    this.jouer(id, this.ac().currentTime + 0.02, this.state.vol / 100).catch(function (e) { self.setState({ err: 'Le son ne se charge pas : ' + e.message }); });
    this._tm = [setTimeout(function () { self.setState({ cur: '' }); }, Math.min(SONS[id].d, 10) * 1000 + 100)];
  }
  basculer(id) {
    var l = this.state.gardes.slice(), i = l.indexOf(id);
    if (i < 0) { l.push(id); } else { l.splice(i, 1); }
    l.sort(function (a, b) { return TOUS.indexOf(a) - TOUS.indexOf(b); });
    ecrireGardes(l);
    this.setState({ gardes: l, copie: '' });
  }
  texte() {
    var l = this.state.gardes;
    return 'Sons gardés (' + l.length + ') : ' + (l.length ? l.map(function (id) { return SONS[id].n; }).join(', ') : 'aucun');
  }
  copier() {
    var self = this, t = this.texte(), ok = false;
    var MANUEL = 'Pas copié : clique dans le cadre, Cmd+A puis Cmd+C';
    try { if (this._ta) { this._ta.focus(); this._ta.select(); ok = document.execCommand('copy'); } } catch (e) { ok = false; }
    if (ok) { this.setState({ copie: 'Copié' }); return; }
    try {
      navigator.clipboard.writeText(t).then(function () { self.setState({ copie: 'Copié' }); }, function () { self.setState({ copie: MANUEL }); });
    } catch (e) { this.setState({ copie: MANUEL }); }
  }
  renderVals() {
    var self = this, st = this.state;
    var familles = ['1', '2', '3', '4'].filter(function (f) { return TOUS.some(function (id) { return SONS[id].f === f; }); }).map(function (f) {
      return {
        nom: FAM[f],
        sons: TOUS.filter(function (id) { return SONS[id].f === f; }).map(function (id) {
          var on = st.cur === id, g = st.gardes.indexOf(id) >= 0;
          return { n: SONS[id].n, d: SONS[id].d.toFixed(2).replace('.', ',') + ' s',
            bg: on ? '#FF7033' : (g ? '#2A1A12' : '#1E1E1E'), fg: on ? '#0A0A0A' : '#EFEFEF', dfg: on ? '#0A0A0A' : '#8A8A8A',
            bd: g ? '#FF7033' : '#2E2E2E',
            gTxt: g ? 'Gardé' : 'Garder', gBg: g ? '#FF7033' : 'transparent', gFg: g ? '#0A0A0A' : '#A3A3A3', gBd: g ? '#FF7033' : '#5A5A5A',
            gPressed: g ? 'true' : 'false', gLabel: (g ? 'Retirer ' : 'Garder ') + SONS[id].n,
            go: function () { self.ecouter(id); },
            garde: function () { self.basculer(id); } };
        })
      };
    });
    return { familles: familles, vol: st.vol, volTxt: Math.round(st.vol) + ' %', err: st.err, aErr: !!st.err,
      nb: st.gardes.length + ' / ' + TOUS.length, texte: this.texte(), copie: st.copie, aCopie: !!st.copie,
      onCopier: function () { self.copier(); },
      setTa: function (el) { self._ta = el; },
      onVol: function (ev) { self.setState({ vol: Number(ev.target.value) }); } };
  }
}
"""
    corps = """<div style="width: 1240px; height: 1320px; box-sizing: border-box; padding: 44px 48px; background: #121212; color: #EFEFEF; font-family: Inter, sans-serif; display: flex; flex-direction: column; gap: 22px; overflow: hidden">
<div style="display: flex; flex-direction: column; gap: 10px">
<div style="display: flex; align-items: center; gap: 12px"><span style="display: inline-block; width: 14px; height: 14px; background: #FF7033"></span><span style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 15px; letter-spacing: 0.08em; text-transform: uppercase; color: #A3A3A3">Animation caption et son · la banque</span></div>
<h1 style="margin: 0; font-family: 'Big Shoulders Display', sans-serif; font-weight: 900; font-size: 60px; line-height: 0.95; letter-spacing: 0.01em; text-transform: uppercase">Tes sons gardés</h1>
<p style="margin: 0; max-width: 1100px; font-size: 18px; line-height: 1.45; font-weight: 500; color: #A3A3A3">Les 11 sons que tu as gardés dans le pack « ChatCut - Effets sonores » (8 novembre). Ce sont les seuls proposés dans les animations. Clique pour écouter ; « Garder » sert encore si tu veux resserrer. Les sons de plus de 10 s sont coupés à 10 s ici.</p>
<div style="display: flex; align-items: center; gap: 28px; flex-wrap: wrap">
<label style="display: flex; align-items: center; gap: 12px; width: 420px; font-size: 14px; font-weight: 700; color: #A3A3A3">Volume d’écoute
<input type="range" min="0" max="100" step="5" value="{{vol}}" onChange="{{onVol}}" style="flex: 1; accent-color: #FF7033">
<span style="width: 46px; text-align: right; font-family: 'JetBrains Mono', monospace; color: #EFEFEF">{{volTxt}}</span></label>
<div style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 14px; color: #FF7033">Gardés : {{nb}}</div>
</div>
<sc-if value="{{aErr}}" hint-placeholder-val="{{ false }}"><p style="margin: 0; font-size: 14px; color: #FF7033">{{err}}</p></sc-if>
</div>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px 32px">
<sc-for list="{{familles}}" as="fam" hint-placeholder-count="4">
<div style="display: flex; flex-direction: column; gap: 6px">
<div style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 13px; letter-spacing: 0.08em; text-transform: uppercase; color: #FF7033; padding-bottom: 6px; border-bottom: 1px solid #2E2E2E">{{fam.nom}}</div>
<sc-for list="{{fam.sons}}" as="s" hint-placeholder-count="8">
<div style="display: flex; gap: 6px">
<button type="button" onClick="{{s.go}}" style="flex: 1; min-width: 0; display: flex; align-items: center; justify-content: space-between; gap: 8px; min-height: 40px; padding: 6px 10px; border: 1px solid {{s.bd}}; border-radius: 6px; background: {{s.bg}}; color: {{s.fg}}; font-family: Inter, sans-serif; font-weight: 700; font-size: 13px; text-align: left; cursor: pointer"><span>{{s.n}}</span><span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: {{s.dfg}}">{{s.d}}</span></button>
<button type="button" onClick="{{s.garde}}" aria-pressed="{{s.gPressed}}" aria-label="{{s.gLabel}}" style="width: 70px; min-height: 40px; border: 1px solid {{s.gBd}}; border-radius: 6px; background: {{s.gBg}}; color: {{s.gFg}}; font-family: Inter, sans-serif; font-weight: 800; font-size: 12px; cursor: pointer">{{s.gTxt}}</button>
</div>
</sc-for>
</div>
</sc-for>
</div>
<div style="margin-top: auto; display: flex; flex-direction: column; gap: 8px; padding: 14px 18px; border-radius: 8px; background: #EFEFEF; color: #0A0A0A">
<div style="display: flex; align-items: center; justify-content: space-between; gap: 12px">
<div style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #5A5A5A">Ta sélection · copie-la et envoie-la-moi</div>
<div style="display: flex; align-items: center; gap: 10px">
<sc-if value="{{aCopie}}" hint-placeholder-val="{{ false }}"><span style="font-size: 13px; font-weight: 700; color: #5A5A5A">{{copie}}</span></sc-if>
<button type="button" onClick="{{onCopier}}" style="min-height: 36px; padding: 6px 14px; border: 0; border-radius: 6px; background: #0A0A0A; color: #EFEFEF; font-family: Inter, sans-serif; font-weight: 800; font-size: 13px; cursor: pointer">Copier la liste</button>
</div>
</div>
<textarea readonly="readonly" ref="{{setTa}}" value="{{texte}}" aria-label="Liste des sons gardés" rows="3" style="width: 100%; box-sizing: border-box; resize: none; padding: 8px 10px; border: 1px solid #BDBDBD; border-radius: 6px; background: #FFFFFF; color: #0A0A0A; font-family: Inter, sans-serif; font-size: 14px; line-height: 1.45; font-weight: 700"></textarea>
</div>
</div>"""
    return doc("Choisis tes sons", corps, script, 1240, 1320)

# ---------------------------------------------------------------- écriture

fichiers = {"AS-Banque.dc.html": page_banque()}
for i, a in enumerate(ANIMS, 1):
    fichiers[a["fichier"]] = page_anim(a, i)
for f, t in fichiers.items():
    open(os.path.join(OUT, f), "w").write(t)

# plan des planches
pos = []
cols = [0, 1320]
items = [("AS-Banque.dc.html", "Banque — ton pack de sons")] + [(a["fichier"], a["titre"]) for a in ANIMS]
for k, (f, t) in enumerate(items):
    pos.append((f, t, cols[k % 2], (k // 2) * 1440))
json.dump(pos, open(os.path.join(ICI, "positions.json"), "w"), ensure_ascii=False, indent=1)
print("\n".join(f"{f} {len(fichiers[f])} o" for f in fichiers))
