#!/usr/bin/env python3
"""talkcut.py — find silences and repetitions in a HyperFrames talking-head edit.

Usage (run from the project folder, with python3 -I):
  python3 -I talkcut.py silences [--min 0.4] [--room 0.15]   -> JSON stretches for script.editWords (kind cut)
  python3 -I talkcut.py repeats                             -> played words per clip + repetition candidates
  python3 -I talkcut.py doubles                             -> clips that replay media another clip already plays

Reads index.html and compositions/*.html (<video>/<audio> with data-media-start,
data-duration, src) and the transcripts in .hyperframes/transcripts/*.json.
It never writes anything.
"""
import glob, html, json, os, re, sys

STOP = {"le","la","les","l'","un","une","des","de","du","d'","et","ou","à","a","en","je","j'",
        "tu","il","y","que","qui","ce","c'est","se","sur","dans","pour","pas","ne","n'","mon",
        "ma","mes","ton","ta","tes","son","sa","ses","the","a","an","and","or","to","of","in",
        "i","you","it","is","that","this","on","for","with"}

def norm(t):
    return re.sub(r"[^\w']+", "", t.lower().replace("’", "'"))

def attr(tag, k):
    m = re.search(r'\s' + re.escape(k) + r'="([^"]*)"', tag)
    return html.unescape(m.group(1)) if m else None

def load_clips():
    files = ["index.html"] + sorted(glob.glob("compositions/*.html"))
    clips = []
    for f in files:
        if not os.path.exists(f):
            continue
        for tag in re.findall(r"<(?:video|audio)\b[^>]*>", open(f, encoding="utf-8").read()):
            ms, du, st, src = (attr(tag, "data-media-start"), attr(tag, "data-duration"),
                               attr(tag, "data-start"), attr(tag, "src"))
            if None in (du, st, src):
                continue
            ms = float(ms or 0)
            clips.append({"id": attr(tag, "data-hf-id") or attr(tag, "id"), "file": f, "src": src,
                          "start": float(st), "a": ms, "b": ms + float(du)})
    clips.sort(key=lambda c: c["start"])
    return clips

def load_transcripts():
    out = {}
    for f in glob.glob(".hyperframes/transcripts/*.json"):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        if isinstance(d, dict) and d.get("src") and d.get("words"):
            out[d["src"]] = [w for w in d["words"] if "start" in w and "end" in w]
    return out

def played(clips, src, a, b):
    return sum(max(0.0, min(b, c["b"]) - max(a, c["a"])) for c in clips if c["src"] == src)

def silences(min_gap, room):
    clips, tr = load_clips(), load_transcripts()
    out, total = [], 0.0
    for src, words in tr.items():
        if not any(c["src"] == src for c in clips):
            continue
        for p, q in zip(words, words[1:]):
            gap = q["start"] - p["end"]
            pl = played(clips, src, p["end"], q["start"])
            if gap >= min_gap and pl > 2 * room + 0.05:
                out.append({"src": src, "from": round(p["end"], 3), "to": round(q["start"], 3),
                            "text": "pause", "_between": f'{p["text"]} | {q["text"]}',
                            "_played": round(pl, 2)})
                total += pl - 2 * room
    print(json.dumps({"count": len(out), "secondsRemovedApprox": round(total, 1),
                      "stretches": out}, ensure_ascii=False, indent=1))

def played_words(clips, tr):
    seq = []
    for c in clips:
        for w in tr.get(c["src"], []):
            mid = (w["start"] + w["end"]) / 2
            if c["a"] <= mid < c["b"]:
                seq.append({**w, "clip": c["id"], "src": c["src"]})
    return seq

def repeats():
    clips, tr = load_clips(), load_transcripts()
    seq = played_words(clips, tr)
    cands = []
    # 1. truncated words / restarts ("de...", "pour—")
    for i, w in enumerate(seq):
        if re.search(r"(\.\.\.|…|—|-)$", w["text"]):
            j = i
            while j > 0 and not re.search(r"[.!?]$", seq[j - 1]["text"]) and i - j < 12:
                j -= 1
            cands.append({"kind": "restart", "src": w["src"], "from": seq[j]["start"], "to": w["end"],
                          "text": " ".join(x["text"] for x in seq[j:i + 1]),
                          "next": " ".join(x["text"] for x in seq[i + 1:i + 9])})
    # 2. the same 1-4 word phrase said twice within 14 words
    seen = set()
    for n in (4, 3, 2, 1):
        for i in range(len(seq) - n):
            g = [norm(x["text"]) for x in seq[i:i + n]]
            if n == 1 and (g[0] in STOP or len(g[0]) < 4):
                continue
            if n > 1 and all(x in STOP for x in g):
                continue
            for k in range(i + n, min(len(seq) - n + 1, i + n + (6 if n == 1 else 14))):
                if [norm(x["text"]) for x in seq[k:k + n]] == g:
                    key = (i, k)
                    if any(a <= i < a + m and b <= k < b + m for a, b, m in seen):
                        continue
                    seen.add((i, k, n))
                    cands.append({"kind": "repeated-phrase", "phrase": " ".join(x["text"] for x in seq[i:i + n]),
                                  "first": {"src": seq[i]["src"], "from": seq[i]["start"], "to": seq[i + n - 1]["end"]},
                                  "second": {"src": seq[k]["src"], "from": seq[k]["start"], "to": seq[k + n - 1]["end"]},
                                  "context": " ".join(x["text"] for x in seq[max(0, i - 6):k + n + 6])})
                    break
    lines = []
    for c in clips:
        ws = [w for w in seq if w["clip"] == c["id"]]
        if ws:
            lines.append({"clip": c["id"], "at": round(c["start"], 2),
                          "words": " ".join(f'{w["text"]}@{w["start"]:.2f}-{w["end"]:.2f}' for w in ws)})
    print(json.dumps({"candidates": cands, "playedWords": lines}, ensure_ascii=False, indent=1))

def doubles():
    clips = load_clips()
    out = []
    for i, c in enumerate(clips):
        for d in clips[:i]:
            ov = min(c["b"], d["b"]) - max(c["a"], d["a"])
            if d["src"] == c["src"] and ov > 0.02:
                out.append({"clip": c["id"], "alsoPlayedBy": d["id"], "src": c["src"],
                            "overlap": [round(max(c["a"], d["a"]), 3), round(min(c["b"], d["b"]), 3)],
                            "clipCoversOnly": round(c["b"] - c["a"], 3)})
    print(json.dumps({"doubles": out}, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    a = sys.argv[1:] or ["silences"]
    opt = lambda k, dflt: float(a[a.index(k) + 1]) if k in a else dflt
    {"silences": lambda: silences(opt("--min", 0.4), opt("--room", 0.15)),
     "repeats": repeats, "doubles": doubles}[a[0]]()
