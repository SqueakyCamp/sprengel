"""Bausteine fuer die Kursdateien. Jede Aussage traegt Verweise ("doc", seite); ("@key", 0) ist eine Web-Zusatzquelle aus docs.WEB."""

class Course:
    def __init__(self, id, **meta):
        self.meta = dict(id=id, **meta)
        self.chapters, self.topics, self.cards, self.opens = [], [], [], []
        self.terms, self.traps, self.people, self.timeline = [], [], [], []

    def CH(self, id, name, span, line, docs, pending=False):
        self.chapters.append(dict(id=id, name=name, span=span, line=line, docs=docs, sober=False, book=None, pending=pending))

    def T(self, id, ch, title, text, src):
        self.topics.append(dict(id=id, ch=ch, title=title, text=text, src=src))

    def _add(self, type, topic, lf, why, src, **kw):
        self.cards.append(dict(type=type, topic=topic, lf=lf, why=why, src=src or [], **kw))

    def MC(self, topic, lf, q, right, wrong, why, src=None):
        self._add("mc", topic, lf, why, src, q=q, right=right, wrong=wrong)

    def TF(self, topic, lf, stmt, val, why, src=None):
        self._add("tf", topic, lf, why, src, q=stmt, val=val)

    def ORD(self, topic, lf, q, items, why, src=None, hint="Tippe in der richtigen Reihenfolge."):
        """items: Texte in der richtigen Reihenfolge."""
        self._add("ord", topic, lf, why, src, q=q, items=[[str(i + 1), t] for i, t in enumerate(items)], hint=hint, free=True)

    def MATCH(self, topic, lf, q, pairs, why, src=None):
        self._add("match", topic, lf, why, src, q=q, pairs=pairs)

    def MULTI(self, topic, lf, q, right, wrong, why, src=None):
        self._add("multi", topic, lf, why, src, q=q, right=right, wrong=wrong)

    def BUCKET(self, topic, lf, q, buckets, items, why, src=None):
        """items: (Text, Index des richtigen Fachs)."""
        self._add("bucket", topic, lf, why, src, q=q, buckets=buckets, items=[list(x) for x in items])

    def CHAIN(self, topic, lf, q, intro, steps, why, src=None):
        """Kleine Fallkette: mehrere Fragen hintereinander, mit Sofort-Rueckmeldung."""
        s = [dict(q=a, right=b, wrong=c, why=d, src=e) for a, b, c, d, e in steps]
        all_src = list(src or [])
        for x in s:
            all_src += [tuple(y) for y in x["src"] if tuple(y) not in all_src]
        self._add("chain", topic, lf, why, all_src, q=q, intro=intro, steps=s)

    def CALC(self, topic, lf, q, expr, unit, steps, why, src=None, tol=0.5):
        self._add("calc", topic, lf, why, src, q=q, answer=round(eval(expr), 2), unit=unit, steps=steps, tol=tol)

    def OPEN(self, n, group, q, gist, points, ch, note=None, deep=None):
        self.opens.append(dict(n=n, group=group, q=q, gist=gist, points=[dict(t=t, src=s) for t, s in points], ch=ch, note=note,
                               **({"deep": [dict(t=t, src=s) for t, s in deep]} if deep else {})))

    def TERM(self, term, text, src):
        self.terms.append(dict(term=term, text=text, src=src))

    def TRAP(self, title, text, src):
        self.traps.append(dict(title=title, text=text, src=src))

    def TL(self, y, t, src):
        self.timeline.append(dict(y=y, t=t, src=src))

    def PERSON(self, name, dates, text, src):
        self.people.append(dict(name=name, dates=dates, text=text, src=src))
