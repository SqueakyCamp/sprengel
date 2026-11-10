// App-Dateien: Netz zuerst, damit Updates ankommen. Folien: aus dem Cache, weil sie sich nicht aendern.
const SHELL = "sprengel-shell-8";
const SLIDES = "sprengel-slides-1";
const FILES = ["./", "index.html", "style.css", "app.js", "manifest.webmanifest", "data/geschichte.json", "data/matsi.json", "data/recht.json", "data/sopol.json", "data/faelle.json", "data/orbe.json", "data/links.json", "slides/manifest.json", "slides/salt.txt", "slides/check.bin",
  "fonts/big-shoulders-display-latin-800-normal.woff2", "fonts/atkinson-hyperlegible-latin-400-normal.woff2", "fonts/atkinson-hyperlegible-latin-700-normal.woff2", "icons/icon.svg", "icons/icon-192.png"];

self.addEventListener("install", e => { e.waitUntil(caches.open(SHELL).then(c => c.addAll(FILES)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== SHELL && k !== SLIDES).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", e => {
  const url = new URL(e.request.url);
  if (e.request.method !== "GET" || url.origin !== location.origin) return;
  if (/\/slides\/[a-z0-9]+\/[^/]+\.bin$/.test(url.pathname)) {
    e.respondWith(caches.open(SLIDES).then(async c => {
      const hit = await c.match(e.request);
      if (hit) return hit;
      const r = await fetch(e.request);
      if (r.ok) c.put(e.request, r.clone());
      return r;
    }));
    return;
  }
  e.respondWith(fetch(e.request).then(r => {
    if (r.ok) { const copy = r.clone(); caches.open(SHELL).then(c => c.put(e.request, copy)); }
    return r;
  }).catch(() => caches.match(e.request, { ignoreSearch: true }).then(h => h || caches.match("index.html"))));
});
