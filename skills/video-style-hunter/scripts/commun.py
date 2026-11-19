"""Fonctions partagées par les scripts de video-style-hunter (stdlib + ffmpeg seulement)."""
import json
import os
import re
import subprocess
import unicodedata

VIDEO_EXT = {".mp4", ".mov", ".m4v", ".webm", ".mkv", ".avi"}
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".heic"}

# Arborescence du canevas (relevée le 2026-11-05 sur la version en ligne).
# Ne pas la modifier sans l'accord de Wanzt. Code de classement -> chemin du dossier.
ARBO = {
    "A": "A - Sous-titres et typographie",
    "B1": "B - Accroche/B1 - Intervenant toujours a l'ecran",
    "B2": "B - Accroche/B2 - Sous-titres dans la moitie basse",
    "B3": "B - Accroche/B3 - Le mot qui donne envie de rester",
    "C1": "C - Types de scene/C1 - Sous-titres seuls",
    "C2": "C - Types de scene/C2 - Sous-titres + petite animation en bas",
    "C3": "C - Types de scene/C3 - Ecran partage",
    "C4": "C - Types de scene/C4 - Animation plein ecran",
    "D1.texte": "D - Types d'animation/D1 - Centree sur le texte/Texte seul",
    "D1.objet": "D - Types d'animation/D1 - Centree sur le texte/Texte + objet",
    "D1.graphique": "D - Types d'animation/D1 - Centree sur le texte/Texte + graphique",
    "D2.centre": "D - Types d'animation/D2 - Centree sur une personne/Personne au centre",
    "D2.cote": "D - Types d'animation/D2 - Centree sur une personne/Personne sur le cote",
    "D3.texte": "D - Types d'animation/D3 - Centree sur un objet/Objet au milieu + texte",
    "D3.graphique": "D - Types d'animation/D3 - Centree sur un objet/Objet au milieu + graphique",
    "D4": "D - Types d'animation/D4 - Centree sur un graphique/Charts, interfaces (UI)",
    "E1": "E - Fonds/E1 - Grappes de carres vers les bords",
    "E2": "E - Fonds/E2 - Grille gommee autour du sujet",
    "E3": "E - Fonds/E3 - Grille gommee d'ambiance",
    "F1": "F - Composition/F1 - Fond",
    "F2": "F - Composition/F2 - Point focal",
    "F3": "F - Composition/F3 - Elements de soutien",
    "F4": "F - Composition/F4 - Elements de profondeur",
    "G1": "G - Design/G1 - Couleur",
    "G2": "G - Design/G2 - Polices",
    "G3": "G - Design/G3 - Textes",
    "G4": "G - Design/G4 - Objets (ombres, textures)",
    "G5": "G - Design/G5 - Fonds",
    "H": "H - Animations pendant que je parle",
    "IU": "I - Inspiration generale/IU - UI",
    "IG": "I - Inspiration generale/IG - Graphiques et data",
    "IS": "I - Inspiration generale/IS - Scenes completes",
}

REJET = "_rejete"
FAVORI = "++"
RE_FORMAT = re.compile(r"_(\d+x\d+)\.[A-Za-z0-9]+$")


def planche(code):
    return ARBO[code].split("/")[0]


def lettre(code):
    return code[0]


def chemin_lot(lot, *parts):
    return os.path.join(lot, *parts)


def travail(lot, *parts):
    return os.path.join(lot, "_travail", *parts)


def sonde(chemin):
    """(largeur, hauteur, durée en s ou None) après rotation."""
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height:stream_side_data=rotation:format=duration",
         "-of", "json", chemin],
        capture_output=True, text=True)
    try:
        d = json.loads(out.stdout or "{}")
    except json.JSONDecodeError:
        d = {}
    st = (d.get("streams") or [{}])[0]
    w, h = int(st.get("width") or 0), int(st.get("height") or 0)
    rot = 0
    for sd in st.get("side_data_list") or []:
        if "rotation" in sd:
            rot = int(float(sd["rotation"]))
    if abs(rot) % 180 == 90:
        w, h = h, w
    dur = (d.get("format") or {}).get("duration")
    return w, h, (float(dur) if dur not in (None, "N/A") else None)


def tag_format(w, h):
    if not w or not h:
        return "0x0"
    r = w / h
    for tag, val in (("9x16", 9 / 16), ("16x9", 16 / 9), ("1x1", 1.0), ("4x5", 4 / 5),
                     ("3x4", 3 / 4), ("4x3", 4 / 3), ("2x3", 2 / 3), ("21x9", 21 / 9)):
        if abs(r - val) / val < 0.04:
            return tag
    return f"{w}x{h}"


def format_de(nom):
    m = RE_FORMAT.search(nom)
    return m.group(1) if m else "?"


def slugifier(s, maxlen=28):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^A-Za-z0-9._]+", "-", s.lower()).strip("-._")
    return (s[:maxlen].strip("-._")) or "source"


def slug_depuis_nom(nom):
    base = os.path.splitext(os.path.basename(nom))[0]
    base = re.sub(r"^\d{1,4}[_ -]+", "", base)          # numéro de tri en tête
    base = re.sub(r"[_ -]+\d{8,}$", "", base)            # identifiant TikTok/IG en fin
    if re.fullmatch(r"[0-9a-fA-F]{12,}", base):          # nom = hash
        base = base[:8]
    elif re.fullmatch(r"\d{9,}", base):                  # nom = identifiant numérique
        base = base[-6:]
    return slugifier(base)


def fmt_t(t):
    return f"{t:.1f}"


def parse_temps(s):
    if s is None or s == "":
        return None
    s = str(s).strip()
    if ":" in s:
        parts = [float(p) for p in s.split(":")]
        v = 0.0
        for p in parts:
            v = v * 60 + p
        return v
    return float(s)


def hms(t):
    t = int(round(t))
    return f"{t // 3600}:{t % 3600 // 60:02d}:{t % 60:02d}" if t >= 3600 else f"{t // 60}:{t % 60:02d}"


def dist(a, b):
    """Écart moyen (0-255) entre deux vignettes rgb24 de même taille."""
    return sum(abs(x - y) for x, y in zip(a, b)) / len(a)


def charger_index(lot):
    p = travail(lot, "index.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return {"sources": [], "elements": []}


def sauver_index(lot, idx):
    os.makedirs(travail(lot), exist_ok=True)
    with open(travail(lot, "index.json"), "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=1)


# ---------------------------------------------------------------- planches contact
# Petite police bitmap 3x5 pour numéroter les cases (ffmpeg n'a pas drawtext ici).
_CHIFFRES = {
    "0": ("111", "101", "101", "101", "111"), "1": ("010", "110", "010", "010", "111"),
    "2": ("111", "001", "111", "100", "111"), "3": ("111", "001", "111", "001", "111"),
    "4": ("101", "101", "111", "001", "001"), "5": ("111", "100", "111", "001", "111"),
    "6": ("111", "100", "111", "101", "111"), "7": ("111", "001", "010", "010", "010"),
    "8": ("111", "101", "111", "101", "111"), "9": ("111", "101", "111", "001", "111"),
}


def _rect(buf, W, x0, y0, w, h, rgb):
    for y in range(y0, y0 + h):
        row = (y * W + x0) * 3
        buf[row:row + w * 3] = bytes(rgb) * w


def _texte(buf, W, x0, y0, txt, echelle=4, rgb=(255, 255, 255)):
    x = x0
    for ch in txt:
        g = _CHIFFRES.get(ch)
        if g:
            for gy, ligne in enumerate(g):
                for gx, bit in enumerate(ligne):
                    if bit == "1":
                        _rect(buf, W, x + gx * echelle, y0 + gy * echelle, echelle, echelle, rgb)
        x += 4 * echelle


def image_cellule(chemin, cw, ch, temps=None):
    """Image rgb24 cw x ch (letterbox) d'un fichier image ou vidéo."""
    cmd = ["ffmpeg", "-v", "error"]
    ext = os.path.splitext(chemin)[1].lower()
    if ext in VIDEO_EXT:
        if temps is None:
            _, _, d = sonde(chemin)
            temps = (d or 0) / 2
        cmd += ["-ss", f"{temps:.2f}"]
    cmd += ["-i", chemin, "-frames:v", "1", "-vf",
            f"scale={cw}:{ch}:force_original_aspect_ratio=decrease,"
            f"pad={cw}:{ch}:(ow-iw)/2:(oh-ih)/2:color=0x1c1c1c",
            "-f", "rawvideo", "-pix_fmt", "rgb24", "pipe:1"]
    out = subprocess.run(cmd, capture_output=True).stdout
    return out if len(out) == cw * ch * 3 else bytes([60, 0, 0]) * (cw * ch)


def taille_cellule(fichiers):
    """Cases 9:16 si la majorité est verticale, 16:9 si horizontale, carrées sinon."""
    fm = [format_de(os.path.basename(f)) for f in fichiers]
    v = sum(f in ("9x16", "2x3", "3x4", "4x5") for f in fm)
    h = sum(f in ("16x9", "21x9", "4x3") for f in fm)
    if v > 0.6 * len(fm):
        return 216, 384
    if h > 0.6 * len(fm):
        return 400, 225
    return 300, 300


def planches_contact(fichiers, prefixe, colonnes=None, lignes=None, cell=None, marques=None):
    """Assemble des planches numérotées (1..n) et une légende <prefixe>.txt.
    marques: dict chemin -> (r,g,b) pour un carré de couleur en haut à droite
    (orange = extrait vidéo par défaut)."""
    os.makedirs(os.path.dirname(prefixe) or ".", exist_ok=True)
    cw, chh = cell or taille_cellule(fichiers)
    auto = {(216, 384): (10, 3), (400, 225): (5, 6)}.get((cw, chh), (6, 5))
    colonnes, lignes = colonnes or auto[0], lignes or auto[1]
    par_page = colonnes * lignes
    sorties = []
    with open(prefixe + ".txt", "w", encoding="utf-8") as leg:
        for p in range(0, len(fichiers), par_page):
            lot = fichiers[p:p + par_page]
            W, H = colonnes * cw, ((len(lot) + colonnes - 1) // colonnes) * chh
            buf = bytearray(b"\x10" * (W * H * 3))
            for i, f in enumerate(lot):
                n = p + i + 1
                leg.write(f"{n}\t{f}\n")
                cx, cy = (i % colonnes) * cw, (i // colonnes) * chh
                iw, ih = cw - 4, chh - 4
                img = image_cellule(f, iw, ih)
                for y in range(ih):
                    o = ((cy + 2 + y) * W + cx + 2) * 3
                    buf[o:o + iw * 3] = img[y * iw * 3:(y + 1) * iw * 3]
                lab = str(n)
                _rect(buf, W, cx + 2, cy + 2, len(lab) * 16 + 8, 28, (0, 0, 0))
                _texte(buf, W, cx + 6, cy + 6, lab)
                coul = (marques or {}).get(f)
                if coul is None and os.path.splitext(f)[1].lower() in VIDEO_EXT:
                    coul = (255, 106, 26)
                if coul:
                    _rect(buf, W, cx + cw - 26, cy + 4, 20, 20, coul)
            sortie = f"{prefixe}_{p // par_page + 1:02d}.jpg"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                            "-s", f"{W}x{H}", "-i", "pipe:0", "-frames:v", "1", "-q:v", "3", sortie],
                           input=bytes(buf), check=True)
            sorties.append(sortie)
    return sorties
