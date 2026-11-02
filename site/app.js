"use strict";
/* Sprengel: mobiles Lernzentrum. Keine Bibliotheken, Fortschritt liegt im localStorage des Geraets. */

const STORE = "sprengel.v1";
const DAILY_GOAL = 60;
const BOX_DAYS = [0, 1, 2, 4, 8, 16];
const LEVELS = [
  [0, "Ehrenamt"], [150, "Berufspflege"], [400, "Fachkurs"], [800, "Fürsorgeschule"], [1400, "Sprengeldienst"],
  [2200, "Case Work"], [3200, "Sozialakademie"], [4500, "FH-Diplom"], [6500, "Master"],
];
const BADGES = [
  ["first", "Erste Fahrt", "Eine Runde abgeschlossen", s => s.runs >= 1],
  ["streak3", "Drei Tage", "3 Tage in Folge gelernt", s => s.bestStreak >= 3],
  ["streak7", "Eine Woche", "7 Tage in Folge gelernt", s => s.bestStreak >= 7],
  ["combo10", "Zehn am Stück", "10 richtige Antworten in Folge", s => s.bestCombo >= 10],
  ["open5", "Frei formuliert", "5 Leitfragen frei beantwortet", s => s.opens >= 5],
  ["exam", "Probe bestanden", "Eine Probeprüfung abgeschlossen", s => s.exams >= 1],
  ["stamp5", "Fünf Stempel", "5 Leitfragen gestempelt", (s, n) => n >= 5],
  ["stamp26", "Volle Karte", "Alle 26 Leitfragen gestempelt", (s, n) => n >= 26],
];

let D, M; // Kursdaten, Folienmanifest
const $ = (s, r = document) => r.querySelector(s);
const main = $("#main"), viewerEl = $("#viewer"), navEl = $("#nav");
const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const shuffle = a => { a = [...a]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const dayKey = (d = new Date()) => { const z = new Date(d.getTime() - d.getTimezoneOffset() * 6e4); return z.toISOString().slice(0, 10); };
const dayDiff = (a, b) => Math.round((new Date(b + "T12:00") - new Date(a + "T12:00")) / 864e5);

/* ---------- Zustand ---------- */
const blank = () => ({ xp: 0, cards: {}, lfOpen: {}, days: {}, runs: 0, opens: 0, exams: 0, bestCombo: 0, bestStreak: 0, exam: null, key: null, examLast: null, offline: false });
let S = load();
function load() { try { return { ...blank(), ...JSON.parse(localStorage.getItem(STORE) || "{}") }; } catch { return blank(); } }
function save() { try { localStorage.setItem(STORE, JSON.stringify(S)); } catch {} }

function streak() {
  let d = dayKey(), n = 0;
  if (!S.days[d]) { const y = new Date(); y.setDate(y.getDate() - 1); d = dayKey(y); }
  while (S.days[d]) { n++; const x = new Date(d + "T12:00"); x.setDate(x.getDate() - 1); d = dayKey(x); }
  return n;
}
function addXp(n) { S.xp += n; const d = dayKey(); S.days[d] = (S.days[d] || 0) + n; S.bestStreak = Math.max(S.bestStreak, streak()); }
function level(xp = S.xp) {
  let i = 0; while (i + 1 < LEVELS.length && xp >= LEVELS[i + 1][0]) i++;
  const next = LEVELS[i + 1];
  return { name: LEVELS[i][1], i, next, pct: next ? (xp - LEVELS[i][0]) / (next[0] - LEVELS[i][0]) : 1 };
}
function daysToExam() {
  const e = D.course.exams.find(x => x.id === S.exam);
  return e ? { ...e, left: dayDiff(dayKey(), e.date) } : null;
}
function intervalDays(box) {
  const ex = daysToExam(); let d = BOX_DAYS[box];
  if (ex && ex.left > 0) d = Math.min(d, Math.max(1, Math.ceil(ex.left / 3)));
  return d;
}
function grade(id, ok) {
  const c = S.cards[id] || { box: 0, seen: 0, wrong: 0 };
  c.seen++;
  if (ok) c.box = Math.min(c.box + 1, 5); else { c.box = 0; c.wrong++; }
  c.due = Date.now() + intervalDays(c.box) * 864e5 - 36e5;
  S.cards[id] = c;
}

/* ---------- Fortschritt ---------- */
const topicOf = id => D.topics.find(t => t.id === id);
const chapterOf = id => D.chapters.find(c => c.id === id);
const cardsIn = ch => D.cards.filter(k => topicOf(k.topic).ch === ch);
const learned = k => (S.cards[k.id]?.box || 0) >= 2;
function chapterPct(ch) { const c = cardsIn(ch); return c.filter(learned).length / c.length; }
function lfScore(n) {
  const cards = D.cards.filter(k => k.lf.includes(n));
  const quiz = cards.length ? cards.filter(learned).length / cards.length : 0;
  const open = S.lfOpen[n]?.best || 0;
  return Math.round((quiz * .4 + open * .6) * 100);
}
const stamped = n => lfScore(n) >= 80;
const stampCount = () => D.leitfragen.filter(l => stamped(l.n)).length;

/* ---------- Folien-Entschluesselung ---------- */
const b64 = { to: b => btoa(String.fromCharCode(...new Uint8Array(b))), from: s => Uint8Array.from(atob(s), c => c.charCodeAt(0)) };
let cryptoKey = null;
async function deriveKey(pass) {
  const salt = (await (await fetch("slides/salt.txt")).text()).trim();
  const raw = await crypto.subtle.importKey("raw", new TextEncoder().encode(pass.trim()), "PBKDF2", false, ["deriveBits"]);
  const bits = await crypto.subtle.deriveBits({ name: "PBKDF2", hash: "SHA-256", iterations: M.iters, salt: Uint8Array.from(salt.match(/../g), h => parseInt(h, 16)) }, raw, 256);
  return bits;
}
async function importBits(bits) { return crypto.subtle.importKey("raw", bits, "AES-GCM", false, ["decrypt"]); }
async function openBin(url, key = cryptoKey) {
  const r = await fetch(url);
  if (!r.ok) throw new Error("fetch");
  const buf = await r.arrayBuffer();
  return crypto.subtle.decrypt({ name: "AES-GCM", iv: buf.slice(0, 12) }, key, buf.slice(12));
}
async function unlock(pass) {
  const bits = await deriveKey(pass);
  const key = await importBits(bits);
  await openBin("slides/check.bin", key); // wirft bei falschem Code
  cryptoKey = key; S.key = b64.to(bits); save();
}
async function restoreKey() { if (S.key && !cryptoKey) { try { cryptoKey = await importBits(b64.from(S.key)); } catch { S.key = null; } } }

/* ---------- Bausteine ---------- */
const ICONS = {
  home: '<path d="M6 3v18M6 7h12M6 17h12"/><circle cx="6" cy="7" r="2"/><circle cx="6" cy="17" r="2"/>',
  lf: '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M8 9l2 2 4-4M8 16h8"/>',
  stoff: '<path d="M4 5a2 2 0 0 1 2-2h13v18H6a2 2 0 0 1-2-2zM8 8h7M8 12h7"/>',
  me: '<circle cx="12" cy="8" r="4"/><path d="M4 21c1-5 4-7 8-7s7 2 8 7"/>',
};
const docName = d => M.docs[d]?.name || d;
function chip(src) {
  return `<button class="chip" data-slide="${src[0]}:${src[1]}"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="13" rx="1"/><path d="M12 18v3"/></svg>${esc(docName(src[0]))}, S. ${src[1]}</button>`;
}
const uniq = src => { const seen = new Set(); return src.filter(s => { const k = s.join(":"); if (seen.has(k)) return false; seen.add(k); return true; }); };
const chips = src => `<div class="chips">${uniq(src).map(chip).join("")}</div>`;
function context(t, shown = []) {
  const ch = chapterOf(t.ch), have = new Set(shown.map(x => x.join(":")));
  const rest = uniq(t.src).filter(x => !have.has(x.join(":")));
  return `<section class="context"><h3>${esc(t.title)}</h3><div class="era">${esc(ch.name)}, ${esc(ch.span)}</div><p>${esc(t.text)}</p>${rest.length ? chips(rest) : ""}</section>`;
}
const lfRefs = list => list.length ? `<div class="lfrefs">Gehört zu Leitfrage ${list.join(", ")}</div>` : "";

function renderNav(active) {
  const item = (hash, ic, label, key) => `<button data-go="${hash}" ${active === key ? 'aria-current="page"' : ""}><svg viewBox="0 0 24 24" aria-hidden="true">${ICONS[ic]}</svg>${label}</button>`;
  navEl.innerHTML = `<div class="brand">Sprengel</div>` + item("#/", "home", "Linie", "home") + item("#/lf", "lf", "Leitfragen", "lf") + item("#/stoff", "stoff", "Stoff", "stoff") + item("#/ich", "me", "Ich", "me");
}

/* ---------- Startseite ---------- */
function viewHome() {
  const lv = level(), st = streak(), today = S.days[dayKey()] || 0, ex = daysToExam();
  const pcts = D.chapters.map(c => chapterPct(c.id));
  const firstOpen = D.chapters.findIndex((c, i) => pcts[i] < .8);
  const exText = ex ? (ex.left > 1 ? `Noch ${ex.left} Tage bis zur Prüfung` : ex.left === 1 ? "Morgen ist Prüfung" : ex.left === 0 ? "Heute ist Prüfung. Viel Erfolg!" : "Die Prüfung ist vorbei") : "";
  const wrong = wrongCards().length;
  main.innerHTML = `
  <header class="hero"><div class="hero-in">
    <div class="hero-top"><h1>Sprengel</h1><div class="level">${esc(lv.name)}<br>${S.xp} XP</div></div>
    <div class="stats">
      <div class="stat"><b>${st}</b><span>${st === 1 ? "Tag" : "Tage"} in Folge</span></div>
      <div class="stat"><b>${stampCount()}/26</b><span>Stempel</span></div>
      <div class="goal"><div class="bar"><i style="width:${Math.min(100, today / DAILY_GOAL * 100)}%"></i></div><span>Heute ${Math.min(today, DAILY_GOAL)} von ${DAILY_GOAL} XP</span></div>
    </div>
    <div class="starts">
      <button class="start" data-run="5"><b>5 Min</b><span>8 Karten</span></button>
      <button class="start alt" data-run="10"><b>10 Min</b><span>15 Karten</span></button>
    </div>
    <div class="quick">
      ${wrong ? `<button data-run="wrong">Fehler üben (${wrong})</button>` : ""}
      <button data-run="exam">Probeprüfung mit 7 Fragen</button>
    </div>
    ${ex ? `<p class="small" style="color:var(--on-petrol-soft);margin-top:8px">${esc(exText)}</p>` : `
    <div class="exam-pick"><b>Wann schreibst du die Prüfung?</b><div class="row">
      ${D.course.exams.map(e => `<button class="btn small" data-exam="${e.id}">${esc(e.label)}, ${e.date.slice(8)}.${e.date.slice(5, 7)}.</button>`).join("")}
    </div></div>`}
  </div></header>
  <div class="pad">
    <h2 class="line-title">${esc(D.course.name)}</h2>
    <ol class="line">
      ${D.chapters.map((c, i) => {
        const p = pcts[i];
        return `<li class="stop ${p >= .8 ? "done" : p > 0 ? "begun" : ""}">
          <span class="fill" style="height:${i < firstOpen || firstOpen < 0 ? "100%" : i === firstOpen ? Math.round(p * 100) + "%" : "0"}"></span><span class="dot"></span>
          <button data-go="#/stoff/${c.id}"><h3>${esc(c.name)}</h3><div class="span">${esc(c.span)}${p > 0 ? `, ${Math.round(p * 100)} % gelernt` : ""}</div><div class="sub">${esc(c.line)}</div></button>
        </li>`;
      }).join("")}
    </ol>
  </div>`;
}

/* ---------- Fahrt (Lernrunde) ---------- */
let R = null;
const isDue = k => { const c = S.cards[k.id]; return c && c.due <= Date.now(); };
const isNew = k => !S.cards[k.id];
const wrongCards = () => D.cards.filter(k => S.cards[k.id]?.seen && S.cards[k.id].box === 0);

function pick(pool, n) {
  const due = shuffle(pool.filter(isDue)).sort((a, b) => S.cards[a.id].box - S.cards[b.id].box);
  const fresh = shuffle(pool.filter(isNew));
  // Fokus: vier von fuenf neuen Karten gehoeren zu einer Leitfrage
  const withLf = fresh.filter(k => k.lf.length), noLf = fresh.filter(k => !k.lf.length);
  const mixed = []; let i = 0;
  while (withLf.length || noLf.length) { mixed.push(((i++ % 5 === 4 && noLf.length) || !withLf.length) ? noLf.shift() : withLf.shift()); }
  const later = shuffle(pool.filter(k => !isDue(k) && !isNew(k))).sort((a, b) => S.cards[a.id].box - S.cards[b.id].box);
  const dueShare = due.slice(0, Math.ceil(n * .6));
  const out = [...dueShare, ...mixed.slice(0, n - dueShare.length)];
  for (const k of [...due.slice(dueShare.length), ...later]) { if (out.length >= n) break; if (!out.includes(k)) out.push(k); }
  return spread(shuffle(out.slice(0, n)));
}
function spread(list) { // gleiche Themen nicht direkt hintereinander
  const out = [], rest = [...list];
  while (rest.length) {
    const prev = out[out.length - 1];
    const i = rest.findIndex(k => !prev || k.topic !== prev.topic);
    out.push(rest.splice(i < 0 ? 0 : i, 1)[0]);
  }
  return out;
}
function pickLf(n, focus) {
  const scored = shuffle(D.leitfragen).filter(l => !focus || l.ch === focus).sort((a, b) => lfScore(a.n) - lfScore(b.n));
  return scored.slice(0, n).map(l => ({ type: "open", id: "lf" + l.n, lf: [l.n], leit: l }));
}

function startRun(kind, opts = {}) {
  let items = [], title = "";
  if (kind === "5" || kind === "10") {
    const n = kind === "5" ? 7 : 13, open = kind === "5" ? 1 : 2;
    items = pick(D.cards, n);
    items.splice(Math.floor(items.length / 2), 0, ...pickLf(open));
    title = kind === "5" ? "Kurze Fahrt" : "Lange Fahrt";
  } else if (kind === "wrong") {
    items = spread(shuffle(wrongCards()).slice(0, 12)); title = "Fehler üben";
  } else if (kind === "chapter") {
    const ch = chapterOf(opts.ch);
    items = pick(cardsIn(opts.ch), 10); title = ch.name;
    items.splice(5, 0, ...pickLf(1, opts.ch));
  } else if (kind === "lf") {
    const lf = D.leitfragen.find(l => l.n === opts.n);
    items = pick(D.cards.filter(k => k.lf.includes(opts.n)), 6);
    items.push({ type: "open", id: "lf" + lf.n, lf: [lf.n], leit: lf }); title = "Leitfrage " + lf.n;
  } else if (kind === "open") {
    const lf = D.leitfragen.find(l => l.n === opts.n);
    items = [{ type: "open", id: "lf" + lf.n, lf: [lf.n], leit: lf }]; title = "Leitfrage " + lf.n;
  } else if (kind === "exam") {
    items = shuffle(D.leitfragen).slice(0, 7).map(l => ({ type: "open", id: "lf" + l.n, lf: [l.n], leit: l, exam: true }));
    title = "Probeprüfung";
  }
  if (!items.length) { location.hash = "#/"; return; }
  R = { kind, title, items, i: 0, xp: 0, right: 0, total: 0, combo: 0, bestCombo: 0, retry: new Set(), missed: [], examPts: [0, 0], stampsBefore: stampCount(), start: Date.now(), answered: false, state: {} };
  document.body.classList.add("running");
    history.pushState({ run: 1 }, "", "#/fahrt");
  renderCard();
}
function endRun() { R = null; document.body.classList.remove("running"); }

function runHeader(item) {
  const sober = isSober(item);
  const n = R.items.length;
  return `<div class="run-top"><button class="run-x" data-quit aria-label="Runde beenden">×</button>
    <div class="track" aria-label="Karte ${R.i + 1} von ${n}"><i style="width:${R.i / n * 100}%"></i>${n <= 18 ? R.items.map((_, i) => `<b class="${i < R.i ? "on" : ""}"></b>`).join("") : ""}</div>
    <div class="combo">${!sober && R.combo >= 3 ? `${R.combo}×` : ""}</div></div>`;
}
const isSober = item => item.topic ? chapterOf(topicOf(item.topic).ch).sober : (item.leit && chapterOf(item.leit.ch).sober);

function renderCard() {
  const k = R.items[R.i];
  R.answered = false; R.state = {};
  window.scrollTo(0, 0);
  if (k.type === "open") return renderOpen(k);
  const t = topicOf(k.topic);
  const head = runHeader(k) + `<div class="tag">${esc(t.title)}</div>`;
  if (k.type === "mc") {
    R.state.opts = shuffle([k.right, ...k.wrong]);
    main.innerHTML = `<div class="run">${head}<p class="q">${esc(k.q)}</p><div class="grow"></div>
      <div class="answers">${R.state.opts.map((o, i) => `<button class="opt" data-mc="${i}">${esc(o)}</button>`).join("")}</div></div>`;
  } else if (k.type === "tf") {
    main.innerHTML = `<div class="run">${head}<p class="tag" style="margin-top:4px">Stimmt das?</p><p class="q">${esc(k.q)}</p><div class="grow"></div>
      <div class="tf"><button class="opt" data-tf="1">Stimmt</button><button class="opt" data-tf="0">Falsch</button></div></div>`;
  } else if (k.type === "multi") {
    R.state.opts = shuffle([...k.right, ...k.wrong]); R.state.sel = new Set();
    main.innerHTML = `<div class="run">${head}<p class="q">${esc(k.q)}</p><p class="tag" style="margin-top:4px">Mehrere Antworten möglich</p><div class="grow"></div>
      <div class="answers">${R.state.opts.map((o, i) => `<button class="opt" aria-pressed="false" data-multi="${i}">${esc(o)}</button>`).join("")}</div>
      <div style="margin-top:12px"><button class="btn" data-check-multi disabled>Antwort prüfen</button></div></div>`;
  } else if (k.type === "ord") {
    R.state.pool = shuffle(k.items.map((x, i) => i)); R.state.seq = [];
    renderOrd(k, head);
  } else if (k.type === "match") {
    R.state.left = shuffle(k.pairs.map((_, i) => i)); R.state.right = shuffle(k.pairs.map((_, i) => i));
    R.state.done = new Set(); R.state.errors = 0; R.state.sel = null;
    renderMatch(k, head);
  }
}
function renderOrd(k, head = runHeader(k) + `<div class="tag">${esc(topicOf(k.topic).title)}</div>`) {
  const s = R.state;
  main.innerHTML = `<div class="run">${head}<p class="q">${esc(k.q)}</p><p class="tag" style="margin-top:4px">Tippe vom frühesten zum spätesten Ereignis.</p>
    <div class="seq" style="margin-top:12px">${k.items.map((_, i) => { const it = s.seq[i]; return `<button class="slot ${it !== undefined ? "full" : ""}" ${it !== undefined ? `data-ord-out="${i}"` : "disabled"}><span class="n">${i + 1}</span><span>${it !== undefined ? esc(k.items[it][1]) : ""}</span></button>`; }).join("")}</div>
    <div class="grow"></div><div class="pool">${s.pool.filter(i => !s.seq.includes(i)).map(i => `<button class="opt" data-ord="${i}">${esc(k.items[i][1])}</button>`).join("")}</div>
    <div style="margin-top:12px"><button class="btn" data-check-ord ${s.seq.length < k.items.length ? "disabled" : ""}>Reihenfolge prüfen</button></div></div>`;
}
function renderMatch(k, head = runHeader(k) + `<div class="tag">${esc(topicOf(k.topic).title)}</div>`) {
  const s = R.state;
  main.innerHTML = `<div class="run">${head}<p class="q">${esc(k.q)}</p><div class="grow"></div>
    <div class="pairs"><div class="col">${s.left.map(i => `<button class="pair ${s.done.has(i) ? "ok" : ""} ${s.sel === i ? "sel" : ""}" ${s.done.has(i) ? "disabled" : ""} data-ml="${i}">${esc(k.pairs[i][0])}</button>`).join("")}</div>
    <div class="col">${s.right.map(i => `<button class="pair ${s.done.has(i) ? "ok" : ""}" ${s.done.has(i) ? "disabled" : ""} data-mr="${i}">${esc(k.pairs[i][1])}</button>`).join("")}</div></div></div>`;
}

function score(k, ok) {
  const sober = isSober(k);
  grade(k.id, ok); R.total++;
  let gain = ok ? 10 + (sober ? 0 : Math.min(R.combo, 5)) : 2;
  if (ok) { R.right++; R.combo++; R.bestCombo = Math.max(R.bestCombo, R.combo); S.bestCombo = Math.max(S.bestCombo, R.combo); }
  else {
    R.combo = 0; R.missed.push(k);
    if (!R.retry.has(k.id) && R.kind !== "exam") { R.retry.add(k.id); R.items.push(k); } // am Ende nochmal
  }
  R.xp += gain; addXp(gain); save();
  if (navigator.vibrate) navigator.vibrate(ok ? 12 : [25, 40, 25]);
  return gain;
}
function feedback(k, ok, gain, givenHtml) {
  const t = topicOf(k.topic), sober = isSober(k);
  R.answered = true;
  const res = sober
    ? `<div class="result"><div class="plain-result">${ok ? "Richtig." : "Nicht richtig."}</div></div>`
    : `<div class="result anim"><div class="stamp ${ok ? "good" : "bad"}">${ok ? "Richtig" : "Nicht ganz"}</div><div class="plus">+${gain} XP</div></div>`;
  main.innerHTML = `<div class="run">${runHeader(k)}${res}
    <p class="q small">${esc(k.q)}</p><div class="given">${givenHtml}</div>
    <p class="why">${esc(k.why)}</p>
    ${chips(k.src)}
    ${context(t, k.src)}
    ${lfRefs(k.lf)}
    <div class="sticky"><button class="btn" data-next>${R.i + 1 < R.items.length ? "Weiter" : "Ankommen"}</button></div></div>`;
  $(".btn[data-next]").focus({ preventScroll: true });
}
function renderOpen(k) {
  const l = k.leit;
  const prev = R.state.text || "";
  main.innerHTML = `<div class="run">${runHeader(k)}<div class="tag">${k.exam ? `Probeprüfung, Frage ${R.i + 1} von ${R.items.length}` : `Leitfrage ${l.n} frei beantworten`}</div>
    <p class="q">${esc(l.q)}</p>
    <textarea id="mine" placeholder="${k.exam ? "Schreib deine Antwort wie in der Prüfung." : "Stichworte tippen oder im Kopf antworten."}">${esc(prev)}</textarea>
    <div class="grow"></div><div style="margin-top:12px"><button class="btn" data-reveal>Antwort aufdecken</button></div></div>`;
}
function revealOpen(k) {
  const l = k.leit, mine = $("#mine")?.value.trim();
  R.state.mine = mine;
  main.innerHTML = `<div class="run">${runHeader(k)}<div class="tag">Leitfrage ${l.n}</div><p class="q small">${esc(l.q)}</p>
    ${mine ? `<div class="mine">${esc(mine)}</div>` : ""}
    <p class="gist">${esc(l.gist)}</p>
    ${l.note ? `<div class="note">${esc(l.note)}</div>` : ""}
    <p class="tag">Hake an, was du selbst genannt hättest.</p>
    <ul class="points">${l.points.map((p, i) => `<li class="point"><label><input type="checkbox" data-pt="${i}"><span>${esc(p.t)}</span></label>${chips(p.src)}</li>`).join("")}</ul>
    <div class="sticky"><button class="btn" data-open-done>Selbsteinschätzung speichern</button></div></div>`;
  window.scrollTo(0, 0);
}
function finishOpen(k) {
  const l = k.leit, boxes = [...main.querySelectorAll("[data-pt]")];
  const hit = boxes.filter(b => b.checked).length, ratio = hit / boxes.length;
  const rec = S.lfOpen[l.n] || { best: 0, tries: 0 };
  rec.tries++; rec.best = Math.max(rec.best, ratio); rec.last = ratio; S.lfOpen[l.n] = rec;
  S.opens++;
  const gain = Math.round(10 + ratio * 25);
  R.xp += gain; addXp(gain); R.total++; if (ratio >= .6) R.right++;
  if (ratio < .6) R.missed.push(k);
  if (k.exam) { R.examPts[0] += ratio; R.examPts[1]++; }
  save();
  nextCard();
}
function nextCard() {
  R.i++;
  if (R.i < R.items.length) renderCard(); else renderArrive();
}

function renderArrive() {
  S.runs++;
  if (R.kind === "exam") S.exams++;
  save();
  const r = R, newStamps = stampCount() - r.stampsBefore, today = S.days[dayKey()] || 0;
  const missedTopics = [...new Map(r.missed.filter(k => k.topic).map(k => [k.topic, topicOf(k.topic)])).values()];
  const missedLf = r.missed.filter(k => k.leit).map(k => k.leit);
  const badge = BADGES.filter(b => b[3](S, stampCount()) && !S["b_" + b[0]]);
  badge.forEach(b => S["b_" + b[0]] = 1); save();
  const examLine = r.kind === "exam" && r.examPts[1] ? `<div><b>${Math.round(r.examPts[0] / r.examPts[1] * 100)} %</b><span>der Punkte genannt</span></div>` : "";
  endRun();
  history.replaceState(null, "", "#/angekommen");
  main.innerHTML = `<div class="pad arrive"><h1>${r.kind === "exam" ? "Probeprüfung fertig" : "Angekommen"}</h1>
    <div class="score">${examLine}<div><b>+${r.xp}</b><span>XP</span></div>${r.kind === "exam" ? "" : `<div><b>${r.right}/${r.total}</b><span>richtig</span></div>`}<div><b>${streak()}</b><span>Tage in Folge</span></div></div>
    ${today >= DAILY_GOAL && today - r.xp < DAILY_GOAL ? `<p style="margin-top:14px"><b>Tagesziel geschafft.</b></p>` : ""}
    ${newStamps > 0 ? `<p style="margin-top:14px"><b>${newStamps === 1 ? "Neuer Stempel" : newStamps + " neue Stempel"}</b> auf deiner Karte.</p>` : ""}
    ${badge.length ? `<div class="badges">${badge.map(b => `<div class="badge on"><b>${esc(b[1])}</b>${esc(b[2])}</div>`).join("")}</div>` : ""}
    ${missedTopics.length || missedLf.length ? `<section class="review"><h2>Noch einmal nachlesen</h2>
      <ul>${missedLf.map(l => `<li><button class="back" data-go="#/lf/${l.n}">Leitfrage ${l.n}</button></li>`).join("")}</ul>
      <div class="reading">${missedTopics.slice(0, 3).map(context).join("")}</div></section>` : ""}
    <div style="margin-top:22px"><button class="btn" data-run="5">Noch 5 Minuten</button><button class="btn ghost" data-go="#/">Zur Linie</button></div></div>`;
  renderNav("home");
  window.scrollTo(0, 0);
}

/* ---------- Leitfragen ---------- */
function viewLf() {
  main.innerHTML = `<div class="pad"><h1 class="h1">Stempelkarte</h1>
    <p class="lead">Die Prüfung stellt 7 Überblicksfragen aus diesem Themenkreis. Ein Stempel kommt, wenn du die Punkte frei nennen kannst und die Quizkarten sitzen.</p>
    <div class="stamps">${D.leitfragen.map(l => { const s = lfScore(l.n), d = stamped(l.n); return `<button class="field ${d ? "done" : ""}" data-go="#/lf/${l.n}" aria-label="Leitfrage ${l.n}, ${s} Prozent"><i style="height:${s}%"></i><span>${l.n}</span></button>`; }).join("")}</div>
    <div class="pcta"><button class="btn" data-run="exam">Probeprüfung starten</button></div>
    <ol class="lflist">${D.leitfragen.map(l => `<li class="${stamped(l.n) ? "done" : ""}"><button data-go="#/lf/${l.n}"><span class="n">${l.n}</span><span>${esc(l.q)}<small>${lfScore(l.n)} %</small></span></button></li>`).join("")}</ol></div>`;
}
function viewLfDetail(n) {
  const l = D.leitfragen.find(x => x.n === n);
  if (!l) return viewLf();
  const cards = D.cards.filter(k => k.lf.includes(n));
  const tids = [...new Set(cards.map(k => k.topic))].map(topicOf);
  const open = S.lfOpen[n];
  const seen = !!open || !!S["peek" + n];
  main.innerHTML = `<div class="pad"><button class="back" data-go="#/lf">Alle Leitfragen</button>
    <h1 class="h1" style="font-size:1.95rem;margin-top:6px">Leitfrage ${n}</h1>
    <p class="q" style="margin-top:8px">${esc(l.q)}</p>
    <p class="small" style="margin-top:6px">${lfScore(n)} % bis zum Stempel gesammelt${open ? `, zuletzt ${Math.round(open.last * 100)} % der Punkte genannt` : ""}</p>
    <div class="pcta"><button class="btn" data-open-run="${n}">Frei beantworten</button><button class="btn ghost" data-lf-run="${n}">${cards.length} Quizkarten üben</button></div>
    <section class="section"><h2>Musterantwort</h2>
      <details ${seen ? "open" : ""} data-peek="${n}"><summary style="cursor:pointer;min-height:36px">Antwort anzeigen</summary>
      <p class="gist">${esc(l.gist)}</p>
      ${l.note ? `<div class="note">${esc(l.note)}</div>` : ""}
      <ul class="points">${l.points.map(p => `<li class="point ro">${esc(p.t)}${chips(p.src)}</li>`).join("")}</ul></details>
    </section>
    <section class="section"><h2>Einordnung</h2><div class="reading">${tids.slice(0, 5).map(context).join("")}</div></section></div>`;
}

/* ---------- Stoff ---------- */
let stoffTab = "linie";
function viewStoff() {
  const tabs = [["linie", "Stationen"], ["zeit", "Zeitstrahl"], ["personen", "Personen"], ["begriffe", "Begriffe"], ["fallen", "Stolperfallen"], ["folien", "Folien"]];
  let body = "";
  if (stoffTab === "linie") body = `<ol class="line">${D.chapters.map(c => `<li class="stop"><span class="dot"></span><button data-go="#/stoff/${c.id}"><h3>${esc(c.name)}</h3><div class="span">${esc(c.span)}</div></button></li>`).join("")}</ol>`;
  if (stoffTab === "zeit") body = `<ol class="tl">${D.timeline.map(x => `<li><span class="y">${esc(x.y)}</span><span class="c">${esc(x.t)}${chips(x.src)}</span></li>`).join("")}</ol>`;
  if (stoffTab === "personen") body = D.people.map(p => `<div class="item"><h3>${esc(p.name)}</h3>${p.dates ? `<small>${esc(p.dates)}</small>` : ""}<p>${esc(p.text)}</p>${chips(p.src)}</div>`).join("");
  if (stoffTab === "begriffe") body = D.terms.map(p => `<div class="item"><h3>${esc(p.term)}</h3><p>${esc(p.text)}</p>${chips(p.src)}</div>`).join("");
  if (stoffTab === "fallen") body = `<p class="lead">Hier widersprechen sich Unterlagen oder etwas fehlt. Im Zweifel frag in der LV nach.</p>` + D.traps.map(p => `<div class="item"><h3>${esc(p.title)}</h3><p>${esc(p.text)}</p>${chips(p.src)}</div>`).join("");
  if (stoffTab === "folien") body = `<div class="docs">${Object.entries(M.docs).map(([id, d]) => `<button class="opt" data-slide="${id}:1">${esc(d.name)}<small>${d.pages} Seiten</small></button>`).join("")}</div>`;
  main.innerHTML = `<div class="pad"><h1 class="h1">Stoff</h1>
    <div class="tabs">${tabs.map(([k, v]) => `<button aria-pressed="${stoffTab === k}" data-stoff-tab="${k}">${v}</button>`).join("")}</div>${body}</div>`;
}
function viewChapter(id) {
  const c = chapterOf(id);
  if (!c) return viewStoff();
  const tp = D.topics.filter(t => t.ch === id);
  const lfs = D.leitfragen.filter(l => l.ch === id);
  main.innerHTML = `<div class="pad"><button class="back" data-go="#/stoff">Stoff</button>
    <h1 class="h1" style="margin-top:6px">${esc(c.name)}</h1><p class="lead">${esc(c.span)}, ${Math.round(chapterPct(id) * 100)} % gelernt</p>
    <div class="pcta"><button class="btn" data-ch-run="${id}">Diese Station üben</button><button class="btn ghost" data-slide="${c.docs[0]}:1">Foliensatz öffnen</button></div>
    ${lfs.length ? `<section class="section"><h2>Leitfragen dazu</h2><ol class="lflist" style="margin-top:0">${lfs.map(l => `<li class="${stamped(l.n) ? "done" : ""}"><button data-go="#/lf/${l.n}"><span class="n">${l.n}</span><span>${esc(l.q)}</span></button></li>`).join("")}</ol></section>` : ""}
    <section class="section"><h2>Zusammenfassung</h2><div class="reading">${tp.map(context).join("")}</div></section></div>`;
}

/* ---------- Ich ---------- */
function viewMe() {
  const lv = level(), n = stampCount();
  const seen = Object.keys(S.cards).length, ex = daysToExam();
  main.innerHTML = `<div class="pad"><h1 class="h1">${esc(lv.name)}</h1>
    <div class="levelbar"><div class="progress"><i style="width:${lv.pct * 100}%"></i></div>
    <p class="small" style="margin-top:4px">${S.xp} XP${lv.next ? `, nächste Stufe „${esc(lv.next[1])}“ bei ${lv.next[0]} XP` : ""}</p></div>
    <p class="small" style="margin-top:6px">${seen} von ${D.cards.length} Karten gesehen, längste Serie ${S.bestStreak} Tage</p>
    <section class="section"><h2>Abzeichen</h2><div class="badges">${BADGES.map(b => `<div class="badge ${b[3](S, n) ? "on" : ""}"><b>${esc(b[1])}</b>${esc(b[2])}</div>`).join("")}</div></section>
    <section class="section"><h2>Prüfungstermin</h2><div class="field-row">${D.course.exams.map(e => `<button class="btn small ${S.exam === e.id ? "" : "ghost"}" data-exam="${e.id}">${esc(e.label)}, ${e.date.slice(8)}.${e.date.slice(5, 7)}.</button>`).join("")}</div>
      <p class="small" style="margin-top:6px">Termine laut Einführungsfolie. Dazu kommt die schriftliche Reflexion mit mindestens 3500 Zeichen.</p></section>
    <section class="section"><h2>Folien</h2>
      ${S.key ? `<p>Folien sind freigeschaltet.</p>` : `<p>Folien sind gesperrt. Gib den Code ein, um sie zu öffnen.</p><form class="field-row" data-unlock-form><input type="text" name="code" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Zugangscode" aria-label="Zugangscode"><button class="btn small">Freischalten</button></form><p class="small" data-unlock-msg></p>`}
      ${S.key ? `<div class="field-row"><button class="btn small ghost" data-offline>${S.offline ? "Folien neu für offline laden" : "Alle Folien für offline laden (ca. 30 MB)"}</button></div><div id="dl" hidden><div class="progress"><i style="width:0"></i></div><p class="small" style="margin-top:4px"></p></div>` : ""}
    </section>
    <section class="section"><h2>Fortschritt übertragen</h2>
      <p class="small">Dein Fortschritt liegt nur auf diesem Gerät. Kopiere den Text zum Handy oder Laptop, um dort weiterzulernen.</p>
      <div class="field-row"><button class="btn small ghost" data-export>Sicherung erzeugen</button></div>
      <textarea id="bak" placeholder="Sicherung hier einfügen" aria-label="Sicherung" style="min-height:76px"></textarea>
      <div class="field-row"><button class="btn small ghost" data-import>Sicherung übernehmen</button><button class="btn small ghost" data-reset>Fortschritt löschen</button></div><p class="small" id="bakmsg"></p>
    </section>
    <section class="section"><h2>Woher der Inhalt kommt</h2>
      <p class="small">${esc(D.course.name)}, ${esc(D.course.term)}, ${esc(D.course.lecturer)}. Fragen und Zusammenfassungen wurden aus den Folien und der Zeittafel geschrieben und jeweils mit den Seiten verknüpft. Der Zusatztext „100 Jahre Jugendamt“ und der Reader sind noch nicht enthalten.</p></section></div>`;
}

/* ---------- Folienansicht ---------- */
const V = { doc: null, page: 1, mode: "bild", zoom: false, texts: {}, url: null, seq: 0 };
async function openSlide(doc, page) {
  await restoreKey();
  V.doc = doc; V.page = page; V.zoom = false;
  if (viewerEl.hidden) history.pushState({ ...history.state, viewer: 1 }, "", location.hash);
  viewerEl.hidden = false;
  document.body.classList.add("viewing");
  renderSlide();
}
function closeSlide() {
  viewerEl.hidden = true; document.body.classList.remove("viewing");
  if (V.url) { URL.revokeObjectURL(V.url); V.url = null; }
}
function slideChrome(inner, hasBar = true) {
  const n = M.docs[V.doc].pages;
  viewerEl.innerHTML = `<div class="v-top"><div class="ttl"><b>${esc(docName(V.doc))}</b><small>Seite ${V.page} von ${n}</small></div><button data-v-close aria-label="Folie schließen">×</button></div>
    <div class="v-body ${V.zoom ? "zoom" : ""}">${inner}</div>
    ${hasBar ? `<div class="v-bar"><button data-v-prev ${V.page <= 1 ? "disabled" : ""} aria-label="Vorherige Seite">Zurück</button><button data-v-mode aria-pressed="${V.mode === "text"}">Text</button><button data-v-zoom aria-pressed="${V.zoom}">Zoom</button><button data-v-next ${V.page >= n ? "disabled" : ""} aria-label="Nächste Seite">Vor</button></div>` : ""}`;
}
async function renderSlide() {
  const seq = ++V.seq, { doc, page } = V;
  if (!cryptoKey) {
    slideChrome(`<div class="v-msg"><h2>Folien freischalten</h2><p>Die Folien gehören zur Lehrveranstaltung und liegen deshalb verschlüsselt auf der öffentlichen Seite. Gib den Zugangscode einmal ein, dann merkt sich dieser Browser ihn.</p>
      <form class="field-row" data-unlock-form style="margin-top:12px"><input type="text" name="code" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Zugangscode" aria-label="Zugangscode"><button class="btn small">Freischalten</button></form><p class="small" data-unlock-msg></p></div>`, false);
    return;
  }
  if (V.mode === "text") {
    slideChrome(`<div class="v-msg">Text wird geladen.</div>`);
    try {
      if (!V.texts[doc]) V.texts[doc] = JSON.parse(new TextDecoder().decode(await openBin(`slides/${doc}/text.bin`)));
      if (seq !== V.seq) return;
      const lines = V.texts[doc][page] || [];
      slideChrome(`<div class="v-text">${lines.length ? lines.map(l => `<p class="${l.startsWith("•") ? "bl" : ""}">${esc(l)}</p>`).join("") : `<p>Auf dieser Folie gibt es keinen Text, nur Bilder. Wechsle zurück zur Bildansicht.</p>`}</div>`);
    } catch { if (seq === V.seq) slideError(); }
    return;
  }
  slideChrome(`<div class="v-msg">Folie wird geladen.</div>`);
  try {
    const buf = await openBin(`slides/${doc}/${String(page).padStart(3, "0")}.bin`);
    if (seq !== V.seq) return;
    if (V.url) URL.revokeObjectURL(V.url);
    V.url = URL.createObjectURL(new Blob([buf], { type: "image/jpeg" }));
    slideChrome(`<img class="v-img" alt="Folie ${page} aus ${esc(docName(doc))}" src="${V.url}">`);
  } catch { if (seq === V.seq) slideError(); }
}
function slideError() {
  slideChrome(`<div class="v-msg"><h2>Folie nicht verfügbar</h2><p>Diese Seite ist nicht auf dem Gerät gespeichert und es gibt gerade kein Netz. Unter „Ich“ kannst du alle Folien für offline laden.</p></div>`);
}
async function handleUnlock(form) {
  const msg = form.parentElement.querySelector("[data-unlock-msg]"), code = form.code.value;
  if (!code.trim()) return;
  msg.textContent = "Code wird geprüft.";
  try {
    await unlock(code);
    if (!viewerEl.hidden) renderSlide(); else route();
  } catch { msg.textContent = "Dieser Code passt nicht. Prüfe die Schreibweise und versuche es nochmal."; }
}
async function downloadAll() {
  const box = $("#dl"); if (!box) return;
  box.hidden = false;
  const bar = box.querySelector("i"), txt = box.querySelector("p");
  const urls = [];
  for (const [id, d] of Object.entries(M.docs)) {
    urls.push(`slides/${id}/text.bin`);
    for (let p = 1; p <= d.pages; p++) urls.push(`slides/${id}/${String(p).padStart(3, "0")}.bin`);
  }
  let done = 0, failed = 0, i = 0;
  await Promise.all(Array.from({ length: 6 }, async () => {
    while (i < urls.length) {
      const u = urls[i++];
      try { const r = await fetch(u); if (!r.ok) failed++; await r.arrayBuffer(); } catch { failed++; }
      done++;
      bar.style.width = done / urls.length * 100 + "%";
      txt.textContent = `${done} von ${urls.length} Dateien`;
    }
  }));
  txt.textContent = failed ? `${failed} Dateien fehlen noch. Versuch es mit besserem Netz nochmal.` : "Alle Folien sind auf dem Gerät gespeichert.";
  if (!failed) { S.offline = true; save(); }
}

/* ---------- Ereignisse ---------- */
document.addEventListener("click", e => {
  const b = e.target.closest("button, summary, details"); if (!b) return;
  const a = n => b.getAttribute(n), has = n => b.hasAttribute(n);
  if (has("data-slide")) { const [d, p] = a("data-slide").split(":"); openSlide(d, +p); return; }
  if (has("data-v-close")) { history.back(); return; }
  if (has("data-v-prev")) { V.page--; renderSlide(); return; }
  if (has("data-v-next")) { V.page++; renderSlide(); return; }
  if (has("data-v-mode")) { V.mode = V.mode === "text" ? "bild" : "text"; renderSlide(); return; }
  if (has("data-v-zoom")) { V.zoom = !V.zoom; V.mode = "bild"; $(".v-body", viewerEl)?.classList.toggle("zoom", V.zoom); b.setAttribute("aria-pressed", V.zoom); if (!$(".v-img", viewerEl)) renderSlide(); return; }
  if (has("data-go")) { if (R) quitRun(); go(a("data-go")); return; }
  if (has("data-run")) { startRun(a("data-run")); return; }
  if (has("data-ch-run")) { startRun("chapter", { ch: a("data-ch-run") }); return; }
  if (has("data-lf-run")) { startRun("lf", { n: +a("data-lf-run") }); return; }
  if (has("data-open-run")) { startRun("open", { n: +a("data-open-run") }); return; }
  if (has("data-exam")) { S.exam = a("data-exam"); save(); route(); return; }
  if (has("data-stoff-tab")) { stoffTab = a("data-stoff-tab"); viewStoff(); return; }
  if (has("data-quit")) { history.back(); return; }
  if (has("data-next")) { nextCard(); return; }
  if (has("data-reveal")) { revealOpen(R.items[R.i]); return; }
  if (has("data-open-done")) { finishOpen(R.items[R.i]); return; }
  if (has("data-offline")) { downloadAll(); return; }
  if (has("data-export")) { const t = $("#bak"); t.value = b64.to(new TextEncoder().encode(JSON.stringify({ ...S, key: null }))); t.select(); navigator.clipboard?.writeText(t.value).then(() => $("#bakmsg").textContent = "In die Zwischenablage kopiert.").catch(() => {}); return; }
  if (has("data-import")) { try { const key = S.key; S = { ...blank(), ...JSON.parse(new TextDecoder().decode(b64.from($("#bak").value.trim()))), key }; save(); viewMe(); $("#bakmsg").textContent = "Sicherung übernommen."; } catch { $("#bakmsg").textContent = "Dieser Text ist keine gültige Sicherung."; } return; }
  if (has("data-reset")) { if (confirm("Fortschritt auf diesem Gerät löschen?")) { const key = S.key; S = { ...blank(), key }; save(); route(); } return; }
  if (!R || R.answered) return;
  const k = R.items[R.i], s = R.state;
  if (has("data-mc")) {
    const o = s.opts[+a("data-mc")], ok = o === k.right, gain = score(k, ok);
    feedback(k, ok, gain, (ok ? "" : `<div class="opt wrong">${esc(o)}</div>`) + `<div class="opt right">${esc(k.right)}</div>`);
  } else if (has("data-tf")) {
    const v = a("data-tf") === "1", ok = v === k.val, gain = score(k, ok);
    feedback(k, ok, gain, `<div class="opt ${k.val ? "right" : "wrong"}">Die Aussage ${k.val ? "stimmt" : "ist falsch"}.</div>`);
  } else if (has("data-multi")) {
    const i = +a("data-multi"); s.sel.has(i) ? s.sel.delete(i) : s.sel.add(i);
    b.classList.toggle("picked"); b.setAttribute("aria-pressed", s.sel.has(i));
    $("[data-check-multi]").disabled = !s.sel.size;
  } else if (has("data-check-multi")) {
    const picked = [...s.sel].map(i => s.opts[i]), ok = picked.length === k.right.length && picked.every(p => k.right.includes(p)), gain = score(k, ok);
    feedback(k, ok, gain, s.opts.map(o => { const r = k.right.includes(o), p = picked.includes(o); return `<div class="opt ${r && p ? "right" : r ? "missed" : p ? "wrong" : ""}">${esc(o)}</div>`; }).filter((h, i) => k.right.includes(s.opts[i]) || picked.includes(s.opts[i])).join(""));
  } else if (has("data-ord")) { s.seq.push(+a("data-ord")); renderOrd(k); }
  else if (has("data-ord-out")) { s.seq.splice(+a("data-ord-out"), 1); renderOrd(k); }
  else if (has("data-check-ord")) {
    const ok = s.seq.every((x, i) => x === i), gain = score(k, ok);
    feedback(k, ok, gain, k.items.map((it, i) => `<div class="opt ${s.seq[i] === i ? "right" : "missed"}"><b>${esc(it[0])}</b> ${esc(it[1])}</div>`).join(""));
  } else if (has("data-ml")) { s.sel = +a("data-ml"); renderMatch(k); }
  else if (has("data-mr")) {
    if (s.sel === null) return;
    const r = +a("data-mr");
    if (k.pairs[r][1] === k.pairs[s.sel][1]) {
      // Bei gleichem Text rechts zaehlt jedes passende Feld: die Felder tauschen, damit das getippte erledigt wird.
      const t = s.right.indexOf(s.sel), u = s.right.indexOf(r);
      [s.right[t], s.right[u]] = [s.right[u], s.right[t]];
      s.done.add(s.sel);
      s.sel = null;
      if (s.done.size === k.pairs.length) {
        const ok = s.errors === 0, gain = score(k, ok);
        feedback(k, ok, gain, k.pairs.map(p => `<div class="opt right"><b>${esc(p[0])}</b>: ${esc(p[1])}</div>`).join(""));
      } else renderMatch(k);
    } else {
      s.errors++; b.classList.add("bad");
      setTimeout(() => b.classList.remove("bad"), 320);
    }
  }
});
document.addEventListener("toggle", e => { const d = e.target; if (d.tagName === "DETAILS" && d.dataset.peek && d.open) { S["peek" + d.dataset.peek] = 1; save(); } }, true);
document.addEventListener("submit", e => { if (e.target.matches("[data-unlock-form]")) { e.preventDefault(); handleUnlock(e.target); } });
document.addEventListener("keydown", e => {
  if (e.target.matches("input, textarea")) return;
  if (e.key === "Escape" && !viewerEl.hidden) { history.back(); return; }
  if (!R) return;
  if (e.key === "Enter" && R.answered) { e.preventDefault(); nextCard(); return; }
  const n = +e.key;
  if (n >= 1 && n <= 5) { const opts = main.querySelectorAll("[data-mc],[data-tf],[data-multi]"); opts[n - 1]?.click(); }
});

/* ---------- Navigation ---------- */
function go(hash) { if (location.hash === hash) route(); else location.hash = hash; }
function quitRun() { if (R) endRun(); }
function route() {
  const h = location.hash.replace(/^#/, "") || "/";
  if (h === "/fahrt") { if (R) return; history.replaceState(null, "", "#/"); return route(); }
  if (R) endRun();
  const p = h.split("/").filter(Boolean);
  const tab = !p.length ? "home" : p[0] === "angekommen" ? "home" : p[0];
  renderNav(tab);
  if (!p.length || p[0] === "angekommen") viewHome();
  else if (p[0] === "lf") p[1] ? viewLfDetail(+p[1]) : viewLf();
  else if (p[0] === "stoff") p[1] ? viewChapter(p[1]) : viewStoff();
  else if (p[0] === "ich") viewMe();
  else viewHome();
  window.scrollTo(0, 0);
  main.focus({ preventScroll: true });
}
window.addEventListener("hashchange", route);
window.addEventListener("popstate", () => {
  if (!viewerEl.hidden && !history.state?.viewer) { closeSlide(); return; }
  if (R && !history.state?.run) { quitRun(); route(); }
});

(async function init() {
  const [d, m] = await Promise.all([fetch("data/geschichte.json").then(r => r.json()), fetch("slides/manifest.json").then(r => r.json())]);
  D = d; M = m;
  const hk = location.hash.match(/^#key=(.+)$/);
  if (hk) {
    try { await unlock(decodeURIComponent(hk[1])); } catch {}
    history.replaceState(null, "", location.pathname);
  }
  await restoreKey();
  route();
  if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});
})().catch(() => { main.innerHTML = `<div class="pad"><h1 class="h1">Die Daten konnten nicht geladen werden</h1><p class="lead">Prüfe die Internetverbindung und lade die Seite neu.</p></div>`; });
