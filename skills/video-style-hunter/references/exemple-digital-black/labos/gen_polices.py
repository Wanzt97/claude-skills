# Planche « Combinaisons de polices » : amorce Inter 800 + 5 polices tech pour le mot clé, à la place de Redaction.
import os, html

ICI = os.path.dirname(os.path.abspath(__file__))
FOND = "/_blob/83ff0c0731a6cc1983b7375106d54c42"
RED = "/_blob/113612acc014ae1a0af417b8f8c1c679"
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" '
         'href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@900&amp;family=Inter:wght@500;700;800'
         '&amp;family=JetBrains+Mono:wght@600&amp;family=Unbounded:wght@900&amp;family=Space+Mono:ital,wght@1,700'
         '&amp;family=Sixtyfour&amp;family=Rubik+Glitch&amp;family=Major+Mono+Display&amp;family=Google+Sans+Flex:wght@800&amp;display=swap">')
HALO = "text-shadow: 0 0 36px rgba(10,10,10,0.8), 0 2px 6px rgba(10,10,10,0.6)"
AMORCE = f"font-family: Inter, sans-serif; font-weight: 800; font-size: 56px; line-height: 1.05; letter-spacing: -0.01em; color: #EFEFEF; {HALO}"

COMBOS = [
    dict(n="TON CHOIX", nom="JetBrains Mono 700 + Google Sans Flex 800", fam="'Google Sans Flex', sans-serif", w=800, st="normal", ls="-0.03em", z=0.85,
         am=dict(fam="'JetBrains Mono', monospace", w=700, ls="-0.02em", t=50),
         pourquoi="Ta combinaison (8 novembre) : l’amorce se lit comme une ligne de code, le mot clé en grotesque ronde et grasse de Google. C’est elle qui est par défaut sur les 7 animations."),
    dict(n="01", nom="Unbounded 900", fam="'Unbounded', sans-serif", w=900, st="normal", ls="-0.03em", z=0.62,
         pourquoi="Une grotesque large et très grasse, typique des marques tech récentes. Nette et moderne, sans texture."),
    dict(n="02", nom="Space Mono 700 Italic", fam="'Space Mono', monospace", w=700, st="italic", ls="-0.04em", z=0.8,
         pourquoi="Une mono de code en italique. Elle garde l’élan penché de Redaction, avec un ton ordinateur."),
    dict(n="03", nom="Sixtyfour", fam="'Sixtyfour', monospace", w=400, st="normal", ls="-0.04em", z=0.55,
         pourquoi="Une police d’écran rétro avec des lignes de balayage. De la texture, comme Redaction, mais côté machine."),
    dict(n="04", nom="Rubik Glitch", fam="'Rubik Glitch', sans-serif", w=400, st="normal", ls="-0.01em", z=0.85,
         pourquoi="Une grotesque ronde, découpée comme un signal qui saute. L’effet glitch, à garder pour les mots qui claquent."),
    dict(n="05", nom="Major Mono Display", fam="'Major Mono Display', monospace", w=400, st="normal", ls="-0.04em", z=0.75,
         pourquoi="Une mono géométrique et fine, aux formes de schéma technique. La plus calme et la plus graphique des cinq."),
]

def carte(c):
    am = c.get("am", dict(fam="Inter, sans-serif", w=800, ls="-0.01em", t=56))
    amorce = (f"font-family: {am['fam']}; font-weight: {am['w']}; font-size: {am['t']}px; line-height: 1.05; "
              f"letter-spacing: {am['ls']}; color: #EFEFEF; {HALO}")
    bord = "#FF7033" if "am" in c else "#3A3A3A"
    mot = (f"font-family: {c['fam']}; font-weight: {c['w']}; font-style: {c['st']}; font-size: {round(200 * c['z'])}px; "
           f"line-height: 0.9; letter-spacing: {c['ls']}; color: #FF7033; {HALO}; white-space: nowrap")
    return f"""<figure style="margin: 0; width: 324px; display: flex; flex-direction: column; gap: 14px">
<div style="position: relative; width: 324px; height: 576px; overflow: hidden; border-radius: 8px; border: 2px solid {bord}; box-sizing: content-box; background: #1A1A1A">
<div style="position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; transform: scale(0.3); transform-origin: 0 0">
<img src="{FOND}" alt="Image de ton rush, en plan face caméra" style="position: absolute; inset: 0; width: 1080px; height: 1920px; object-fit: cover; display: block">
<div style="position: absolute; left: 60px; right: 60px; bottom: 380px; display: flex; flex-direction: column; align-items: center; text-align: center">
<div style="{amorce}">le montage prend</div>
<div style="{mot}">1&#160;Heure</div>
</div>
</div>
</div>
<figcaption style="display: flex; flex-direction: column; gap: 8px">
<div style="display: flex; align-items: baseline; gap: 10px"><span style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 13px; color: #FF7033">{c['n']}</span><span style="font-size: 19px; font-weight: 800; color: #EFEFEF">{html.escape(c['nom'])}</span></div>
<div style="display: flex; flex-direction: column; align-items: flex-start; gap: 4px; padding: 14px 16px; border-radius: 8px; background: #1A1A1A; border: 1px solid #2E2E2E; overflow: hidden">
<span style="font-family: {am['fam']}; font-weight: {am['w']}; font-size: 24px; line-height: 1.1; letter-spacing: {am['ls']}; color: #EFEFEF">le montage prend</span>
<span style="font-family: {c['fam']}; font-weight: {c['w']}; font-style: {c['st']}; font-size: {round(64 * c['z'])}px; line-height: 1; letter-spacing: {c['ls']}; color: #FF7033; white-space: nowrap">1&#160;Heure</span>
</div>
<div style="font-family: {c['fam']}; font-weight: {c['w']}; font-style: {c['st']}; font-size: 18px; color: #A3A3A3">Doublé Contrôle 24</div>
<div style="font-size: 14px; line-height: 1.45; font-weight: 500; color: #A3A3A3">{html.escape(c['pourquoi'])}</div>
</figcaption>
</figure>"""

corps = f"""<div style="width: 2200px; height: 1200px; box-sizing: border-box; padding: 48px; background: #121212; color: #EFEFEF; font-family: Inter, sans-serif; display: flex; flex-direction: column; gap: 32px">
<div style="display: flex; flex-direction: column; gap: 12px">
<div style="display: flex; align-items: center; gap: 12px"><span style="display: inline-block; width: 14px; height: 14px; background: #FF7033"></span><span style="font-family: 'JetBrains Mono', monospace; font-weight: 600; font-size: 15px; letter-spacing: 0.08em; text-transform: uppercase; color: #A3A3A3">Animation caption et son · polices</span></div>
<h1 style="margin: 0; font-family: 'Big Shoulders Display', sans-serif; font-weight: 900; font-size: 64px; line-height: 0.95; letter-spacing: 0.01em; text-transform: uppercase">Combinaisons de polices</h1>
<p style="margin: 0; max-width: 1500px; font-size: 19px; line-height: 1.45; font-weight: 500; color: #A3A3A3">Ton choix d’abord (cadre braise) : JetBrains Mono 700 pour l’amorce, Google Sans Flex 800 pour le mot clé. Ensuite, les 5 polices tech essayées pour le mot clé, avec l’amorce en Inter 800.</p>
</div>
<div style="display: flex; gap: 28px; align-items: flex-start">
{''.join(carte(c) for c in COMBOS)}
</div>
</div>"""

doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>5 combinaisons de polices</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
body{{margin:0}}
@font-face{{font-family:'Redaction 50';src:url({RED}) format('woff2');font-weight:400;font-style:italic;font-display:block}}
</style>
</helmet>
{corps}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":2200,"height":1200}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
"""
open(os.path.join(ICI, "project", "AS-Polices.dc.html"), "w").write(doc)
# aperçu local
loc = doc.replace(FOND, "fond-8.jpg").replace(RED, "redaction-50-latin-400-italic.woff2")
loc = loc.replace("<x-dc>", "").replace("</x-dc>", "").replace("<helmet>", "").replace("</helmet>", "")
open(os.path.join(ICI, "test-polices.html"), "w").write(loc)
print("ok")
