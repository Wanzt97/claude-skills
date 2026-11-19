#!/usr/bin/env python3
"""
fcpxml_to_json.py — Convertit un fichier FCPXML (Final Cut Pro) en un JSON
autonome et exploitable par un agent qui n'a pas accès au FCPXML lui-meme,
mais qui a acces au dossier de rushs (media).

Le JSON produit resout toutes les references internes du FCPXML (ref -> asset,
ref -> effet), calcule les positions ABSOLUES sur la timeline finale (pas de
coordonnees locales a interpreter), separe les notes de montage (hashtags de
type de plan, indications de mouvement/transition) du texte parle, et remonte
les rappels de production generaux (qui ne concernent pas un plan precis) au
niveau racine du fichier.

Principe directeur : NE JAMAIS supprimer une information du FCPXML source.
Tout element ou attribut non explicitement gere par ce script est capture en
brut (raw_xml) plutot que d'etre silencieusement ignore, et un avertissement
est ajoute dans "_warnings" pour signaler qu'une revue manuelle peut etre utile.

Usage:
    python3 fcpxml_to_json.py <input.fcpxml> [<output.json>]

Si <output.json> est omis, le fichier est ecrit a cote de l'entree avec le
suffixe "_timeline_reconstruction.json".
"""

import sys
import re
import json
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

# Mots-cles utilises pour detecter qu'une note de montage est en fait un
# rappel de production general (concerne toute la video) plutot qu'une
# instruction specifique au plan sur lequel elle a ete trouvee dans le
# FCPXML. Base sur l'usage observe de Wanzt ; a completer si de nouveaux
# schemas de notes apparaissent dans de futurs projets.
GLOBAL_NOTE_KEYWORDS = [
    'avant publication', 'miniature de la vidéo', 'sous-titres obligatoires',
    'coupe les silences', 'filme le bloc',
]


# ---------------------------------------------------------------------------
# Utilitaires de temps
# ---------------------------------------------------------------------------

def frac_to_seconds(frac):
    if frac is None:
        return 0.0
    frac = frac.rstrip('s')
    if '/' in frac:
        num, den = frac.split('/')
        return float(num) / float(den)
    return float(frac)


def seconds_to_tc(sec, fps):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = int(sec % 60)
    f = round((sec - int(sec)) * fps)
    if f >= round(fps):
        f = 0
        s += 1
    return f"{h:02d}:{m:02d}:{s:02d}:{f:02d}"


def decode_path(uri):
    if uri is None:
        return None
    return urllib.parse.unquote(uri).replace('file://', '')


def raw_xml(el):
    """Capture brute d'un element non gere explicitement — rien n'est perdu."""
    return ET.tostring(el, encoding='unicode').strip()


# ---------------------------------------------------------------------------
# Extraction des notes de montage (hashtags / indications / texte parle)
# ---------------------------------------------------------------------------

def split_notes_and_script(raw):
    shot_tags, direction_notes, script_lines = [], [], []
    for line in (raw or "").split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith('//'):
            direction_notes.append(line.lstrip('/ ').strip())
        elif line.startswith('#'):
            shot_tags.extend(re.findall(r'#(\S+)', line))
        else:
            script_lines.append(line)
    return shot_tags, direction_notes, " ".join(script_lines).strip()


def convert(src_path, out_path):
    warnings = []
    tree = ET.parse(src_path)
    root = tree.getroot()

    # --- Format (resolution / fps / colorimetrie) ---------------------------
    format_el = root.find('.//resources/format')
    if format_el is None:
        raise ValueError("Aucun element <format> trouve dans <resources> — fichier FCPXML inattendu.")
    fd = format_el.attrib.get('frameDuration', '1/30s').rstrip('s')
    num, den = fd.split('/')
    fps = round(float(den) / float(num), 3)
    fmt = {
        "id": format_el.attrib.get('id'),
        "name": format_el.attrib.get('name'),
        "frame_duration": format_el.attrib.get('frameDuration'),
        "width": int(format_el.attrib.get('width', 0)) or None,
        "height": int(format_el.attrib.get('height', 0)) or None,
        "color_space": format_el.attrib.get('colorSpace'),
        "fps": fps,
    }

    # --- Effets ---------------------------------------------------------------
    effects = {}
    for eff in root.findall('.//resources/effect'):
        effects[eff.attrib['id']] = {
            "id": eff.attrib['id'],
            "name": eff.attrib.get('name'),
            "uid": eff.attrib.get('uid'),
        }

    # --- Assets (rushs) ---------------------------------------------------------
    assets = {}
    for a in root.findall('.//resources/asset'):
        aid = a.attrib['id']
        mr = a.find('media-rep')
        src_uri = mr.attrib.get('src') if mr is not None else None
        decoded_path = decode_path(src_uri)
        codecs, ingest_date = None, None
        md_el = a.find('metadata')
        if md_el is not None:
            for m in md_el.findall('md'):
                key = m.attrib.get('key')
                if key == 'com.apple.proapps.spotlight.kMDItemCodecs':
                    arr = m.find('array')
                    if arr is not None:
                        codecs = [s.text for s in arr.findall('string')]
                elif key == 'com.apple.proapps.mio.ingestDate':
                    ingest_date = m.attrib.get('value')
        assets[aid] = {
            "id": aid,
            "name": a.attrib.get('name'),
            "filename": decoded_path.split('/')[-1] if decoded_path else a.attrib.get('name'),
            "uid": a.attrib.get('uid'),
            "has_video": a.attrib.get('hasVideo') == '1',
            "has_audio": a.attrib.get('hasAudio') == '1',
            "video_sources": a.attrib.get('videoSources'),
            "audio_sources": a.attrib.get('audioSources'),
            "audio_channels": a.attrib.get('audioChannels'),
            "audio_rate": a.attrib.get('audioRate'),
            "codecs": codecs,
            "ingest_date": ingest_date,
            "original_file_path_on_source_machine": decoded_path,
        }

    # --- Autres types de ressources rencontres (media/compound clips, etc.) ---
    # Captures generiquement pour ne rien perdre si un futur projet en contient.
    other_resources = []
    handled_res_tags = {'format', 'effect', 'asset'}
    resources_el = root.find('resources')
    if resources_el is not None:
        for child in resources_el:
            if child.tag not in handled_res_tags:
                other_resources.append({"tag": child.tag, "raw_xml": raw_xml(child)})
                warnings.append(
                    f"Ressource de type <{child.tag}> (id={child.attrib.get('id')}) "
                    f"non geree specifiquement — capturee en brut dans 'other_resources'."
                )

    # --- Projet / sequence ------------------------------------------------------
    project_el = root.find('.//project')
    sequence_el = root.find('.//sequence')
    if project_el is None or sequence_el is None:
        raise ValueError("Aucun <project>/<sequence> trouve — ce script attend un FCPXML contenant une timeline montee.")

    project = {"name": project_el.attrib.get('name'), "uid": project_el.attrib.get('uid')}
    seq_duration_s = frac_to_seconds(sequence_el.attrib.get('duration'))
    sequence = {
        "format_ref": sequence_el.attrib.get('format'),
        "duration_seconds": round(seq_duration_s, 3),
        "duration_tc": seconds_to_tc(seq_duration_s, fps),
        "duration_frames": round(seq_duration_s * fps),
        "tc_start": sequence_el.attrib.get('tcStart'),
        "tc_format": sequence_el.attrib.get('tcFormat'),
        "audio_layout": sequence_el.attrib.get('audioLayout'),
        "audio_rate": sequence_el.attrib.get('audioRate'),
    }

    # --- text-style-defs (police/couleur/alignement des titres) ---------------
    text_styles = {}
    for tsd in root.iter('text-style-def'):
        ts = tsd.find('text-style')
        if ts is not None:
            text_styles[tsd.attrib.get('id')] = dict(ts.attrib)

    def resolve_asset_ref(ref):
        a = assets.get(ref)
        if a is None:
            return {"ref": ref, "name": None, "filename": None}
        return {"ref": ref, "name": a["name"], "filename": a["filename"]}

    def parse_title(title_el, parent_abs_offset, parent_start):
        t_offset = frac_to_seconds(title_el.attrib.get('offset'))
        t_start = frac_to_seconds(title_el.attrib.get('start', '0s'))
        t_duration = frac_to_seconds(title_el.attrib.get('duration'))
        abs_offset = parent_abs_offset + (t_offset - parent_start)

        params = {p.attrib.get('name'): p.attrib.get('value') for p in title_el.findall('param')}

        full_text, style = None, None
        text_el = title_el.find('text')
        if text_el is not None:
            ts_el = text_el.find('text-style')
            if ts_el is not None:
                full_text = (ts_el.text or "").strip()
                style = text_styles.get(ts_el.attrib.get('ref'))

        shot_tags, direction_notes, script_text = split_notes_and_script(full_text)
        ref = title_el.attrib.get('ref')

        return {
            "lane": title_el.attrib.get('lane'),
            "type": "title",
            "effect_ref": {"ref": ref, "name": effects.get(ref, {}).get('name')},
            "enabled": title_el.attrib.get('enabled', '1') != '0',
            "timeline_offset_seconds": round(abs_offset, 3),
            "timeline_offset_tc": seconds_to_tc(abs_offset, fps),
            "timeline_duration_seconds": round(t_duration, 3),
            "timeline_duration_frames": round(t_duration * fps),
            "params": params,
            "text_raw": full_text,
            "shot_tags": shot_tags,
            "direction_notes": direction_notes,
            "script_text": script_text if script_text else None,
            "text_style": style,
        }

    def parse_connected_clip(clip_el, parent_abs_offset, parent_start):
        c_offset = frac_to_seconds(clip_el.attrib.get('offset'))
        c_start = frac_to_seconds(clip_el.attrib.get('start', '0s'))
        c_duration = frac_to_seconds(clip_el.attrib.get('duration'))
        abs_offset = parent_abs_offset + (c_offset - parent_start)
        return {
            "lane": clip_el.attrib.get('lane'),
            "type": "asset-clip",
            "source_asset": resolve_asset_ref(clip_el.attrib.get('ref')),
            "timeline_offset_seconds": round(abs_offset, 3),
            "timeline_offset_tc": seconds_to_tc(abs_offset, fps),
            "timeline_duration_seconds": round(c_duration, 3),
            "timeline_duration_frames": round(c_duration * fps),
            "source_in_point_seconds": round(c_start, 3),
            "source_out_point_seconds": round(c_start + c_duration, 3),
        }

    def parse_marker(marker_el, parent_abs_offset, parent_start):
        m_offset = frac_to_seconds(marker_el.attrib.get('start'))
        abs_offset = parent_abs_offset + (m_offset - parent_start)
        return {
            "type": "marker",
            "name": marker_el.attrib.get('value'),
            "note": marker_el.attrib.get('note'),
            "timeline_offset_seconds": round(abs_offset, 3),
            "timeline_offset_tc": seconds_to_tc(abs_offset, fps),
            "completed": marker_el.attrib.get('completed'),
        }

    # --- Parcours de la timeline (spine) ---------------------------------------
    spine = root.find('.//spine')
    if spine is None:
        raise ValueError("Aucun <spine> trouve dans le projet — impossible de lire la timeline.")

    KNOWN_PRIMARY_TAGS = {'asset-clip', 'gap'}
    KNOWN_CONNECTED_TAGS = {'title', 'asset-clip', 'marker'}

    primary_track = []
    for idx, el in enumerate(spine, 1):
        kind = el.tag
        offset = frac_to_seconds(el.attrib.get('offset'))
        duration = frac_to_seconds(el.attrib.get('duration'))
        start = frac_to_seconds(el.attrib.get('start', '0s'))

        entry = {
            "order": idx,
            "type": "gap" if kind == "gap" else ("clip" if kind == "asset-clip" else kind),
            "source_asset": None if kind != "asset-clip" else resolve_asset_ref(el.attrib.get('ref')),
            "timeline_offset_seconds": round(offset, 3),
            "timeline_offset_tc": seconds_to_tc(offset, fps),
            "timeline_duration_seconds": round(duration, 3),
            "timeline_duration_frames": round(duration * fps),
            "source_in_point_seconds": None if kind != "asset-clip" else round(start, 3),
            "source_out_point_seconds": None if kind != "asset-clip" else round(start + duration, 3),
            "connected_items": [],
        }

        if kind not in KNOWN_PRIMARY_TAGS:
            entry["raw_xml"] = raw_xml(el)
            warnings.append(
                f"Segment #{idx} sur la piste principale est de type <{kind}>, non geree "
                f"specifiquement (seuls asset-clip/gap le sont) — capture brute incluse."
            )

        for child in el:
            if child.tag == 'title':
                entry["connected_items"].append(parse_title(child, offset, start))
            elif child.tag == 'asset-clip':
                entry["connected_items"].append(parse_connected_clip(child, offset, start))
            elif child.tag == 'marker':
                entry["connected_items"].append(parse_marker(child, offset, start))
            else:
                entry["connected_items"].append({"type": child.tag, "raw_xml": raw_xml(child)})
                warnings.append(
                    f"Segment #{idx} contient un element attache de type <{child.tag}>, "
                    f"non gere specifiquement — capture brute incluse dans 'connected_items'."
                )

        primary_track.append(entry)

    # --- Remonter les rappels de production generaux ---------------------------
    general_production_notes = []
    for entry in primary_track:
        for item in entry["connected_items"]:
            if item.get("type") == "title":
                for note in item.get("direction_notes", []):
                    if any(kw in note.lower() for kw in GLOBAL_NOTE_KEYWORDS):
                        general_production_notes.append({
                            "note": note,
                            "found_on_segment_order": entry["order"],
                            "scope": "whole_video_not_segment_specific",
                        })

    output = {
        "_meta": {
            "purpose": (
                "Reconstruction complete et exploitable par un agent (hors FCPXML) de la "
                "timeline Final Cut Pro. Toutes les references internes (ref -> resource) sont "
                "resolues ; toutes les positions sont exprimees en secondes absolues sur la "
                "timeline finale."
            ),
            "source_file": Path(src_path).name,
            "generated_from": "Final Cut Pro FCPXML",
            "media_files_required": sorted(set(a["filename"] for a in assets.values())),
            "matching_instructions": (
                "Faire correspondre chaque 'filename' (ici et dans resources.assets / "
                "source_asset) aux fichiers du dossier media fourni separement, par NOM DE "
                "FICHIER — ignorer 'original_file_path_on_source_machine', qui pointe vers "
                "une machine differente de celle qui traitera ce JSON."
            ),
            "_warnings": warnings,
        },
        "project": project,
        "format": fmt,
        "sequence": sequence,
        "resources": {
            "assets": assets,
            "effects": effects,
            "other_resources": other_resources,
        },
        "general_production_notes": general_production_notes,
        "timeline": {
            "primary_track": primary_track,
        },
    }

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    return output, warnings


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fcpxml_to_json.py <input.fcpxml> [<output.json>]")
        sys.exit(1)

    src = Path(sys.argv[1])
    if not src.exists():
        print(f"Fichier introuvable : {src}")
        sys.exit(1)

    if len(sys.argv) >= 3:
        out = Path(sys.argv[2])
    else:
        out = src.with_name(src.stem + "_timeline_reconstruction.json")

    output, warnings = convert(str(src), str(out))

    print(f"OK — JSON ecrit dans {out}")
    print(f"Segments sur la piste principale : {len(output['timeline']['primary_track'])}")
    print(f"Assets/rushs references : {len(output['resources']['assets'])}")
    print(f"Notes de production generales extraites : {len(output['general_production_notes'])}")
    if warnings:
        print(f"\n⚠ {len(warnings)} avertissement(s) — elements non geres specifiquement, captures en brut :")
        for w in warnings:
            print("  -", w)
    else:
        print("Aucun avertissement — tous les elements de la timeline ont ete geres specifiquement.")


if __name__ == "__main__":
    main()
