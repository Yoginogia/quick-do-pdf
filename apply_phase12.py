import os

folder = r"d:\Yogi\Yogesh\quick-do-pdf"

new_head = """<link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap"></noscript>
  <link rel="stylesheet" href="tools.css"""

for file in os.listdir(folder):
    if file.endswith(".html"):
        path = os.path.join(folder, file)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if '<link rel="stylesheet" href="tools.css' in content and 'family=Outfit' not in content:
            content = content.replace('<link rel="stylesheet" href="tools.css', new_head)
            
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

index_path = os.path.join(folder, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    idx = f.read()

idx = idx.replace("@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap');", "")
idx = idx.replace('<section class="hero">', '<main>\n  <section class="hero">')
idx = idx.replace('</section>\n\n    <footer>', '</section>\n  </main>\n\n    <footer>')
idx = idx.replace('style="color:var(--accent1,#2a8bff);text-decoration:none;"', 'style="color:var(--accent1,#2a8bff);"')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx)
print("Phase 12 re-applied safely.")
