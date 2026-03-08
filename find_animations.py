import os
import re

folder = r"d:\Yogi\Yogesh\quick-do-pdf"

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".css") or file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Find all keyframes blocks
            keyframes = re.findall(r'@keyframes\s+([_a-zA-Z0-9-]+)\s*\{([^}]+)\}', content, flags=re.MULTILINE|re.DOTALL)
            if keyframes:
                for k in keyframes:
                    print(f"File {file} -> @keyframes {k[0]}:")
                    # simple check of properties
                    if 'background' in k[1]:
                        print("  [WARNING: background animated in CSS]")
                    if 'width' in k[1] or 'height' in k[1] or 'top' in k[1] or 'left' in k[1]:
                        print("  [WARNING: layout animated in CSS]")
