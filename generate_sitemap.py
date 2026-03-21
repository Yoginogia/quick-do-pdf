import os
import glob

sitemap_template = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""

domain = "https://quickdopdf.com/"

def generate_sitemap():
    # Find all html files in root
    root_htmls = glob.glob("*.html")
    # Find all html files in blog
    blog_htmls = glob.glob("blog/*.html")
    
    urls = []
    
    # Homepage gets highest priority
    urls.append(f"  <url><loc>{domain}</loc><priority>1.0</priority><changefreq>weekly</changefreq></url>")
    
    # Process Root Tools
    for file in root_htmls:
        if file in ["index.html", "404.html"]: continue
        
        # Determine priority based on type
        priority = "0.8"
        if file in ["merge.html", "split.html", "compress.html", "pdf-to-word.html", "compress-pdf-100kb.html"]:
            priority = "0.9" # High intent tools
        elif file in ["privacy-policy.html", "terms.html", "about.html", "contact.html"]:
            priority = "0.5" # Info pages
            
        urls.append(f"  <url><loc>{domain}{file}</loc><priority>{priority}</priority><changefreq>monthly</changefreq></url>")
        
    # Process Blog Directory
    for file in blog_htmls:
        url_path = file.replace("\\", "/") # Normalize for windows
        
        priority = "0.7"
        changefreq = "monthly"
        
        if file == "blog\\index.html" or file == "blog/index.html":
            priority = "0.8"
            changefreq = "weekly"
            
        urls.append(f"  <url><loc>{domain}{url_path}</loc><priority>{priority}</priority><changefreq>{changefreq}</changefreq></url>")
        
    # Write to sitemap
    with open("sitemap.xml", 'w', encoding='utf-8') as f:
        f.write(sitemap_template.format(urls="\n".join(urls)))
        
    print(f"Generated sitemap with {len(urls)} URLs")

if __name__ == "__main__":
    generate_sitemap()
