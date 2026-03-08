import os
import re

folder = r"d:\Yogi\Yogesh\quick-do-pdf"
mojibakes = set()

for file in os.listdir(folder):
    if file.endswith(".html"):
        path = os.path.join(folder, file)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Find all sequences of weird characters starting with ðŸ or â
        # A typical mojibake is 2 to 6 characters long
        matches = re.findall(r'[ðâÃ][\x80-\xFF\w\sï¸”Œ”“’‘•—–\-\,\.\<\>\/\?\;\'\:\"\[\]\{\}\\\|\=\+\_\)\(\*\&\^\%\$\#\@\!]{1,5}', content)
        for m in matches:
            # specifically look for ones that look like emoji corruptions (e.g., ðŸ“„)
            if "ðŸ" in m or "â" in m:
                # clean up the match a bit
                clean_m = re.search(r'(ðŸ..|â..|ðŸ...|â...|ðŸ.|â.)', m)
                if clean_m:
                    mojibakes.add(clean_m.group(1))
                else:
                    mojibakes.add(m[:4])

print("Found Mojibakes:")
for m in mojibakes:
    print(repr(m))
