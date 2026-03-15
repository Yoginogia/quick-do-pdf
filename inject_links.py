import os
import glob
import re

tools_mapping = {
    r"\bcompress(ing)? pdf\b": "../compress.html",
    r"\breduce(ing)? file size\b": "../compress.html",
    r"\bcompress pdf under 100kb\b": "../compress-pdf-100kb.html",
    r"\bmerge pdf\b": "../merge.html",
    r"\bcombine multiple\b": "../merge.html",
    r"\bunlock pdf\b": "../unlock.html",
    r"\bremove password\b": "../unlock.html",
    r"\bprotect pdf\b": "../protect.html",
    r"\bpdf to word\b": "../pdf-to-word.html",
    r"\bpdf to excel\b": "../pdf-to-excel.html",
    r"\bjpg to pdf\b": "../jpg-to-pdf.html",
    r"\bimage to pdf\b": "../jpg-to-pdf.html",
    r"\bedit pdf\b": "../edit-pdf.html",
    r"\bsplit pdf\b": "../split.html",
    r"\bextract images\b": "../extract-images.html",
    r"\bcrop pdf\b": "../crop.html",
    r"\bimage merger\b": "../merge-images.html"
}

blogs_mapping = {
    r"\byou\(?r\)? pdf so large\b": "why-is-my-pdf-so-large.html",
    r"\bbest free pdf tools\b": "best-free-pdf-tools-2026.html",
    r"\bilovepdf\b": "ilovepdf-vs-smallpdf-comparison.html",
    r"\bsmallpdf\b": "ilovepdf-vs-smallpdf-comparison.html",
    r"\bmac preview\b": "how-to-compress-pdf-mac-preview.html",
    r"\barraybuffer\b": "how-to-fix-detached-arraybuffer-error-pdf.html",
    r"\bmojibake\b": "how-to-fix-pdf-text-mojibake-garbled.html",
    r"\bpdf/a compliance\b": "what-is-pdf-a-compliance.html",
    r"\bgmail'?s limit\b": "how-to-reduce-pdf-size-for-gmail.html",
    r"\bwithout losing formatting\b": "convert-pdf-without-losing-formatting.html"
}

def inject_internal_links(filepath):
    filename = os.path.basename(filepath)
    if filename == "index.html" or filename == "blog-layout.css":
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Isolate blog content (both new and legacy templates wrap content in <article>)
    match = re.search(r'(<article[^>]*>)(.*?)(</article>)', html, re.DOTALL)
    if not match:
        print(f"Skipping {filename} - No <article> found.")
        return

    prefix = match.group(1)
    content = match.group(2)
    suffix = match.group(3)

    # Split into HTML tags and Text
    tokens = re.split(r'(<[^>]+>)', content)
    
    in_a_tag = False
    in_h_tag = False
    
    tool_links_added = 0
    blog_links_added = 0
    max_tools = 3
    max_blogs = 2
    
    # Keep track of what we linked to avoid spamming the same link
    linked_urls = set()

    new_tokens = []
    
    for token in tokens:
        if token.startswith('<') and token.endswith('>'):
            tag_name_match = re.match(r'</?([a-zA-Z0-9]+)', token)
            if tag_name_match:
                tag_name = tag_name_match.group(1).lower()
                if tag_name == 'a':
                    in_a_tag = not token.startswith('</')
                elif tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'button']:
                    in_h_tag = not token.startswith('</')
            new_tokens.append(token)
            continue

        if in_a_tag or in_h_tag or not token.strip():
            new_tokens.append(token)
            continue

        # We are in standard text. Let's try replacements.
        text = token
        
        # Tools Replacement
        if tool_links_added < max_tools:
            for pattern, url in tools_mapping.items():
                if tool_links_added >= max_tools: break
                if url in linked_urls: continue
                
                search = re.search(pattern, text, re.IGNORECASE)
                if search:
                    original_text = search.group(0)
                    tag = f'<a href="{url}" style="color: var(--a1); font-weight: 600; text-decoration: none;">{original_text}</a>'
                    text = text[:search.start()] + tag + text[search.end():]
                    linked_urls.add(url)
                    tool_links_added += 1

        # Blogs Replacement (only if not linking to self)
        if blog_links_added < max_blogs:
            for pattern, url in blogs_mapping.items():
                if blog_links_added >= max_blogs: break
                if url in linked_urls or url == filename: continue
                
                search = re.search(pattern, text, re.IGNORECASE)
                if search:
                    original_text = search.group(0)
                    tag = f'<a href="{url}" style="color: var(--a1); font-weight: 600; text-decoration: none;">{original_text}</a>'
                    text = text[:search.start()] + tag + text[search.end():]
                    linked_urls.add(url)
                    blog_links_added += 1

        new_tokens.append(text)

    new_content = ''.join(new_tokens)
    final_html = html[:match.start()] + prefix + new_content + suffix + html[match.end():]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_html)
        
    print(f"[{filename}] Added {tool_links_added} Tool links, {blog_links_added} Blog links.")

if __name__ == "__main__":
    blog_dir = "d:\\Yogi\\Yogesh\\quick-do-pdf\\blog"
    html_files = glob.glob(os.path.join(blog_dir, "*.html"))
    for file in html_files:
        inject_internal_links(file)
    print("Internal linking complete.")
