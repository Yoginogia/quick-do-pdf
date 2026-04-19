// theme.js - Handles Light/Dark Mode Toggling
(function() {
    // Prevent FOUC by applying theme immediately
    const savedTheme = localStorage.getItem('quickdopdf_theme');
    if (savedTheme === 'light') {
        document.documentElement.classList.add('theme-light');
        // Add to body as well if it exists, otherwise wait for DOMContentLoaded
        if (document.body) document.body.classList.add('theme-light');
    }

    document.addEventListener('DOMContentLoaded', () => {
        const body = document.body;
        if (savedTheme === 'light') {
            body.classList.add('theme-light');
        }

        const toggleBtn = document.getElementById('themeToggle');
        const themeIcon = document.getElementById('themeIcon');
        
        if (!toggleBtn) return;

        // Set initial icon if exists
        if (themeIcon) {
            if (body.classList.contains('theme-light')) {
                themeIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path>';
            } else {
                themeIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>';
            }
        } else {
            // For simple emoji toggles like on EMI Calculator
            toggleBtn.innerHTML = body.classList.contains('theme-light') ? '🌙' : '☀️';
        }

        toggleBtn.addEventListener('click', () => {
            body.classList.toggle('theme-light');
            const isLight = body.classList.contains('theme-light');
            
            localStorage.setItem('quickdopdf_theme', isLight ? 'light' : 'dark');

            if (themeIcon) {
                if (isLight) {
                    themeIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path>'; // Moon
                } else {
                    themeIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>'; // Sun
                }
            } else {
                // Update simple emoji toggle
                toggleBtn.innerHTML = isLight ? '🌙' : '☀️';
            }
        });
    });
})();


// Lazy Load Heavy Scripts (Analytics & AdSense)
let adsLoaded = false;
function loadAds() {
    if (adsLoaded) return;
    adsLoaded = true;
    
    const ga = document.createElement('script');
    ga.src = 'https://www.googletagmanager.com/gtag/js?id=G-KXQBGLEXZ6';
    ga.async = true;
    document.head.appendChild(ga);
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-KXQBGLEXZ6');

    const ads = document.createElement('script');
    ads.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3543763798528021';
    ads.crossOrigin = 'anonymous';
    ads.async = true;
    document.head.appendChild(ads);
}
['scroll', 'mousemove', 'touchstart', 'click', 'keydown'].forEach(evt => {
    window.addEventListener(evt, loadAds, {once: true, passive: true});
});
setTimeout(loadAds, 4500);
