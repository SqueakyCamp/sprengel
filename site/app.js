"use strict";
/* Sprengel: mobiles Lernzentrum fuer mehrere Lehrveranstaltungen. Keine Bibliotheken, Fortschritt liegt im localStorage des Geraets. */

const STORE = "sprengel.v1";
const DAILY_GOAL = 60;
const BOX_DAYS = [0, 1, 2, 4, 8, 16];
const COURSE_IDS = ["matsi", "recht", "sopol", "faelle", "geschichte"];
const MODULE = ["matsi", "recht", "sopol", "faelle"];
const COURSE_DOCS = {
  geschichte: ["e", "a1", "a2", "eb", "rw", "t", "n", "zs", "z", "lf", "j"], matsi: ["msp", "msk"],
  recht: ["f2", "f3", "f4", "f5", "f6", "f7", "rv", "r2", "r3"], sopol: ["s1", "s2", "s3", "s4", "s5", "s6", "zb", "zf", "zn", "zt", "zw"],
  faelle: ["cr", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "cu", "cb"],
};
const NAV_LABEL = { geschichte: "Leitfragen", recht: "Fernlehre", matsi: "Kernfragen", sopol: "Kernfragen" };
const COURSE_LINE = {
  geschichte: "Leitfragen, Zeitstrahl, Personen", matsi: "WMS, Wohnen, Schulden", recht: "Fernlehren, Instanzen, Fristen",
  sopol: "Gerechtigkeit, Sozialstaat, Arbeit, Vermögen", faelle: "11 Fälle nach dem Raster",
};
const LEVELS = [
  [0, "Ehrenamt"], [150, "Berufspflege"], [400, "Fachkurs"], [800, "Fürsorgeschule"], [1400, "Sprengeldienst"],
  [2200, "Case Work"], [3200, "Sozialakademie"], [4500, "FH-Diplom"], [6500, "Master"], [9000, "Fachaufsicht"], [12500, "Lehrauftrag"], [17000, "Sprengelleitung"],
];
const BADGES = [
  ["first", "Erste Fahrt", "Eine Runde abgeschlossen", s => s.runs >= 1],
  ["streak3", "Drei Tage", "3 Tage in Folge gelernt", s => s.bestStreak >= 3],
  ["streak7", "Eine Woche", "7 Tage in Folge gelernt", s => s.bestStreak >= 7],
  ["combo10", "Zehn am Stück", "10 richtige Antworten in Folge", s => s.bestCombo >= 10],
  ["open5", "Frei formuliert", "5 Fragen frei beantwortet", s => s.opens >= 5],
  ["exam", "Probe bestanden", "Eine Probeprüfung abgeschlossen", s => s.exams >= 1],
  ["stamp5", "Fünf Stempel", "5 Leitfragen in Geschichte gestempelt", (s, n) => n >= 5],
  ["stamp26", "Volle Karte", "Alle 26 Leitfragen gestempelt", (s, n) => n >= 26],
  ["fall1", "Erste Akte", "Einen Fall durch das ganze Raster gebracht", () => casesDone() >= 1],
  ["fall11", "Alle Akten", "Alle 11 Fälle durch das Raster gebracht", () => casesDone() >= 11],
  ["blitz15", "Blitzmerker", "15 Richtige in einer Blitzrunde", s => Object.values(s.blitz).some(v => v >= 15)],
  ["bridge5", "Brückenbauer*in", "5 Exkurse gelesen", s => Object.keys(s.links).length >= 5],
  ["bridgeAll", "Das ganze Netz", "Alle Exkurse gelesen", s => LINKS.length && Object.keys(s.links).length >= LINKS.length],
  ["fristen", "Fristgerecht", "Recht: 5 Fernlehre-Fragen gestempelt", () => stampCount(DATA.recht) >= 5],
  ["netz", "Zweites Netz", "MATS: 5 Kernfragen gestempelt", () => stampCount(DATA.matsi) >= 5],
  ["floete", "Flöte verteilt", "SoPol: 5 Kernfragen gestempelt", () => stampCount(DATA.sopol) >= 5],
  ["modul", "Modul im Griff", "In allen vier Teilen des Moduls gelernt", s => MODULE.every(c => (s.cx[c] || 0) > 0)],
];
const QUESTS = [
  ["cards", 10, "10 Karten beantworten"], ["opens", 2, "2 Fragen frei beantworten"], ["blitz", 1, "Eine Blitzrunde spielen"],
  ["cases", 1, "Einen Rasterschritt bearbeiten"], ["links", 1, "Einen Exkurs lesen"], ["courses", 2, "In 2 Lehrveranstaltungen lernen"],
];

let D, M, DATA = {}, LINKS = [], WEB = {}; // aktueller Kurs, Folienmanifest, alle Kurse, Exkurse
const TOPIC = {}, CHAPTER = {}, CARD = {};
const $ = (s, r = document) => r.querySelector(s);
const main = $("#main"), viewerEl = $("#viewer"), navEl = $("#nav");
const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const shuffle = a => { a = [...a]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const dayKey = (d = new Date()) => { const z = new Date(d.getTime() - d.getTimezoneOffset() * 6e4); return z.toISOString().slice(0, 10); };
const dayDiff = (a, b) => Math.round((new Date(b + "T12:00") - new Date(a + "T12:00")) / 864e5);

/* ---------- Zustand ---------- */
const blank = () => ({ xp: 0, cards: {}, lfOpen: {}, days: {}, runs: 0, opens: 0, exams: 0, bestCombo: 0, bestStreak: 0, exam: null, key: null, examLast: null, offline: false,
  cx: {}, ex: {}, exDate: {}, cases: {}, links: {}, blitz: {}, q: null, last: null });
let S = load();
function migrate(s) {
  // Alter Stand kannte nur Geschichte: XP und Termin dorthin buchen.
  if (s.xp && !Object.keys(s.cx).length) s.cx.geschichte = s.xp;
  if (s.exam && !s.ex.geschichte) s.ex.geschichte = s.exam;
  return s;
}
function load() { try { return migrate({ ...blank(), ...JSON.parse(localStorage.getItem(STORE) || "{}") }); } catch { return blank(); } }
function save() { try { localStorage.setItem(STORE, JSON.stringify(S)); } catch {} }

function streak() {
  let d = dayKey(), n = 0;
  if (!S.days[d]) { const y = new Date(); y.setDate(y.getDate() - 1); d = dayKey(y); }
  while (S.days[d]) { n++; const x = new Date(d + "T12:00"); x.setDate(x.getDate() - 1); d = dayKey(x); }
  return n;
}
function addXp(n, cid = D?.course.id) {
  S.xp += n; const d = dayKey(); S.days[d] = (S.days[d] || 0) + n; S.bestStreak = Math.max(S.bestStreak, streak());
  if (cid) { S.cx[cid] = (S.cx[cid] || 0) + n; questTick("courses", cid); }
}
function level(xp = S.xp) {
  let i = 0; while (i + 1 < LEVELS.length && xp >= LEVELS[i + 1][0]) i++;
  const next = LEVELS[i + 1];
  return { name: LEVELS[i][1], i, next, pct: next ? (xp - LEVELS[i][0]) / (next[0] - LEVELS[i][0]) : 1 };
}
function rank(c) {
  const xp = S.cx[c.course.id] || 0, r = c.course.ranks;
  if (!r) return null;
  let i = 0; while (i + 1 < r.length && xp >= r[i + 1][0]) i++;
  return { name: r[i][1], next: r[i + 1], xp, pct: r[i + 1] ? (xp - r[i][0]) / (r[i + 1][0] - r[i][0]) : 1 };
}
function daysToExam(c = D) {
  const id = c.course.id, ex = c.course.exams || [];
  const e = ex.find(x => x.id === S.ex[id]) || (ex.length === 1 ? ex[0] : null);
  const date = e?.date || S.exDate[id];
  return date ? { ...(e || { label: "Prüfung" }), date, left: dayDiff(dayKey(), date) } : null;
}
function intervalDays(box, cid) {
  const ex = daysToExam(DATA[cid] || D); let d = BOX_DAYS[box];
  if (ex && ex.left > 0) d = Math.min(d, Math.max(1, Math.ceil(ex.left / 3)));
  return d;
}
function grade(id, ok, cid) {
  const c = S.cards[id] || { box: 0, seen: 0, wrong: 0 };
  c.seen++;
  if (ok) c.box = Math.min(c.box + 1, 5); else { c.box = 0; c.wrong++; }
  c.due = Date.now() + intervalDays(c.box, cid) * 864e5 - 36e5;
  S.cards[id] = c;
}

/* ---------- Tagesauftraege ---------- */
function quests() {
  const d = dayKey();
  if (!S.q || S.q.day !== d) {
    let h = 0; for (const c of d) h = (h * 31 + c.charCodeAt(0)) >>> 0;
    const a = [...QUESTS.keys()].sort((x, y) => ((x + 1) * 2654435761 ^ h) % 97 - ((y + 1) * 2654435761 ^ h) % 97).slice(0, 3);
    S.q = { day: d, pick: a, n: {}, set: [], done: [] };
  }
  return S.q;
}
function questTick(key, val) {
  const q = quests();
  if (key === "courses") { if (!q.set.includes(val)) q.set.push(val); q.n.courses = q.set.length; }
  else q.n[key] = (q.n[key] || 0) + 1;
  q.pick.forEach(i => {
    const [k, goal, label] = QUESTS[i];
    if (k === key && !q.done.includes(i) && (q.n[k] || 0) >= goal) {
      q.done.push(i); S.xp += 15; S.days[dayKey()] = (S.days[dayKey()] || 0) + 15;
      toast(`Tagesauftrag geschafft: ${label}. +15 XP`);
    }
  });
}
let toastT = 0;
function toast(msg) {
  let t = $("#toast");
  if (!t) { t = document.createElement("div"); t.id = "toast"; t.className = "toast"; t.setAttribute("role", "status"); document.body.append(t); }
  t.textContent = msg; t.classList.add("on");
  clearTimeout(toastT); toastT = setTimeout(() => t.classList.remove("on"), 3400);
}

/* ---------- Fortschritt ---------- */
const topicOf = id => TOPIC[id];
const chapterOf = id => CHAPTER[id];
const cardsIn = (ch, c = D) => c.cards.filter(k => topicOf(k.topic).ch === ch);
const learned = k => (S.cards[k.id]?.box || 0) >= 2;
function chapterPct(ch) { const c = cardsIn(ch); return c.length ? c.filter(learned).length / c.length : 0; }
const answered = k => (S.cards[k.id]?.box || 0) >= 1; // zuletzt richtig beantwortet
const cardCount = cards => `${cards.filter(answered).length} von ${cards.length} ${cards.length === 1 ? "Karte" : "Karten"} richtig beantwortet`;
function coursePct(c) { const m = c.cards.filter(k => !k.extra); return m.length ? m.filter(learned).length / m.length : 0; }
const lfKey = (n, c = D) => c.course.id === "geschichte" ? n : c.course.id + ":" + n;
function lfScore(n, c = D) {
  const cards = c.cards.filter(k => k.lf.includes(n) && !k.extra); // Zusatztext zaehlt nicht gegen den Stempel
  const open = openCredit(S.lfOpen[lfKey(n, c)]?.best || 0);
  if (!cards.length) return Math.round(open * 100);
  const quiz = cards.filter(learned).length / cards.length;
  return Math.round((quiz * .4 + open * .6) * 100);
}
const OPEN_FULL = .7; // wer das meiste nennt, bekommt die volle Punktzahl
const openCredit = r => Math.min(1, r / OPEN_FULL);
const stamped = (n, c = D) => lfScore(n, c) >= 80;
const stampCount = (c = D) => c.leitfragen.filter(l => stamped(l.n, c)).length;
const openName = (c = D) => c.course.openName || "Leitfrage";
const allCases = () => DATA.faelle.cases;
const caseRec = id => S.cases[id] || (S.cases[id] = {});
function casePct(cs) { const secs = DATA.faelle.sections; return secs.reduce((a, s) => a + (S.cases[cs.id]?.[s.key] || 0), 0) / secs.length; }
const caseDone = cs => DATA.faelle.sections.every(s => (S.cases[cs.id]?.[s.key] || 0) >= .5);
const casesDone = () => DATA.faelle ? allCases().filter(caseDone).length : 0;

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
  all: '<rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/>',
  net: '<circle cx="5" cy="6" r="2.5"/><circle cx="19" cy="6" r="2.5"/><circle cx="12" cy="18" r="2.5"/><path d="M7 7l4 9M17 7l-4 9M7.5 6h9"/>',
  fall: '<path d="M4 7a2 2 0 0 1 2-2h4l2 2h6a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/>',
};
const docName = d => M.docs[d]?.name || d;
function chip(src) {
  if (src[0][0] === "@") { const w = WEB[src[0].slice(1)]; return `<a class="chip web" href="${esc(w.u)}" target="_blank" rel="noopener">Zusatzquelle: ${esc(w.t)}</a>`; }
  return `<button class="chip" data-slide="${src[0]}:${src[1]}"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="13" rx="1"/><path d="M12 18v3"/></svg>${esc(docName(src[0]))}, S. ${src[1]}</button>`;
}
const uniq = src => { const seen = new Set(); return src.filter(s => { const k = s.join(":"); if (seen.has(k)) return false; seen.add(k); return true; }); };
const chips = src => `<div class="chips">${uniq(src).map(chip).join("")}</div>`;
function context(t, shown = []) {
  const ch = chapterOf(t.ch), have = new Set(shown.map(x => x.join(":")));
  const rest = uniq(t.src).filter(x => !have.has(x.join(":")));
  const tc = Object.values(CARD).filter(k => k.topic === t.id);
  return `<section class="context"><h3>${esc(t.title)}</h3><div class="era">${esc(ch.name)}${ch.span ? `, ${esc(ch.span)}` : ""}${tc.length ? `<br>${cardCount(tc)}` : ""}</div><p>${esc(t.text)}</p>${rest.length ? chips(rest) : ""}</section>`;
}
const lfRefs = k => k.lf.length ? `<div class="lfrefs">Gehört zu ${esc(openName(DATA[k.course]))} ${k.lf.join(", ")}</div>` : "";
const courseTag = cid => `<span class="ctag" style="--c:${DATA[cid].course.accent || "var(--petrol)"}">${esc(DATA[cid].course.short || "Geschichte")}</span>`;
function linkBox(l) {
  const read = S.links[l.id];
  return `<section class="xlink"><div class="ctags">${l.courses.map(courseTag).join("")}</div><h3>Exkurs: ${esc(l.title)}</h3><p>${esc(l.text)}</p>${chips(l.src)}
    ${read ? `<p class="small" style="margin-top:8px">Gelesen</p>` : `<button class="btn small ghost" style="margin-top:9px" data-link-read="${l.id}">Gelesen, +5 XP</button>`}</section>`;
}
const linkFor = k => LINKS.find(l => l.topics.includes(k.topic) && !S.links[l.id]) || LINKS.find(l => l.topics.includes(k.topic));

function renderNav(active, ctx) {
  const item = (hash, ic, label, key) => `<button data-go="${hash}" ${active === key ? 'aria-current="page"' : ""}><svg viewBox="0 0 24 24" aria-hidden="true">${ICONS[ic]}</svg>${label}</button>`;
  let h = `<button class="brand" data-go="#/">Sprengel</button>`;
  if (ctx) {
    const id = ctx.course.id;
    h += item("#/", "all", "Alle LVs", "hub");
    if (id === "faelle") h += item("#/faelle", "fall", "Fälle", "home");
    else h += item("#/" + id, "home", id === "geschichte" ? "Linie" : "Start", "home") + item(`#/${id}/lf`, "lf", NAV_LABEL[id], "lf");
    h += item(`#/${id}/stoff`, "stoff", "Stoff", "stoff") + item("#/ich", "me", "Ich", "me");
  } else h += item("#/", "all", "Alle LVs", "hub") + item("#/netz", "net", "Netz", "netz") + item("#/ich", "me", "Ich", "me");
  navEl.innerHTML = h;
}
function useCourse(id) {
  D = DATA[id]; S.last = id;
  document.body.style.setProperty("--petrol", D.course.accent || "");
  if (!D.course.accent) document.body.style.removeProperty("--petrol");
}
function clearCourse() { document.body.style.removeProperty("--petrol"); }

/* ---------- Alle Lehrveranstaltungen ---------- */
function viewHub() {
  clearCourse();
  const lv = level(), st = streak(), today = S.days[dayKey()] || 0, q = quests(); save();
  const wrong = wrongCards(MODULE).length;
  const tile = id => {
    const c = DATA[id], pct = id === "faelle" ? allCases().reduce((a, x) => a + casePct(x), 0) / allCases().length : coursePct(c), r = rank(c), ex = daysToExam(c);
    const sub = id === "faelle" ? `${casesDone()} von ${allCases().length} Fällen durch das Raster` : `${stampCount(c)} von ${c.leitfragen.length} ${esc(c.course.openNamePl || "Leitfragen")} gestempelt`;
    return `<button class="tile" data-go="#/${id}" style="--c:${c.course.accent || "#0F3D3E"}"><span class="tile-top"><b>${esc(id === "geschichte" ? "Geschichte der Sozialen Arbeit" : c.course.name)}</b>${ex && ex.left >= 0 ? `<em>${ex.left === 0 ? "Heute" : `${ex.left} ${ex.left === 1 ? "Tag" : "Tage"}`}</em>` : ""}</span>
      <span class="small">${esc(COURSE_LINE[id])}</span>
      <span class="tile-bar"><i style="width:${Math.round(pct * 100)}%"></i></span>
      <span class="small">${r ? esc(r.name) + ", " : ""}${sub}</span><span class="small">${cardCount(c.cards)}</span></button>`;
  };
  main.innerHTML = `<header class="hero"><div class="hero-in">
    <div class="hero-top"><h1>Sprengel</h1><div class="level">${esc(lv.name)}<br>${S.xp} XP</div></div>
    <div class="stats">
      <div class="stat"><b>${st}</b><span>${st === 1 ? "Tag" : "Tage"} in Folge</span></div>
      <div class="goal"><div class="bar"><i style="width:${Math.min(100, today / DAILY_GOAL * 100)}%"></i></div><span>Heute ${Math.min(today, DAILY_GOAL)} von ${DAILY_GOAL} XP</span></div>
    </div>
    <div class="starts">
      <button class="start" data-run="mix"><b>Modul-Mix</b><span>12 Karten aus MATS, Recht und SoPol, aus den Fällen nur Einzelfragen</span></button>
      ${S.last && DATA[S.last] ? `<button class="start alt" data-go="#/${S.last}"><b>Weiter</b><span>${esc(DATA[S.last].course.short || "Geschichte")}</span></button>` : `<button class="start alt" data-go="#/faelle"><b>Fall</b><span>Fallwerkstatt öffnen</span></button>`}
    </div>
    <div class="quick">${wrong ? `<button data-run="wrongmix">Fehler im Modul üben (${wrong})</button>` : ""}<button data-go="#/netz">Exkurse zwischen den LVs</button></div>
  </div></header>
  <div class="pad">
    <section class="section" style="margin-top:18px"><h2>Tagesaufträge</h2><ul class="quests">${q.pick.map(i => { const [k, goal, label] = QUESTS[i], n = Math.min(q.n[k] || 0, goal), done = q.done.includes(i); return `<li class="${done ? "done" : ""}"><span>${esc(label)}</span><b>${done ? "+15 XP" : `${n}/${goal}`}</b></li>`; }).join("")}</ul></section>
    <section class="section"><h2>Modul Grundsicherung</h2><div class="tiles">${MODULE.map(tile).join("")}</div></section>
    <section class="section"><h2>Weitere Lehrveranstaltungen</h2><div class="tiles">${tile("geschichte")}</div></section>
  </div>`;
}

/* ---------- Netz der Exkurse ---------- */
let netFilter = "alle";
function viewNet() {
  clearCourse();
  const list = LINKS.filter(l => netFilter === "alle" || l.courses.includes(netFilter));
  main.innerHTML = `<div class="pad"><h1 class="h1">Netz</h1><p class="lead">Wo die Lehrveranstaltungen zusammenhängen. ${Object.keys(S.links).length} von ${LINKS.length} gelesen.</p>
    <div class="tabs"><button aria-pressed="${netFilter === "alle"}" data-net="alle">Alle</button>${COURSE_IDS.map(id => `<button aria-pressed="${netFilter === id}" data-net="${id}">${esc(DATA[id].course.short || "Geschichte")}</button>`).join("")}</div>
    <div class="reading">${list.map(linkBox).join("")}</div></div>`;
}

/* ---------- Startseite einer Lehrveranstaltung ---------- */
function examBlock(ex) {
  const exText = ex ? (ex.left > 1 ? `Noch ${ex.left} Tage bis zur Prüfung` : ex.left === 1 ? "Morgen ist Prüfung" : ex.left === 0 ? "Heute ist Prüfung. Viel Erfolg!" : "Die Prüfung ist vorbei") : "";
  if (ex) return `<p class="small" style="color:var(--on-petrol-soft);margin-top:8px">${esc(exText)}</p>`;
  if (D.course.exams?.length) return `<div class="exam-pick"><b>Wann schreibst du die Prüfung?</b><div class="row">${D.course.exams.map(e => `<button class="btn small" data-exam="${e.id}">${esc(e.label)}, ${e.date.slice(8)}.${e.date.slice(5, 7)}.</button>`).join("")}</div></div>`;
  return `<form class="exam-pick" data-exam-form><label for="exd"><b>Prüfungstermin</b> (die Abstände der Wiederholung richten sich danach)</label><div class="row"><input id="exd" name="d" type="date"><button class="btn small">Speichern</button></div></form>`;
}
function viewHome() {
  if (D.course.id === "faelle") return viewCases();
  const lv = rank(D), st = streak(), today = S.days[dayKey()] || 0, ex = daysToExam(), id = D.course.id;
  const xp = S.cx[id] || 0, label = lv.name;
  const pcts = D.chapters.map(c => chapterPct(c.id));
  const firstOpen = D.chapters.findIndex((c, i) => !c.pending && pcts[i] < .8);
  const wrong = wrongCards([id]).length, modes = D.course.modes || [];
  const n = D.leitfragen.length, examN = id === "geschichte" ? 7 : Math.min(5, n);
  main.innerHTML = `
  <header class="hero"><div class="hero-in">
    <div class="hero-top"><h1>${esc(D.course.short)}</h1><div class="level">${esc(label)}<br>${xp} XP</div></div>
    <div class="stats">
      <div class="stat"><b>${st}</b><span>${st === 1 ? "Tag" : "Tage"} in Folge</span></div>
      <div class="stat"><b>${stampCount()}/${n}</b><span>Stempel</span></div>
      <div class="goal"><div class="bar"><i style="width:${Math.min(100, today / DAILY_GOAL * 100)}%"></i></div><span>Heute ${Math.min(today, DAILY_GOAL)} von ${DAILY_GOAL} XP</span></div>
    </div>
    <div class="starts">
      <button class="start" data-run="5"><b>5 Min</b><span>8 Karten</span></button>
      <button class="start alt" data-run="10"><b>10 Min</b><span>15 Karten</span></button>
    </div>
    <div class="quick">
      ${wrong ? `<button data-run="wrong">Fehler üben (${wrong})</button>` : ""}
      <button data-run="exam">${id === "geschichte" ? "Probeprüfung mit 7 Fragen" : `Probelauf mit ${examN} offenen Fragen`}</button>
      ${modes.includes("blitz") ? `<button data-run="blitz">Blitzrunde${S.blitz[id] ? ` (Rekord ${S.blitz[id]})` : ""}</button>` : ""}
      ${modes.includes("chains") ? `<button data-run="chains">Fallketten</button>` : ""}
      ${modes.includes("rechner") ? `<button data-run="calc">WMS-Rechner</button>` : ""}
    </div>
    ${examBlock(ex)}
  </div></header>
  <div class="pad">
    <p class="small count-all">Insgesamt ${cardCount(D.cards)}</p>
    ${D.course.upcoming ? `<p class="note upcoming">${esc(D.course.upcoming)}</p>` : ""}
    <h2 class="line-title">${esc(D.course.lineTitle || D.course.name)}</h2>
    <ol class="line">
      ${D.chapters.map((c, i) => {
        const p = pcts[i];
        if (c.pending) return `<li class="stop pending"><span class="dot"></span><div class="stop-in"><h3>${esc(c.name)}</h3><div class="span">${esc(c.span)}</div><div class="sub">${esc(c.line)}</div></div></li>`;
        return `<li class="stop ${p >= .8 ? "done" : p > 0 ? "begun" : ""}">
          <span class="fill" style="height:${i < firstOpen || firstOpen < 0 ? "100%" : i === firstOpen ? Math.round(p * 100) + "%" : "0"}"></span><span class="dot"></span>
          <button data-go="#/${id}/stoff/${c.id}"><h3>${esc(c.name)}</h3><div class="span">${esc(c.span)}${p > 0 ? `, ${Math.round(p * 100)} % gelernt` : ""}</div><div class="sub">${esc(c.line)}</div><div class="sub count">${cardCount(cardsIn(c.id))}</div></button>
        </li>`;
      }).join("")}
    </ol>
  </div>`;
}

/* ---------- Fallwerkstatt ---------- */
function viewCases() {
  const r = rank(D), done = casesDone(), cases = allCases(), wrong = wrongCards(["faelle"]).length;
  main.innerHTML = `<header class="hero"><div class="hero-in">
    <div class="hero-top"><h1>Fallwerkstatt</h1><div class="level">${esc(r.name)}<br>${r.xp} XP</div></div>
    <div class="stats"><div class="stat"><b>${done}/${cases.length}</b><span>Fälle durchs Raster</span></div><div class="stat"><b>${S.blitz.faelle || 0}</b><span>Blitz-Rekord</span></div></div>
    <div class="starts"><button class="start" data-run="randcase"><b>Zufallsfall</b><span>Alle 6 Rasterschritte, wie in der Prüfung</span></button><button class="start alt" data-run="drill"><b>Drill</b><span>Fallketten und Prioritäten aus allen Fällen</span></button></div>
    <div class="quick">${wrong ? `<button data-run="wrong">Fehler üben (${wrong})</button>` : ""}<button data-run="blitz">Blitzrunde</button><button data-slide="cr:1">Fallanalyseraster öffnen</button></div>
  </div></header>
  <div class="pad">
    <p class="note upcoming">Fallbearbeitung geht vor allem über MATS. Punkte mit Recht-Blick und SoPol-Blick zeigen die Zusammenhänge. Die Lösungspunkte sind von Claude aus den Unterlagen abgeleitet und nicht von den Lehrenden; andere gut begründete Lösungen können genauso richtig sein.</p>
    <h2 class="line-title">Die Fälle</h2>
    <div class="tiles" style="margin-top:12px">${cases.map(cs => { const p = casePct(cs), d = caseDone(cs); return `<button class="tile case ${d ? "done" : ""}" data-go="#/faelle/fall/${cs.id}" style="--c:var(--petrol)"><span class="tile-top"><b>${esc(cs.title)}</b>${d ? `<em>Fertig</em>` : ""}</span><span class="small">${esc(cs.where)}, ${esc(cs.who)}</span><span class="tile-bar"><i style="width:${Math.round(p * 100)}%"></i></span><span class="ctags">${cs.tags.map(t => `<span class="ctag plain">${esc(t)}</span>`).join("")}</span></button>`; }).join("")}</div>
  </div>`;
}
function viewCase(id) {
  const cs = allCases().find(x => x.id === id);
  if (!cs) return viewCases();
  const secs = DATA.faelle.sections;
  main.innerHTML = `<div class="pad"><button class="back" data-go="#/faelle">Alle Fälle</button>
    <h1 class="h1" style="margin-top:6px">${esc(cs.title)}</h1><p class="lead">${esc(cs.where)}, ${esc(cs.who)}</p>
    <div class="pcta"><button class="btn" data-case-all="${id}">Ganzes Raster bearbeiten</button><button class="btn ghost" data-case-drill="${id}">Fallkette und Prioritäten</button></div>
    <section class="section"><h2>Der Fall</h2><div id="casetext" class="casetext"><p>${esc(cs.lead)}</p></div>${chips([[cs.doc, 1]])}</section>
    <section class="section"><h2>Fallanalyseraster</h2><ol class="lflist" style="margin-top:0">${secs.map(s => { const b = S.cases[id]?.[s.key]; return `<li class="${b >= .5 ? "done" : ""}"><button data-case-sec="${id}:${s.key}"><span class="n">${s.n}</span><span>${esc(s.title)}<small>${b === undefined ? "Noch offen" : `Zuletzt beste Bewertung ${Math.round(b * 100)} %`}</small></span></button></li>`; }).join("")}</ol></section>
    ${(() => { const l = LINKS.filter(x => x.topics.includes("f-" + id)); return l.length ? `<section class="section"><h2>Zusammenhänge</h2><div class="reading">${l.map(linkBox).join("")}</div></section>` : ""; })()}
  </div>`;
  loadCaseText(cs);
}
async function loadCaseText(cs) {
  const el = $("#casetext"); if (!el) return;
  await restoreKey();
  if (!cryptoKey) { el.insertAdjacentHTML("beforeend", `<p class="small" style="margin-top:6px">Den ganzen Fall siehst du, sobald die Folien unter „Ich“ freigeschaltet sind.</p>`); return; }
  try {
    // Die Fallblaetter sind ein einziger Textblock: alle drei Saetze ein Absatz, damit man am Handy lesen kann.
    const t = await docText(cs.doc), sent = Object.values(t).flat().join(" ").split(/(?<=[.!?“])\s+(?=[A-ZÄÖÜ„])/), paras = [];
    for (let i = 0; i < sent.length; i += 3) paras.push(sent.slice(i, i + 3).join(" "));
    el.innerHTML = paras.map(p => `<p>${esc(p)}</p>`).join("");
  } catch {}
}
async function docText(doc) {
  if (!V.texts[doc]) V.texts[doc] = JSON.parse(new TextDecoder().decode(await openBin(`slides/${doc}/text.bin`)));
  return V.texts[doc];
}

/* ---------- Fahrt (Lernrunde) ---------- */
let R = null;
const isDue = k => { const c = S.cards[k.id]; return c && c.due <= Date.now(); };
const isNew = k => !S.cards[k.id];
const wrongCards = ids => ids.flatMap(id => DATA[id].cards).filter(k => S.cards[k.id]?.seen && S.cards[k.id].box === 0);

function pick(pool, n) {
  const due = shuffle(pool.filter(isDue)).sort((a, b) => S.cards[a.id].box - S.cards[b.id].box);
  const fresh = freshMix(pool);
  // Neue Karten haben Vorrang: hoechstens gut ein Drittel faellige Wiederholungen, solange es Neues gibt
  const dueShare = due.slice(0, fresh.length ? Math.ceil(n * .35) : n);
  const out = [...dueShare, ...fresh.slice(0, n - dueShare.length)];
  const later = shuffle(pool.filter(k => !isDue(k) && !isNew(k))).sort((a, b) => S.cards[a.id].box - S.cards[b.id].box || S.cards[a.id].due - S.cards[b.id].due);
  for (const k of [...due.slice(dueShare.length), ...later]) { if (out.length >= n) break; if (!out.includes(k)) out.push(k); }
  return spread(shuffle(out.slice(0, n)));
}
function freshMix(pool) { // neue Karten reihum aus den Themen, die du am wenigsten kennst; Zusatztext nur jede fuenfte
  const byTopic = new Map();
  for (const k of pool) { const t = byTopic.get(k.topic) || { seen: 0, all: 0, fresh: [] }; t.all++; if (isNew(k)) { if (!k.extra) t.fresh.push(k); } else t.seen++; byTopic.set(k.topic, t); }
  const topics = shuffle([...byTopic.values()].filter(t => t.fresh.length)).sort((a, b) => a.seen / a.all - b.seen / b.all);
  topics.forEach(t => t.fresh = shuffle(t.fresh));
  const main = [];
  for (let round = 0; main.length < pool.length && topics.some(t => t.fresh.length); round++) for (const t of topics) if (t.fresh.length) main.push(t.fresh.shift());
  const extra = shuffle(pool.filter(k => isNew(k) && k.extra)), out = [];
  let i = 0;
  while (main.length || extra.length) out.push(((i++ % 5 === 4 && extra.length) || !main.length) ? extra.shift() : main.shift());
  return out;
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
const caseItem = (cs, s, exam) => ({ type: "open", id: `case-${cs.id}-${s.key}`, lf: [], caseStep: true, cs, sec: s, exam, leit: { n: s.n, q: s.prompt, gist: "", points: cs.sections[s.key], ch: cs.id, course: "faelle" } });

function startRun(kind, opts = {}) {
  let items = [], title = "";
  if (kind === "5" || kind === "10") {
    const n = kind === "5" ? 7 : 13, open = kind === "5" ? 1 : 2;
    items = pick(D.cards, n);
    items.splice(Math.floor(items.length / 2), 0, ...pickLf(open));
    title = kind === "5" ? "Kurze Fahrt" : "Lange Fahrt";
  } else if (kind === "wrong") {
    items = spread(shuffle(wrongCards([D.course.id])).slice(0, 12)); title = "Fehler üben";
  } else if (kind === "wrongmix") {
    items = spread(shuffle(wrongCards(MODULE)).slice(0, 12)); title = "Fehler üben";
  } else if (kind === "mix") {
    const pool = MODULE.flatMap(id => DATA[id].cards).filter(k => k.course !== "faelle" || k.solo); // Fallketten und Reihungen brauchen den ganzen Fall
    items = pick(pool, 12); title = "Modul-Mix";
  } else if (kind === "chapter") {
    const ch = chapterOf(opts.ch);
    items = pick(cardsIn(opts.ch), 10); title = ch.name;
    items.splice(5, 0, ...pickLf(1, opts.ch));
  } else if (kind === "lf") {
    const lf = D.leitfragen.find(l => l.n === opts.n);
    items = pick(D.cards.filter(k => k.lf.includes(opts.n)), 6);
    items.push({ type: "open", id: "lf" + lf.n, lf: [lf.n], leit: lf }); title = `${openName()} ${lf.n}`;
  } else if (kind === "open") {
    const lf = D.leitfragen.find(l => l.n === opts.n);
    items = [{ type: "open", id: "lf" + lf.n, lf: [lf.n], leit: lf }]; title = `${openName()} ${lf.n}`;
  } else if (kind === "exam") {
    const n = D.course.id === "geschichte" ? 7 : Math.min(5, D.leitfragen.length);
    items = shuffle(D.leitfragen).slice(0, n).map(l => ({ type: "open", id: "lf" + l.n, lf: [l.n], leit: l, exam: true }));
    title = "Probeprüfung";
  } else if (kind === "chains") {
    items = spread(shuffle(D.cards.filter(k => k.type === "chain")).sort((a, b) => (S.cards[a.id]?.box || 0) - (S.cards[b.id]?.box || 0)).slice(0, 4)); title = "Fallketten";
  } else if (kind === "calc") {
    items = shuffle(D.cards.filter(k => k.type === "calc")).sort((a, b) => (S.cards[a.id]?.box || 0) - (S.cards[b.id]?.box || 0)).slice(0, 6); title = "WMS-Rechner";
  } else if (kind === "blitz") {
    items = shuffle(D.cards.filter(k => (k.type === "mc" || k.type === "tf") && k.q.length < 130 && !isSober(k))); title = "Blitzrunde";
  } else if (kind === "drill") {
    items = spread(shuffle(D.cards.filter(k => k.type === "chain" || k.type === "ord")).sort((a, b) => (S.cards[a.id]?.box || 0) - (S.cards[b.id]?.box || 0)).slice(0, 6)); title = "Drill";
  } else if (kind === "casedrill") {
    items = D.cards.filter(k => k.topic === "f-" + opts.id); title = "Fallkette";
  } else if (kind === "case") {
    const cs = allCases().find(x => x.id === opts.id);
    items = DATA.faelle.sections.map(s => caseItem(cs, s)); title = cs.title;
  } else if (kind === "randcase") {
    const cs = shuffle(allCases()).sort((a, b) => casePct(a) - casePct(b))[0];
    items = DATA.faelle.sections.map(s => caseItem(cs, s, true)); title = cs.title;
  } else if (kind === "casesec") {
    const cs = allCases().find(x => x.id === opts.id), s = DATA.faelle.sections.find(x => x.key === opts.key);
    items = [caseItem(cs, s)]; title = cs.title;
  }
  if (!items.length) { location.hash = "#/"; return; }
  R = { kind, title, items, i: 0, xp: 0, right: 0, total: 0, combo: 0, bestCombo: 0, retry: new Set(), missed: [], examPts: [0, 0], stampsBefore: D ? stampCount() : 0, start: Date.now(), answered: false, state: {}, origin: D?.course.id };
  document.body.classList.add("running");
  history.pushState({ run: 1 }, "", "#/fahrt");
  if (kind === "blitz") { R.end = Date.now() + 60000; R.timer = setInterval(blitzTick, 250); R.wrongList = []; }
  renderCard();
}
function endRun() { if (R?.timer) clearInterval(R.timer); R = null; document.body.classList.remove("running"); }
function blitzTick() {
  if (!R) return;
  const left = R.end - Date.now(), bar = $("#blitzbar");
  if (bar) { bar.style.width = Math.max(0, left / 600) + "%"; }
  const lab = $("#blitzsec"); if (lab) lab.textContent = Math.max(0, Math.ceil(left / 1000));
  if (left <= 0) { clearInterval(R.timer); renderArrive(); }
}

function runHeader(item) {
  if (R.kind === "blitz") return `<div class="run-top"><button class="run-x" data-quit aria-label="Runde beenden">×</button><div class="track blitz"><i id="blitzbar" style="width:${Math.max(0, (R.end - Date.now()) / 600)}%"></i></div><div class="combo"><span id="blitzsec">${Math.max(0, Math.ceil((R.end - Date.now()) / 1000))}</span></div></div>`;
  const sober = isSober(item);
  const n = R.items.length;
  return `<div class="run-top"><button class="run-x" data-quit aria-label="Runde beenden">×</button>
    <div class="track" aria-label="Karte ${R.i + 1} von ${n}"><i style="width:${R.i / n * 100}%"></i>${n <= 18 ? R.items.map((_, i) => `<b class="${i < R.i ? "on" : ""}"></b>`).join("") : ""}</div>
    <div class="combo">${!sober && R.combo >= 3 ? `${R.combo}×` : ""}</div></div>`;
}
const isSober = item => item.topic ? chapterOf(topicOf(item.topic).ch).sober : (item.leit && chapterOf(item.leit.ch)?.sober);

function renderCard() {
  const k = R.items[R.i];
  R.answered = false; R.state = {};
  window.scrollTo(0, 0);
  if (k.type === "open") return renderOpen(k);
  const head = runHeader(k) + cardTag(k);
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
  } else if (k.type === "bucket") {
    R.state.order = shuffle(k.items.map((_, i) => i)); R.state.at = 0; R.state.wrong = [];
    renderBucket(k);
  } else if (k.type === "chain") {
    R.state.step = 0; R.state.errors = 0; R.state.log = [];
    renderChain(k);
  } else if (k.type === "calc") {
    main.innerHTML = `<div class="run">${head}<p class="q">${esc(k.q)}</p><div class="grow"></div>
      <form data-calc-form class="calc"><label for="calc">Dein Ergebnis in ${esc(k.unit)}</label><div class="field-row"><input id="calc" type="text" inputmode="decimal" autocomplete="off" name="v" placeholder="z. B. 360,31"><button class="btn small">Prüfen</button></div></form></div>`;
    $("#calc").focus({ preventScroll: true });
  }
}
const cardTag = k => {
  const showC = R.kind === "mix" || R.kind === "wrongmix";
  return `<div class="tag">${showC ? courseTag(k.course) + " " : ""}${esc(topicOf(k.topic).title)}${k.extra ? ", aus einer Zusatzquelle" : ""}</div>`;
};
function renderOrd(k, head = runHeader(k) + cardTag(k)) {
  const s = R.state;
  main.innerHTML = `<div class="run">${head}<p class="q">${esc(k.q)}</p><p class="tag" style="margin-top:4px">${esc(k.hint || "Tippe vom frühesten zum spätesten Ereignis.")}</p>
    <div class="seq" style="margin-top:12px">${k.items.map((_, i) => { const it = s.seq[i]; return `<button class="slot ${it !== undefined ? "full" : ""}" ${it !== undefined ? `data-ord-out="${i}"` : "disabled"}><span class="n">${i + 1}</span><span>${it !== undefined ? esc(k.items[it][1]) : ""}</span></button>`; }).join("")}</div>
    <div class="grow"></div><div class="pool">${s.pool.filter(i => !s.seq.includes(i)).map(i => `<button class="opt" data-ord="${i}">${esc(k.items[i][1])}</button>`).join("")}</div>
    <div style="margin-top:12px"><button class="btn" data-check-ord ${s.seq.length < k.items.length ? "disabled" : ""}>Reihenfolge prüfen</button></div></div>`;
}
function renderMatch(k, head = runHeader(k) + cardTag(k)) {
  const s = R.state;
  main.innerHTML = `<div class="run">${head}<p class="q">${esc(k.q)}</p><div class="grow"></div>
    <div class="pairs"><div class="col">${s.left.map(i => `<button class="pair ${s.done.has(i) ? "ok" : ""} ${s.sel === i ? "sel" : ""}" ${s.done.has(i) ? "disabled" : ""} data-ml="${i}">${esc(k.pairs[i][0])}</button>`).join("")}</div>
    <div class="col">${s.right.map(i => `<button class="pair ${s.done.has(i) ? "ok" : ""}" ${s.done.has(i) ? "disabled" : ""} data-mr="${i}">${esc(k.pairs[i][1])}</button>`).join("")}</div></div></div>`;
}
function renderBucket(k, flash = "") {
  const s = R.state, it = k.items[s.order[s.at]];
  main.innerHTML = `<div class="run">${runHeader(k)}${cardTag(k)}<p class="q">${esc(k.q)}</p>
    <div class="bk-count">${s.at + 1} von ${k.items.length}</div>
    <div class="bk-item ${flash}"><b>${esc(it[0])}</b></div>
    <div class="grow"></div><div class="answers ${k.buckets.length === 2 ? "two" : ""}">${k.buckets.map((b, i) => `<button class="opt" data-bk="${i}">${esc(b)}</button>`).join("")}</div></div>`;
}
function renderChain(k) {
  const s = R.state, st = k.steps[s.step];
  s.opts = shuffle([st.right, ...st.wrong]); s.answeredStep = false;
  main.innerHTML = `<div class="run">${runHeader(k)}${cardTag(k)}<p class="q small" style="margin-top:6px"><b>${esc(k.q)}</b>. ${esc(k.intro)}</p>
    <div class="chain-dots">${k.steps.map((_, i) => `<i class="${i < s.step ? (s.log[i] ? "ok" : "bad") : i === s.step ? "cur" : ""}"></i>`).join("")}</div>
    <p class="q">${esc(st.q)}</p><div class="grow"></div>
    <div class="answers">${s.opts.map((o, i) => `<button class="opt" data-chain="${i}">${esc(o)}</button>`).join("")}</div></div>`;
}

function score(k, ok) {
  const sober = isSober(k);
  grade(k.id, ok, k.course); R.total++;
  let gain = ok ? 10 + (sober ? 0 : Math.min(R.combo, 5)) : 2;
  if (ok && (k.type === "chain" || k.type === "calc" || k.type === "bucket")) gain += 5;
  if (ok) { R.right++; R.combo++; R.bestCombo = Math.max(R.bestCombo, R.combo); S.bestCombo = Math.max(S.bestCombo, R.combo); }
  else {
    R.combo = 0; R.missed.push(k);
    if (!R.retry.has(k.id) && R.kind !== "exam" && R.kind !== "blitz") { R.retry.add(k.id); R.items.push(k); } // am Ende nochmal
  }
  R.xp += gain; addXp(gain, k.course); questTick("cards"); save();
  if (navigator.vibrate) navigator.vibrate(ok ? 12 : [25, 40, 25]);
  return gain;
}
function feedback(k, ok, gain, givenHtml) {
  const t = topicOf(k.topic), sober = isSober(k), l = sober ? null : linkFor(k);
  R.answered = true;
  const res = sober
    ? `<div class="result"><div class="plain-result">${ok ? "Richtig." : "Nicht richtig."}</div></div>`
    : `<div class="result anim"><div class="stamp ${ok ? "good" : "bad"}">${ok ? "Richtig" : "Nicht ganz"}</div><div class="plus">+${gain} XP</div></div>`;
  main.innerHTML = `<div class="run">${runHeader(k)}${res}
    <p class="q small">${esc(k.q)}</p><div class="given">${givenHtml}</div>
    <p class="why">${esc(k.why)}</p>
    ${chips(k.src)}
    ${context(t, k.src)}
    ${l ? linkBox(l) : ""}
    ${lfRefs(k)}
    <div class="sticky"><button class="btn" data-next>${R.i + 1 < R.items.length ? "Weiter" : "Ankommen"}</button></div></div>`;
  $(".btn[data-next]").focus({ preventScroll: true });
}
function renderOpen(k) {
  const l = k.leit;
  const prev = R.state.text || "";
  const label = k.caseStep ? `${esc(k.cs.title)}, Schritt ${k.sec.n} von 6: ${esc(k.sec.title)}` : k.exam ? `Probeprüfung, Frage ${R.i + 1} von ${R.items.length}` : `${esc(openName(DATA[l.course]))} ${l.n} frei beantworten`;
  main.innerHTML = `<div class="run">${runHeader(k)}<div class="tag">${label}</div>
    <p class="q">${esc(l.q)}</p>
    ${k.caseStep ? chips([[k.cs.doc, 1], ["cr", 1]]) : ""}
    <textarea id="mine" placeholder="${k.exam ? "Schreib deine Antwort wie in der Prüfung." : "Stichworte tippen oder im Kopf antworten."}">${esc(prev)}</textarea>
    <div class="grow"></div><div style="margin-top:12px"><button class="btn" data-reveal>Antwort aufdecken</button></div></div>`;
}
const deepBlock = l => l.deep ? `<p class="tag">Vertiefung aus einem Zusatztext, zählt nicht für den Stempel</p><ul class="points">${l.deep.map(p => `<li class="point ro">${esc(p.t)}${chips(p.src)}</li>`).join("")}</ul>` : "";
const lensBadge = p => p.lens ? `<span class="lens ${p.lens}">${p.lens === "recht" ? "Recht-Blick" : "SoPol-Blick"}</span>` : "";
function revealOpen(k) {
  const l = k.leit, mine = $("#mine")?.value.trim();
  R.state.mine = mine;
  main.innerHTML = `<div class="run">${runHeader(k)}<div class="tag">${k.caseStep ? `${esc(k.cs.title)}: ${esc(k.sec.title)}` : `${esc(openName(DATA[l.course]))} ${l.n}`}</div><p class="q small">${esc(l.q)}</p>
    ${mine ? `<div class="mine">${esc(mine)}</div>` : ""}
    ${l.gist ? `<p class="gist">${esc(l.gist)}</p>` : ""}
    ${l.note ? `<div class="note">${esc(l.note)}</div>` : ""}
    <p class="tag">${k.caseStep ? "Das wären mögliche Punkte. Hake an, was du ähnlich hattest." : "Hake an, was du selbst genannt hättest. Ab 70 % der Punkte zählt die Antwort voll."}</p>
    <ul class="points">${l.points.map((p, i) => `<li class="point"><label><input type="checkbox" data-pt="${i}"><span>${lensBadge(p)}${esc(p.t)}</span></label>${chips(p.src)}</li>`).join("")}</ul>
    ${deepBlock(l)}
    <div class="sticky"><button class="btn" data-open-done>Selbsteinschätzung speichern</button></div></div>`;
  window.scrollTo(0, 0);
}
function finishOpen(k) {
  const l = k.leit, boxes = [...main.querySelectorAll("[data-pt]")];
  const hit = boxes.filter(b => b.checked).length, ratio = hit / boxes.length;
  if (k.caseStep) { const r = caseRec(k.cs.id); r[k.sec.key] = Math.max(r[k.sec.key] || 0, ratio); questTick("cases"); }
  else {
    const key = lfKey(l.n, DATA[l.course]), rec = S.lfOpen[key] || { best: 0, tries: 0 };
    rec.tries++; rec.best = Math.max(rec.best, ratio); rec.last = ratio; S.lfOpen[key] = rec;
    S.opens++; questTick("opens");
  }
  const gain = Math.round(10 + (k.caseStep ? ratio : openCredit(ratio)) * 25);
  R.xp += gain; addXp(gain, l.course); R.total++; if (ratio >= .6) R.right++;
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
  if (R.kind === "blitz") { const id = D.course.id; S.blitz[id] = Math.max(S.blitz[id] || 0, R.right); questTick("blitz"); }
  save();
  const r = R, newStamps = D ? stampCount() - r.stampsBefore : 0, today = S.days[dayKey()] || 0;
  const missedTopics = [...new Map(r.missed.filter(k => k.topic).map(k => [k.topic, topicOf(k.topic)])).values()];
  const missedLf = r.missed.filter(k => k.leit && !k.caseStep).map(k => k.leit);
  const n = DATA.geschichte ? stampCount(DATA.geschichte) : 0;
  const badge = BADGES.filter(b => b[3](S, n) && !S["b_" + b[0]]);
  badge.forEach(b => S["b_" + b[0]] = 1); save();
  const examLine = r.examPts[1] ? `<div><b>${Math.round(r.examPts[0] / r.examPts[1] * 100)} %</b><span>der Punkte genannt</span></div>` : "";
  const back = r.kind === "mix" || r.kind === "wrongmix" ? "#/" : "#/" + (D?.course.id || "");
  const caseId = r.items[0]?.cs?.id;
  endRun();
  history.replaceState(null, "", "#/angekommen");
  main.innerHTML = `<div class="pad arrive"><h1>${r.kind === "exam" ? "Probeprüfung fertig" : r.kind === "blitz" ? `${r.right} richtig` : "Angekommen"}</h1>
    <div class="score">${examLine}<div><b>+${r.xp}</b><span>XP</span></div>${r.kind === "exam" || !r.total ? "" : `<div><b>${r.right}/${r.total}</b><span>richtig</span></div>`}<div><b>${streak()}</b><span>Tage in Folge</span></div></div>
    ${today >= DAILY_GOAL && today - r.xp < DAILY_GOAL ? `<p style="margin-top:14px"><b>Tagesziel geschafft.</b></p>` : ""}
    ${newStamps > 0 ? `<p style="margin-top:14px"><b>${newStamps === 1 ? "Neuer Stempel" : newStamps + " neue Stempel"}</b> auf deiner Karte.</p>` : ""}
    ${badge.length ? `<div class="badges">${badge.map(b => `<div class="badge on"><b>${esc(b[1])}</b>${esc(b[2])}</div>`).join("")}</div>` : ""}
    ${missedTopics.length || missedLf.length ? `<section class="review"><h2>Noch einmal nachlesen</h2>
      <ul>${missedLf.map(l => `<li><button class="back" data-go="#/${l.course}/lf/${l.n}">${esc(openName(DATA[l.course]))} ${l.n}</button></li>`).join("")}</ul>
      <div class="reading">${missedTopics.slice(0, 3).map(t => context(t)).join("")}</div></section>` : ""}
    <div style="margin-top:22px">${caseId ? `<button class="btn" data-go="#/faelle/fall/${caseId}">Zum Fall</button>` : `<button class="btn" data-run="${r.kind === "mix" ? "mix" : "5"}">Noch eine Runde</button>`}<button class="btn ghost" data-go="${back}">Zurück</button></div></div>`;
  if (back === "#/") renderNav("hub"); else renderNav("home", D);
  window.scrollTo(0, 0);
}

/* ---------- Offene Fragen ---------- */
function viewLf() {
  const id = D.course.id, lead = D.course.openLead || "Die Prüfung stellt 7 Überblicksfragen aus diesem Themenkreis. Ein Stempel kommt, wenn du die Punkte frei nennen kannst und die Quizkarten sitzen.";
  let lastGroup = null;
  main.innerHTML = `<div class="pad"><h1 class="h1">${id === "geschichte" ? "Stempelkarte" : esc(D.course.openNamePl)}</h1>
    <p class="lead">${esc(lead)}</p>
    <div class="stamps">${D.leitfragen.map(l => { const s = lfScore(l.n), d = stamped(l.n); return `<button class="field ${d ? "done" : ""}" data-go="#/${id}/lf/${l.n}" aria-label="${esc(openName())} ${l.n}, ${s} Prozent"><i style="height:${s}%"></i><span>${l.n}</span></button>`; }).join("")}</div>
    <div class="pcta"><button class="btn" data-run="exam">${id === "geschichte" ? "Probeprüfung starten" : "Probelauf starten"}</button></div>
    ${D.course.upcoming ? `<p class="small" style="margin-top:10px">${esc(D.course.upcoming)}</p>` : ""}
    <ol class="lflist">${D.leitfragen.map(l => { const h = l.group && l.group !== lastGroup ? `<li class="group">${esc(l.group)}</li>` : ""; lastGroup = l.group; return h + `<li class="${stamped(l.n) ? "done" : ""}"><button data-go="#/${id}/lf/${l.n}"><span class="n">${l.n}</span><span>${esc(l.q)}<small>${lfScore(l.n)} %</small></span></button></li>`; }).join("")}</ol></div>`;
}
function viewLfDetail(n) {
  const l = D.leitfragen.find(x => x.n === n), id = D.course.id;
  if (!l) return viewLf();
  const cards = D.cards.filter(k => k.lf.includes(n));
  const tids = [...new Set(cards.map(k => k.topic))].map(topicOf);
  const open = S.lfOpen[lfKey(n)];
  const seen = !!open || !!S["peek" + lfKey(n)];
  main.innerHTML = `<div class="pad"><button class="back" data-go="#/${id}/lf">Alle ${esc(D.course.openNamePl || "Leitfragen")}</button>
    <h1 class="h1" style="font-size:1.95rem;margin-top:6px">${esc(openName())} ${n}</h1>
    ${l.group ? `<p class="small">${esc(l.group)}</p>` : ""}
    <p class="q" style="margin-top:8px">${esc(l.q)}</p>
    <p class="small" style="margin-top:6px">${lfScore(n)} % bis zum Stempel gesammelt (ab 80 %; freie Antwort zählt 60 %, Quizkarten 40 %, ab 70 % der Punkte gilt die Antwort als voll)${open ? `, zuletzt ${Math.round(open.last * 100)} % der Punkte genannt` : ""}</p>
    <div class="pcta"><button class="btn" data-open-run="${n}">Frei beantworten</button>${cards.length ? `<button class="btn ghost" data-lf-run="${n}">${cards.length} Quizkarten üben</button>` : ""}</div>
    <section class="section"><h2>Musterantwort</h2>
      <details ${seen ? "open" : ""} data-peek="${lfKey(n)}"><summary style="cursor:pointer;min-height:36px">Antwort anzeigen</summary>
      <p class="gist">${esc(l.gist)}</p>
      ${l.note ? `<div class="note">${esc(l.note)}</div>` : ""}
      <ul class="points">${l.points.map(p => `<li class="point ro">${esc(p.t)}${chips(p.src)}</li>`).join("")}</ul>${deepBlock(l)}</details>
    </section>
    ${tids.length ? `<section class="section"><h2>Einordnung</h2><div class="reading">${tids.slice(0, 5).map(t => context(t)).join("")}</div></section>` : ""}</div>`;
}

/* ---------- Stoff ---------- */
let stoffTab = "linie";
function viewStoff() {
  const id = D.course.id, net = LINKS.filter(l => l.courses.includes(id));
  const tabs = [["linie", id === "faelle" ? "Fälle" : id === "geschichte" ? "Stationen" : "Kapitel"], D.timeline.length && ["zeit", "Zeitstrahl"], D.people.length && ["personen", "Personen"], D.terms.length && ["begriffe", "Begriffe"], D.traps.length && ["fallen", "Stolperfallen"], net.length && ["netz", "Exkurse"], ["folien", id === "geschichte" ? "Folien und Texte" : "Dokumente"]].filter(Boolean);
  if (!tabs.some(t => t[0] === stoffTab)) stoffTab = "linie";
  let body = "";
  if (stoffTab === "linie") body = `<ol class="line">${D.chapters.filter(c => !c.pending).map(c => `<li class="stop"><span class="dot"></span><button data-go="#/${id}/stoff/${c.id}"><h3>${esc(c.name)}</h3><div class="span">${esc(c.span)}</div></button></li>`).join("")}</ol>`;
  if (stoffTab === "zeit") body = `<ol class="tl">${D.timeline.map(x => `<li><span class="y">${esc(x.y)}</span><span class="c">${esc(x.t)}${chips(x.src)}</span></li>`).join("")}</ol>`;
  if (stoffTab === "personen") body = D.people.map(p => `<div class="item"><h3>${esc(p.name)}</h3>${p.dates ? `<small>${esc(p.dates)}</small>` : ""}<p>${esc(p.text)}</p>${chips(p.src)}</div>`).join("");
  if (stoffTab === "begriffe") body = D.terms.map(p => `<div class="item"><h3>${esc(p.term)}</h3><p>${esc(p.text)}</p>${chips(p.src)}</div>`).join("");
  if (stoffTab === "fallen") body = `<p class="lead">Hier widersprechen sich Unterlagen oder etwas fehlt. Im Zweifel frag in der LV nach.</p>` + D.traps.map(p => `<div class="item"><h3>${esc(p.title)}</h3><p>${esc(p.text)}</p>${chips(p.src)}</div>`).join("");
  if (stoffTab === "netz") body = `<div class="reading">${net.map(linkBox).join("")}</div>`;
  if (stoffTab === "folien") body = `<div class="docs">${COURSE_DOCS[id].filter(d => M.docs[d]).map(d => `<button class="opt" data-slide="${d}:1">${esc(M.docs[d].name)}<small>${M.docs[d].pages} Seiten</small></button>`).join("")}</div>${D.more?.length ? `<section class="section"><h2>Zum Weiterlesen im Netz</h2><p class="small">Zusatzquellen, daraus stammt hier nur, was als Zusatzquelle gekennzeichnet ist.</p><div class="chips">${D.more.map(m => `<a class="chip web" href="${esc(m[1])}" target="_blank" rel="noopener">${esc(m[0])}</a>`).join("")}</div></section>` : ""}`;
  main.innerHTML = `<div class="pad"><h1 class="h1">Stoff</h1>
    <div class="tabs">${tabs.map(([k, v]) => `<button aria-pressed="${stoffTab === k}" data-stoff-tab="${k}">${v}</button>`).join("")}</div>${body}</div>`;
}
function chapterDocs(c) { // Startseite je Dokument: erste zitierte Seite der Kapitelthemen
  const src = D.topics.filter(t => t.ch === c.id).flatMap(t => t.src).filter(([d]) => M.docs[d] && d !== "j" && !d.startsWith("@"));
  const own = c.docs.filter(d => src.some(s => s[0] === d)), order = own.length ? own : [...new Set(src.map(s => s[0]))].slice(0, 1);
  if (!order.length) return c.docs[0] && c.docs[0] !== "j" && M.docs[c.docs[0]] ? [[c.docs[0], 1]] : [];
  return order.slice(0, 2).map(d => [d, Math.min(...src.filter(s => s[0] === d).map(s => s[1]))]);
}
function viewChapter(id) {
  const c = chapterOf(id), cid = D.course.id;
  if (!c) return viewStoff();
  if (cid === "faelle" && id !== "raster") { location.hash = "#/faelle/fall/" + id; return; }
  const tp = D.topics.filter(t => t.ch === id);
  const lfs = D.leitfragen.filter(l => l.ch === id);
  const hasCards = cardsIn(id).length > 0;
  main.innerHTML = `<div class="pad"><button class="back" data-go="#/${cid}/stoff">Stoff</button>
    <h1 class="h1" style="margin-top:6px">${esc(c.name)}</h1><p class="lead">${esc(c.span)}, ${Math.round(chapterPct(id) * 100)} % gelernt<br>${cardCount(cardsIn(id))}</p>
    <div class="pcta">${hasCards ? `<button class="btn" data-ch-run="${id}">${cid === "geschichte" ? "Diese Station üben" : "Dieses Kapitel üben"}</button>` : ""}${chapterDocs(c).map(([d, p], i) => `<button class="btn ghost" data-slide="${d}:${p}">${i ? `${esc(docName(d))}, S. ${p}` : `Dokument öffnen, S. ${p}`}</button>`).join("")}${c.book ? `<button class="btn ghost" data-slide="j:${c.book}">Im Zusatztext lesen</button>` : ""}</div>
    ${lfs.length ? `<section class="section"><h2>${esc(D.course.openNamePl || "Leitfragen")} dazu</h2><ol class="lflist" style="margin-top:0">${lfs.map(l => `<li class="${stamped(l.n) ? "done" : ""}"><button data-go="#/${cid}/lf/${l.n}"><span class="n">${l.n}</span><span>${esc(l.q)}</span></button></li>`).join("")}</ol></section>` : ""}
    <section class="section"><h2>Zusammenfassung</h2><div class="reading">${tp.map(t => context(t)).join("")}</div></section></div>`;
}

/* ---------- Ich ---------- */
function viewMe() {
  const lv = level(), n = stampCount(DATA.geschichte);
  const seen = Object.keys(S.cards).length, total = COURSE_IDS.reduce((a, id) => a + DATA[id].cards.length, 0);
  main.innerHTML = `<div class="pad"><h1 class="h1">${esc(lv.name)}</h1>
    <div class="levelbar"><div class="progress"><i style="width:${lv.pct * 100}%"></i></div>
    <p class="small" style="margin-top:4px">${S.xp} XP${lv.next ? `, nächste Stufe „${esc(lv.next[1])}“ bei ${lv.next[0]} XP` : ""}</p></div>
    <p class="small" style="margin-top:6px">${seen} von ${total} Karten gesehen, längste Serie ${S.bestStreak} Tage, ${casesDone()} Fälle fertig, ${Object.keys(S.links).length} Exkurse gelesen</p>
    <section class="section"><h2>Lehrveranstaltungen</h2><div class="ranks">${COURSE_IDS.map(id => { const c = DATA[id], r = rank(c), xp = S.cx[id] || 0; return `<div class="rank"><b>${esc(id === "geschichte" ? "Geschichte" : c.course.name)}</b><span class="small">${r ? esc(r.name) + ", " : ""}${xp} XP${r?.next ? `, nächster Rang bei ${r.next[0]}` : ""}</span>${r ? `<div class="progress"><i style="width:${r.pct * 100}%"></i></div>` : ""}</div>`; }).join("")}</div></section>
    <section class="section"><h2>Abzeichen</h2><div class="badges">${BADGES.map(b => `<div class="badge ${b[3](S, n) ? "on" : ""}"><b>${esc(b[1])}</b>${esc(b[2])}</div>`).join("")}</div></section>
    <section class="section"><h2>Prüfungstermine</h2>
      ${COURSE_IDS.filter(id => id !== "faelle").map(id => { const c = DATA[id], ex = c.course.exams || [], cur = daysToExam(c); return `<div class="exam-row"><b>${esc(c.course.short || "Geschichte")}</b>${ex.length ? `<div class="field-row">${ex.map(e => `<button class="btn small ${cur?.id === e.id ? "" : "ghost"}" data-exam2="${id}:${e.id}">${esc(e.label)}, ${e.date.slice(8)}.${e.date.slice(5, 7)}.</button>`).join("")}</div>` : `<form class="field-row" data-exam-form data-c="${id}"><input name="d" type="date" value="${esc(S.exDate[id] || "")}" aria-label="Prüfungstermin ${esc(c.course.short)}"><button class="btn small ghost">Speichern</button></form>`}</div>`; }).join("")}
      <p class="small" style="margin-top:6px">SoPol-Termin laut Semesterplan, Geschichte laut Einführungsfolie. Bei Geschichte kommt die schriftliche Reflexion mit mindestens 3500 Zeichen dazu.</p></section>
    <section class="section"><h2>Folien</h2>
      ${S.key ? `<p>Folien sind freigeschaltet.</p>` : `<p>Folien sind gesperrt. Gib den Code ein, um sie zu öffnen.</p><form class="field-row" data-unlock-form><input type="text" name="code" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Zugangscode" aria-label="Zugangscode"><button class="btn small">Freischalten</button></form><p class="small" data-unlock-msg></p>`}
      ${S.key ? `<div class="field-row"><button class="btn small ghost" data-offline>${S.offline ? "Folien und Texte neu für offline laden" : "Alle Folien und Texte für offline laden (ca. 130 MB)"}</button></div><div id="dl" hidden><div class="progress"><i style="width:0"></i></div><p class="small" style="margin-top:4px"></p></div>` : ""}
    </section>
    <section class="section"><h2>Fortschritt übertragen</h2>
      <p class="small">Dein Fortschritt liegt nur auf diesem Gerät. Kopiere den Text zum Handy oder Laptop, um dort weiterzulernen.</p>
      <div class="field-row"><button class="btn small ghost" data-export>Sicherung erzeugen</button></div>
      <textarea id="bak" placeholder="Sicherung hier einfügen" aria-label="Sicherung" style="min-height:76px"></textarea>
      <div class="field-row"><button class="btn small ghost" data-import>Sicherung übernehmen</button><button class="btn small ghost" data-reset>Fortschritt löschen</button></div><p class="small" id="bakmsg"></p>
    </section>
    <section class="section"><h2>Woher der Inhalt kommt</h2>
      ${COURSE_IDS.map(id => { const c = DATA[id].course; return `<p class="small" style="margin-top:6px"><b>${esc(id === "geschichte" ? "Geschichte" : c.name)}.</b> ${esc(c.source || "Fragen und Zusammenfassungen wurden aus den Folien, der Zeittafel und dem Zusatztext „100 Jahre Wiener Jugendamt“ geschrieben und mit den Seiten verknüpft. Der Reader ist noch nicht enthalten.")}</p>`; }).join("")}
    </section></div>`;
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
  slideChrome(`<div class="v-msg"><h2>Folie nicht verfügbar</h2><p>Diese Seite ist nicht auf dem Gerät gespeichert und es gibt gerade kein Netz. Unter „Ich“ kannst du alle Folien und Texte für offline laden.</p></div>`);
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
  txt.textContent = failed ? `${failed} Dateien fehlen noch. Versuch es mit besserem Netz nochmal.` : "Alle Folien und Texte sind auf dem Gerät gespeichert.";
  if (!failed) { S.offline = true; save(); }
}

/* ---------- Ereignisse ---------- */
function checkCalc(form) {
  const k = R.items[R.i], raw = form.v.value.trim().replace(/\s/g, "").replace(/€/g, "");
  if (!raw) return;
  const v = parseFloat(raw.includes(",") ? raw.replace(/\./g, "").replace(",", ".") : raw);
  const ok = Math.abs(v - k.answer) <= k.tol, gain = score(k, ok), fmt = x => x.toLocaleString("de-AT", { minimumFractionDigits: Number.isInteger(x) ? 0 : 2, maximumFractionDigits: 2 });
  feedback(k, ok, gain, `${ok ? "" : `<div class="opt wrong">Deine Antwort: ${esc(raw)}</div>`}<div class="opt right">${fmt(k.answer)} ${esc(k.unit)}</div><ol class="calc-steps">${k.steps.map(s => `<li>${esc(s)}</li>`).join("")}</ol>`);
}
document.addEventListener("click", e => {
  const b = e.target.closest("button, summary, details"); if (!b) return;
  const a = n => b.getAttribute(n), has = n => b.hasAttribute(n);
  if (has("data-slide")) { const [d, p] = a("data-slide").split(":"); openSlide(d, +p); return; }
  if (has("data-v-close")) { history.back(); return; }
  if (has("data-v-prev")) { V.page--; renderSlide(); return; }
  if (has("data-v-next")) { V.page++; renderSlide(); return; }
  if (has("data-v-mode")) { V.mode = V.mode === "text" ? "bild" : "text"; renderSlide(); return; }
  if (has("data-v-zoom")) { V.zoom = !V.zoom; V.mode = "bild"; $(".v-body", viewerEl)?.classList.toggle("zoom", V.zoom); b.setAttribute("aria-pressed", V.zoom); if (!$(".v-img", viewerEl)) renderSlide(); return; }
  if (has("data-link-read")) { const id = a("data-link-read"); if (!S.links[id]) { S.links[id] = 1; addXp(5, null); questTick("links"); save(); } b.replaceWith(Object.assign(document.createElement("p"), { className: "small", textContent: "Gelesen, +5 XP" })); return; }
  if (has("data-net")) { netFilter = a("data-net"); viewNet(); return; }
  if (has("data-go")) { if (R) quitRun(); go(a("data-go")); return; }
  if (has("data-run")) { startRun(a("data-run")); return; }
  if (has("data-ch-run")) { startRun("chapter", { ch: a("data-ch-run") }); return; }
  if (has("data-lf-run")) { startRun("lf", { n: +a("data-lf-run") }); return; }
  if (has("data-open-run")) { startRun("open", { n: +a("data-open-run") }); return; }
  if (has("data-case-all")) { startRun("case", { id: a("data-case-all") }); return; }
  if (has("data-case-drill")) { startRun("casedrill", { id: a("data-case-drill") }); return; }
  if (has("data-case-sec")) { const [id, key] = a("data-case-sec").split(":"); startRun("casesec", { id, key }); return; }
  if (has("data-exam")) { S.ex[D.course.id] = a("data-exam"); save(); route(); return; }
  if (has("data-exam2")) { const [c, id] = a("data-exam2").split(":"); S.ex[c] = id; save(); route(); return; }
  if (has("data-stoff-tab")) { stoffTab = a("data-stoff-tab"); viewStoff(); return; }
  if (has("data-quit")) { history.back(); return; }
  if (has("data-next")) { nextCard(); return; }
  if (has("data-reveal")) { revealOpen(R.items[R.i]); return; }
  if (has("data-open-done")) { finishOpen(R.items[R.i]); return; }
  if (has("data-offline")) { downloadAll(); return; }
  if (has("data-export")) { const t = $("#bak"); t.value = b64.to(new TextEncoder().encode(JSON.stringify({ ...S, key: null }))); t.select(); navigator.clipboard?.writeText(t.value).then(() => $("#bakmsg").textContent = "In die Zwischenablage kopiert.").catch(() => {}); return; }
  if (has("data-import")) { try { const key = S.key; S = migrate({ ...blank(), ...JSON.parse(new TextDecoder().decode(b64.from($("#bak").value.trim()))), key }); save(); viewMe(); $("#bakmsg").textContent = "Sicherung übernommen."; } catch { $("#bakmsg").textContent = "Dieser Text ist keine gültige Sicherung."; } return; }
  if (has("data-reset")) { if (confirm("Fortschritt auf diesem Gerät löschen?")) { const key = S.key; S = { ...blank(), key }; save(); route(); } return; }
  if (has("data-chain-next")) {
    const k = R.items[R.i], s = R.state; s.step++;
    if (s.step < k.steps.length) renderChain(k);
    else { const ok = s.errors === 0, gain = score(k, ok); feedback(k, ok, gain, k.steps.map((st, i) => `<div class="opt ${s.log[i] ? "right" : "missed"}"><small>${esc(st.q)}</small><br>${esc(st.right)}</div>`).join("")); }
    return;
  }
  if (!R || R.answered) return;
  const k = R.items[R.i], s = R.state;
  if (has("data-mc")) {
    const o = s.opts[+a("data-mc")], ok = o === k.right, gain = score(k, ok);
    if (R.kind === "blitz") return blitzNext(ok, k);
    feedback(k, ok, gain, (ok ? "" : `<div class="opt wrong">${esc(o)}</div>`) + `<div class="opt right">${esc(k.right)}</div>`);
  } else if (has("data-tf")) {
    const v = a("data-tf") === "1", ok = v === k.val, gain = score(k, ok);
    if (R.kind === "blitz") return blitzNext(ok, k);
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
  } else if (has("data-bk")) {
    const it = k.items[s.order[s.at]], ok = it[1] === +a("data-bk");
    if (!ok) s.wrong.push(s.order[s.at]);
    s.at++;
    if (s.at < k.items.length) { renderBucket(k, ok ? "good" : "bad"); return; }
    const good = !s.wrong.length, gain = score(k, good);
    feedback(k, good, gain, k.buckets.map((name, bi) => `<div class="bk-res"><b>${esc(name)}</b>${k.items.map((x, i) => x[1] === bi ? `<span class="${s.wrong.includes(i) ? "miss" : ""}">${esc(x[0])}</span>` : "").join("")}</div>`).join(""));
  } else if (has("data-chain")) {
    if (s.answeredStep) return;
    s.answeredStep = true;
    const st = k.steps[s.step], o = s.opts[+a("data-chain")], ok = o === st.right;
    s.log[s.step] = ok; if (!ok) s.errors++;
    if (navigator.vibrate) navigator.vibrate(ok ? 12 : [25, 40, 25]);
    main.querySelector(".answers").outerHTML = `<div class="given">${ok ? "" : `<div class="opt wrong">${esc(o)}</div>`}<div class="opt right">${esc(st.right)}</div></div><p class="why">${esc(st.why)}</p>${chips(st.src)}<div class="sticky"><button class="btn" data-chain-next>Weiter</button></div>`;
    $("[data-chain-next]").focus({ preventScroll: true });
  }
});
function blitzNext(ok, k) {
  R.end += ok ? 1500 : -4000;
  if (!ok) toast("Nicht ganz: " + (k.type === "mc" ? k.right : (k.val ? "Stimmt" : "Falsch")));
  R.i++;
  if (R.i >= R.items.length || R.end <= Date.now()) { clearInterval(R.timer); renderArrive(); return; }
  renderCard();
}
document.addEventListener("toggle", e => { const d = e.target; if (d.tagName === "DETAILS" && d.dataset.peek && d.open) { S["peek" + d.dataset.peek] = 1; save(); } }, true);
document.addEventListener("submit", e => {
  if (e.target.matches("[data-unlock-form]")) { e.preventDefault(); handleUnlock(e.target); }
  else if (e.target.matches("[data-calc-form]")) { e.preventDefault(); if (R && !R.answered) checkCalc(e.target); }
  else if (e.target.matches("[data-exam-form]")) { e.preventDefault(); const id = e.target.dataset.c || D.course.id; S.exDate[id] = e.target.d.value; save(); route(); }
});
document.addEventListener("keydown", e => {
  if (e.target.matches("input, textarea")) return;
  if (e.key === "Escape" && !viewerEl.hidden) { history.back(); return; }
  if (!R) return;
  if (e.key === "Enter") { const c = $("[data-chain-next]"); if (c) { e.preventDefault(); c.click(); return; } }
  if (e.key === "Enter" && R.answered) { e.preventDefault(); nextCard(); return; }
  const n = +e.key;
  if (n >= 1 && n <= 5) { const opts = main.querySelectorAll("[data-mc],[data-tf],[data-multi],[data-bk],[data-chain]"); opts[n - 1]?.click(); }
});

/* ---------- Navigation ---------- */
function go(hash) { if (location.hash === hash) route(); else location.hash = hash; }
function quitRun() { if (R) endRun(); }
function route() {
  const h = location.hash.replace(/^#/, "") || "/";
  if (h === "/fahrt") { if (R) return; history.replaceState(null, "", "#/"); return route(); }
  if (R) endRun();
  let p = h.split("/").filter(Boolean);
  if (p[0] === "lf" || p[0] === "stoff") p = ["geschichte", ...p]; // alte Links
  if (p[0] === "angekommen") p = S.last ? [S.last] : [];
  if (COURSE_IDS.includes(p[0])) {
    useCourse(p[0]); save();
    const sub = p[1], tab = !sub ? "home" : sub;
    renderNav(tab === "fall" ? "home" : tab, D);
    if (!sub) viewHome();
    else if (sub === "lf") p[2] ? viewLfDetail(+p[2]) : viewLf();
    else if (sub === "stoff") p[2] ? viewChapter(p[2]) : viewStoff();
    else if (sub === "fall") viewCase(p[2]);
    else viewHome();
  } else if (p[0] === "ich") { clearCourse(); renderNav("me", D && S.last ? DATA[S.last] : null); viewMe(); }
  else if (p[0] === "netz") { renderNav("netz"); viewNet(); }
  else { renderNav("hub"); viewHub(); }
  window.scrollTo(0, 0);
  main.focus({ preventScroll: true });
}
window.addEventListener("hashchange", route);
window.addEventListener("popstate", () => {
  if (!viewerEl.hidden && !history.state?.viewer) { closeSlide(); return; }
  if (R && !history.state?.run) { quitRun(); route(); }
});

(async function init() {
  const [m, lk, ...cs] = await Promise.all([fetch("slides/manifest.json").then(r => r.json()), fetch("data/links.json").then(r => r.json()), ...COURSE_IDS.map(id => fetch(`data/${id}.json`).then(r => r.json()))]);
  M = m; LINKS = lk.links; WEB = lk.web;
  cs.forEach((c, i) => {
    const id = COURSE_IDS[i];
    c.course.id = id; DATA[id] = c;
    if (id === "geschichte") Object.assign(c.course, { short: "Geschichte", openNamePl: "Leitfragen", modes: ["blitz"], lineTitle: c.course.name, ranks: LEVELS.slice(0, 9) });
    c.topics.forEach(t => { TOPIC[t.id] = t; });
    c.chapters.forEach(ch => { CHAPTER[ch.id] = ch; });
    c.cards.forEach(k => { k.course = id; CARD[k.id] = k; });
    c.leitfragen.forEach(l => { l.course = id; });
  });
  const hk = location.hash.match(/^#key=(.+)$/);
  if (hk) {
    try { await unlock(decodeURIComponent(hk[1])); } catch {}
    history.replaceState(null, "", location.pathname);
  }
  await restoreKey();
  route();
  if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});
})().catch(err => { console.error(err); main.innerHTML = `<div class="pad"><h1 class="h1">Die Daten konnten nicht geladen werden</h1><p class="lead">Prüfe die Internetverbindung und lade die Seite neu.</p></div>`; });
