"use strict";
/* Sprengel: mobiles Lernzentrum fuer mehrere Lehrveranstaltungen. Keine Bibliotheken, Fortschritt liegt im localStorage des Geraets. */

const STORE = "sprengel.v1";
const DAILY_GOAL = 60;
const BOX_DAYS = [0, 1, 2, 4, 8, 16];
const COURSE_IDS = ["matsi", "recht", "sopol", "faelle", "geschichte", "orbe"];
const MODULE = ["matsi", "recht", "sopol", "faelle"];
const COURSE_DOCS = {
  geschichte: ["e", "a1", "a2", "eb", "rw", "t", "n", "zs", "z", "lf", "j"], matsi: ["msp", "msk"],
  recht: ["f2", "f3", "f4", "f5", "f6", "f7", "rv", "r2", "r3"], sopol: ["s1", "s2", "s3", "s4", "s5", "s6", "zb", "zf", "zn", "zt", "zw"],
  orbe: ["ob"], faelle: ["cr", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "cu", "cb"],
};
const NAV_LABEL = { geschichte: "Leitfragen", recht: "Fernlehre", matsi: "Fragen", sopol: "Kernfragen", orbe: "Fragen" };
const COURSE_LINE = {
  geschichte: "Leitfragen, Zeitstrahl, Personen", matsi: "WMS, Wohnen, Schulden", recht: "Fernlehren, Instanzen, Fristen",
  sopol: "Gerechtigkeit, Sozialstaat, Arbeit, Vermögen", faelle: "11 Fälle nach dem Raster", orbe: "Berufsfelder, Einrichtungen, Altfragen",
};
// Stufen: ein Berufsweg der Sozialen Arbeit in sechs Etappen, die Abstaende wachsen. Danach Ehrenstufen ohne Ende.
const ETAPPEN = [
  ["Studium", "#4F7A64", ["Erstsemester", "Hörsaal", "Lerngruppe", "Hospitation", "Referat", "Praktikum", "Reflexion"]],
  ["Praxis", "#2C6A8A", ["Erstgespräch", "Hausbesuch", "Beratungsstelle", "Streetwork", "Sozialraum", "Netzwerk", "Supervision"]],
  ["Fachkraft", "#6B4A99", ["Hilfeplan", "Case Management", "Krisenintervention", "Clearing", "Gemeinwesenarbeit", "Anwaltschaft", "Fachkraft"]],
  ["Expertise", "#A4243B", ["Fachberatung", "Praxisanleitung", "Konzeptarbeit", "Qualitätszirkel", "Fachtagung", "Teamleitung", "Expertise"]],
  ["Gestaltung", "#A85A17", ["Projektleitung", "Sozialplanung", "Einrichtungsleitung", "Stellungnahme", "Sozialpolitik", "Lehrauftrag"]],
  ["Wirkung", "#B8860B", ["Forschung", "Fachbuch", "Begutachtung", "Sozialreform", "Ehrenpreis", "Lebenswerk"]],
];
const LEVELS = ETAPPEN.flatMap(([et, col, names], ei) => names.map(name => ({ name, et, ei, col }))).map((l, k) => ({ ...l, n: k + 1, xp: Math.round((60 * k * k + 90 * k) / 50) * 50 }));
const HONOR = 12000; // nach der letzten Stufe: alle 12.000 XP ein Stern
const GESCH_RANKS = [
  [0, "Ehrenamt"], [150, "Berufspflege"], [400, "Fachkurs"], [800, "Fürsorgeschule"], [1400, "Sprengeldienst"],
  [2200, "Case Work"], [3200, "Sozialakademie"], [4500, "FH-Diplom"], [6500, "Master"], [9000, "Fachaufsicht"], [12500, "Lehrauftrag"], [17000, "Sprengelleitung"],
];
// Abzeichen mit Stufen: [id, Name, Text je Schwelle, Schwellen, aktueller Wert]
const TIER = ["Bronze", "Silber", "Gold", "Platin"];
const BADGES = [
  ["streak", "Dranbleiben", n => `${n} Tage in Folge gelernt`, [3, 7, 14, 30], s => s.bestStreak],
  ["goal", "Tagesziel", n => `An ${n} Tagen das Tagesziel geschafft`, [5, 20, 60], s => Object.values(s.days).filter(v => v >= DAILY_GOAL).length],
  ["cards", "Kartenstapel", n => `${n} Antworten gegeben`, [100, 500, 1500, 4000], s => Object.values(s.cards).reduce((a, c) => a + (c.seen || 0), 0)],
  ["learned", "Sitzt", n => `${n} Karten sicher gelernt`, [50, 200, 500, 800], s => Object.values(s.cards).filter(c => c.box >= 2).length],
  ["combo", "Lauf", n => `${n} richtige Antworten in Folge`, [10, 25, 50], s => s.bestCombo],
  ["open", "Frei formuliert", n => `${n} offene Fragen beantwortet`, [5, 25, 75], s => s.opens],
  ["stufen", "Stufenweise", n => `${n} offene Fragen über Erkennen und Ergänzen erarbeitet`, [3, 15, 40], s => Object.values(s.lfStage).filter(v => v >= 2).length],
  ["stamps", "Stempelsammlung", n => `${n} Stempel in allen LVs zusammen`, [10, 40, 90], () => allStamps()],
  ["boss", "Bossbezwinger*in", n => `${n} ${n === 1 ? "Kapitel-Boss" : "Kapitel-Bosse"} besiegt`, [1, 10, 30], s => Object.keys(s.boss).length],
  ["akten", "Akte zu", n => `${n} ${n === 1 ? "Akte" : "Akten"} abgeschlossen`, [1, 5, 11], s => Object.keys(s.akten).length],
  ["exam", "Probe aufs Exempel", n => `${n} Probeläufe oder Simulationen`, [1, 5, 15], s => s.exams],
  ["plan", "Nach Plan", n => `${n}-mal den Prüfungsplan des Tages erfüllt`, [3, 10, 25], s => s.planDone],
  ["blitz", "Blitzmerker*in", n => `${n} Richtige in einer Blitzrunde`, [10, 20, 30], s => Math.max(0, ...Object.values(s.blitz))],
  ["links", "Brückenbauer*in", n => `${n} Exkurse gelesen`, [5, 15, 25], s => Object.keys(s.links).length],
  ["wide", "Breit aufgestellt", n => `In ${n} Lehrveranstaltungen gelernt`, [3, 6], s => Object.values(s.cx).filter(v => v > 0).length],
  ["backup", "Sicher ist sicher", () => "Eine Sicherungsdatei gespeichert", [1], s => s.backups],
];
const tierOf = b => { const v = b[4](S) || 0; return { v, t: b[3].filter(x => v >= x).length }; };
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
  cx: {}, ex: {}, exDate: {}, cases: {}, links: {}, blitz: {}, q: null, last: null,
  lfStage: {}, boss: {}, akten: {}, aktOk: {}, plan: null, planDone: 0, bd: null, lvSeen: null, backups: 0, lastBackup: null });
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
  let i = 0; while (i + 1 < LEVELS.length && xp >= LEVELS[i + 1].xp) i++;
  const L = LEVELS[i], top = LEVELS[LEVELS.length - 1];
  if (i + 1 < LEVELS.length) { const nx = LEVELS[i + 1]; return { ...L, i, honor: 0, next: nx, toNext: nx.xp - xp, pct: (xp - L.xp) / (nx.xp - L.xp) }; }
  const honor = Math.floor((xp - top.xp) / HONOR), base = top.xp + honor * HONOR;
  return { ...L, i, honor, name: honor ? `${top.name} ★${honor}` : top.name, next: { name: `${top.name} ★${honor + 1}`, xp: base + HONOR }, toNext: base + HONOR - xp, pct: (xp - base) / HONOR };
}
const levelKey = lv => lv.n * 1000 + lv.honor;
function rank(c) {
  const xp = S.cx[c.course.id] || 0, r = c.course.ranks;
  if (!r) return null;
  let i = 0; while (i + 1 < r.length && xp >= r[i + 1][0]) i++;
  if (r[i + 1]) return { name: r[i][1], next: r[i + 1], xp, pct: (xp - r[i][0]) / (r[i + 1][0] - r[i][0]) };
  const last = r[r.length - 1], step = Math.max(500, Math.round(last[0] / 4 / 50) * 50), h = Math.floor((xp - last[0]) / step), base = last[0] + h * step;
  return { name: h ? `${last[1]} ★${h}` : last[1], next: [base + step, `${last[1]} ★${h + 1}`], xp, pct: (xp - base) / step };
}
// Emblem: Sechseck in der Farbe der Etappe, der Ring zeigt den Weg zur naechsten Stufe
function emblem(lv, size = 64, ring = true) {
  const r = 28, C = 2 * Math.PI * r, hex = [...Array(6)].map((_, k) => { const a = Math.PI / 3 * k - Math.PI / 2; return `${(32 + 20 * Math.cos(a)).toFixed(1)},${(32 + 20 * Math.sin(a)).toFixed(1)}`; }).join(" ");
  return `<svg class="emblem" width="${size}" height="${size}" viewBox="0 0 64 64" aria-hidden="true">
    ${ring ? `<circle cx="32" cy="32" r="${r}" fill="none" stroke="currentColor" stroke-opacity=".22" stroke-width="5"/><circle cx="32" cy="32" r="${r}" fill="none" stroke="var(--mustard)" stroke-width="5" stroke-linecap="round" stroke-dasharray="${(Math.max(.02, lv.pct) * C).toFixed(1)} ${C.toFixed(1)}" transform="rotate(-90 32 32)"/>` : ""}
    <polygon points="${hex}" fill="${lv.col}" stroke="#fff" stroke-opacity=".55" stroke-width="1.5"/>
    <text x="32" y="${lv.honor ? 36 : 39}" text-anchor="middle" font-family="Big Shoulders, Arial Narrow, sans-serif" font-weight="800" font-size="${lv.n > 9 ? 18 : 20}" fill="#fff">${lv.n}</text>
    ${lv.honor ? `<text x="32" y="47" text-anchor="middle" font-size="8" fill="#fff">★${lv.honor}</text>` : ""}</svg>`;
}
const allStamps = () => COURSE_IDS.filter(id => DATA[id]?.leitfragen.length).reduce((a, id) => a + stampCount(DATA[id]), 0);
// Stufenaufstieg und neue Abzeichen werden gefeiert, sobald eine Runde fertig ist
function celebrateBadges() {
  if (!S.bd) S.bd = Object.fromEntries(BADGES.map(b => [b[0], tierOf(b).t]));
  const newB = BADGES.map(b => ({ b, ...tierOf(b) })).filter(x => x.t > (S.bd[x.b[0]] || 0));
  newB.forEach(x => S.bd[x.b[0]] = x.t); save();
  return newB;
}
function celebrate() {
  const lv = level(), key = levelKey(lv);
  if (S.lvSeen == null) S.lvSeen = key;
  if (key > S.lvSeen) {
    const prev = S.lvSeen; S.lvSeen = key; save();
    const prevEi = LEVELS[Math.min(LEVELS.length, Math.floor(prev / 1000)) - 1]?.ei;
    showLevelUp(lv, prevEi !== undefined && prevEi < lv.ei);
  }
  save();
}
function showLevelUp(lv, newEt) {
  const box = document.createElement("div");
  box.className = "lvup"; box.setAttribute("role", "dialog"); box.setAttribute("aria-label", "Neue Stufe");
  box.innerHTML = `<div class="lvup-in" style="--lc:${lv.col}"><div class="lvup-burst"></div>${emblem({ ...lv, pct: 1 }, 132)}
    <p class="lvup-kick">${newEt ? `Neue Etappe: ${esc(lv.et)}` : lv.honor ? "Ehrenstufe" : "Neue Stufe"}</p><h2>${esc(lv.name)}</h2>
    <p class="small">Stufe ${lv.n} von ${LEVELS.length}${lv.honor ? `, ${lv.honor}. Stern` : ""}. ${lv.next ? `Bis „${esc(lv.next.name)}“ fehlen ${lv.toNext.toLocaleString("de-AT")} XP.` : ""}</p>
    <button class="btn" data-lvup-close>Weiter</button></div>`;
  document.body.append(box);
  box.querySelector("button").focus();
  if (navigator.vibrate) navigator.vibrate([20, 60, 20, 60, 40]);
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
/* ---------- Pruefungsplan: rueckwaerts vom Termin ---------- */
// Arbeit bis zur Pruefung: neue oder falsche Karten brauchen zwei richtige Antworten, Box 1 noch eine, faellige Wiederholungen eine.
function planNeed(c) {
  let need = 0; const now = Date.now();
  for (const k of c.cards) { if (k.extra) continue; const st = S.cards[k.id]; need += !st || st.box === 0 ? 2 : st.box === 1 ? 1 : st.due <= now ? 1 : 0; }
  return need;
}
function planDay() { const d = dayKey(); if (!S.plan || S.plan.day !== d) S.plan = { day: d, t: {}, n: {}, done: [] }; return S.plan; }
function planFor(c) {
  const id = c.course.id; if (id === "faelle" || !c.cards.length) return null;
  const ex = daysToExam(c); if (!ex || ex.left < 1) return null;
  const p = planDay();
  if (p.t[id] === undefined) { const need = planNeed(c); p.t[id] = need ? Math.min(60, Math.max(5, Math.ceil(need / Math.max(1, ex.left - 1)))) : 0; save(); } // letzter Tag bleibt fuer Wiederholung
  const learnedN = c.cards.filter(k => !k.extra && learned(k)).length, all = c.cards.filter(k => !k.extra).length;
  return { id, c, ex, target: p.t[id], did: p.n[id] || 0, pct: all ? learnedN / all : 0, done: p.done.includes(id) };
}
const plans = () => COURSE_IDS.map(id => DATA[id] && planFor(DATA[id])).filter(Boolean).sort((a, b) => a.ex.left - b.ex.left);
function planTick(cid) {
  const c = DATA[cid]; if (!c) return;
  const pl = planFor(c); if (!pl) return;
  const p = planDay(); p.n[cid] = (p.n[cid] || 0) + 1;
  if (pl.target && p.n[cid] >= pl.target && !p.done.includes(cid)) {
    p.done.push(cid); S.planDone = (S.planDone || 0) + 1; S.xp += 10; S.cx[cid] = (S.cx[cid] || 0) + 10; S.days[dayKey()] = (S.days[dayKey()] || 0) + 10;
    toast(`Prüfungsplan ${c.course.short} für heute erfüllt. +10 XP`);
  }
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
// Offene Fragen zaehlen zum Fortschritt, sobald der Lueckentext (Stufe 2) sitzt; der Stempel verlangt weiter die freie Antwort.
const lfDone = (l, c = DATA[l.course]) => (canStage(l) && stageOf(l, c) >= 2) || openCredit(S.lfOpen[lfKey(l.n, c)]?.best || 0) >= .5;
const lfsIn = (ch, c = D) => c.leitfragen.filter(l => l.ch === ch);
function chapterPct(ch) { const c = cardsIn(ch), l = lfsIn(ch), n = c.length + l.length; return n ? (c.filter(learned).length + l.filter(x => lfDone(x)).length) / n : 0; }
const answered = k => (S.cards[k.id]?.box || 0) >= 1; // zuletzt richtig beantwortet
const cardCount = cards => `${cards.filter(answered).length} von ${cards.length} ${cards.length === 1 ? "Karte" : "Karten"} richtig beantwortet`;
function coursePct(c) { const m = c.cards.filter(k => !k.extra), l = c.leitfragen || [], n = m.length + l.length; return n ? (m.filter(learned).length + l.filter(x => lfDone(x, c)).length) / n : 0; }
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
    const sub = id === "faelle" ? `${Object.keys(S.akten).length} von ${allCases().length} Akten abgeschlossen` : `${stampCount(c)} von ${c.leitfragen.length} ${esc(c.course.openNamePl || "Leitfragen")} gestempelt`;
    return `<button class="tile" data-go="#/${id}" style="--c:${c.course.accent || "#0F3D3E"}"><span class="tile-top"><b>${esc(id === "geschichte" ? "Geschichte der Sozialen Arbeit" : c.course.name)}</b>${ex && ex.left >= 0 ? `<em>${ex.left === 0 ? "Heute" : `${ex.left} ${ex.left === 1 ? "Tag" : "Tage"}`}</em>` : ""}</span>
      <span class="small">${esc(COURSE_LINE[id])}</span>
      <span class="tile-bar"><i style="width:${Math.round(pct * 100)}%"></i></span>
      <span class="small">${r ? esc(r.name) + ", " : ""}${sub}</span><span class="small">${cardCount(c.cards)}</span></button>`;
  };
  main.innerHTML = `<header class="hero"><div class="hero-in">
    <div class="hero-top"><h1>Sprengel</h1><button class="lvbtn" data-go="#/stufen" aria-label="Stufe ${lv.n}, ${esc(lv.name)}, alle Stufen ansehen">${emblem(lv, 58)}<span><b>${esc(lv.name)}</b><small>${esc(lv.et)}, Stufe ${lv.n}</small><small>noch ${lv.toNext.toLocaleString("de-AT")} XP ›</small></span></button></div>
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
    ${backupNag()}
    <section class="section"><h2>Modul Grundsicherung</h2><div class="tiles">${MODULE.map(tile).join("")}</div></section>
    <section class="section"><h2>Weitere Lehrveranstaltungen</h2><div class="tiles">${tile("orbe")}${tile("geschichte")}</div></section>
    <section class="section"><h2>Mehr zum Studium</h2><div class="tiles"><a class="tile ext" href="https://squeakycamp.github.io/sozialarbeitskarte/" target="_blank" rel="noopener" style="--c:#2E6B4F"><span class="tile-top"><b>Sozialarbeitskarte</b><em>öffnet neu ↗</em></span><span class="small">Wien-Karte sozialer Einrichtungen: wer was anbietet und wo</span></a></div></section>
  </div>`;
}
function backupNag() {
  if (Object.keys(S.cards).length < 20) return "";
  const ago = S.lastBackup ? dayDiff(S.lastBackup, dayKey()) : null;
  if (ago !== null && ago < 7) return "";
  return `<p class="nag">Dein Fortschritt liegt nur in diesem Browser. ${ago === null ? "Du hast noch keine Sicherung gespeichert." : `Letzte Sicherung vor ${ago} Tagen.`} <button data-backup-file>Jetzt als Datei sichern</button></p>`;
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
  const pl = planFor(D), bossReady = D.chapters.map(c => c.id).filter(ch => { const b = bossState(ch); return b && b.open && !b.beaten; });
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
      ${D.course.exam ? `<button data-px-start>Prüfungsmodus (${D.course.exam.n} Fragen, ${D.course.exam.minutes} Min.)</button>` : ""}
      <button data-run="exam">${id === "geschichte" ? "Probeprüfung mit 7 Fragen" : `Probelauf mit ${examN} offenen Fragen`}</button>
      ${modes.includes("blitz") ? `<button data-run="blitz">Blitzrunde${S.blitz[id] ? ` (Rekord ${S.blitz[id]})` : ""}</button>` : ""}
      ${modes.includes("chains") ? `<button data-run="chains">Fallketten</button>` : ""}
      ${modes.includes("rechner") ? `<button data-run="calc">WMS-Rechner</button>` : ""}
      ${bossReady.length ? `<button data-boss="${bossReady[0]}">Boss bereit: ${esc(chapterOf(bossReady[0]).name)}${bossReady.length > 1 ? ` (+${bossReady.length - 1})` : ""}</button>` : ""}
    </div>
    ${pl ? `<div class="hero-plan"><span>Prüfungsplan heute: ${pl.target === 0 ? "alles sitzt" : `${Math.min(pl.did, pl.target)} von ${pl.target} Antworten`}</span>${pl.done || pl.target === 0 ? "<b>✓</b>" : `<button data-plan="${id}">Plan-Runde</button>`}</div>` : ""}
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
        const b = bossState(c.id);
        return `<li class="stop ${p >= .8 ? "done" : p > 0 ? "begun" : ""} ${b?.beaten ? "gold" : ""}">
          <span class="fill" style="height:${i < firstOpen || firstOpen < 0 ? "100%" : i === firstOpen ? Math.round(p * 100) + "%" : "0"}"></span><span class="dot"></span>
          <button data-go="#/${id}/stoff/${c.id}"><h3>${esc(c.name)}</h3><div class="span">${esc(c.span)}${p > 0 ? `, ${Math.round(p * 100)} % gelernt` : ""}</div><div class="sub">${esc(c.line)}</div><div class="sub count">${cardCount(cardsIn(c.id))}${b?.beaten ? `, <span class="bosstag">Boss besiegt</span>` : b?.open ? `, <span class="bosstag ready">Boss bereit</span>` : ""}</div></button>
        </li>`;
      }).join("")}
    </ol>
  </div>`;
}

/* ---------- Fallwerkstatt ---------- */
// Akten: 6 Rasterschritte (ab 50 %) plus Fallkette und Prioritaeten (einmal richtig) ergeben die Stempel; dann laesst sich die Akte schliessen.
const aktNo = cs => `GZ 2026/F${String(allCases().indexOf(cs) + 1).padStart(2, "0")}`;
function aktStamps(cs) {
  const secs = DATA.faelle.sections.map(s => ({ label: s.title, kind: "sec", key: s.key, ok: (S.cases[cs.id]?.[s.key] || 0) >= .5 }));
  const cards = DATA.faelle.cards.filter(k => k.topic === "f-" + cs.id && (k.type === "chain" || k.type === "ord"))
    .map(k => ({ label: k.type === "chain" ? "Fallkette" : "Prioritäten", kind: "card", key: k.id, ok: !!S.aktOk[k.id] || (S.cards[k.id]?.box || 0) >= 1 }));
  return [...secs, ...cards];
}
const aktReady = cs => aktStamps(cs).every(x => x.ok);
function aktTile(cs) {
  const st = aktStamps(cs), closed = S.akten[cs.id], n = st.filter(x => x.ok).length;
  return `<button class="akt-tile ${closed ? "closed" : ""}" data-go="#/faelle/fall/${cs.id}"><span class="akt-tab">${aktNo(cs)}</span>
    <span class="tile-top"><b>${esc(cs.title)}</b>${closed ? `<em class="akt-mini">Erledigt</em>` : aktReady(cs) ? `<em>Bereit zum Schließen</em>` : ""}</span>
    <span class="small">${esc(cs.who)}</span>
    <span class="akt-dots" aria-label="${n} von ${st.length} Vermerken">${st.map(x => `<i class="${x.ok ? "on" : ""}"></i>`).join("")}</span>
    ${closed ? `<span class="small">Abgeschlossen am ${closed.slice(8)}.${closed.slice(5, 7)}.</span>` : `<span class="ctags">${cs.tags.map(t => `<span class="ctag plain">${esc(t)}</span>`).join("")}</span>`}</button>`;
}
function viewCases() {
  const r = rank(D), cases = allCases(), wrong = wrongCards(["faelle"]).length;
  const open = cases.filter(cs => !S.akten[cs.id]), arch = cases.filter(cs => S.akten[cs.id]);
  main.innerHTML = `<header class="hero"><div class="hero-in">
    <div class="hero-top"><h1>Fallwerkstatt</h1><div class="level">${esc(r.name)}<br>${r.xp} XP</div></div>
    <div class="stats"><div class="stat"><b>${arch.length}/${cases.length}</b><span>Akten abgeschlossen</span></div><div class="stat"><b>${S.blitz.faelle || 0}</b><span>Blitz-Rekord</span></div></div>
    <div class="starts"><button class="start" data-run="randcase"><b>Zufallsfall</b><span>Alle 6 Rasterschritte, wie in der Prüfung</span></button><button class="start alt" data-run="drill"><b>Drill</b><span>Fallketten und Prioritäten aus allen Fällen</span></button></div>
    <div class="quick">${wrong ? `<button data-run="wrong">Fehler üben (${wrong})</button>` : ""}<button data-run="blitz">Blitzrunde</button><button data-slide="cr:1">Fallanalyseraster öffnen</button></div>
  </div></header>
  <div class="pad">
    <p class="note upcoming">Fallbearbeitung geht vor allem über MATS. Punkte mit Recht-Blick und SoPol-Blick zeigen die Zusammenhänge. Die Lösungspunkte sind von Claude aus den Unterlagen abgeleitet und nicht von den Lehrenden; andere gut begründete Lösungen können genauso richtig sein.</p>
    <h2 class="line-title">Offene Akten</h2>
    <p class="small" style="margin-top:4px">Jede Akte hat 8 Vermerke: die 6 Schritte des Rasters (ab 50 % der Punkte) sowie Fallkette und Prioritäten (einmal richtig). Sind alle gestempelt, schließt du die Akte.</p>
    <div class="akten">${open.length ? open.map(aktTile).join("") : `<p class="small">Alle Akten sind abgeschlossen. Stark!</p>`}</div>
    ${arch.length ? `<h2 class="line-title">Archiv</h2><div class="akten">${arch.map(aktTile).join("")}</div>` : ""}
  </div>`;
}
function viewCase(id) {
  const cs = allCases().find(x => x.id === id);
  if (!cs) return viewCases();
  const secs = DATA.faelle.sections, st = aktStamps(cs), closed = S.akten[id], ready = aktReady(cs);
  const cardSt = st.filter(x => x.kind === "card");
  main.innerHTML = `<div class="pad"><button class="back" data-go="#/faelle">Alle Akten</button>
    <div class="akt ${closed ? "closed" : ""}"><div class="akt-head"><span class="akt-no">${aktNo(cs)}</span>${closed ? `<span class="akt-stamp">Erledigt</span>` : `<span class="akt-state">${st.filter(x => x.ok).length} von ${st.length} Vermerken</span>`}</div>
      <h1 class="h1">${esc(cs.title)}</h1><p class="lead">${esc(cs.where)}, ${esc(cs.who)}</p>
      <div class="ctags" style="margin-top:8px">${cs.tags.map(t => `<span class="ctag plain">${esc(t)}</span>`).join("")}</div>
      ${!closed && ready ? `<button class="btn akt-close" data-akt-close="${id}">Akte schließen, +50 XP</button>` : ""}
      ${closed ? `<p class="small" style="margin-top:10px">Abgeschlossen am ${closed.slice(8)}.${closed.slice(5, 7)}.${closed.slice(0, 4)}. Du kannst jederzeit weiter üben.</p>` : ""}</div>
    <div class="pcta"><button class="btn" data-case-all="${id}">Ganzes Raster bearbeiten</button><button class="btn ghost" data-case-drill="${id}">Fallkette und Prioritäten</button></div>
    <section class="section"><h2>Der Fall</h2><div id="casetext" class="casetext"><p>${esc(cs.lead)}</p></div>${chips([[cs.doc, 1]])}</section>
    <section class="section"><h2>Aktenvermerke</h2><ol class="lflist vermerke" style="margin-top:0">${secs.map(s => { const b = S.cases[id]?.[s.key]; return `<li class="${b >= .5 ? "done" : ""}"><button data-case-sec="${id}:${s.key}"><span class="n">${b >= .5 ? "✓" : s.n}</span><span>${esc(s.title)}<small>${b === undefined ? "Noch offen" : `Zuletzt beste Bewertung ${Math.round(b * 100)} %${b >= .5 ? ", gestempelt" : ", ab 50 % gestempelt"}`}</small></span></button></li>`; }).join("")}
      ${cardSt.map(x => `<li class="${x.ok ? "done" : ""}"><button data-case-drill="${id}"><span class="n">${x.ok ? "✓" : "·"}</span><span>${x.label}<small>${x.ok ? "Richtig gelöst, gestempelt" : "Einmal richtig lösen"}</small></span></button></li>`).join("")}</ol></section>
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
// Offene Fragen werden schrittweise schwerer: 1 Erkennen, 2 Ergaenzen, dann frei. In normalen Runden kommt die naechste offene Stufe.
const stageOf = (l, c = DATA[l.course]) => S.lfStage[lfKey(l.n, c)] || 0;
const canStage = l => l.points.length >= 2;
function lfItem(l, stage) {
  if (stage === 1 || stage === 2) return { type: "stage" + stage, id: `st${stage}-${l.course}-${l.n}`, lf: [l.n], leit: l };
  return { type: "open", id: "lf" + l.n, lf: [l.n], leit: l };
}
const nextStage = l => canStage(l) ? Math.min(3, stageOf(l) + 1) : 3;
const nextLfItem = l => lfItem(l, nextStage(l));
// Erst Stufe 1 aller Fragen, dann Stufe 2 aller, dann frei; innerhalb einer Stufe die schwaechsten zuerst.
function pickLf(n, focus) {
  const scored = shuffle(D.leitfragen).filter(l => !focus || l.ch === focus).sort((a, b) => nextStage(a) - nextStage(b) || lfScore(a.n) - lfScore(b.n));
  return scored.slice(0, n).map(nextLfItem);
}
function mixIn(items, extra) { // offene Fragen gleichmaessig zwischen die Karten
  const out = [...items], step = (out.length + 1) / (extra.length + 1);
  extra.forEach((x, i) => out.splice(Math.round(step * (i + 1)) + i, 0, x));
  return out;
}
/* ---------- Kapitel-Boss ---------- */
const BOSS_N = 10, BOSS_LIVES = 2;
function bossState(ch, c = D) {
  const chap = chapterOf(ch); if (!chap || chap.sober || chap.pending || c.course.id === "faelle") return null;
  const cards = c.cards.filter(k => topicOf(k.topic).ch === ch && !k.extra);
  if (cards.length < 6) return null;
  const p = cards.filter(learned).length / cards.length;
  return { cards, p, open: p >= .8, beaten: S.boss[ch] };
}
function bossItems(ch) {
  const b = bossState(ch); if (!b) return [];
  const hard = [...b.cards].sort((x, y) => (S.cards[y.id]?.wrong || 0) - (S.cards[x.id]?.wrong || 0) || (S.cards[x.id]?.box || 0) - (S.cards[y.id]?.box || 0));
  return spread(shuffle(hard.slice(0, Math.max(BOSS_N, Math.ceil(hard.length * .5)))).slice(0, BOSS_N));
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
    const cards = cardsIn(opts.ch), left = cards.filter(k => !learned(k)).length, todo = lfsIn(opts.ch).filter(l => !lfDone(l)).length;
    // Fehlen nur noch wenige Karten, kommen die offenen Fragen gleich mit, damit man nicht endlos Karten wiederholt.
    const nLf = !todo ? 1 : left <= 3 ? Math.min(todo, 4) : todo >= 3 ? 2 : 1;
    items = mixIn(pick(cards, left === 0 && todo ? 6 : 10), pickLf(nLf, opts.ch)); title = ch.name;
  } else if (kind === "lf") {
    const lf = D.leitfragen.find(l => l.n === opts.n);
    items = pick(D.cards.filter(k => k.lf.includes(opts.n)), 6);
    items.push(nextLfItem(lf)); title = `${openName()} ${lf.n}`;
  } else if (kind === "open") {
    const lf = D.leitfragen.find(l => l.n === opts.n);
    items = [lfItem(lf, opts.stage || 3)]; title = `${openName()} ${lf.n}`;
  } else if (kind === "lfgroup") {
    const ns = D.leitfragen.filter(l => l.group === opts.g).map(l => l.n);
    items = pick(D.cards.filter(k => k.lf.some(n => ns.includes(n))), 12); title = opts.g;
  } else if (kind === "boss") {
    items = bossItems(opts.ch); title = "Boss: " + chapterOf(opts.ch).name;
  } else if (kind === "plan") {
    const pl = planFor(D), n = Math.min(15, Math.max(5, pl ? pl.target - pl.did : 10));
    items = pick(D.cards.filter(k => !k.extra), n); title = "Prüfungsplan " + D.course.short;
  } else if (kind === "exam") {
    const n = D.course.id === "geschichte" ? 7 : Math.min(5, D.leitfragen.length);
    items = shuffle(D.leitfragen).slice(0, n).map(l => ({ type: "open", id: "lf" + l.n, lf: [l.n], leit: l, exam: true }));
    title = "Probeprüfung";
  } else if (kind === "pf") {
    const pool = pfCards().filter(k => !opts.block || k.pf === opts.block);
    items = opts.one ? pool.filter(k => k.id === opts.one) : spread(shuffle(pool).sort((a, b) => (S.cards[a.id]?.box || 0) - (S.cards[b.id]?.box || 0)).slice(0, 15));
    title = opts.block || pfName();
  } else if (kind === "pfwrong") {
    items = shuffle(pfCards().filter(k => S.cards[k.id]?.seen && S.cards[k.id].box === 0)); title = "Falsche wiederholen";
  } else if (kind === "pfexam") {
    const pf = D.course.pf, all = pfCards();
    items = shuffle(all).slice(0, Math.min(pf.n || all.length, all.length)); title = "Prüfungssimulation";
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
  R = { kind, title, items, i: 0, xp: 0, right: 0, total: 0, combo: 0, bestCombo: 0, retry: new Set(), missed: [], examPts: [0, 0], stampsBefore: D ? stampCount() : 0, start: Date.now(), answered: false, state: {}, origin: D?.course.id, skipped: 0 };
  if (kind === "boss") { R.boss = opts.ch; R.lives = BOSS_LIVES; }
  document.body.classList.add("running");
  history.pushState({ run: 1 }, "", "#/fahrt");
  if (kind === "blitz") { R.end = Date.now() + 60000; R.timer = setInterval(blitzTick, 250); R.wrongList = []; }
  if (kind === "pfexam") { R.quiet = true; R.end = Date.now() + D.course.pf.minutes * 60000; R.timer = setInterval(pfTick, 500); }
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

function pfTick() {
  if (!R) return;
  const left = R.end - Date.now(), lab = $("#pfclock");
  if (lab) lab.textContent = clock(left);
  if (left <= 0) { clearInterval(R.timer); R.timeout = true; renderArrive(); }
}
const clock = ms => { const t = Math.max(0, Math.ceil(ms / 1000)); return `${Math.floor(t / 60)}:${String(t % 60).padStart(2, "0")}`; };
function runHeader(item) {
  if (R.kind === "blitz") return `<div class="run-top"><button class="run-x" data-quit aria-label="Runde beenden">×</button><div class="track blitz"><i id="blitzbar" style="width:${Math.max(0, (R.end - Date.now()) / 600)}%"></i></div><div class="combo"><span id="blitzsec">${Math.max(0, Math.ceil((R.end - Date.now()) / 1000))}</span></div></div>`;
  const sober = isSober(item);
  const n = R.items.length;
  return `<div class="run-top"><button class="run-x" data-quit aria-label="Runde beenden">×</button>
    <div class="track" aria-label="Karte ${R.i + 1} von ${n}"><i style="width:${R.i / n * 100}%"></i>${n <= 18 ? R.items.map((_, i) => `<b class="${i < R.i ? "on" : ""}"></b>`).join("") : ""}</div>
    <div class="combo">${R.kind === "pfexam" ? `<span id="pfclock">${clock(R.end - Date.now())}</span>` : R.boss ? `<span class="hearts" aria-label="${R.lives} Herzen übrig">${"♥".repeat(Math.max(0, R.lives))}<s>${"♥".repeat(BOSS_LIVES - Math.max(0, R.lives))}</s></span>` : !sober && R.combo >= 3 ? `${R.combo}×` : ""}</div></div>`;
}
const isSober = item => item.topic ? chapterOf(topicOf(item.topic).ch).sober : (item.leit && chapterOf(item.leit.ch)?.sober);

function renderCard() {
  const k = R.items[R.i];
  R.answered = false; R.state = {};
  window.scrollTo(0, 0);
  if (k.type === "open") return renderOpen(k);
  if (k.type === "stage1") return renderStage1(k);
  if (k.type === "stage2") return renderStage2(k);
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
  if (R.kind === "blitz") gain = ok ? 3 : 0; // schnelles Durchklicken soll nicht die meisten XP bringen
  if (ok && k.course === "faelle" && (k.type === "chain" || k.type === "ord")) S.aktOk[k.id] = 1;
  if (ok) { R.right++; R.combo++; R.bestCombo = Math.max(R.bestCombo, R.combo); S.bestCombo = Math.max(S.bestCombo, R.combo); }
  else {
    R.combo = 0; R.missed.push(k);
    if (R.boss) R.lives--;
    if (!R.retry.has(k.id) && !["exam", "blitz", "pfexam", "boss"].includes(R.kind)) { R.retry.add(k.id); R.items.push(k); } // am Ende nochmal
  }
  R.xp += gain; addXp(gain, k.course); questTick("cards"); planTick(k.course); save();
  if (navigator.vibrate) navigator.vibrate(ok ? 12 : [25, 40, 25]);
  return gain;
}
function feedback(k, ok, gain, givenHtml) {
  if (R.quiet) { R.answered = true; nextCard(); return; }
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
    <div class="sticky"><button class="btn" data-next>${R.i + 1 < R.items.length && !(R.boss && R.lives <= 0) ? "Weiter" : "Ankommen"}</button></div></div>`;
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
    <div class="grow"></div><div style="margin-top:12px"><button class="btn" data-reveal>Antwort aufdecken</button>${skipBtn()}</div></div>`;
}
const skipBtn = () => `<button class="skip" data-skip>Überspringen, zählt nicht</button>`;
function skipItem() { R.skipped++; nextCard(); }

/* Stufe 1: Erkennen. Welche Punkte gehoeren zur Antwort? Dazwischen Punkte aus anderen Fragen derselben LV. */
function stageForeign(l, n) {
  const c = DATA[l.course], same = c.leitfragen.filter(x => x.n !== l.n && x.ch === l.ch), other = c.leitfragen.filter(x => x.n !== l.n && x.ch !== l.ch);
  const pool = [...shuffle(same.flatMap(x => x.points)), ...shuffle(other.flatMap(x => x.points))];
  const own = new Set(l.points.map(p => p.t)), out = [];
  for (const p of pool) { if (out.length >= n) break; if (!own.has(p.t) && !out.some(o => o.t === p.t)) out.push(p); }
  return out;
}
function renderStage1(k) {
  const l = k.leit, s = R.state;
  if (!s.opts) {
    const own = shuffle(l.points).slice(0, 6), foreign = stageForeign(l, Math.min(4, Math.max(2, Math.round(own.length * .6))));
    s.opts = shuffle([...own.map(p => ({ ...p, own: true })), ...foreign.map(p => ({ ...p, own: false }))]); s.sel = new Set();
  }
  main.innerHTML = `<div class="run">${runHeader(k)}<div class="tag">${esc(openName(DATA[l.course]))} ${l.n}, Stufe 1 von 3: Erkennen</div>
    <p class="q">${esc(l.q)}</p><p class="tag" style="margin-top:4px">Welche Punkte gehören in die Antwort? Die anderen stammen aus anderen Fragen.</p><div class="grow"></div>
    <div class="answers">${s.opts.map((o, i) => `<button class="opt st-opt" aria-pressed="${s.sel.has(i)}" data-st1="${i}">${esc(o.t)}</button>`).join("")}</div>
    <div style="margin-top:12px"><button class="btn" data-st1-check ${s.sel.size ? "" : "disabled"}>Prüfen</button>${skipBtn()}</div></div>`;
}
function checkStage1(k) {
  const s = R.state, l = k.leit;
  const miss = s.opts.filter((o, i) => o.own !== s.sel.has(i)).length, ok = miss <= 1;
  stageDone(k, 1, ok, s.opts.map((o, i) => { const p = s.sel.has(i); return `<div class="opt ${o.own && p ? "right" : o.own ? "missed" : p ? "wrong" : ""}">${o.own ? "" : `<small>Gehört zu einer anderen Frage</small><br>`}${esc(o.t)}</div>`; }).join(""),
    ok ? (miss ? "Fast alles richtig erkannt. Damit ist Stufe 2 dran: Lücken ergänzen." : "Alles richtig erkannt. Als Nächstes kommt Stufe 2: Lücken ergänzen.") : "Hier waren noch mehrere Punkte falsch zugeordnet. Lies die grün markierten nach, dann versuch es nochmal.");
}
/* Stufe 2: Ergaenzen. In jedem Punkt fehlt ein Schluesselwort; Woerter aus einer Wortbank einsetzen. */
const GAP_STOP = new Set("aber alle allem allen aller alles auch dabei damit dann darauf daraus dass deren diese diesem diesen dieser dieses durch einem einen einer eines erst etwa ihre ihrem ihren ihrer nach nicht noch oder ohne sich sind sowie statt über unter viele vielen wegen wenn werden wird wurde wurden zwischen seit beim keine kein mehr nur sehr gibt kann können muss müssen soll sollen haben hatte hatten waren worden selbst immer schon wieder eigene eigenen eigener".split(" "));
function gapWord(t) {
  const words = (t.match(/[A-Za-zÄÖÜäöüß§][\wÄÖÜäöüß-]*/g) || []).filter(w => w.length >= 6 && !GAP_STOP.has(w.toLowerCase()));
  if (!words.length) return null;
  const caps = words.filter(w => /^[A-ZÄÖÜ]/.test(w));
  return (caps.length ? caps : words).sort((a, b) => b.length - a.length)[0];
}
function renderStage2(k) {
  const l = k.leit, s = R.state;
  if (!s.gaps) {
    // Auswahl zufaellig, Reihenfolge wie in der Antwort, damit die Punkte logisch aufeinander folgen (z. B. Instanzenzug)
    const pick6 = new Set(shuffle(l.points.map((_, i) => i)).slice(0, 6));
    s.gaps = l.points.filter((_, i) => pick6.has(i)).map(p => ({ p, w: gapWord(p.t) })).filter(g => g.w);
    const extra = stageForeign(l, 6).map(p => gapWord(p.t)).filter(w => w && !s.gaps.some(g => g.w === w)).slice(0, 2);
    s.bank = shuffle([...s.gaps.map(g => g.w), ...extra]); s.fill = s.gaps.map(() => null); s.cur = 0;
    if (s.gaps.length < 2) { k.type = "open"; return renderOpen(k); }
  }
  const used = new Set(s.fill.filter(x => x !== null));
  main.innerHTML = `<div class="run">${runHeader(k)}<div class="tag">${esc(openName(DATA[l.course]))} ${l.n}, Stufe 2 von 3: Ergänzen</div>
    <p class="q">${esc(l.q)}</p><p class="tag" style="margin-top:4px">Tippe eine Lücke an und dann das passende Wort.</p>
    <ol class="gaps">${s.gaps.map((g, i) => { const [a, ...b] = g.p.t.split(g.w); const f = s.fill[i];
      return `<li>${esc(a)}<button class="gap ${s.cur === i ? "cur" : ""} ${f !== null ? "full" : ""}" data-gap="${i}" aria-label="Lücke ${i + 1}${f !== null ? ": " + esc(s.bank[f]) : ""}">${f !== null ? esc(s.bank[f]) : "…"}</button>${esc(b.join(g.w))}</li>`; }).join("")}</ol>
    <div class="grow"></div><div class="bank">${s.bank.map((w, i) => `<button class="opt" data-bank="${i}" ${used.has(i) ? "disabled" : ""}>${esc(w)}</button>`).join("")}</div>
    <div style="margin-top:12px"><button class="btn" data-st2-check ${s.fill.every(x => x !== null) ? "" : "disabled"}>Prüfen</button>${skipBtn()}</div></div>`;
}
function checkStage2(k) {
  const s = R.state, hit = s.gaps.filter((g, i) => s.bank[s.fill[i]] === g.w).length, ratio = hit / s.gaps.length, ok = ratio >= .8;
  stageDone(k, 2, ok, s.gaps.map((g, i) => { const r = s.bank[s.fill[i]] === g.w; return `<div class="opt ${r ? "right" : "wrong"}">${esc(g.p.t)}${r ? "" : `<br><small>Du hattest: ${esc(s.bank[s.fill[i]])}</small>`}</div>`; }).join(""),
    ok ? "Lücken sitzen. Jetzt bist du bereit für Stufe 3: die Antwort frei formulieren." : `${hit} von ${s.gaps.length} Lücken richtig. Ab 80 % ist die Stufe geschafft.`);
}
function stageDone(k, stage, ok, given, msg) {
  const l = k.leit, key = lfKey(l.n, DATA[l.course]);
  if (ok) S.lfStage[key] = Math.max(S.lfStage[key] || 0, stage);
  const gain = ok ? 12 : 4; R.total++; if (ok) R.right++; else R.missed.push(k);
  R.xp += gain; addXp(gain, l.course); save();
  R.answered = true;
  main.innerHTML = `<div class="run">${runHeader(k)}<div class="result anim"><div class="stamp ${ok ? "good" : "bad"}">${ok ? `Stufe ${stage} geschafft` : "Noch nicht"}</div><div class="plus">+${gain} XP</div></div>
    <p class="q small">${esc(l.q)}</p><p class="why">${esc(msg)}</p><div class="given">${given}</div>
    ${chips(l.points.flatMap(p => p.src))}
    <div class="sticky"><button class="btn" data-next>${R.i + 1 < R.items.length ? "Weiter" : "Ankommen"}</button></div></div>`;
  window.scrollTo(0, 0);
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
    <div class="sticky"><button class="btn" data-open-done>Selbsteinschätzung speichern</button>${skipBtn()}</div></div>`;
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
  if (R.boss && R.lives <= 0) return renderArrive();
  if (R.i < R.items.length) renderCard(); else renderArrive();
}

function renderArrive() {
  S.runs++;
  if (R.kind === "exam") S.exams++;
  let bonus = "";
  if (R.kind === "blitz") {
    const id = D.course.id, rec = R.right > (S.blitz[id] || 0) && R.right >= 5;
    S.blitz[id] = Math.max(S.blitz[id] || 0, R.right); questTick("blitz");
    if (rec) { R.xp += 15; addXp(15, id); bonus = `<p style="margin-top:14px"><b>Neuer Rekord.</b> +15 XP</p>`; }
  }
  const bossWon = R.boss && R.lives > 0 && R.i >= R.items.length;
  if (bossWon) { const first = !S.boss[R.boss]; S.boss[R.boss] = dayKey(); const g = first ? 60 : 20; R.xp += g; addXp(g, D.course.id); }
  save();
  const r = R, newStamps = D ? stampCount() - r.stampsBefore : 0, today = S.days[dayKey()] || 0;
  const missedTopics = [...new Map(r.missed.filter(k => k.topic).map(k => [k.topic, topicOf(k.topic)])).values()];
  const missedLf = r.missed.filter(k => k.leit && !k.caseStep).map(k => k.leit);
  const sober = r.items.some(k => isSober(k));
  const badge = sober ? [] : celebrateBadges();
  const pfLine = r.kind === "pfexam" ? (() => { const pct = Math.round(r.right / r.items.length * 100), id = D.course.id; S.pfBest = S.pfBest || {}; S.pfBest[id] = Math.max(S.pfBest[id] || 0, pct); save();
    return `<div><b>${pct} %</b><span>von ${r.items.length} richtig</span></div>`; })() : "";
  const pfReview = r.kind === "pfexam" ? `<section class="review"><h2>${r.timeout ? "Zeit abgelaufen. " : ""}${r.missed.length ? "Das war nicht richtig" : "Alles richtig!"}</h2>
    ${r.timeout && r.items.length > r.total ? `<p class="small">${r.items.length - r.total} Fragen nicht mehr beantwortet.</p>` : ""}
    <div class="reading">${r.missed.map(k => `<div class="item"><h3>${esc(k.q)}</h3><p><b>${esc(rightText(k))}</b></p><p class="small">${esc(k.why)}</p>${chips(k.src)}</div>`).join("")}</div></section>` : "";
  const examLine = r.examPts[1] ? `<div><b>${Math.round(r.examPts[0] / r.examPts[1] * 100)} %</b><span>der Punkte genannt</span></div>` : "";
  const oneLf = r.kind === "open" && r.items[0]?.leit && !r.items[0].caseStep ? `#/${r.items[0].leit.course}/lf/${r.items[0].leit.n}` : null;
  const back = oneLf ? oneLf : ["mix", "wrongmix", "plan"].includes(r.kind) ? "#/" : r.kind.startsWith("pf") ? `#/${D.course.id}/lf` : r.boss ? `#/${D.course.id}/stoff/${r.boss}` : "#/" + (D?.course.id || "");
  const caseId = r.items[0]?.cs?.id;
  endRun();
  history.replaceState(null, "", "#/angekommen");
  const head = r.boss ? (bossWon ? "Boss besiegt" : "Knapp daneben") : r.kind === "pfexam" ? "Simulation fertig" : r.kind === "exam" ? "Probeprüfung fertig" : r.kind === "blitz" ? `${r.right} richtig` : "Angekommen";
  const again = oneLf ? `<button class="btn" data-go="${oneLf}">Zur Frage${r.items[0].type !== "open" && canStage(r.items[0].leit) && stageOf(r.items[0].leit) >= +r.items[0].type.slice(-1) ? ", nächste Stufe" : ""}</button>` : caseId ? `<button class="btn" data-go="#/faelle/fall/${caseId}">Zur Akte</button>` : r.boss ? (bossWon ? `<button class="btn" data-go="#/${D.course.id}/stoff/${r.boss}">Zum Kapitel</button>` : `<button class="btn" data-boss="${r.boss}">Nochmal antreten</button>`)
    : r.kind === "plan" ? `<button class="btn" data-plan="${D.course.id}">Weiter nach Plan</button>` : `<button class="btn" data-run="${r.kind === "mix" ? "mix" : r.kind === "pfexam" ? "pfexam" : r.kind === "blitz" ? "blitz" : "5"}">Noch eine Runde</button>`;
  main.innerHTML = `<div class="pad arrive"><h1>${head}</h1>
    ${r.boss ? `<div class="boss-res ${bossWon ? "won" : ""}"><span class="boss-medal">${bossWon ? "★" : "♥"}</span><p>${bossWon ? `„${esc(chapterOf(r.boss).name)}“ trägt jetzt einen goldenen Stempel auf deiner Linie.` : `${r.right} von ${r.items.length} Karten geschafft, dann waren die Herzen weg. Die Karten von eben kommen in deinen Wiederholungen wieder.`}</p></div>` : ""}
    <div class="score">${pfLine}${examLine}<div><b>+${r.xp}</b><span>XP</span></div>${r.kind === "exam" || r.kind === "pfexam" || !r.total ? "" : `<div><b>${r.right}/${r.total}</b><span>richtig</span></div>`}<div><b>${streak()}</b><span>Tage in Folge</span></div></div>
    ${r.kind === "blitz" ? `<p class="small" style="margin-top:10px">In der Blitzrunde gibt es 3 XP pro richtiger Antwort, für einen neuen Rekord 15 XP dazu.</p>` : ""}${bonus}
    ${r.skipped ? `<p class="small" style="margin-top:10px">${r.skipped} ${r.skipped === 1 ? "Frage" : "Fragen"} übersprungen, ohne Wertung.</p>` : ""}
    ${today >= DAILY_GOAL && today - r.xp < DAILY_GOAL ? `<p style="margin-top:14px"><b>Tagesziel geschafft.</b></p>` : ""}
    ${newStamps > 0 ? `<p style="margin-top:14px"><b>${newStamps === 1 ? "Neuer Stempel" : newStamps + " neue Stempel"}</b> auf deiner Karte.</p>` : ""}
    ${pfReview}
    ${badge.length ? `<section class="review"><h2>Neue Abzeichen</h2><div class="badges">${badge.map(x => badgeCard(x.b, x)).join("")}</div></section>` : ""}
    ${r.kind !== "pfexam" && (missedTopics.length || missedLf.length) ? `<section class="review"><h2>Noch einmal nachlesen</h2>
      <ul>${missedLf.map(l => `<li><button class="back" data-go="#/${l.course}/lf/${l.n}">${esc(openName(DATA[l.course]))} ${l.n}</button></li>`).join("")}</ul>
      <div class="reading">${missedTopics.slice(0, 3).map(t => context(t)).join("")}</div></section>` : ""}
    <div style="margin-top:22px">${again}<button class="btn ghost" data-go="${back}">Zurück</button></div></div>`;
  if (back === "#/") renderNav("hub"); else renderNav("home", D);
  window.scrollTo(0, 0);
  if (!sober) celebrate();
}

/* ---------- Prüfungsmodus (Recht): Aufbau wie die echte Prüfung, frei springen und markieren, Plus- und Minuspunkte ---------- */
let PX = null;
const PX_TYPES = ["mc", "tf", "multi"];
function startPx() {
  const ex = D.course.exam, used = new Set(), closed = [], nClosed = ex.n - ex.open;
  const pools = ex.blocks.map(b => shuffle(D.cards.filter(k => !k.extra && PX_TYPES.includes(k.type) && k.q.length < 260 && (b.tf ? k.type === "tf" && k.lf.length : b.topics.includes(k.topic)))));
  for (let i = 0, guard = 0; closed.length < nClosed && guard < 400; i++, guard++) {
    const bi = i % pools.length, k = pools[bi].find(x => !used.has(x.id));
    if (k) { used.add(k.id); closed.push({ kind: "c", k, block: ex.blocks[bi].name, opts: k.type === "tf" ? null : shuffle(k.type === "mc" ? [k.right, ...k.wrong] : [...k.right, ...k.wrong]), sel: new Set(), tf: null }); }
  }
  closed.sort((a, b) => ex.blocks.findIndex(x => x.name === a.block) - ex.blocks.findIndex(x => x.name === b.block));
  const opens = Object.entries(ex.topf).map(([t, ns]) => { const l = shuffle(D.leitfragen.filter(x => ns.includes(x.n)))[0]; return l && { kind: "o", l, topf: t, text: "", pts: new Set() }; }).filter(Boolean);
  PX = { qs: [...closed, ...opens], i: 0, mark: new Set(), end: Date.now() + ex.minutes * 60000, phase: "run", start: Date.now() };
  PX.timer = setInterval(pxTick, 500);
  document.body.classList.add("running");
  history.pushState({ run: 1 }, "", "#/pruefung");
  renderPx();
}
function endPx() { if (PX?.timer) clearInterval(PX.timer); PX = null; document.body.classList.remove("running"); }
function pxTick() {
  if (!PX || PX.phase !== "run") return;
  const left = PX.end - Date.now(), lab = $("#pxclock");
  if (lab) { lab.textContent = clock(left); lab.classList.toggle("late", left < 5 * 60000); }
  if (left <= 0) { PX.timeout = true; pxSubmit(); }
}
const pxAnswered = q => q.kind === "o" ? !!q.text.trim() : q.k.type === "tf" ? q.tf !== null : q.sel.size > 0;
function pxScore(q) { // Anteil 0..1; falsche Kreuze ziehen so viel ab, wie ein richtiges bringt, nie unter 0
  const k = q.k;
  if (k.type === "tf") return q.tf === null ? 0 : (q.tf === k.val ? 1 : 0);
  const right = k.type === "mc" ? [k.right] : k.right;
  let hit = 0, bad = 0; q.sel.forEach(i => right.includes(q.opts[i]) ? hit++ : bad++);
  return Math.max(0, (hit - bad) / right.length);
}
function renderPx() {
  const ex = D.course.exam, q = PX.qs[PX.i], n = PX.qs.length;
  const nav = `<nav class="pxnav" aria-label="Fragen">${PX.qs.map((x, i) => `<button class="${i === PX.i ? "cur" : ""} ${pxAnswered(x) ? "ans" : ""} ${PX.mark.has(i) ? "mk" : ""}" data-px-go="${i}" aria-label="Frage ${i + 1}${pxAnswered(x) ? ", beantwortet" : ""}${PX.mark.has(i) ? ", markiert" : ""}">${i + 1}</button>`).join("")}</nav>`;
  let body;
  if (q.kind === "o") {
    body = `<div class="tag">Offene Frage, Topf ${q.topf} · zusammen ${ex.openPts} Punkte für alle offenen</div><p class="q">${esc(q.l.q.replace(/^Topf \d: /, ""))}</p>
      <textarea id="pxtext" placeholder="Antworte wie in der Prüfung, in Stichworten oder ganzen Sätzen.">${esc(q.text)}</textarea>`;
  } else if (q.k.type === "tf") {
    body = `<div class="tag">${esc(q.block)}</div><p class="tag" style="margin-top:4px">Stimmt die Aussage?</p><p class="q">${esc(q.k.q)}</p><div class="grow"></div>
      <div class="tf"><button class="opt ${q.tf === true ? "picked" : ""}" data-px-tf="1" aria-pressed="${q.tf === true}">Stimmt</button><button class="opt ${q.tf === false ? "picked" : ""}" data-px-tf="0" aria-pressed="${q.tf === false}">Falsch</button></div>`;
  } else {
    body = `<div class="tag">${esc(q.block)}</div><p class="q">${esc(q.k.q)}</p><p class="tag" style="margin-top:4px">${q.k.type === "mc" ? "Eine Antwort ist richtig." : "Eine oder mehrere Antworten sind richtig. Falsche Kreuze geben Minuspunkte."}</p><div class="grow"></div>
      <div class="answers">${q.opts.map((o, i) => `<button class="opt ${q.sel.has(i) ? "picked" : ""}" aria-pressed="${q.sel.has(i)}" data-px-opt="${i}">${esc(o)}</button>`).join("")}</div>`;
  }
  const open = PX.qs.filter(x => !pxAnswered(x)).length;
  main.innerHTML = `<div class="run px"><div class="run-top"><button class="run-x" data-quit aria-label="Prüfung abbrechen">×</button><div class="pxtitle">Prüfungsmodus · Frage ${PX.i + 1} von ${n}</div><div class="combo"><span id="pxclock">${clock(PX.end - Date.now())}</span></div></div>
    ${nav}${body}
    <div class="pxbar"><button class="btn ghost small" data-px-prev ${PX.i ? "" : "disabled"}>Zurück</button><button class="btn ghost small ${PX.mark.has(PX.i) ? "on" : ""}" data-px-mark aria-pressed="${PX.mark.has(PX.i)}">${PX.mark.has(PX.i) ? "Markiert" : "Markieren"}</button>${PX.i + 1 < n ? `<button class="btn small" data-px-next>Weiter</button>` : ""}</div>
    <div style="margin-top:14px"><button class="btn ${PX.i + 1 === n ? "" : "ghost"}" data-px-submit>Abgeben${open ? ` (${open} offen)` : ""}</button></div></div>`;
}
function pxSubmit() {
  if (PX.phase !== "run") return;
  clearInterval(PX.timer); PX.phase = "self"; PX.used = Date.now() - PX.start;
  renderPxSelf();
}
function renderPxSelf() {
  const ex = D.course.exam, os = PX.qs.filter(q => q.kind === "o");
  main.innerHTML = `<div class="pad"><h1 class="h1">${PX.timeout ? "Zeit abgelaufen" : "Abgegeben"}</h1>
    <p class="lead">Die geschlossenen Fragen wertet die App selbst. Bei den offenen Fragen hakst du jetzt ab, welche Punkte deine Antwort enthält.</p>
    ${os.map((q, qi) => `<section class="section"><h2>Offene Frage ${qi + 1} (Topf ${q.topf})</h2><p class="q small">${esc(q.l.q.replace(/^Topf \d: /, ""))}</p>
      ${q.text.trim() ? `<div class="mine">${esc(q.text)}</div>` : `<p class="small">Keine Antwort geschrieben.</p>`}
      <ul class="points">${q.l.points.map((p, i) => `<li class="point"><label><input type="checkbox" data-pxpt="${PX.qs.indexOf(q)}:${i}" ${q.pts.has(i) ? "checked" : ""}><span>${esc(p.t)}</span></label>${chips(p.src)}</li>`).join("")}</ul></section>`).join("")}
    <div style="margin-top:18px"><button class="btn" data-px-result>Auswerten</button></div></div>`;
  window.scrollTo(0, 0);
}
function pxResult() {
  main.querySelectorAll("[data-pxpt]").forEach(b => { const [qi, i] = b.dataset.pxpt.split(":").map(Number); b.checked ? PX.qs[qi].pts.add(i) : PX.qs[qi].pts.delete(i); });
  const ex = D.course.exam, cs = PX.qs.filter(q => q.kind === "c"), os = PX.qs.filter(q => q.kind === "o");
  const per = (ex.total - ex.openPts) / cs.length, perOpen = ex.openPts / os.length;
  let cPts = 0, oPts = 0;
  cs.forEach(q => { q.s = pxScore(q); cPts += q.s * per; if (pxAnswered(q)) grade(q.k.id, q.s === 1, D.course.id); });
  os.forEach(q => { q.s = q.pts.size / q.l.points.length; oPts += q.s * perOpen;
    const key = lfKey(q.l.n), rec = S.lfOpen[key] || { best: 0, tries: 0 }; rec.tries++; rec.best = Math.max(rec.best, q.s); rec.last = q.s; S.lfOpen[key] = rec; });
  const tot = cPts + oPts, pct = Math.round(tot / ex.total * 100), gain = 40 + Math.round(pct / 2);
  S.exams++; S.pxBest = S.pxBest || {}; S.pxBest[D.course.id] = Math.max(S.pxBest[D.course.id] || 0, pct);
  S.pxLog = [...(S.pxLog || []), { d: dayKey(), c: D.course.id, p: pct }].slice(-20);
  addXp(gain); save();
  const blocks = ex.blocks.map(b => { const qs = cs.filter(q => q.block === b.name); return qs.length ? [b.name, qs.reduce((a, q) => a + q.s, 0), qs.length] : null; }).filter(Boolean);
  const fmt = x => x.toLocaleString("de-AT", { maximumFractionDigits: 1 });
  const wrong = cs.filter(q => q.s < 1);
  const mine = q => q.k.type === "tf" ? (q.tf === null ? "keine Antwort" : q.tf ? "Stimmt" : "Falsch") : q.sel.size ? [...q.sel].map(i => q.opts[i]).join(" · ") : "keine Antwort";
  PX.phase = "done";
  main.innerHTML = `<div class="pad arrive"><h1>Prüfungsmodus fertig</h1>
    <div class="score"><div><b>${pct} %</b><span>${fmt(tot)} von ${ex.total} Punkten</span></div><div><b>${fmt(cPts)}</b><span>von ${ex.total - ex.openPts} geschlossen</span></div><div><b>${fmt(oPts)}</b><span>von ${ex.openPts} offen</span></div><div><b>+${gain}</b><span>XP</span></div></div>
    <p class="small" style="margin-top:10px">Zeit: ${clock(PX.used)} von ${ex.minutes}:00.${S.pxLog.filter(x => x.c === D.course.id).length > 1 ? ` Bisher: ${S.pxLog.filter(x => x.c === D.course.id).map(x => x.p + " %").join(", ")}.` : ""} Die Punkte je geschlossener Frage (${fmt(per)}) sind eine Annahme, genannt wurden nur die ${ex.openPts} Punkte für die offenen Fragen.</p>
    <section class="review"><h2>Nach Themenblock</h2><ul class="pxblocks">${blocks.map(([n, s, c]) => `<li><span>${esc(n)}</span><b>${fmt(s)} / ${c}</b></li>`).join("")}${os.map(q => `<li><span>Offen: ${esc(q.l.q.replace(/^Topf \d: /, "").slice(0, 70))}…</span><b>${Math.round(q.s * 100)} %</b></li>`).join("")}</ul></section>
    <section class="review"><h2>${wrong.length ? "Nicht ganz richtig" : "Alle geschlossenen Fragen richtig!"}</h2>
      <div class="reading">${wrong.map(q => `<div class="item"><h3>${esc(q.k.q)}</h3><p class="small">Deine Antwort: ${esc(mine(q))}${q.s > 0 ? ` (${Math.round(q.s * 100)} % der Punkte)` : ""}</p><p><b>${esc(rightText(q.k))}</b></p><p class="small">${esc(q.k.why)}</p>${chips(q.k.src)}</div>`).join("")}</div></section>
    <div style="margin-top:22px"><button class="btn" data-px-start>Noch einmal</button><button class="btn ghost" data-px-leave>Zurück</button></div></div>`;
  clearInterval(PX.timer); document.body.classList.remove("running");
  history.replaceState(null, "", "#/angekommen");
  renderNav("home", D); window.scrollTo(0, 0);
  celebrate();
}
function pxClick(b) {
  const has = x => b.hasAttribute(x), a = x => b.getAttribute(x);
  if (has("data-px-start")) { endPx(); startPx(); return; }
  if (has("data-px-leave")) { endPx(); go(`#/${D.course.id}/lf`); return; }
  if (!PX) return;
  if (has("data-px-result")) { pxResult(); return; }
  if (PX.phase !== "run") return;
  const q = PX.qs[PX.i];
  if (has("data-px-go")) PX.i = +a("data-px-go");
  else if (has("data-px-prev")) PX.i = Math.max(0, PX.i - 1);
  else if (has("data-px-next")) PX.i = Math.min(PX.qs.length - 1, PX.i + 1);
  else if (has("data-px-mark")) PX.mark.has(PX.i) ? PX.mark.delete(PX.i) : PX.mark.add(PX.i);
  else if (has("data-px-tf")) q.tf = q.tf === (a("data-px-tf") === "1") ? null : a("data-px-tf") === "1";
  else if (has("data-px-opt")) { const i = +a("data-px-opt"); if (q.k.type === "mc") { const was = q.sel.has(i); q.sel.clear(); if (!was) q.sel.add(i); } else q.sel.has(i) ? q.sel.delete(i) : q.sel.add(i); }
  else if (has("data-px-submit")) { const open = PX.qs.filter(x => !pxAnswered(x)).length; if (PX.end > Date.now() && !confirm(open ? `${open} Fragen sind noch offen. Trotzdem abgeben?` : "Prüfung abgeben?")) return; pxSubmit(); return; }
  renderPx();
  if (has("data-px-go") || has("data-px-prev") || has("data-px-next")) window.scrollTo(0, 0);
}

/* ---------- Offene Fragen ---------- */
let lfTab = {};
const pfCards = (c = D) => c.cards.filter(k => k.pf);
const pfName = (c = D) => c.course.pf.blocks.length === 1 ? c.course.pf.blocks[0] : "Prüfungsfragen";
const lfTabs = () => D.course.pf ? `<div class="tabs"><button aria-pressed="${lfTab[D.course.id] !== "pf"}" data-lf-tab="kf">${esc(D.course.openNamePl)}</button><button aria-pressed="${lfTab[D.course.id] === "pf"}" data-lf-tab="pf">${esc(pfName())}</button></div>` : "";
function rightText(k) {
  if (k.type === "mc") return k.right;
  if (k.type === "tf") return k.val ? "Stimmt" : "Falsch";
  if (k.type === "multi") return k.right.join(" · ");
  if (k.type === "match") return k.pairs.map(p => p[0] + ": " + p[1]).join(" · ");
  if (k.type === "bucket") return k.items.map(x => x[0] + " → " + k.buckets[x[1]]).join(" · ");
  return "";
}
function viewPf() {
  const pf = D.course.pf, all = pfCards(), id = D.course.id;
  const st = k => !S.cards[k.id]?.seen ? "" : S.cards[k.id].box > 0 ? "ok" : "bad";
  const wrong = all.filter(k => st(k) === "bad").length, n = Math.min(pf.n || all.length, all.length);
  const block = b => { const ks = all.filter(k => k.pf === b);
    return `<section class="section"><h2>${esc(b)}</h2><p class="small">${cardCount(ks)}</p>
      <div class="pcta" style="margin-top:6px"><button class="btn small" data-pf-run="${esc(b)}">${ks.length > 15 ? `Üben, 15 von ${ks.length} pro Runde` : `${ks.length} Fragen üben`}</button></div>
      <ol class="pflist">${ks.map((k, i) => `<li class="${st(k)}"><button data-pf-one="${k.id}"><span class="n">${pf.ordered ? i + 1 : st(k) === "ok" ? "✓" : st(k) === "bad" ? "✗" : "·"}</span><span>${esc(k.q)}${st(k) ? `<small>${st(k) === "ok" ? "zuletzt richtig" : "zuletzt falsch"}</small>` : ""}</span></button></li>`).join("")}</ol></section>`; };
  main.innerHTML = `<div class="pad"><h1 class="h1">${esc(pfName())}</h1>${lfTabs()}
    <p class="lead">${esc(pf.info)}</p><p class="small">Insgesamt ${cardCount(all)}.${S.pfBest?.[id] !== undefined ? ` Beste Simulation: ${S.pfBest[id]} %.` : ""}</p>
    <div class="pcta"><button class="btn" data-run="pfexam">Simulation, ${n} Fragen in ${pf.minutes} Min.</button>${wrong ? `<button class="btn ghost" data-run="pfwrong">Falsche wiederholen (${wrong})</button>` : ""}${pf.blocks.length > 1 ? `<button class="btn ghost" data-pf-run="">Alle gemischt üben</button>` : ""}</div>
    <p class="small" style="margin-top:6px">In der Simulation gibt es keine Rückmeldung zwischendurch, die Auflösung kommt am Ende.</p>
    ${pf.blocks.map(block).join("")}</div>`;
}
function viewLf() {
  if (D.course.pf && lfTab[D.course.id] === "pf") return viewPf();
  if (D.course.groupedLf) return viewLfGrouped();
  const id = D.course.id, lead = D.course.openLead || "Die Prüfung stellt 7 Überblicksfragen aus diesem Themenkreis. Ein Stempel kommt, wenn du die Punkte frei nennen kannst und die Quizkarten sitzen.";
  let lastGroup = null;
  main.innerHTML = `<div class="pad"><h1 class="h1">${id === "geschichte" ? "Stempelkarte" : esc(D.course.openNamePl)}</h1>${lfTabs()}
    <p class="lead">${esc(lead)}</p>
    <div class="stamps">${D.leitfragen.map(l => { const s = lfScore(l.n), d = stamped(l.n); return `<button class="field ${d ? "done" : ""}" data-go="#/${id}/lf/${l.n}" aria-label="${esc(openName())} ${l.n}, ${s} Prozent"><i style="height:${s}%"></i><span>${l.n}</span></button>`; }).join("")}</div>
    <div class="pcta"><button class="btn" data-run="exam">${id === "geschichte" ? "Probeprüfung starten" : "Probelauf starten"}</button></div>
    ${D.course.upcoming ? `<p class="small" style="margin-top:10px">${esc(D.course.upcoming)}</p>` : ""}
    <ol class="lflist">${D.leitfragen.map(l => { const h = l.group && l.group !== lastGroup ? `<li class="group">${esc(l.group)}</li>` : ""; lastGroup = l.group; return h + lfRow(l); }).join("")}</ol></div>`;
}
const stageDots = l => canStage(l) ? `<span class="stdots" aria-label="Stufe ${stageOf(l)} von 2 erarbeitet">${[1, 2].map(i => `<i class="${stageOf(l) >= i ? "on" : ""}"></i>`).join("")}</span>` : "";
const lfRow = l => `<li class="${stamped(l.n) ? "done" : ""}"><button data-go="#/${D.course.id}/lf/${l.n}"><span class="n">${l.n}</span><span>${esc(l.q)}<small>${lfScore(l.n)} %${stageDots(l)}</small></span></button></li>`;
// Recht: Fragen nach Fernlehre gruppiert, jede Gruppe mit eigener Stempelreihe und Quizrunde
function viewLfGrouped() {
  const id = D.course.id, groups = [...new Set(D.leitfragen.map(l => l.group))];
  main.innerHTML = `<div class="pad"><h1 class="h1">${esc(D.course.openNamePl)}</h1>${lfTabs()}
    <p class="lead">${esc(D.course.openLead)}</p>
    <div class="pcta">${D.course.exam ? `<button class="btn" data-px-start>Prüfungsmodus: ${D.course.exam.n} Fragen, ${D.course.exam.minutes} Min.</button>` : ""}<button class="btn ${D.course.exam ? "ghost" : ""}" data-run="exam">Probelauf nur offene Fragen</button></div>
    ${D.course.exam ? `<p class="small" style="margin-top:6px">${esc(D.course.exam.info)}${S.pxBest?.[id] !== undefined ? ` Bestes Ergebnis: ${S.pxBest[id]} %.` : ""}</p>` : ""}
    ${D.course.upcoming ? `<p class="small" style="margin-top:10px">${esc(D.course.upcoming)}</p>` : ""}
    <nav class="gjump" aria-label="Zu einer Gruppe springen">${groups.map((g, i) => `<button data-jump="g${i}">${esc(g.replace("Fernlehre ", "FL "))}</button>`).join("")}</nav>
    ${groups.map((g, gi) => { const ls = D.leitfragen.filter(l => l.group === g).sort((a, b) => a.n - b.n), done = ls.filter(l => stamped(l.n)).length;
      const chs = [...new Set(ls.map(l => l.ch))].map(c => chapterOf(c)?.name).filter(Boolean), ns = ls.map(l => l.n), nCards = D.cards.filter(k => k.lf.some(x => ns.includes(x))).length;
      return `<section class="lfgroup" id="g${gi}"><div class="lfg-head"><h2>${esc(g)}</h2><span class="small">${done} von ${ls.length} gestempelt</span></div>
        <p class="small">Kapitel: ${chs.map(esc).join(", ")}</p>
        <div class="stamps small-stamps">${ls.map(l => { const sc = lfScore(l.n); return `<button class="field ${stamped(l.n) ? "done" : ""}" data-go="#/${id}/lf/${l.n}" aria-label="${esc(openName())} ${l.n}, ${sc} Prozent"><i style="height:${sc}%"></i><span>${l.n}</span></button>`; }).join("")}</div>
        ${nCards ? `<div class="pcta" style="margin-top:10px"><button class="btn small ghost" data-lfgroup="${esc(g)}">Quizkarten zu ${esc(g)} üben (${nCards})</button></div>` : ""}
        <ol class="lflist" style="margin-top:8px">${ls.map(lfRow).join("")}</ol></section>`; }).join("")}</div>`;
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
    ${canStage(l) ? `<ol class="ladder">${[["Erkennen", "Richtige Punkte zwischen fremden finden"], ["Ergänzen", "Schlüsselwörter in die Lücken setzen"], ["Frei formulieren", "Selbst antworten und abhaken"]].map(([t, d], i) => { const st = stageOf(l), done = i < 2 ? st > i : !!open, next = i === Math.min(2, st);
      return `<li class="${done ? "done" : ""} ${next ? "next" : ""}"><button data-open-run="${n}" data-stage="${i + 1}"><span class="n">${done ? "✓" : i + 1}</span><span><b>${t}</b><small>${d}</small></span></button></li>`; }).join("")}</ol>` : ""}
    <div class="pcta">${canStage(l) ? "" : `<button class="btn" data-open-run="${n}" data-stage="3">Frei beantworten</button>`}${cards.length ? `<button class="btn ghost" data-lf-run="${n}">${cards.length} Quizkarten üben</button>` : ""}</div>
    <section class="section"><h2>Musterantwort</h2>
      <details ${seen ? "open" : ""} data-peek="${lfKey(n)}"><summary style="cursor:pointer;min-height:36px">Antwort anzeigen</summary>
      <p class="gist">${esc(l.gist)}</p>
      ${l.note ? `<div class="note">${esc(l.note)}</div>` : ""}
      <ul class="points">${l.points.map(p => `<li class="point ro">${esc(p.t)}${chips(p.src)}</li>`).join("")}</ul>${deepBlock(l)}</details>
    </section>
    ${figsFor(l.ch)}
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
    <h1 class="h1" style="margin-top:6px">${esc(c.name)}</h1><p class="lead">${esc(c.span)}, ${Math.round(chapterPct(id) * 100)} % gelernt<br>${cardCount(cardsIn(id))}${lfs.length ? `<br>${lfs.filter(l => lfDone(l)).length} von ${lfs.length} ${esc(lfs.length === 1 ? openName() : D.course.openNamePl || "Leitfragen")} bis zum Lückentext geschafft` : ""}</p>
    <div class="pcta">${hasCards ? `<button class="btn" data-ch-run="${id}">${cid === "geschichte" ? "Diese Station üben" : "Dieses Kapitel üben"}</button>` : ""}${chapterDocs(c).map(([d, p], i) => `<button class="btn ghost" data-slide="${d}:${p}">${i ? `${esc(docName(d))}, S. ${p}` : `Dokument öffnen, S. ${p}`}</button>`).join("")}${c.book ? `<button class="btn ghost" data-slide="j:${c.book}">Im Zusatztext lesen</button>` : ""}</div>
    ${bossPanel(id)}
    ${lfs.length ? `<section class="section"><h2>${esc(D.course.openNamePl || "Leitfragen")} dazu</h2><ol class="lflist" style="margin-top:0">${lfs.map(l => `<li class="${stamped(l.n) ? "done" : ""}"><button data-go="#/${cid}/lf/${l.n}"><span class="n">${l.n}</span><span>${esc(l.q)}${l.group && D.course.groupedLf ? `<small>${esc(l.group)}</small>` : ""}</span></button></li>`).join("")}</ol></section>` : ""}
    <section class="section"><h2>Zusammenfassung</h2>${figsFor(id, true)}<div class="reading">${tp.map(t => context(t)).join("")}</div></section></div>`;
}
function bossPanel(ch) {
  const b = bossState(ch); if (!b) return "";
  if (b.beaten) return `<div class="bossbox won"><span class="boss-medal">★</span><div><b>Boss besiegt</b><p class="small">Am ${b.beaten.slice(8)}.${b.beaten.slice(5, 7)}. Goldener Stempel auf der Linie. Nochmal antreten bringt 20 XP.</p><button class="btn small ghost" data-boss="${ch}">Nochmal antreten</button></div></div>`;
  if (b.open) return `<div class="bossbox ready"><span class="boss-medal">♥♥</span><div><b>Boss-Runde bereit</b><p class="small">${BOSS_N} schwere Karten aus diesem Kapitel, bei denen du dich bisher am öftesten vertan hast. Du hast ${BOSS_LIVES} Herzen, beim zweiten Fehler ist Schluss. Sieg: 60 XP und ein goldener Stempel.</p><button class="btn small" data-boss="${ch}">Antreten</button></div></div>`;
  return `<div class="bossbox"><span class="boss-medal">♥</span><div><b>Boss ab 80 % gelernt</b><p class="small">Jetzt ${Math.round(b.p * 100)} %. Lerne die Karten dieses Kapitels sicher (zweimal richtig), dann schaltet sich die Boss-Runde frei.</p><div class="progress"><i style="width:${Math.min(100, b.p / .8 * 100)}%"></i></div></div></div>`;
}

/* ---------- Stufen ---------- */
function viewLevels() {
  const lv = level(), xp = S.xp;
  const rankRow = (r, i, cur, x, list) => { const next = list[i + 1], done = x >= r[0], here = i === cur;
    return `<li class="lvl ${done ? "done" : ""} ${here ? "here" : ""}"><span class="n">${done ? "✓" : i + 1}</span><span><b>${esc(r[1])}</b><small>${r[0].toLocaleString("de-AT")} XP${here ? (next ? `, du bist hier, noch ${(next[0] - x).toLocaleString("de-AT")} XP bis „${esc(next[1])}“` : ", danach Sterne") : done ? ", erreicht" : `, noch ${(r[0] - x).toLocaleString("de-AT")} XP`}</small></span></li>`; };
  const rankIdx = (r, x) => { let i = 0; while (i + 1 < r.length && x >= r[i + 1][0]) i++; return i; };
  main.innerHTML = `<div class="pad"><button class="back" data-go="#/ich">Ich</button>
    <div class="lvhero" style="--lc:${lv.col}">${emblem(lv, 104)}<div><p class="small">${esc(lv.et)}, Stufe ${lv.n} von ${LEVELS.length}</p><h1 class="h1">${esc(lv.name)}</h1>
      <div class="progress"><i style="width:${lv.pct * 100}%"></i></div><p class="small" style="margin-top:4px">${xp.toLocaleString("de-AT")} XP, noch ${lv.toNext.toLocaleString("de-AT")} bis „${esc(lv.next.name)}“</p></div></div>
    <p class="lead">Dein Weg durch die Soziale Arbeit: sechs Etappen vom ersten Semester bis zum Lebenswerk. Je weiter, desto größer die Abstände. Nach „Lebenswerk“ gibt es alle ${HONOR.toLocaleString("de-AT")} XP einen Stern.</p>
    ${ETAPPEN.map(([et, col], ei) => { const ls = LEVELS.filter(l => l.ei === ei), doneEt = lv.ei > ei, cur = lv.ei === ei;
      return `<details class="etappe ${doneEt ? "done" : ""} ${cur ? "cur" : ""}" style="--ec:${col}" ${cur || ei === lv.ei + 1 ? "open" : ""}><summary><span class="et-badge">${ei + 1}</span><b>${esc(et)}</b><span class="small">${doneEt ? "abgeschlossen" : cur ? "du bist hier" : `ab ${ls[0].xp.toLocaleString("de-AT")} XP`}</span></summary>
        <ol class="et-levels">${ls.map(l => { const done = xp >= l.xp, here = l.n === lv.n; return `<li class="${done ? "done" : ""} ${here ? "here" : ""}">${emblem({ ...l, honor: 0, pct: 0 }, 38, false)}<span><b>${esc(l.name)}</b><small>${l.xp.toLocaleString("de-AT")} XP${here ? ", du bist hier" : done ? "" : `, noch ${(l.xp - xp).toLocaleString("de-AT")}`}</small></span></li>`; }).join("")}</ol></details>`; }).join("")}
    <section class="section"><h2>So gibt es XP</h2><ul class="xplist">
      <li><b>10 bis 15</b>Richtige Karte, mit Serie bis 5 mehr; Fallkette, Zuordnen und Rechnen 5 mehr</li><li><b>2</b>Falsche Karte</li>
      <li><b>3</b>Richtige Antwort in der Blitzrunde, neuer Rekord 15</li><li><b>10 bis 35</b>Offene Frage frei beantwortet</li>
      <li><b>12</b>Stufe Erkennen oder Ergänzen geschafft</li><li><b>15</b>Tagesauftrag</li><li><b>10</b>Prüfungsplan des Tages erfüllt</li>
      <li><b>60</b>Kapitel-Boss besiegt</li><li><b>50</b>Akte abgeschlossen</li><li><b>5</b>Exkurs gelesen</li></ul></section>
    <section class="section"><h2>Ränge in den Lehrveranstaltungen</h2><p class="small">Jede LV hat eigene Ränge, gezählt werden nur die XP aus dieser LV. Nach dem letzten Rang gibt es Sterne.</p>
    ${COURSE_IDS.map(id => { const c = DATA[id], r = c.course.ranks; if (!r) return ""; const x = S.cx[id] || 0, rk = rank(c);
      return `<details class="rankbox"><summary><b>${esc(c.course.short || "Geschichte")}</b> <span class="small">${esc(rk.name)}, ${x.toLocaleString("de-AT")} XP</span></summary><ol class="lflist lvls">${r.map((y, i) => rankRow(y, i, rankIdx(r, x), x, r)).join("")}</ol></details>`; }).join("")}</section></div>`;
}

function badgeCard(b, st) {
  const max = b[3].length, next = b[3][st.t], tier = st.t ? TIER[st.t - 1] : "";
  return `<div class="badge ${st.t ? "on t" + st.t : ""}"><span class="medal" aria-hidden="true">${st.t ? "★".repeat(st.t) : "☆"}</span><b>${esc(b[1])}</b>
    <span>${st.t ? esc(b[2](b[3][st.t - 1])) : esc(b[2](b[3][0]))}</span>
    <small>${st.t ? `${tier}${max > 1 ? `, Stufe ${st.t} von ${max}` : ""}` : "Noch offen"}${next !== undefined ? `. Nächste: ${esc(b[2](next))}` : ""}</small>
    ${next !== undefined ? `<div class="progress"><i style="width:${Math.min(100, st.v / next * 100)}%"></i></div>` : ""}</div>`;
}

/* ---------- Grafiken ---------- */
const FIG = {};
const figsFor = (ch, inline) => { const fs = Object.values(FIG).filter(f => f.ch === ch && f.course === D.course.id); return fs.length ? (inline ? "" : `<section class="section"><h2>Überblick</h2>`) + fs.map(figHtml).join("") + (inline ? "" : "</section>") : ""; };
function figHtml(f) {
  const nb = (n, key) => `<button class="fg-n ${n.tag || ""}" data-fig="${f.id}|${key}" aria-pressed="false"><b>${esc(n.label)}</b>${n.sub ? `<small>${esc(n.sub)}</small>` : ""}</button>`;
  let body = "";
  if (f.kind === "pyramid") body = `<div class="fg-pyr">${f.nodes.map((n, i) => `<div class="fg-step" style="--w:${Math.round(44 + 56 * i / Math.max(1, f.nodes.length - 1))}%">${nb(n, "n" + i)}</div>`).join("")}</div>`;
  if (f.kind === "lanes") body = `<div class="fg-lanes" style="--n:${f.cols.length}">${f.cols.map((c, ci) => `<div class="fg-lane"><h4>${esc(c.title)}</h4>${c.nodes.map((n, i) => `${n.edge ? `<div class="fg-edge"><span>${esc(n.edge)}</span></div>` : ""}${nb(n, ci + "-" + i)}`).join("")}</div>`).join("")}</div>`;
  if (f.kind === "compare") body = `<div class="fg-cmp" style="--n:${f.cols.length}">${f.cols.map((c, ci) => `<button class="fg-n fg-h ${c.tag || ""}" data-fig="${f.id}|c${ci}" aria-pressed="false"><b>${esc(c.title)}</b></button>`).join("")}
    ${f.rows.map((r, ri) => `<div class="fg-row">${esc(r)}</div>${f.cols.map((c, ci) => { const x = c.cells[ri], t = Array.isArray(x) ? x : [x, ""]; return `<button class="fg-c ${t[1]} ${c.tag || ""}" data-fig="${f.id}|c${ci}" tabindex="-1">${esc(t[0])}</button>`; }).join("")}`).join("")}</div>`;
  return `<section class="fig" id="${f.id}"><h3>${esc(f.title)}</h3><p class="small">${esc(f.lead)}</p>${body}<div class="fg-detail" aria-live="polite"><p class="small">Tippe auf ein Feld, dann steht hier die Erklärung mit Quelle.</p></div></section>`;
}
function figPart(f, key) {
  if (key[0] === "n") return f.nodes[+key.slice(1)];
  if (key[0] === "c") { const c = f.cols[+key.slice(1)]; return { label: c.title, text: c.text, src: c.src }; }
  const [ci, i] = key.split("-").map(Number); const n = f.cols[ci].nodes[i]; return { ...n, label: `${f.cols[ci].title}: ${n.label}` };
}
function showFig(btn) {
  const [id, key] = btn.dataset.fig.split("|"), f = FIG[id], box = btn.closest(".fig"), n = figPart(f, key);
  box.querySelectorAll("[data-fig]").forEach(b => { const on = b.dataset.fig === btn.dataset.fig; b.classList.toggle("sel", on); if (b.hasAttribute("aria-pressed")) b.setAttribute("aria-pressed", on); });
  box.querySelector(".fg-detail").innerHTML = `<h4>${esc(n.label.replace(/\u00ad/g, ""))}</h4><p>${esc(n.text)}</p>${chips(n.src)}`;
}

/* ---------- Sicherung ---------- */
function backupFile() {
  const blob = new Blob([JSON.stringify({ app: "sprengel", saved: new Date().toISOString(), state: { ...S, key: null } })], { type: "application/json" });
  const a = Object.assign(document.createElement("a"), { href: URL.createObjectURL(blob), download: `sprengel-sicherung-${dayKey()}.json` });
  document.body.append(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(a.href), 2000);
  S.lastBackup = dayKey(); S.backups = (S.backups || 0) + 1; save();
  toast("Sicherung gespeichert. Leg die Datei an einen sicheren Ort.");
}
function restoreState(text) {
  let o; try { o = JSON.parse(text); } catch { o = JSON.parse(new TextDecoder().decode(b64.from(text.trim()))); }
  if (o && o.app === "sprengel") o = o.state;
  if (!o || typeof o !== "object" || !("xp" in o)) throw new Error("keine Sicherung");
  const key = S.key; S = migrate({ ...blank(), ...o, key }); save();
}

/* ---------- Ich ---------- */
function viewMe() {
  const lv = level();
  const seen = Object.keys(S.cards).length, total = COURSE_IDS.reduce((a, id) => a + DATA[id].cards.length, 0);
  main.innerHTML = `<div class="pad"><button class="lvhero me" data-go="#/stufen" style="--lc:${lv.col}">${emblem(lv, 84)}<div><p class="small">${esc(lv.et)}, Stufe ${lv.n} von ${LEVELS.length}</p><h1 class="h1">${esc(lv.name)}</h1>
      <p class="small">${S.xp.toLocaleString("de-AT")} XP, noch ${lv.toNext.toLocaleString("de-AT")} bis „${esc(lv.next.name)}“. Alle Stufen ›</p></div></button>
    <p class="small" style="margin-top:10px">${seen} von ${total} Karten gesehen, längste Serie ${S.bestStreak} Tage, ${Object.keys(S.akten).length} Akten abgeschlossen, ${Object.keys(S.boss).length} Bosse besiegt, ${Object.keys(S.links).length} Exkurse gelesen</p>
    <section class="section"><h2>Lehrveranstaltungen</h2><div class="ranks">${COURSE_IDS.map(id => { const c = DATA[id], r = rank(c), xp = S.cx[id] || 0; return `<div class="rank"><b>${esc(id === "geschichte" ? "Geschichte" : c.course.name)}</b><span class="small">${r ? esc(r.name) + ", " : ""}${xp} XP${r?.next ? `, nächster Rang bei ${r.next[0]}` : ""}</span>${r ? `<div class="progress"><i style="width:${r.pct * 100}%"></i></div>` : ""}</div>`; }).join("")}</div></section>
    <section class="section"><h2>Abzeichen</h2><p class="small">Jedes Abzeichen hat Stufen von Bronze bis Platin.</p><div class="badges">${BADGES.map(b => badgeCard(b, tierOf(b))).join("")}</div></section>
    <section class="section"><h2>Prüfungstermine</h2>
      ${COURSE_IDS.filter(id => id !== "faelle").map(id => { const c = DATA[id], ex = c.course.exams || [], cur = daysToExam(c); return `<div class="exam-row"><b>${esc(c.course.short || "Geschichte")}</b>${ex.length ? `<div class="field-row">${ex.map(e => `<button class="btn small ${cur?.id === e.id ? "" : "ghost"}" data-exam2="${id}:${e.id}">${esc(e.label)}, ${e.date.slice(8)}.${e.date.slice(5, 7)}.</button>`).join("")}</div>` : `<form class="field-row" data-exam-form data-c="${id}"><input name="d" type="date" value="${esc(S.exDate[id] || "")}" aria-label="Prüfungstermin ${esc(c.course.short)}"><button class="btn small ghost">Speichern</button></form>`}</div>`; }).join("")}
      <p class="small" style="margin-top:6px">ORBE-Termin bitte selbst eintragen. SoPol-Termin laut Semesterplan, Geschichte laut Einführungsfolie. Bei Geschichte kommt die schriftliche Reflexion mit mindestens 3500 Zeichen dazu.</p></section>
    <section class="section"><h2>Folien</h2>
      ${S.key ? `<p>Folien sind freigeschaltet.</p>` : `<p>Folien sind gesperrt. Gib den Code ein, um sie zu öffnen.</p><form class="field-row" data-unlock-form><input type="text" name="code" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Zugangscode" aria-label="Zugangscode"><button class="btn small">Freischalten</button></form><p class="small" data-unlock-msg></p>`}
      ${S.key ? `<div class="field-row"><button class="btn small ghost" data-offline>${S.offline ? "Folien und Texte neu für offline laden" : "Alle Folien und Texte für offline laden (ca. 130 MB)"}</button></div><div id="dl" hidden><div class="progress"><i style="width:0"></i></div><p class="small" style="margin-top:4px"></p></div>` : ""}
    </section>
    <section class="section"><h2>Sicherung</h2>
      <p class="small">Dein Fortschritt liegt nur in diesem Browser. Wird der Browserspeicher gelöscht, ist er weg. Speichere ab und zu eine Datei, etwa in deine Cloud, und lade sie auf einem anderen Gerät oder nach einem Reset wieder. ${S.lastBackup ? `Letzte Sicherung: ${S.lastBackup.slice(8)}.${S.lastBackup.slice(5, 7)}.${S.lastBackup.slice(0, 4)}.` : "Noch keine Sicherung gespeichert."}</p>
      <div class="field-row"><button class="btn small" data-backup-file>Als Datei speichern</button><label class="btn small ghost filebtn">Datei laden<input type="file" accept=".json,.txt,application/json,text/plain" data-restore-file hidden></label></div>
      <details class="rankbox" style="margin-top:10px"><summary>Als Text übertragen</summary>
        <div class="field-row"><button class="btn small ghost" data-export>Text erzeugen und kopieren</button></div>
        <textarea id="bak" placeholder="Sicherung hier einfügen" aria-label="Sicherung" style="min-height:76px"></textarea>
        <div class="field-row"><button class="btn small ghost" data-import>Text übernehmen</button></div></details>
      <div class="field-row"><button class="btn small ghost" data-reset>Fortschritt löschen</button></div><p class="small" id="bakmsg"></p>
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
  if (has("data-lvup-close")) { b.closest(".lvup")?.remove(); return; }
  if (has("data-fig")) { showFig(b); return; }
  if (has("data-jump")) { document.getElementById(a("data-jump"))?.scrollIntoView({ behavior: "smooth", block: "start" }); return; }
  if (has("data-plan")) { useCourse(a("data-plan")); startRun("plan"); return; }
  if (has("data-boss")) { startRun("boss", { ch: a("data-boss") }); return; }
  if (has("data-lfgroup")) { startRun("lfgroup", { g: a("data-lfgroup") }); return; }
  if (has("data-backup-file")) { backupFile(); if (location.hash === "#/ich") viewMe(); else b.closest(".nag")?.remove(); return; }
  if (has("data-akt-close")) { const id = a("data-akt-close"), cs = allCases().find(x => x.id === id); if (cs && aktReady(cs) && !S.akten[id]) { S.akten[id] = dayKey(); addXp(50, "faelle"); save(); viewCase(id); $(".akt")?.classList.add("justclosed"); toast("Akte geschlossen. +50 XP"); const nb = celebrateBadges(); if (nb.length) toast(`Neues Abzeichen: ${nb.map(x => x.b[1]).join(", ")}`); celebrate(); } return; }
  if ([...b.attributes].some(x => x.name.startsWith("data-px"))) { pxClick(b); return; }
  if (has("data-go")) { if (R) quitRun(); go(a("data-go")); return; }
  if (has("data-run")) { startRun(a("data-run")); return; }
  if (has("data-ch-run")) { startRun("chapter", { ch: a("data-ch-run") }); return; }
  if (has("data-lf-tab")) { lfTab[D.course.id] = a("data-lf-tab"); viewLf(); return; }
  if (has("data-pf-run")) { startRun("pf", { block: a("data-pf-run") }); return; }
  if (has("data-pf-one")) { startRun("pf", { one: a("data-pf-one") }); return; }
  if (has("data-lf-run")) { startRun("lf", { n: +a("data-lf-run") }); return; }
  if (has("data-open-run")) { startRun("open", { n: +a("data-open-run"), stage: +(a("data-stage") || 3) }); return; }
  if (has("data-case-all")) { startRun("case", { id: a("data-case-all") }); return; }
  if (has("data-case-drill")) { startRun("casedrill", { id: a("data-case-drill") }); return; }
  if (has("data-case-sec")) { const [id, key] = a("data-case-sec").split(":"); startRun("casesec", { id, key }); return; }
  if (has("data-exam")) { S.ex[D.course.id] = a("data-exam"); save(); route(); return; }
  if (has("data-exam2")) { const [c, id] = a("data-exam2").split(":"); S.ex[c] = id; save(); route(); return; }
  if (has("data-stoff-tab")) { stoffTab = a("data-stoff-tab"); viewStoff(); return; }
  if (has("data-quit")) { if (PX && PX.phase === "run" && !confirm("Prüfungsmodus abbrechen? Die Antworten gehen verloren.")) return; history.back(); return; }
  if (has("data-next")) { nextCard(); return; }
  if (has("data-reveal")) { revealOpen(R.items[R.i]); return; }
  if (has("data-open-done")) { finishOpen(R.items[R.i]); return; }
  if (has("data-offline")) { downloadAll(); return; }
  if (has("data-export")) { const t = $("#bak"); t.value = b64.to(new TextEncoder().encode(JSON.stringify({ ...S, key: null }))); t.select(); navigator.clipboard?.writeText(t.value).then(() => $("#bakmsg").textContent = "In die Zwischenablage kopiert.").catch(() => {}); return; }
  if (has("data-import")) { try { restoreState($("#bak").value); viewMe(); $("#bakmsg").textContent = "Sicherung übernommen."; } catch { $("#bakmsg").textContent = "Dieser Text ist keine gültige Sicherung."; } return; }
  if (has("data-reset")) { if (confirm("Fortschritt auf diesem Gerät löschen?")) { const key = S.key; S = { ...blank(), key }; save(); route(); } return; }
  if (has("data-chain-next")) {
    const k = R.items[R.i], s = R.state; s.step++;
    if (s.step < k.steps.length) renderChain(k);
    else { const ok = s.errors === 0, gain = score(k, ok); feedback(k, ok, gain, k.steps.map((st, i) => `<div class="opt ${s.log[i] ? "right" : "missed"}"><small>${esc(st.q)}</small><br>${esc(st.right)}</div>`).join("")); }
    return;
  }
  if (!R || R.answered) return;
  const k = R.items[R.i], s = R.state;
  if (has("data-skip")) { skipItem(); return; }
  if (has("data-st1")) { const i = +a("data-st1"); s.sel.has(i) ? s.sel.delete(i) : s.sel.add(i); b.setAttribute("aria-pressed", s.sel.has(i)); $("[data-st1-check]").disabled = !s.sel.size; return; }
  if (has("data-st1-check")) { checkStage1(k); return; }
  if (has("data-gap")) { const i = +a("data-gap"); if (s.fill[i] !== null) s.fill[i] = null; s.cur = i; renderStage2(k); return; }
  if (has("data-bank")) { if (s.cur === null || s.cur === undefined) s.cur = s.fill.indexOf(null); if (s.cur < 0) return; s.fill[s.cur] = +a("data-bank"); const nx = s.fill.findIndex((x, j) => x === null && j > s.cur); s.cur = nx >= 0 ? nx : s.fill.indexOf(null); renderStage2(k); return; }
  if (has("data-st2-check")) { checkStage2(k); return; }
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
document.addEventListener("change", e => {
  if (!e.target.matches("[data-restore-file]")) return;
  const f = e.target.files?.[0]; if (!f) return;
  f.text().then(t => { restoreState(t); viewMe(); $("#bakmsg").textContent = "Sicherung aus der Datei übernommen."; }).catch(() => { $("#bakmsg").textContent = "Diese Datei ist keine gültige Sprengel-Sicherung."; });
});
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
  if (n >= 1 && n <= 5) { const opts = main.querySelectorAll("[data-mc],[data-tf],[data-multi],[data-bk],[data-chain],[data-st1]"); opts[n - 1]?.click(); }
});

/* ---------- Navigation ---------- */
function go(hash) { if (location.hash === hash) route(); else location.hash = hash; }
function quitRun() { if (R) endRun(); }
function route() {
  const h = location.hash.replace(/^#/, "") || "/";
  if (h === "/fahrt") { if (R) return; history.replaceState(null, "", "#/"); return route(); }
  if (h === "/pruefung") { if (PX) return; history.replaceState(null, "", "#/"); return route(); }
  if (PX) endPx();
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
  else if (p[0] === "stufen") { clearCourse(); renderNav("me", null); viewLevels(); }
  else { renderNav("hub"); viewHub(); }
  window.scrollTo(0, 0);
  main.focus({ preventScroll: true });
}
window.addEventListener("hashchange", route);
main.addEventListener("input", e => { if (PX && PX.phase === "run" && e.target.id === "pxtext") PX.qs[PX.i].text = e.target.value; });
window.addEventListener("popstate", () => {
  if (!viewerEl.hidden && !history.state?.viewer) { closeSlide(); return; }
  if (R && !history.state?.run) { quitRun(); route(); }
  if (PX && !history.state?.run) { endPx(); route(); }
});

(async function init() {
  const [m, lk, ...cs] = await Promise.all([fetch("slides/manifest.json").then(r => r.json()), fetch("data/links.json").then(r => r.json()), ...COURSE_IDS.map(id => fetch(`data/${id}.json`).then(r => r.json()))]);
  M = m; LINKS = lk.links; WEB = lk.web;
  cs.forEach((c, i) => {
    const id = COURSE_IDS[i];
    c.course.id = id; DATA[id] = c;
    if (id === "geschichte") Object.assign(c.course, { short: "Geschichte", openNamePl: "Leitfragen", modes: ["blitz"], lineTitle: c.course.name, ranks: GESCH_RANKS });
    if (id === "recht") c.course.groupedLf = true;
    (c.figs || []).forEach(f => { f.course = id; FIG[f.id] = f; });
    c.topics.forEach(t => { TOPIC[t.id] = t; });
    c.chapters.forEach(ch => { CHAPTER[ch.id] = ch; });
    c.cards.forEach(k => { k.course = id; CARD[k.id] = k; });
    c.leitfragen.forEach(l => { l.course = id; });
  });
  // MATS-Kernfragen wurden am 11.11.2026 neu nummeriert: gespeicherten Fortschritt mitnehmen
  const rn = DATA.matsi?.course.renumber;
  if (rn && !S.migMatsi1) {
    const lo = {}, peek = {};
    for (const [k, v] of Object.entries(S.lfOpen)) { const m = k.match(/^matsi:(\d+)$/); lo[m && rn[m[1]] ? "matsi:" + rn[m[1]] : k] = v; }
    for (const k of Object.keys(S)) { const m = k.match(/^peekmatsi:(\d+)$/); if (m) { peek["peekmatsi:" + (rn[m[1]] || m[1])] = S[k]; delete S[k]; } }
    S.lfOpen = lo; Object.assign(S, peek); S.migMatsi1 = 1; save();
  }
  const hk = location.hash.match(/^#key=(.+)$/);
  if (hk) {
    try { await unlock(decodeURIComponent(hk[1])); } catch {}
    history.replaceState(null, "", location.pathname);
  }
  await restoreKey();
  // Beim ersten Start mit dem neuen Stufen- und Abzeichensystem nichts nachfeiern
  if (S.lvSeen == null) S.lvSeen = levelKey(level());
  if (!S.bd) S.bd = Object.fromEntries(BADGES.map(b => [b[0], tierOf(b).t]));
  save();
  route();
  if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});
})().catch(err => { console.error(err); main.innerHTML = `<div class="pad"><h1 class="h1">Die Daten konnten nicht geladen werden</h1><p class="lead">Prüfe die Internetverbindung und lade die Seite neu.</p></div>`; });
