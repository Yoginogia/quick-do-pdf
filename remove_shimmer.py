import os
import re

folder = r"d:\Yogi\Yogesh\quick-do-pdf"

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".css") or file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            if "shimmerText" in content:
                # Remove animation usage
                content = re.sub(r'animation:\s*shimmerText[^;]*;', '', content)
                # Remove keyframes definition
                content = re.sub(r'@keyframes\s+shimmerText\s*\{[^}]+\}', '', content)
                
                with open(path, "w", encoding="utf-8") as f:
                    # Fix empty lines left by regex
                    f.write(content.strip() + "\n")

print("Removed shimmerText non-composited animations.")
