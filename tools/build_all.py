#!/usr/bin/env python3
"""Baut site/data/<kurs>.json und links.json fuer die Grundsicherungs-LVs und prueft jeden Verweis.

Hart: Seite existiert; jede Zahl in Antwort und Erklaerung steht auf einer zitierten Seite.
Weich: genug inhaltliche Woerter stehen auf den zitierten Seiten (Liste zum Nachlesen).
Geschichte baut weiter tools/build_content.py.
"""
import importlib, json, re, sys, hashlib
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "content"))
import docs as D

OLD = {"e":"Geschichte der Sozialen Arbeit Einführung WS 26&27.pdf","a1":"Armenfürsorge I.pdf","rw":"Fürsorge im Roten Wien ohne Abb-1.pdf"}
TEXT = {}
def load(did, path):
    pdf = pymupdf.open(path)
    TEXT[did] = {i + 1: re.sub(r"\s+", " ", p.get_text()) for i, p in enumerate(pdf)}
for did, (fn, _, _) in D.DOCS.items():
    load(did, ROOT / "source/gs" / fn)
    if did in D.OCR:
        ocr = json.loads((ROOT / "source/gs" / D.OCR[did]).read_text())
        for k, v in ocr.items():
            TEXT[did][int(k)] += " " + " ".join(v)
for did, fn in OLD.items():
    load(did, ROOT / "source" / fn)
for (did, p), s in D.FIG.items():
    TEXT[did][p] += " " + s

errors, soft = [], []
STOP = set("""aber alle allem allen aller alles auch dabei damit dann darauf daraus dass deren diese diesem diesen dieser dieses durch einem einen einer eines erst etwa ihre ihrem ihren ihrer nach nicht noch oder ohne sich sind sowie statt über unter viele vielen vom von vor wegen wenn werden wird wurde wurden zugleich zwischen seit beim keine kein mehr nur sehr sie laut folie deine notiz""".split())
stem = lambda w: re.sub(r"(en|er|es|e|n|s)$", "", w.lower())
isweb = lambda d: d.startswith("@")

def pagetext(src):
    return " ".join(TEXT[d].get(p, "") for d, p in src if not isweb(d) and d in TEXT)

def check_src(label, src):
    if not src:
        errors.append(f"{label}: kein Verweis")
    for d, p in src:
        if isweb(d):
            if d[1:] not in D.WEB:
                errors.append(f"{label}: Web-Quelle unbekannt {d}")
        elif d not in TEXT or p not in TEXT[d]:
            errors.append(f"{label}: Seite existiert nicht: {d} {p}")

def check_numbers(label, text, src):
    if any(isweb(d) for d, _ in src):
        return
    hay = pagetext(src).replace(" ", "")
    digits = re.sub(r"\D", "", pagetext(src))
    for num in re.findall(r"\d[\d.,]*\d|\d", re.sub(r"\bMA \d+", "", text)):
        n = num.rstrip(".,")
        if n in D.DERIVED:
            continue
        if len(re.sub(r"\D", "", n)) < 2:
            continue
        if n in hay or re.sub(r"\D", "", n) in digits:
            continue
        errors.append(f"{label}: Zahl {n} steht nicht auf {src}: {text[:90]}")

def check_words(label, text, src):
    hay_raw = pagetext(src).lower()
    hay = {stem(w) for w in re.findall(r"[A-Za-zÄÖÜäöüß]{4,}", hay_raw)}
    words = [w for w in re.findall(r"[A-Za-zÄÖÜäöüß]{5,}", text) if w.lower() not in STOP]
    if not words:
        return
    miss = [w for w in words if stem(w) not in hay and w.lower()[:6] not in hay_raw]
    if len(miss) / len(words) > 0.5:
        soft.append(f"{label}: {len(miss)}/{len(words)} fehlen {miss[:6]} :: {text[:80]}")

def card_text(k):
    t = k["type"]
    if t == "mc": return k["right"]
    if t == "tf": return k["q"]
    if t == "multi": return " ".join(k["right"])
    if t == "ord": return " ".join(x[1] for x in k["items"])
    if t == "match": return " ".join(a + " " + b for a, b in k["pairs"])
    if t == "bucket": return " ".join(x[0] for x in k["items"])
    return ""

all_topics = set()
def build(name):
    mod = importlib.import_module(name)
    c = mod.c
    chs = {x["id"] for x in c.chapters}
    tops = {t["id"]: t for t in c.topics}
    for t in c.topics:
        if t["id"] in all_topics:
            errors.append("Thema doppelt " + t["id"])
        all_topics.add(t["id"])
        if t["ch"] not in chs:
            errors.append("Thema ohne Kapitel " + t["id"])
        check_src("T " + t["id"], t["src"])
        check_numbers("T " + t["id"], t["text"], t["src"])
        check_words("T " + t["id"], t["text"], t["src"])
    out, seen = [], set()
    ns = {o["n"] for o in c.opens}
    for k in c.cards:
        tp = tops.get(k["topic"])
        if not tp:
            errors.append("Karte ohne Thema: " + k["topic"]); continue
        src = [tuple(x) for x in (k["src"] or tp["src"])]
        label = f"{k['topic']} «{k['q'][:40]}»"
        check_src(label, src)
        if k["type"] == "chain":
            for s in k["steps"]:
                check_src(label, s["src"])
                check_numbers(label, s["right"] + " " + s["why"], [tuple(x) for x in s["src"]] + src)
                check_words(label, s["right"] + " " + s["why"], [tuple(x) for x in s["src"]])
        elif k["type"] == "calc":
            pass
        else:
            allsrc = src + [tuple(x) for x in tp["src"]]
            check_numbers(label, card_text(k) + " " + k["why"], allsrc)
            check_words(label, card_text(k) + " " + k["why"], src)
        if k["type"] == "mc" and len(k["wrong"]) != 3:
            errors.append(f"{label}: braucht 3 falsche Antworten")
        if k["type"] == "bucket":
            for it in k["items"]:
                if not 0 <= it[1] < len(k["buckets"]):
                    errors.append(f"{label}: Fach falsch {it}")
        for lf in k["lf"]:
            if lf not in ns:
                errors.append(f"{label}: Frage {lf} gibt es nicht")
        cid = hashlib.sha1((k["topic"] + k["q"]).encode()).hexdigest()[:8]
        if cid in seen:
            errors.append(f"{label}: doppelte Karte")
        seen.add(cid)
        extra = all(isweb(d) or d in D.EXTRA for d, _ in src)
        out.append({**k, "id": cid, "src": src, "extra": extra})
    for o in c.opens:
        if o["ch"] not in chs:
            errors.append(f"Frage {o['n']}: Kapitel {o['ch']}")
        for p in o["points"] + o.get("deep", []):
            check_src(f"F{o['n']}", p["src"])
            check_numbers(f"F{o['n']}", p["t"], p["src"])
            check_words(f"F{o['n']}", p["t"], p["src"])
    for x in c.terms + c.people + c.timeline + c.traps:
        check_src(x.get("term") or x.get("name") or x.get("y") or x.get("title"), x["src"])
    data = dict(course=c.meta, chapters=c.chapters, topics=c.topics, cards=out, leitfragen=c.opens, people=c.people, terms=c.terms, timeline=c.timeline, traps=c.traps, more=D.MORE.get(name, []))
    if name == "faelle":
        data["cases"] = mod.CASES
        data["sections"] = mod.SECTIONS
        for cs in mod.CASES:
            for key, pts in cs["sections"].items():
                for p in pts:
                    check_src(f"Fall {cs['id']} {key}", p["src"])
                    check_numbers(f"Fall {cs['id']} {key}", p["t"], p["src"])
    (ROOT / f"site/data/{name}.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    print(name, "Karten", len(out), "Themen", len(c.topics), "Fragen", len(c.opens))

for n in ["recht", "matsi", "sopol", "faelle", "orbe"]:
    build(n)

import links
geschichte = {t["id"] for t in json.loads((ROOT / "site/data/geschichte.json").read_text())["topics"]}
for l in links.LINKS:
    check_src("Link " + l["id"], l["src"])
    check_numbers("Link " + l["id"], l["text"], l["src"])
    for t in l["topics"]:
        if t not in all_topics and t not in geschichte:
            errors.append(f"Link {l['id']}: Thema {t} gibt es nicht")
(ROOT / "site/data/links.json").write_text(json.dumps(dict(links=links.LINKS, web={k: dict(t=v[0], u=v[1]) for k, v in D.WEB.items()}), ensure_ascii=False, separators=(",", ":")))
print("Exkurse", len(links.LINKS))

print("\nZum Nachlesen:", len(soft))
for s in soft:
    print(" -", s)
print("\nFehler:", len(errors))
for e in errors:
    print(" !", e)
sys.exit(1 if errors else 0)
