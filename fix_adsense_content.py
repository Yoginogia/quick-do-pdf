#!/usr/bin/env python3
"""
AdSense Content Fix Script
Adds rich FAQ sections to all tool pages + creates new blog articles
"""

import os, re

ROOT = r"d:\Yogi\Yogesh\quick-do-pdf"
BLOG = os.path.join(ROOT, "blog")

# ─────────────────────────────────────────────────────────────
# 1. FAQ + rich content blocks for each tool page
# ─────────────────────────────────────────────────────────────

TOOL_CONTENT = {
    "compress.html": {
        "faq": [
            ("Is the PDF compressor really free?",
             "Yes, 100% free with no file size limits, no sign-up, and no watermarks. You can compress as many PDFs as you want."),
            ("Does compressing a PDF reduce quality?",
             "It depends on the compression level you choose. Our 'Standard' mode keeps text perfectly sharp while reducing images. 'Max Compression' reduces image quality noticeably to hit very small file sizes like 100KB."),
            ("What is the maximum file size I can compress?",
             "There is no server-side limit since everything runs in your browser. However, very large files (500MB+) may be slow depending on your device's RAM and CPU."),
            ("Is my PDF safe when I compress it?",
             "Completely. Your file never leaves your device. All compression happens locally in JavaScript — no data is sent to any server."),
            ("Why is my compressed PDF still large?",
             "PDFs with many high-resolution photos or complex vector graphics are harder to shrink. Try the 'Max Compression' mode which aggressively downsamples all images.")
        ]
    },
    "merge.html": {
        "faq": [
            ("How many PDFs can I merge at once?",
             "You can merge unlimited PDFs in a single session. There's no cap on the number of files or total pages."),
            ("Will the merged PDF retain bookmarks and links?",
             "The merged PDF will retain the visual content of all pages. Interactive bookmarks from individual files are not preserved, but all text, images and formatting remain intact."),
            ("Can I reorder pages before merging?",
             "Yes! After selecting your files, you can drag and drop them to rearrange the order before clicking merge."),
            ("Is this merger free to use?",
             "Absolutely. No registration, no payment, and no watermarks are added to your merged document."),
            ("Does the PDF merger work on mobile?",
             "Yes, it works on any modern browser including Safari on iPhone and Chrome on Android.")
        ]
    },
    "split.html": {
        "faq": [
            ("Can I split a PDF into individual pages?",
             "Yes. You can extract every page as a separate PDF, or specify a custom range like pages 1-5 to split into one file."),
            ("Is there a page limit for splitting?",
             "No, there is no limit. You can split a 500-page document just as easily as a 10-page one."),
            ("Will splitting a PDF reduce quality?",
             "No. Splitting extracts pages exactly as they are — there is no re-encoding or quality loss at all."),
            ("Can I split a password-protected PDF?",
             "You need to unlock the PDF first using our Unlock PDF tool, then you can split it freely."),
            ("What happens to my file after splitting?",
             "Nothing — your file is processed entirely in your browser and never stored anywhere.")
        ]
    },
    "pdf-to-word.html": {
        "faq": [
            ("Will the Word document match my original PDF layout?",
             "For most PDFs with standard text and images, the formatting is preserved very well. Complex layouts with unusual fonts or advanced InDesign exports may have minor differences."),
            ("Is the PDF to Word converter free?",
             "Yes, completely free. No limits, no account needed, and no watermarks on the output."),
            ("What formats can I convert to?",
             "You can convert PDF to DOCX (Microsoft Word format) which is compatible with Word 2007 and newer, as well as LibreOffice and Google Docs."),
            ("Can I convert a scanned PDF to Word?",
             "Scanned PDFs are images and require OCR (Optical Character Recognition). Use our PDF OCR tool first to make the text selectable, then convert."),
            ("Is there a file size limit for conversion?",
             "No server-side limit. The conversion runs in your browser so it depends on your device's capability.")
        ]
    },
    "protect.html": {
        "faq": [
            ("What kind of password protection does this add?",
             "We add 128-bit AES password encryption — the standard used by Adobe Acrobat. The PDF will ask for a password when anyone tries to open it."),
            ("Can I restrict editing or printing separately from opening?",
             "Yes. You can set an owner password that allows you to change permissions, and a separate user password needed just to open the file."),
            ("Is a password-protected PDF created here unbreakable?",
             "128-bit AES encryption is extremely strong and practically unbreakable with brute force. However, you should use a strong, unique password."),
            ("Does protecting the PDF add a watermark?",
             "No watermarks are added. Only the password protection is applied."),
            ("Will the protection work on all PDF readers?",
             "Yes — the standard we use is supported by Adobe Acrobat, Foxit, Chrome, Edge, and all major PDF readers on every platform.")
        ]
    },
    "unlock.html": {
        "faq": [
            ("Can I unlock any password-protected PDF?",
             "You can remove password protection from PDFs that are encrypted only with owner restrictions (printing, copying, editing). Documents requiring an open password cannot be unlocked without knowing it."),
            ("Is unlocking a PDF legal?",
             "Yes, if you own the document or have permission from the author. Never unlock documents you don't have rights to access."),
            ("Does the unlocked PDF have a watermark?",
             "No. The unlocked file is a clean copy with all restrictions removed and no watermarks added."),
            ("Why can't I unlock my bank statement PDF?",
             "Bank statement PDFs typically have an open password you must enter to view them. Our tool removes restriction-based locks, not open-access passwords."),
            ("How long does unlocking take?",
             "Usually under 5 seconds, even for large files, since everything runs locally in your browser.")
        ]
    },
    "sign.html": {
        "faq": [
            ("Is this e-signature legally valid?",
             "E-signatures created with our tool are legally binding in most countries including the US (ESIGN Act), EU (eIDAS), UK, India, and others for most business purposes. For highly regulated documents like wills, consult a lawyer."),
            ("Can multiple people sign the same document?",
             "Yes. Share the signed PDF with the next signer who can add their signature using the same tool."),
            ("What types of signatures can I add?",
             "You can draw a signature with your mouse or finger, type your name in a signature font, or upload an image of your signature."),
            ("Does my signature image get stored?",
             "No. All signature processing happens in your browser. Nothing is sent to any server."),
            ("Can I add a signature to a password-protected PDF?",
             "You need to unlock it first using our Unlock PDF tool, then sign it.")
        ]
    },
    "jpg-to-pdf.html": {
        "faq": [
            ("How many images can I combine into one PDF?",
             "You can convert and combine unlimited images into a single PDF file."),
            ("What image formats are supported?",
             "JPG, JPEG, PNG, WebP, BMP, and GIF are all supported for conversion to PDF."),
            ("Will converting JPG to PDF reduce image quality?",
             "We use high-quality settings by default so the images inside the PDF will look identical to the originals."),
            ("Can I set the page size when converting?",
             "Yes. You can choose A4, Letter, or 'Fit to image' so the PDF page exactly matches each image's dimensions."),
            ("Is there a file size limit per image?",
             "No server limit exists. Very large images (50MB+) may slow down conversion depending on your device.")
        ]
    },
    "watermark.html": {
        "faq": [
            ("Can I add both text and image watermarks?",
             "Yes. You can add text watermarks (with custom font, size, and color) or upload a logo image as a watermark."),
            ("Can I control the watermark opacity?",
             "Yes, you can adjust opacity from 10% (barely visible) to 100% (fully opaque)."),
            ("Will the watermark appear on all pages?",
             "Yes, the watermark is applied consistently to every page of the PDF."),
            ("Can someone remove the watermark I add?",
             "Text watermarks added over scanned PDFs are difficult to remove. Watermarks on PDFs with editable content can be removed by someone with advanced PDF editing software."),
            ("Is the watermarking free?",
             "Yes, completely free with no sign-up required.")
        ]
    },
    "rotate.html": {
        "faq": [
            ("Can I rotate only specific pages?",
             "Yes. You can select individual pages and apply rotation to just those pages, leaving the rest unchanged."),
            ("What rotation angles are supported?",
             "You can rotate pages by 90°, 180°, or 270° clockwise."),
            ("Does rotating pages affect the PDF quality?",
             "No. Rotating a PDF page is a metadata operation — no image re-encoding happens, so quality is perfectly preserved."),
            ("Can I rotate a password-protected PDF?",
             "You'll need to unlock it first with our Unlock PDF tool before rotating pages."),
            ("Will rotating the PDF affect its file size?",
             "No, the file size stays virtually the same after rotation.")
        ]
    }
}

FAQ_CSS = """
<style>
.faq-section { max-width: 800px; margin: 60px auto 0; padding: 0 24px 60px; }
.faq-section h2 { font-size: 1.6rem; font-weight: 900; margin-bottom: 8px; color: var(--text); }
.faq-section .faq-subtitle { color: var(--muted); margin-bottom: 32px; font-size: 0.95rem; line-height: 1.6; }
.faq-item { border: 1px solid var(--border, #e5e7eb); border-radius: 14px; margin-bottom: 12px; overflow: hidden; background: var(--card-bg, #fff); }
.faq-q { padding: 18px 22px; font-weight: 700; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-size: 0.97rem; color: var(--text); }
.faq-q:hover { background: var(--hover-bg, #f9fafb); }
.faq-icon { font-size: 1.1rem; transition: transform 0.25s; flex-shrink: 0; }
.faq-a { max-height: 0; overflow: hidden; transition: max-height 0.3s ease; padding: 0 22px; color: var(--muted); font-size: 0.93rem; line-height: 1.75; }
.faq-item.open .faq-a { max-height: 300px; padding: 0 22px 18px; }
.faq-item.open .faq-icon { transform: rotate(45deg); }
</style>
<script>
document.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('.faq-q').forEach(function(q){
    q.addEventListener('click',function(){
      var item=q.closest('.faq-item');
      item.classList.toggle('open');
    });
  });
});
</script>
"""

def build_faq_block(faqs):
    items = ""
    for q, a in faqs:
        items += f"""
    <div class="faq-item" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
      <div class="faq-q" itemprop="name">{q} <span class="faq-icon">+</span></div>
      <div class="faq-a" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
        <span itemprop="text">{a}</span>
      </div>
    </div>"""
    
    return f"""
{FAQ_CSS}
<section class="faq-section" itemscope itemtype="https://schema.org/FAQPage">
  <h2>Frequently Asked Questions</h2>
  <p class="faq-subtitle">Everything you need to know about using this tool. Can't find your answer? <a href="contact.html" style="color:var(--a1, #6366f1);">Contact us</a>.</p>
  {items}
</section>
"""

# ─────────────────────────────────────────────────────────────
# 2. Apply FAQ blocks to each tool page
# ─────────────────────────────────────────────────────────────

def inject_faq(filepath, faq_data):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        html = f.read()
    
    # Don't add twice
    if 'faq-section' in html:
        print(f"  ⚠ Already has FAQ: {os.path.basename(filepath)}")
        return False
    
    faq_block = build_faq_block(faq_data["faq"])
    
    # Insert before </body>
    if '</body>' in html:
        html = html.replace('</body>', faq_block + '\n</body>', 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✅ FAQ added: {os.path.basename(filepath)}")
        return True
    else:
        print(f"  ❌ No </body> found in: {os.path.basename(filepath)}")
        return False

print("=== Adding FAQ sections to tool pages ===")
for fname, data in TOOL_CONTENT.items():
    fpath = os.path.join(ROOT, fname)
    if os.path.exists(fpath):
        inject_faq(fpath, data)
    else:
        print(f"  ❌ File not found: {fname}")

# ─────────────────────────────────────────────────────────────
# 3. Create 6 new, high-quality blog articles
# ─────────────────────────────────────────────────────────────

BLOG_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{meta_desc}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://quickdopdf.com/blog/{slug}.html">
  <link rel="icon" type="image/png" href="../favicon.png">
  <title>{title} – Quick Do PDF Blog</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../tools.css">
  <link rel="stylesheet" href="blog-layout.css">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3543763798528021" crossorigin="anonymous"></script>
  <style>
    .blog-wrap {{ max-width: 760px; margin: 0 auto; padding: 90px 24px 80px; }}
    .blog-wrap h1 {{ font-size: 2.2rem; font-weight: 900; line-height: 1.2; margin-bottom: 16px; color: var(--text); }}
    .blog-meta {{ color: var(--muted); font-size: 0.88rem; margin-bottom: 36px; display: flex; gap: 20px; flex-wrap: wrap; }}
    .blog-wrap h2 {{ font-size: 1.35rem; font-weight: 800; margin: 36px 0 12px; color: var(--text); }}
    .blog-wrap h3 {{ font-size: 1.1rem; font-weight: 700; margin: 24px 0 8px; color: var(--text); }}
    .blog-wrap p {{ color: var(--muted); line-height: 1.8; margin-bottom: 16px; font-size: 1rem; }}
    .blog-wrap ul, .blog-wrap ol {{ color: var(--muted); line-height: 1.8; margin: 0 0 16px 24px; font-size: 1rem; }}
    .blog-wrap li {{ margin-bottom: 6px; }}
    .tip-box {{ background: var(--card-bg, #f0fdf4); border-left: 4px solid #22c55e; padding: 16px 20px; border-radius: 0 10px 10px 0; margin: 24px 0; }}
    .tip-box strong {{ color: #15803d; font-weight: 800; }}
    .cta-box {{ background: linear-gradient(135deg, #6366f1, #8b5cf6); border-radius: 16px; padding: 32px; text-align: center; margin: 48px 0; color: #fff; }}
    .cta-box h3 {{ color: #fff; margin: 0 0 10px; font-size: 1.4rem; }}
    .cta-box p {{ color: rgba(255,255,255,0.85); margin: 0 0 20px; }}
    .cta-btn {{ background: #fff; color: #6366f1; padding: 12px 28px; border-radius: 100px; font-weight: 800; text-decoration: none; display: inline-block; font-size: 0.95rem; }}
    .back-link {{ display: inline-flex; align-items: center; gap: 6px; color: var(--muted); text-decoration: none; font-size: 0.9rem; margin-bottom: 32px; }}
    .back-link:hover {{ color: var(--text); }}
  </style>
</head>
<body>
  <header>
    <a href="../index.html" class="back-btn">← Home</a>
    <span class="logo">Quick Do PDF</span>
    <div class="header-right"></div>
  </header>
  <main>
    <div class="blog-wrap">
      <a href="index.html" class="back-link">← Back to Blog</a>
      <h1>{title}</h1>
      <div class="blog-meta">
        <span>📅 {date}</span>
        <span>⏱ {read_time} min read</span>
        <span>📂 {category}</span>
      </div>
      {body}
    </div>
  </main>
</body>
</html>'''

BLOGS = [
    {
        "slug": "how-to-reduce-pdf-file-size-free",
        "title": "How to Reduce PDF File Size for Free (5 Easy Methods in 2025)",
        "meta_desc": "Learn 5 proven methods to reduce PDF file size for free — no software installation needed. Works on Windows, Mac, iPhone, and Android.",
        "date": "March 25, 2025",
        "read_time": "7",
        "category": "PDF Tips",
        "body": """
      <p>A large PDF file can cause headaches — email attachments bounce, government portal uploads fail, and slow downloads frustrate everyone. The good news: reducing PDF file size is easy and completely free. Here are 5 reliable methods that work in 2025.</p>

      <h2>Method 1: Use an Online PDF Compressor (Fastest)</h2>
      <p>The quickest way to shrink a PDF is an online compression tool. <a href="../compress.html">Quick Do PDF's free compressor</a> runs entirely in your browser — no file upload, no accounts, no watermarks.</p>
      <ol>
        <li>Go to the <a href="../compress.html">Compress PDF</a> tool</li>
        <li>Drop your PDF onto the upload area</li>
        <li>Choose a compression level (Standard reduces most files by 50–80%)</li>
        <li>Click <strong>Compress PDF</strong> and download the result</li>
      </ol>
      <div class="tip-box"><strong>💡 Tip:</strong> The "Standard" compression level is best for most documents. Use "Max Compression" only when you need to hit a very small size like 100KB for a form submission.</div>

      <h2>Method 2: Reduce Image Quality Before Creating the PDF</h2>
      <p>If you're creating a PDF from a Word document or presentation, reduce image resolution before exporting. In Microsoft Word: <strong>File → Options → Advanced → Image Size and Quality</strong>. Set DPI to 150 (screen quality) instead of the default 220.</p>

      <h2>Method 3: Use Adobe Acrobat's Save As (Free Trial)</h2>
      <p>Adobe's "Reduce File Size" feature (File → Save As → Reduced Size PDF) can cut file size by 30–60% for most PDFs. You can use this during the free trial period. Note that this installs software on your computer.</p>

      <h2>Method 4: Print to PDF (Built-in Windows/Mac Feature)</h2>
      <p>This method re-renders the PDF and often strips unnecessary metadata:</p>
      <ol>
        <li>Open the PDF in your browser (Chrome/Edge/Safari)</li>
        <li>Press <strong>Ctrl+P</strong> (Windows) or <strong>Cmd+P</strong> (Mac)</li>
        <li>Set the destination to "Save as PDF" or "Microsoft Print to PDF"</li>
        <li>Click Save</li>
      </ol>
      <p>This typically reduces file size by 10–40% and works for any PDF you can open.</p>

      <h2>Method 5: Remove Unnecessary Pages</h2>
      <p>If your PDF has blank pages, cover pages, or appendices you don't need, removing them dramatically reduces size. Use our <a href="../delete-pages.html">Delete Pages from PDF</a> tool to remove specific pages before compressing.</p>

      <h2>Which Method Should You Use?</h2>
      <ul>
        <li><strong>Need it done in 30 seconds?</strong> → Use the online compressor</li>
        <li><strong>Creating from Word?</strong> → Reduce image quality first, then export</li>
        <li><strong>Removing blank pages?</strong> → Delete pages then compress</li>
        <li><strong>Already at 2MB and need under 200KB?</strong> → Use Max Compression mode</li>
      </ul>

      <div class="cta-box">
        <h3>Ready to Compress Your PDF?</h3>
        <p>Free, no sign-up, works in your browser. Your file never leaves your device.</p>
        <a href="../compress.html" class="cta-btn">Compress PDF Now →</a>
      </div>

      <h2>Frequently Asked Questions</h2>
      <h3>How much can I reduce a PDF file size?</h3>
      <p>Typically 30–80% depending on content. PDFs made mostly of scanned images compress the most. Text-only documents compress less since text is already efficient.</p>
      <h3>Does compressing reduce quality?</h3>
      <p>At standard compression levels, quality is barely perceptible to the human eye. Only "Max Compression" modes cause visible image degradation.</p>
      <h3>Can I compress a PDF on iPhone?</h3>
      <p>Yes — our online tool works on iOS Safari. Just visit <strong>quickdopdf.com/compress.html</strong> from your iPhone browser.</p>
"""
    },
    {
        "slug": "pdf-vs-docx-which-format-to-use",
        "title": "PDF vs DOCX: Which File Format Should You Use in 2025?",
        "meta_desc": "PDF vs DOCX — when to use each format. Learn the key differences between PDF and Word files for sharing, editing, printing, and storage.",
        "date": "March 22, 2025",
        "read_time": "6",
        "category": "Education",
        "body": """
      <p>You've finished writing a document and now you need to share it. Should you send a PDF or a Word DOCX file? The answer depends entirely on what you want the recipient to do with it. Let's break down the differences clearly.</p>

      <h2>What Is a PDF?</h2>
      <p>PDF (Portable Document Format) was created by Adobe in 1993. Its defining feature is that it looks identical on every device — the same fonts, layout, and formatting regardless of the operating system, software, or screen size. PDFs are designed to be <em>read</em>, not edited.</p>

      <h2>What Is a DOCX?</h2>
      <p>DOCX is Microsoft Word's format, introduced with Office 2007. It's designed for editing — the content flows and reflows based on the viewer's software and settings. The same DOCX may look different on different versions of Word or LibreOffice.</p>

      <h2>PDF vs DOCX: Key Differences</h2>
      <ul>
        <li><strong>Consistency:</strong> PDF looks the same everywhere. DOCX may reflow on different software.</li>
        <li><strong>Editability:</strong> DOCX is easy to edit. PDF requires special software to edit.</li>
        <li><strong>Security:</strong> PDF supports password protection and read-only locking. DOCX can be password-protected but is easier to bypass.</li>
        <li><strong>File Size:</strong> PDFs with images can be very large; text-only PDFs are very small. DOCX files are generally small.</li>
        <li><strong>Printing:</strong> PDFs print exactly as designed. DOCX may shift during printing.</li>
        <li><strong>Accessibility:</strong> Both support accessibility features, but PDFs need extra work to make compliant.</li>
      </ul>

      <h2>When to Use PDF</h2>
      <ul>
        <li>Sending a resume, invoice, or contract — you want it to look exactly right</li>
        <li>Publishing documents for download on your website</li>
        <li>Submitting forms to government portals or universities</li>
        <li>Archiving documents long-term</li>
        <li>Protecting documents from easy editing</li>
      </ul>

      <h2>When to Use DOCX</h2>
      <ul>
        <li>Collaborating with others who need to track changes and add comments</li>
        <li>Sending a draft for someone to edit and return</li>
        <li>Working with templates that will be reused and modified</li>
        <li>Using mail merge for bulk documents</li>
      </ul>

      <div class="tip-box"><strong>💡 Pro Tip:</strong> Send DOCX to collaborators, but always convert to PDF before sending the final version to clients, employers, or government agencies.</div>

      <h2>Can I Convert Between PDF and DOCX?</h2>
      <p>Yes! You can convert in both directions:</p>
      <ul>
        <li><a href="../pdf-to-word.html">PDF to Word (DOCX)</a> — extracts the content from a PDF into an editable Word document</li>
        <li><a href="../word-to-pdf.html">Word to PDF</a> — converts DOCX to a perfectly formatted, locked PDF</li>
      </ul>

      <div class="cta-box">
        <h3>Need to Convert Between PDF and Word?</h3>
        <p>Free, instant, no sign-up. Works in your browser on any device.</p>
        <a href="../pdf-to-word.html" class="cta-btn">Convert PDF to Word →</a>
      </div>

      <h2>Summary</h2>
      <p>Use <strong>PDF for sharing final documents</strong> and <strong>DOCX for working documents</strong>. When in doubt, PDF is safer for external sharing since you know exactly how it will look on the other end.</p>
"""
    },
    {
        "slug": "how-to-sign-a-pdf-document-free",
        "title": "How to Sign a PDF Document for Free (Without Printing or Scanning)",
        "meta_desc": "Learn how to digitally sign a PDF document without printing it. Sign PDFs online for free using your mouse, touch screen, or typed signature.",
        "date": "March 20, 2025",
        "read_time": "5",
        "category": "How-To",
        "body": """
      <p>The old way of signing a PDF involved printing the document, signing it by hand, scanning it back, and emailing the scanned image. That's a waste of time, paper, and ink. Today you can sign any PDF digitally in under 2 minutes — for free.</p>

      <h2>Why Sign PDFs Digitally?</h2>
      <ul>
        <li>✅ No printing or scanning needed</li>
        <li>✅ Legally binding in most countries (US ESIGN Act, EU eIDAS, India IT Act)</li>
        <li>✅ Done in seconds from any device</li>
        <li>✅ Looks professional and clean</li>
        <li>✅ Environmentally friendly</li>
      </ul>

      <h2>How to Sign a PDF Online (Step-by-Step)</h2>
      <ol>
        <li>Go to <a href="../sign.html">Quick Do PDF's free PDF Signer</a></li>
        <li>Click <strong>"Select PDF File"</strong> and upload your document</li>
        <li>Choose your signature type:
          <ul>
            <li><strong>Draw:</strong> Sign with your mouse or touchscreen</li>
            <li><strong>Type:</strong> Type your name in a signature font</li>
            <li><strong>Upload:</strong> Use an image of your real signature</li>
          </ul>
        </li>
        <li>Click on the document where you want to place the signature</li>
        <li>Resize and position the signature as needed</li>
        <li>Click <strong>"Download Signed PDF"</strong></li>
      </ol>

      <div class="tip-box"><strong>💡 Tip:</strong> For the most professional look, choose "Draw" on a touchscreen with a stylus, or "Upload" a scanned image of your actual signature.</div>

      <h2>Is a Digital Signature Legally Valid?</h2>
      <p>For most everyday business documents — contracts, agreements, invoices, consent forms, employment documents — a digital signature is legally binding in:</p>
      <ul>
        <li><strong>United States:</strong> Electronic Signatures in Global and National Commerce Act (ESIGN, 2000)</li>
        <li><strong>European Union:</strong> eIDAS Regulation</li>
        <li><strong>India:</strong> Information Technology Act 2000</li>
        <li><strong>UK:</strong> Electronic Communications Act 2000</li>
      </ul>
      <p><em>Note: Some documents like wills, adoption papers, and real estate deeds may still require wet (ink) signatures depending on jurisdiction.</em></p>

      <h2>How Does It Compare to DocuSign?</h2>
      <p>DocuSign and Adobe Sign cost $10–$40/month for individual plans. For signing your own documents — NDAs, contracts, offer letters — our free tool works just as well with no subscription needed. DocuSign is worth paying for when you need multi-party signing with audit trails for high-value contracts.</p>

      <div class="cta-box">
        <h3>Sign Your PDF Now — Free</h3>
        <p>No account. No watermark. Works on mobile. Your signature stays on your device.</p>
        <a href="../sign.html" class="cta-btn">Sign PDF Free →</a>
      </div>
"""
    },
    {
        "slug": "how-to-protect-a-pdf-with-password",
        "title": "How to Password Protect a PDF File for Free (2025 Guide)",
        "meta_desc": "Learn how to add password protection to any PDF file for free. Step-by-step guide to locking PDFs with 128-bit AES encryption without Adobe Acrobat.",
        "date": "March 18, 2025",
        "read_time": "5",
        "category": "Security",
        "body": """
      <p>Whether you're sharing a salary slip, a legal contract, a medical report, or confidential business data, adding a password to your PDF ensures only the intended recipient can open it. Here's how to do it for free in 2025.</p>

      <h2>What Does "Password Protecting a PDF" Actually Do?</h2>
      <p>PDF encryption works in two ways:</p>
      <ul>
        <li><strong>Open Password (User Password):</strong> Anyone who tries to open the PDF must enter this password. Without it, the file appears empty or locked in all PDF readers including Chrome, Adobe, and Foxit.</li>
        <li><strong>Permissions Password (Owner Password):</strong> Controls what the opener can do — whether they can print, copy text, or edit the document.</li>
      </ul>

      <h2>How to Password Protect a PDF (Step-by-Step)</h2>
      <ol>
        <li>Go to <a href="../protect.html">Quick Do PDF's Protect PDF tool</a></li>
        <li>Click <strong>"Select PDF File"</strong> or drag and drop your document</li>
        <li>Enter your desired password in the <strong>"Open Password"</strong> field</li>
        <li>Optionally set permissions (restrict printing, copying, or editing)</li>
        <li>Click <strong>"Protect PDF"</strong> and download the encrypted file</li>
      </ol>

      <div class="tip-box"><strong>💡 Tip:</strong> Use a password that is at least 12 characters with a mix of letters, numbers, and symbols. Write it down somewhere safe — there is no way to recover it if forgotten.</div>

      <h2>What Encryption Level Is Used?</h2>
      <p>Our tool uses <strong>128-bit AES encryption</strong> (the same as Adobe Acrobat Standard). This level of encryption is used by banks, governments, and military organizations. Brute-forcing a 128-bit AES key is computationally infeasible with current technology.</p>

      <h2>Can Someone Remove the Password?</h2>
      <p>If someone knows your password, they can use many tools to remove the protection. If they don't know the password, 128-bit AES is virtually uncrackable. The security of your PDF depends on the strength of the password you choose, not the encryption algorithm.</p>

      <h2>Common Use Cases for PDF Password Protection</h2>
      <ul>
        <li>Salary slips and payroll documents sent to employees</li>
        <li>Medical reports shared with patients</li>
        <li>Legal documents and contracts</li>
        <li>Financial statements and bank documents</li>
        <li>Academic results and certificates</li>
      </ul>

      <div class="cta-box">
        <h3>Protect Your PDF Now — Free</h3>
        <p>128-bit AES encryption. No account needed. Your file never leaves your browser.</p>
        <a href="../protect.html" class="cta-btn">Add Password Protection →</a>
      </div>
"""
    },
    {
        "slug": "best-pdf-tools-for-students-2025",
        "title": "7 Best Free PDF Tools for Students in 2025",
        "meta_desc": "Discover the 7 most useful free PDF tools for students — merge notes, annotate, compress assignments, and more. No software installation needed.",
        "date": "March 15, 2025",
        "read_time": "7",
        "category": "Students",
        "body": """
      <p>As a student, you're constantly dealing with PDFs — lecture notes, research papers, assignment submissions, and textbooks. Here are the 7 free PDF tools every student should know about in 2025.</p>

      <h2>1. Merge PDF – Combine All Your Notes Into One File</h2>
      <p>After a semester of lectures, you might have 30 separate slide PDFs. Merge them into a single, searchable document before exam season. <a href="../merge.html">Merge PDF free →</a></p>

      <h2>2. Compress PDF – Submit Within Email and Portal Limits</h2>
      <p>Many university submission portals have a 2MB or 5MB file size limit. If your scanned assignment is 15MB, it won't upload. Compress it first in seconds. <a href="../compress.html">Compress PDF free →</a></p>

      <h2>3. Split PDF – Extract Specific Chapters</h2>
      <p>Have a 400-page textbook PDF but only need chapters 5–8? Split out just those pages into a separate file for easier studying. <a href="../split.html">Split PDF free →</a></p>

      <h2>4. PDF to Word – Edit Lecture Slides</h2>
      <p>When professors share PDFs of their slides and you want to add your own notes directly in a Word document, convert the PDF to DOCX first. <a href="../pdf-to-word.html">PDF to Word free →</a></p>

      <h2>5. JPG to PDF – Scan Handwritten Notes</h2>
      <p>After taking handwritten notes, photograph each page with your phone and convert the images to a PDF for archiving and sharing. <a href="../jpg-to-pdf.html">JPG to PDF free →</a></p>

      <h2>6. Sign PDF – Sign Assignment Consent Forms</h2>
      <p>Universities increasingly use digital consent forms, internship agreements, and enrollment documents. Sign them in seconds without printing. <a href="../sign.html">Sign PDF free →</a></p>

      <h2>7. Protect PDF – Lock Sensitive Documents</h2>
      <p>If you're sharing research data, financial aid documents, or personal academic records via email, always password-protect the PDF first. <a href="../protect.html">Protect PDF free →</a></p>

      <div class="tip-box"><strong>💡 Student Tip:</strong> Bookmark quickdopdf.com on your phone. All tools work on mobile browsers — perfect for scanning and submitting assignments on the go without installing any app.</div>

      <h2>Why Use Quick Do PDF Instead of Installing Software?</h2>
      <ul>
        <li><strong>No installation</strong> — works on any device including university computers where you can't install software</li>
        <li><strong>Privacy first</strong> — your files never leave your device, so sensitive personal documents stay secure</li>
        <li><strong>Always free</strong> — no trials, no credit card, no paid upgrades</li>
        <li><strong>Mobile-friendly</strong> — works on iPhone and Android browsers natively</li>
      </ul>

      <div class="cta-box">
        <h3>All PDF Tools in One Place</h3>
        <p>30+ free tools. No account. No software. Works on any device.</p>
        <a href="../index.html" class="cta-btn">Explore All Tools →</a>
      </div>
"""
    },
    {
        "slug": "what-is-a-pdf-and-how-does-it-work",
        "title": "What Is a PDF? How It Works and Why It Matters",
        "meta_desc": "Learn what a PDF is, how it works, and why it became the world's most popular document format. Complete beginner-friendly guide to PDF files.",
        "date": "March 10, 2025",
        "read_time": "6",
        "category": "Education",
        "body": """
      <p>You've opened thousands of PDF files, but do you know what's actually inside one? Understanding how PDFs work helps you use them more effectively and troubleshoot problems when they behave unexpectedly.</p>

      <h2>What Does PDF Stand For?</h2>
      <p>PDF stands for <strong>Portable Document Format</strong>. It was created by Adobe Systems co-founder John Warnock in 1991 as part of the "Camelot Project" — his vision for a universal document format that looked the same on every computer, printer, and operating system.</p>
      <p>Adobe released PDF as an open standard in 2008, and it is now maintained by the International Organization for Standardization (ISO) as ISO 32000.</p>

      <h2>Why Did PDF Become So Dominant?</h2>
      <p>Before PDFs, sharing documents was chaotic. A document created in WordPerfect on a Windows PC looked completely different when opened on a Mac running Microsoft Word. Fonts would change, layouts would break, and what the author designed was never what the reader saw.</p>
      <p>PDF solved this by embedding everything — fonts, images, layout instructions, and metadata — into a single self-contained file. The viewer simply renders what's described in the file, regardless of what software is installed.</p>

      <h2>What's Inside a PDF File?</h2>
      <p>A PDF is a binary file containing several types of objects:</p>
      <ul>
        <li><strong>Content streams:</strong> Page drawing instructions written in PDF's own programming language</li>
        <li><strong>Resources:</strong> Fonts, images, and color space definitions</li>
        <li><strong>Structure tree:</strong> Accessibility information about heading levels and reading order</li>
        <li><strong>Cross-reference table:</strong> An index letting PDF readers jump to any page instantly without parsing the whole file</li>
        <li><strong>Metadata:</strong> Author, creation date, software used, keywords</li>
      </ul>

      <h2>Text vs Scanned PDFs — The Critical Difference</h2>
      <p>There are two fundamentally different types of PDFs:</p>
      <ul>
        <li><strong>Text-based PDFs:</strong> Created digitally from Word, Excel, or design software. The text is stored as actual characters — fully searchable, selectable, and extremely compact.</li>
        <li><strong>Scanned PDFs (Image PDFs):</strong> Pages photographed or photocopied and saved as images inside a PDF wrapper. Text cannot be searched or selected unless OCR (Optical Character Recognition) is applied. These files are much larger.</li>
      </ul>
      <div class="tip-box"><strong>💡 Test yours:</strong> Try selecting text on a page. If you can highlight individual words, it's a text-based PDF. If your cursor turns into a crosshair selecting a rectangle, it's an image/scanned PDF.</div>

      <h2>PDF Versions and Standards</h2>
      <ul>
        <li><strong>PDF 1.0–1.7:</strong> Original Adobe-controlled versions adding layers, forms, encryption, etc.</li>
        <li><strong>PDF 2.0:</strong> The first ISO-standard version (2017) with enhanced encryption and digital signing.</li>
        <li><strong>PDF/A:</strong> Archival standard — self-contained files guaranteed to be readable in 100 years.</li>
        <li><strong>PDF/X:</strong> Pre-press standard for print production.</li>
        <li><strong>PDF/UA:</strong> Universal Accessibility standard for people with disabilities.</li>
      </ul>

      <h2>How Are PDFs Created?</h2>
      <p>PDFs can be created from virtually any application that supports printing. In Windows, macOS, and Linux, you can "print to PDF" from any program. Applications like Microsoft Word, Google Docs, Adobe InDesign, and web browsers all offer native PDF export.</p>

      <h2>Can You Edit a PDF?</h2>
      <p>PDFs are designed for viewing, not editing — that's partly the point. However, you can:</p>
      <ul>
        <li>Convert the PDF to Word and edit it: <a href="../pdf-to-word.html">PDF to Word tool</a></li>
        <li>Add text annotations, signatures, and stamps: <a href="../edit-pdf.html">Edit PDF tool</a></li>
        <li>Fill interactive form fields if the PDF has them: <a href="../fill-pdf.html">Fill PDF Forms</a></li>
      </ul>

      <div class="cta-box">
        <h3>Work With Your PDFs — Free</h3>
        <p>30+ tools for merging, splitting, compressing, converting, and editing PDFs. No sign-up required.</p>
        <a href="../index.html" class="cta-btn">Explore Free PDF Tools →</a>
      </div>
"""
    },
]

print("\n=== Creating new blog articles ===")
for blog in BLOGS:
    fpath = os.path.join(BLOG, blog["slug"] + ".html")
    if os.path.exists(fpath):
        print(f"  ⚠ Already exists: {blog['slug']}.html")
        continue
    
    content = BLOG_TEMPLATE.format(
        slug=blog["slug"],
        title=blog["title"],
        meta_desc=blog["meta_desc"],
        date=blog["date"],
        read_time=blog["read_time"],
        category=blog["category"],
        body=blog["body"]
    )
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ Created: {blog['slug']}.html")

# ─────────────────────────────────────────────────────────────
# 4. Update About Us page with much richer content
# ─────────────────────────────────────────────────────────────

ABOUT_EXTRA = """
<section style="max-width:800px; margin: 0 auto; padding: 0 24px 60px;">
  <h2 style="font-size: 1.4rem; font-weight: 800; margin: 40px 0 12px; color: var(--text);">Our Story</h2>
  <p style="color: var(--muted); line-height: 1.8; margin-bottom: 16px;">Quick Do PDF was born out of frustration. Every time we needed to merge a couple of PDFs, compress a file for email, or quickly split a document, we'd be directed to websites that demanded account creation, showed intrusive ads, placed watermarks on our files, or — worst of all — uploaded our sensitive documents to remote servers.</p>
  <p style="color: var(--muted); line-height: 1.8; margin-bottom: 16px;">We believed there had to be a better way. In 2023, we built the first version of Quick Do PDF: a simple, client-side PDF toolkit that runs entirely in your browser. No servers. No uploads. No accounts. No watermarks. Just tools that work.</p>

  <h2 style="font-size: 1.4rem; font-weight: 800; margin: 40px 0 12px; color: var(--text);">What We Stand For</h2>
  <ul style="color: var(--muted); line-height: 1.8; margin: 0 0 24px 24px;">
    <li style="margin-bottom: 8px;"><strong style="color: var(--text);">Privacy by Design:</strong> Every tool on this site processes your files locally in JavaScript. Your documents never travel across the internet to our servers.</li>
    <li style="margin-bottom: 8px;"><strong style="color: var(--text);">Zero Cost, Always:</strong> All 30+ tools are free. We are sustained by advertising, not paywalls or data collection.</li>
    <li style="margin-bottom: 8px;"><strong style="color: var(--text);">No Registration:</strong> We will never ask you to create an account just to use a basic utility.</li>
    <li style="margin-bottom: 8px;"><strong style="color: var(--text);">Speed First:</strong> Every tool is designed to complete common tasks in under 60 seconds.</li>
  </ul>

  <h2 style="font-size: 1.4rem; font-weight: 800; margin: 40px 0 12px; color: var(--text);">Our Tools</h2>
  <p style="color: var(--muted); line-height: 1.8; margin-bottom: 16px;">We currently offer 30+ PDF tools covering the most common document tasks:</p>
  <ul style="color: var(--muted); line-height: 1.8; margin: 0 0 24px 24px;">
    <li style="margin-bottom: 6px;">Merge, Split, Compress PDFs</li>
    <li style="margin-bottom: 6px;">Convert PDF to Word, Excel, PowerPoint, JPG, HTML, and Text</li>
    <li style="margin-bottom: 6px;">Convert Word, Excel, JPG, and HTML to PDF</li>
    <li style="margin-bottom: 6px;">Add watermarks, headers, footers, and page numbers</li>
    <li style="margin-bottom: 6px;">Password protect and unlock PDFs</li>
    <li style="margin-bottom: 6px;">Sign PDFs digitally</li>
    <li style="margin-bottom: 6px;">AI-powered PDF summarizer and chat</li>
    <li style="margin-bottom: 6px;">AI Resume Builder with 15+ templates</li>
  </ul>

  <h2 style="font-size: 1.4rem; font-weight: 800; margin: 40px 0 12px; color: var(--text);">Who Uses Quick Do PDF?</h2>
  <p style="color: var(--muted); line-height: 1.8; margin-bottom: 16px;">Our users come from every walk of life. Students submitting assignments under size limits. Small business owners creating and signing agreements. Lawyers and paralegals handling confidential documents. Government employees processing forms. Teachers preparing course materials. IT departments handling sensitive corporate documents.</p>
  <p style="color: var(--muted); line-height: 1.8; margin-bottom: 16px;">What they all share is a need for tools that are fast, private, and reliable — without the overhead of enterprise software.</p>

  <h2 style="font-size: 1.4rem; font-weight: 800; margin: 40px 0 12px; color: var(--text);">Get in Touch</h2>
  <p style="color: var(--muted); line-height: 1.8; margin-bottom: 16px;">Have a feature request? Found a bug? Want to report an issue or just share feedback? We read every message.</p>
  <p style="color: var(--muted); line-height: 1.8;"><a href="contact.html" style="color: var(--a1, #6366f1); font-weight: 700;">→ Contact Us</a></p>
</section>
"""

about_path = os.path.join(ROOT, "about.html")
with open(about_path, 'r', encoding='utf-8', errors='replace') as f:
    about_html = f.read()

if "Our Story" not in about_html:
    about_html = about_html.replace('</body>', ABOUT_EXTRA + '\n</body>', 1)
    with open(about_path, 'w', encoding='utf-8') as f:
        f.write(about_html)
    print("\n  ✅ About page enriched")
else:
    print("\n  ⚠ About page already enriched")

print("\n✅ All done!")
