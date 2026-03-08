import os
import re

folder = r"d:\Yogi\Yogesh\quick-do-pdf"

# Find HTML files recursively
for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            # Remove GA script tag
            content = re.sub(r'<script[^>]*src=["\']https://(?:www\.)?googletagmanager\.com/gtag/js\?id=G-KXQBGLEXZ6["\'][^>]*></script>', '', content)
            
            # Remove inline gtag config
            content = re.sub(r'<script>\s*window\.dataLayer\s*=\s*window\.dataLayer\s*\|\|\s*\[\];\s*function\s+gtag\(\)\s*\{\s*dataLayer\.push\(arguments\);\s*\}\s*gtag\([\'"]js[\'"],\s*new Date\(\)\);\s*gtag\([\'"]config[\'"],\s*[\'"]G-KXQBGLEXZ6[\'"]\);\s*</script>', '', content)
            
            # Remove inline gtag config (minified single line)
            content = re.sub(r'<script>window\.dataLayer=window\.dataLayer\|\|\[\];function gtag\(\)\{dataLayer\.push\(arguments\);\}gtag\([\'"]js[\'"],new Date\(\)\);gtag\([\'"]config[\'"],[\'"]G-KXQBGLEXZ6[\'"]\);</script>', '', content)

            # Remove AdSense script tag
            content = re.sub(r'<script[^>]*src=["\']https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-3543763798528021["\'][^>]*></script>', '', content)

            # Remove any trailing empty GA comments
            content = re.sub(r'<!--\s*Google Analytics\s*-->', '', content)

            # Clean empty newlines left behind
            content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

            with open(path, "w", encoding="utf-8") as f:
                f.write(content.strip() + "\n")

print("Cleanup complete.")
