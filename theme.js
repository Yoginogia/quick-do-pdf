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
        
        if (!toggleBtn || !themeIcon) return;

        // Set initial icon
        if (body.classList.contains('theme-light')) {
            themeIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path>'; // Moon icon for light mode (to switch back to dark)
        } else {
            themeIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>'; // Sun icon for dark mode (to switch to light)
        }

        toggleBtn.addEventListener('click', () => {
            body.classList.toggle('theme-light');
            const isLight = body.classList.contains('theme-light');
            
            localStorage.setItem('quickdopdf_theme', isLight ? 'light' : 'dark');

            if (isLight) {
                themeIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path>'; // Moon
            } else {
                themeIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>'; // Sun
            }
        });
    });
})();
