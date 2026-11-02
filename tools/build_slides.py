#!/usr/bin/env python3
"""Rendert die Folien aus source/ und legt sie verschluesselt nach site/slides/.
Die Original-PDFs sind Material der Lehrveranstaltung und landen nicht im Klartext im oeffentlichen Repo."""
import json, os, re, secrets, sys, unicodedata
from pathlib import Path
import pymupdf
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ROOT = Path(__file__).resolve().parent.parent
DOCS = {  # id -> (Datei, Anzeigename)
    "e":  ("Geschichte der Sozialen Arbeit Einführung WS 26&27.pdf", "Einführung"),
    "a1": ("Armenfürsorge I.pdf", "Armenfürsorge I"),
    "a2": ("Armenfürsorge II.pdf", "Armenfürsorge II"),
    "eb": ("Vom sozialen Ehrenamt zum Frauenberuf.pdf", "Vom Ehrenamt zum Frauenberuf"),
    "rw": ("Fürsorge im Roten Wien ohne Abb-1.pdf", "Fürsorge im Roten Wien"),
    "t":  ("Fürsorge in Totalitären Regimen.pdf", "Fürsorge in totalitären Regimen"),
    "n":  ("Fürsorge in der Nachkriegszeit& Wirtschaftswunder.pdf", "Nachkriegszeit & Wirtschaftswunder"),
    "zs": ("Von der Fürsorge zur Sozialarbeit.pdf", "Von der Fürsorge zur Sozialarbeit"),
    "z":  ("Zeittafel.Sozialarbeit.pdf", "Zeittafel"),
    "lf": ("Leitfragen & Lernziele_Prüfung.pdf", "Leitfragen & Lernziele"),
    "j":  ("100-jahre-jugendamt.pdf", "Zusatztext: 100 Jahre Jugendamt"),
}
WIDTH = 1280

def clean(t):
    """Fuegt die zerhackten Zeilen der Folien zu lesbaren Absaetzen zusammen."""
    out = []
    for line in t.splitlines():
        s = line.strip()
        if not s:
            continue
        if re.fullmatch(r"\d{1,2}", s):
            continue
        if s[0] in "•●" or not out:
            out.append(s.lstrip("•● ").strip() if s[0] in "•●" else s)
            if s[0] in "•●":
                out[-1] = "• " + out[-1]
        else:
            out[-1] += " " + s
    return out

def main():
    pw = (ROOT / ".slide-passphrase").read_text().strip().encode()
    salt_file = ROOT / "site/slides/salt.txt"
    if salt_file.exists():
        salt = bytes.fromhex(salt_file.read_text().strip())
    else:
        salt = secrets.token_bytes(16)
        salt_file.write_text(salt.hex())
    iters = 200_000
    key = PBKDF2HMAC(hashes.SHA256(), 32, salt, iters).derive(pw)
    a = AESGCM(key)
    def seal(b):
        iv = secrets.token_bytes(12)
        return iv + a.encrypt(iv, b, None)
    if not sys.argv[1:]:
        (ROOT / "site/slides/check.bin").write_bytes(seal(b"sprengel-ok"))
    # Mit Dokument-IDs als Argument nur diese neu bauen, damit sich die uebrigen Dateien nicht aendern.
    only = set(sys.argv[1:])
    mf = ROOT / "site/slides/manifest.json"
    manifest = json.loads(mf.read_text()) if only and mf.exists() else {"iters": iters, "docs": {}}
    total = 0
    for did, (fn, name) in DOCS.items():
        if only and did not in only:
            continue
        pdf = pymupdf.open(ROOT / "source" / fn)
        out = ROOT / "site/slides" / did
        out.mkdir(parents=True, exist_ok=True)
        texts = {}
        blank = []
        for i, page in enumerate(pdf):
            n = i + 1
            m = WIDTH / page.rect.width
            if page.rect.height > page.rect.width:
                m = 1000 / page.rect.width
            pix = page.get_pixmap(matrix=pymupdf.Matrix(m, m), alpha=False)
            data = pix.tobytes("jpeg", jpg_quality=72)
            (out / f"{n:03d}.bin").write_bytes(seal(data))
            total += len(data)
            texts[n] = clean(page.get_text())
            s = pix.samples
            if min(s[::997]) > 245:
                blank.append(n)
        (out / "text.bin").write_bytes(seal(json.dumps(texts, ensure_ascii=False).encode()))
        manifest["docs"][did] = {"name": name, "pages": len(pdf), "blank": blank}
        print(did, name, len(pdf), "blank:", blank, flush=True)
    (ROOT / "site/slides/manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1))
    print("MB", round(total / 1e6, 1))

main()
