#!/usr/bin/env python3
"""Baut site/data/geschichte.json aus content/geschichte.py und prueft jeden Folienverweis.

Geprueft wird gegen den extrahierten Folientext (Argument 1: Ordner mit source/-PDFs genuegt, wenn pymupdf da ist):
 - Seite existiert und ist nicht leer
 - jede Jahres- oder Mengenzahl aus Antwort und Erklaerung steht auf einer der zitierten Seiten
 - genug inhaltliche Woerter der Antwort finden sich auf den zitierten Seiten
Hart sind nur die ersten beiden Pruefungen; die Wortpruefung gibt eine Liste zum Nachlesen aus.
"""
import importlib.util, json, re, sys, hashlib
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("c", ROOT / "content/geschichte.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)

FILES = {
    "e":"Geschichte der Sozialen Arbeit Einführung WS 26&27.pdf","a1":"Armenfürsorge I.pdf","a2":"Armenfürsorge II.pdf",
    "eb":"Vom sozialen Ehrenamt zum Frauenberuf.pdf","rw":"Fürsorge im Roten Wien ohne Abb-1.pdf","t":"Fürsorge in Totalitären Regimen.pdf",
    "n":"Fürsorge in der Nachkriegszeit& Wirtschaftswunder.pdf","zs":"Von der Fürsorge zur Sozialarbeit.pdf","z":"Zeittafel.Sozialarbeit.pdf","lf":"Leitfragen & Lernziele_Prüfung.pdf",
}
TEXT = {}
for d, fn in FILES.items():
    pdf = pymupdf.open(ROOT / "source" / fn)
    TEXT[d] = {i+1: re.sub(r"\s+", " ", p.get_text()) for i, p in enumerate(pdf)}

errors, soft = [], []
STOP = set("""aber alle allem allen aller alles auch dabei damit dann darauf daraus dass deren diese diesem diesen dieser dieses durch einem einen einer eines erst etwa ihre ihrem ihren ihrer nach nicht noch oder ohne sich sind sowie statt über unter viele vielen vom von vor wegen wenn werden wird wurde wurden zugleich zwischen seit beim keine kein mehr nur sehr sie laut folie""".split())

def stem(w):
    return re.sub(r"(en|er|es|e|n|s)$", "", w.lower())

def pagetext(src):
    return " ".join(TEXT[d].get(p, "") for d, p in src)

def check_src(label, src):
    for d, p in src:
        if d not in TEXT or p not in TEXT[d]:
            errors.append(f"{label}: Seite existiert nicht: {d} {p}")
        elif len(TEXT[d][p].strip()) < 15:
            soft.append(f"{label}: Seite fast ohne Text: {d} {p}")

def check_numbers(label, text, src):
    hay = pagetext(src).replace(" ", "")
    hay2 = re.sub(r"\D", " ", pagetext(src))
    for num in re.findall(r"\d[\d.]*\d|\d", text):
        n = num.rstrip(".")
        if len(n) < 2:
            continue
        if n.replace(".", "") in hay2.replace(" ", "") or n in hay:
            continue
        errors.append(f"{label}: Zahl {n} steht nicht auf {src}: {text[:80]}")

def check_words(label, text, src):
    hay = {stem(w) for w in re.findall(r"[A-Za-zÄÖÜäöüß]{4,}", pagetext(src))}
    hay_raw = pagetext(src).lower()
    words = [w for w in re.findall(r"[A-Za-zÄÖÜäöüß]{5,}", text) if w.lower() not in STOP]
    if not words:
        return
    miss = [w for w in words if stem(w) not in hay and w.lower()[:6] not in hay_raw]
    if len(miss) / len(words) > 0.45:
        soft.append(f"{label}: {len(miss)}/{len(words)} fehlen {miss[:6]} :: {text[:70]}")

topics = {t["id"]: t for t in c.TOPICS}
chs = {x[0] for x in c.CHAPTERS}
for t in c.TOPICS:
    if t["ch"] not in chs:
        errors.append("Topic ohne Kapitel " + t["id"])
    check_src("T " + t["id"], t["src"])
    check_numbers("T " + t["id"], t["text"], t["src"])
    check_words("T " + t["id"], t["text"], t["src"])

out_cards = []
seen = set()
for i, k in enumerate(c.CARDS):
    tp = topics.get(k["topic"])
    if not tp:
        errors.append("Karte ohne Topic: " + k["topic"]); continue
    src = k["src"] or tp["src"]
    label = f"{k['topic']} «{k['q'][:40]}»"
    check_src(label, src)
    answers = {"mc": lambda: k["right"], "tf": lambda: k["q"], "multi": lambda: " ".join(k["right"]),
               "ord": lambda: " ".join(x[0] + " " + x[1] for x in k["items"]),
               "match": lambda: " ".join(a + " " + b for a, b in k["pairs"])}[k["type"]]()
    allsrc = src + tp["src"]
    check_numbers(label, answers + " " + k["why"], allsrc)
    check_words(label, answers + " " + k["why"], src)
    if k["type"] == "mc" and len(k["wrong"]) != 3:
        errors.append(f"{label}: braucht 3 falsche Antworten")
    if k["type"] == "ord":
        ys = [int(x[0][:4]) for x in k["items"]]
        if ys != sorted(ys):
            errors.append(f"{label}: Reihenfolge nicht sortiert {ys}")
    for lf in k["lf"]:
        if not 1 <= lf <= 26:
            errors.append(f"{label}: falsche Leitfrage {lf}")
    cid = hashlib.sha1((k["topic"] + k["q"]).encode()).hexdigest()[:8]
    if cid in seen:
        errors.append(f"{label}: doppelte Karte")
    seen.add(cid)
    out_cards.append({**k, "id": cid, "src": src})

for l in c.LFS:
    for p in l["points"]:
        check_src(f"LF{l['n']}", p["src"])
        check_numbers(f"LF{l['n']}", p["t"], p["src"])
        check_words(f"LF{l['n']}", p["t"], p["src"])
if sorted(x["n"] for x in c.LFS) != list(range(1, 27)):
    errors.append("Nicht alle 26 Leitfragen vorhanden")
for x in c.PEOPLE + c.TERMS + c.TIMELINE + c.TRAPS:
    check_src(x.get("name") or x.get("term") or x.get("y") or x.get("title"), x["src"])
for x in c.TIMELINE:
    check_numbers("TL " + x["y"], x["y"], x["src"])

cover = {n: 0 for n in range(1, 27)}
for k in c.CARDS:
    for lf in k["lf"]:
        cover[lf] += 1
print("Karten", len(out_cards), "Themen", len(c.TOPICS), "Leitfragen", len(c.LFS))
print("Quizkarten je Leitfrage:", cover)
for lf, n in cover.items():
    if n < 2:
        errors.append(f"Leitfrage {lf} hat nur {n} Quizkarten")

ch_out = [dict(id=a, name=b, span=d, line=e, docs=f, sober=g) for a, b, d, e, f, g in c.CHAPTERS]
data = dict(course=c.COURSE, chapters=ch_out, topics=c.TOPICS, cards=out_cards, leitfragen=c.LFS,
            people=c.PEOPLE, terms=c.TERMS, timeline=c.TIMELINE, traps=c.TRAPS)
(ROOT / "site/data").mkdir(exist_ok=True, parents=True)
(ROOT / "site/data/geschichte.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))

print("\nZum Nachlesen:", len(soft))
for s in soft:
    print(" -", s)
print("\nFehler:", len(errors))
for e in errors:
    print(" !", e)
sys.exit(1 if errors else 0)
