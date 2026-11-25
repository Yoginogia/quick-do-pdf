const CACHE_NAME = 'quickdopdf-v1';
const CORE_ASSETS = [
  './',
  'index.html',
  'manifest.json',
  'favicon.png',
  'theme.js',
  'tools.css',
  'merge.html',
  'split.html',
  'compress.html',
  'invoice-generator.html',
  'rent-receipt-generator.html',
  'emi-calculator.html',
  'gst-calculator.html'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(CORE_ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin) return;

  // Network-first for HTML pages so updates appear immediately
  if (event.request.mode === 'navigate' || url.pathname.endsWith('.html') || url.pathname === '/') {
    event.respondWith(
      fetch(event.request)
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy));
          return res;
        })
        .catch(() => caches.match(event.request).then((cached) => cached || caches.match('index.html')))
    );
    return;
  }

  // Stale-while-revalidate for local static assets
  event.respondWith(
    caches.match(event.request).then((cached) => {
      const networkFetch = fetch(event.request).then((res) => {
        const copy = res.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy));
        return res;
      }).catch(() => cached);
      return cached || networkFetch;
    })
  );
});
