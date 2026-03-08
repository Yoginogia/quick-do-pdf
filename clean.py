import os

folder = r"d:\Yogi\Yogesh\quick-do-pdf"
for file in os.listdir(folder):
    if file.endswith(".html"):
        path = os.path.join(folder, file)
        
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        content = content.replace('\ufeff', '')
            
        if "ðŸ" in content or "â" in content or "Ã" in content:
            try:
                fixed_content = content.encode('cp1252').decode('utf-8')
                with open(path, "w", encoding="utf-8") as f:
                    f.write(fixed_content)
                print(f"Fixed {file}")
            except Exception as e:
                print(f"Error on {file}: {e}")
