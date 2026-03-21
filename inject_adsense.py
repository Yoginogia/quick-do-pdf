import os
import glob

adsense_script = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3543763798528021" crossorigin="anonymous"></script>'

def inject_into_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # If the exact script is already there, skip
    if "ca-pub-3543763798528021" in content:
        print(f"Skipping {filepath} (Already contains client ID)")
        
        # If it's there but maybe we need to clean up old client IDs?
        # Actually just ensure the new script is there.
        return

    # Check if we have an old adsense script to replace.
    # A generic replacement might be tricky, so let's just insert before </head>
    
    # But wait, we might have our lazy-loaded adsense script. Let's make sure the bot sees the raw one.
    if "</head>" in content:
        # Insert right before the closing head tag
        new_content = content.replace("</head>", f"  {adsense_script}\n</head>")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected AdSense code into {filepath}")
    else:
        print(f"Warning: No </head> found in {filepath}")

# Find all HTML files in root
root_htmls = glob.glob(os.path.join("d:\\Yogi\\Yogesh\\quick-do-pdf", "*.html"))
# Find all HTML files in blog folder
blog_htmls = glob.glob(os.path.join("d:\\Yogi\\Yogesh\\quick-do-pdf\\blog", "*.html"))

all_htmls = root_htmls + blog_htmls

for file in all_htmls:
    inject_into_html(file)

print("AdSense injection complete.")
