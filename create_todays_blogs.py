import os

BLOG = r'd:\Yogi\Yogesh\quick-do-pdf\blog'

TEMPLATE = '''<!DOCTYPE html>
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
    .warn-box {{ background: rgba(251,191,36,0.1); border-left: 4px solid #fbbf24; padding: 16px 20px; border-radius: 0 10px 10px 0; margin: 24px 0; }}
    .cta-box {{ background: linear-gradient(135deg, #6366f1, #8b5cf6); border-radius: 16px; padding: 32px; text-align: center; margin: 48px 0; color: #fff; }}
    .cta-box h3 {{ color: #fff; margin: 0 0 10px; font-size: 1.4rem; }}
    .cta-box p {{ color: rgba(255,255,255,0.85); margin: 0 0 20px; }}
    .cta-btn {{ background: #fff; color: #6366f1; padding: 12px 28px; border-radius: 100px; font-weight: 800; text-decoration: none; display: inline-block; font-size: 0.95rem; }}
    .back-link {{ display: inline-flex; align-items: center; gap: 6px; color: var(--muted); text-decoration: none; font-size: 0.9rem; margin-bottom: 32px; }}
    .steps-box {{ counter-reset: step-counter; list-style: none; margin: 0 0 20px 0; padding: 0; }}
    .steps-box li {{ counter-increment: step-counter; padding: 14px 16px 14px 56px; position: relative; border-left: 3px solid var(--border); margin-bottom: 8px; border-radius: 0 10px 10px 0; background: var(--surface); color: var(--muted); line-height: 1.6; }}
    .steps-box li::before {{ content: counter(step-counter); position: absolute; left: -1px; top: 50%; transform: translateY(-50%); background: #6366f1; color: #fff; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 900; font-size: 0.9rem; }}
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

articles = [
    {
        "slug": "how-to-extract-images-from-pdf",
        "title": "How to Extract Images from a PDF for Free",
        "meta_desc": "Learn how to extract photos, illustrations and graphics from any PDF file for free. Step-by-step guide — no software installation, works in your browser.",
        "date": "March 29, 2026",
        "read_time": "5",
        "category": "How-To",
        "body": """
      <p>PDFs often contain valuable images — product photos, charts, diagrams, scanned documents, and illustrations. Extracting them individually used to require expensive software. Today you can do it for free in seconds. Here's how.</p>

      <h2>Method 1: Use Quick Do PDF (Fastest — No Installation)</h2>
      <ol class="steps-box">
        <li>Go to <a href="../extract-images.html">quickdopdf.com/extract-images.html</a></li>
        <li>Click <strong>"Select PDF File"</strong> or drag your PDF onto the page</li>
        <li>The tool automatically detects and extracts all embedded images</li>
        <li>Preview each image and select which ones to download</li>
        <li>Download as individual JPG/PNG files or as a ZIP archive</li>
      </ol>
      <div class="tip-box"><strong>💡 Tip:</strong> The tool extracts images at their original resolution — no quality loss compared to screenshotting the PDF page.</div>

      <h2>Method 2: Take Screenshots (Quick for 1-2 Images)</h2>
      <p>For just one or two images, a simple screenshot works well:</p>
      <ol>
        <li>Open the PDF in Chrome, Adobe, or any PDF viewer</li>
        <li>Zoom in to full resolution (200% or higher)</li>
        <li>Press <strong>Windows + Shift + S</strong> (Windows Snipping Tool) or <strong>Cmd + Shift + 4</strong> (Mac)</li>
        <li>Select just the image area</li>
        <li>Paste into Paint, Photos, or any image editor and save</li>
      </ol>
      <div class="warn-box"><strong>⚠ Limitation:</strong> Screenshots capture at screen resolution (72-96 DPI), not the original image quality. For print use, always use the proper extraction tool.</div>

      <h2>Method 3: Open PDF in Chrome → Save Image</h2>
      <ol>
        <li>Open the PDF in Chrome browser</li>
        <li>Right-click on the image you want</li>
        <li>Select <strong>"Save image as..."</strong></li>
        <li>Choose your save location</li>
      </ol>
      <p><em>Note: This only works if Chrome can detect the image as a standalone object within the PDF, which depends on how the PDF was created.</em></p>

      <h2>What Types of Images Can Be Extracted?</h2>
      <ul>
        <li><strong>Photos</strong> — JPEG images embedded in the PDF</li>
        <li><strong>Illustrations</strong> — PNG, GIF images in the document</li>
        <li><strong>Charts and graphs</strong> — if embedded as images (not vector SVG)</li>
        <li><strong>Scanned document pages</strong> — each page is typically one large image</li>
        <li><strong>Logos and icons</strong> — small graphics within documents</li>
      </ul>
      <div class="warn-box"><strong>⚠ Note:</strong> Vector graphics (drawn in tools like Illustrator and placed as vectors) cannot be extracted as raster images — they're mathematical paths, not pixel images.</div>

      <h2>Common Use Cases</h2>
      <ul>
        <li>Recovering product photos from a supplier's PDF catalogue</li>
        <li>Extracting charts from research papers for presentations</li>
        <li>Recovering scanned document images</li>
        <li>Designers reusing images from old project PDFs</li>
        <li>Journalists extracting images from press releases</li>
      </ul>

      <div class="cta-box">
        <h3>Extract Images from PDF — Free</h3>
        <p>Original quality. No sign-up. Works on any device in your browser.</p>
        <a href="../extract-images.html" class="cta-btn">Extract PDF Images →</a>
      </div>

      <h2>Frequently Asked Questions</h2>
      <h3>Will extracted images be in their original quality?</h3>
      <p>Yes — our tool extracts images at their original embedded resolution, which is always better than screenshotting.</p>
      <h3>Can I extract images from a scanned PDF?</h3>
      <p>Yes. Each scanned page is stored as one large image in the PDF, and our tool will extract it fully.</p>
      <h3>Can I extract images from a password-protected PDF?</h3>
      <p>You need to <a href="../unlock.html">unlock it first</a>, then extract images.</p>
"""
    },
    {
        "slug": "how-to-add-watermark-to-pdf-free",
        "title": "How to Add a Watermark to a PDF for Free (2026 Guide)",
        "meta_desc": "Add text or image watermarks to any PDF for free. Step-by-step guide to watermarking PDFs with custom text, opacity, and position — no software needed.",
        "date": "March 29, 2026",
        "read_time": "5",
        "category": "How-To",
        "body": """
      <p>Watermarking a PDF protects your work, marks documents as confidential, or brands your deliverables. Here's how to add both text and image watermarks to any PDF for free.</p>

      <h2>Types of Watermarks</h2>
      <ul>
        <li><strong>Text watermark</strong> — "CONFIDENTIAL", "DRAFT", "SAMPLE", or your company name diagonally across each page</li>
        <li><strong>Image watermark</strong> — Your logo or signature placed on every page</li>
        <li><strong>Full-page watermark</strong> — A large semi-transparent mark covering the entire page</li>
      </ul>

      <h2>How to Add a Text Watermark (Step-by-Step)</h2>
      <ol class="steps-box">
        <li>Go to <a href="../watermark.html">quickdopdf.com/watermark.html</a></li>
        <li>Upload your PDF file</li>
        <li>Choose <strong>"Text Watermark"</strong></li>
        <li>Type your watermark text (e.g., "CONFIDENTIAL" or your company name)</li>
        <li>Set font size, color, and opacity (30-50% opacity looks professional)</li>
        <li>Choose position: center, diagonal, corner</li>
        <li>Click <strong>"Add Watermark"</strong> and download</li>
      </ol>

      <h2>How to Add an Image/Logo Watermark</h2>
      <ol class="steps-box">
        <li>Go to <a href="../watermark.html">quickdopdf.com/watermark.html</a></li>
        <li>Upload your PDF file</li>
        <li>Choose <strong>"Image Watermark"</strong></li>
        <li>Upload your logo (PNG with transparent background works best)</li>
        <li>Set size and opacity</li>
        <li>Position it in a corner or center</li>
        <li>Download the watermarked PDF</li>
      </ol>

      <div class="tip-box"><strong>💡 Best Practices:</strong>
        <ul style="margin: 8px 0 0 0;">
          <li>Use 30-40% opacity for text — visible but not blocking content</li>
          <li>PNG logos with transparent backgrounds look cleanest</li>
          <li>Diagonal text watermarks are hardest to remove or crop out</li>
          <li>"DRAFT" and "SAMPLE" watermarks are standard for client review documents</li>
        </ul>
      </div>

      <h2>Common Watermark Use Cases</h2>
      <ul>
        <li><strong>Freelancers:</strong> Watermark portfolio PDFs sent to potential clients with your name/website</li>
        <li><strong>Businesses:</strong> Mark internal reports "CONFIDENTIAL" before sharing</li>
        <li><strong>Authors/Creators:</strong> Add "DRAFT" to manuscripts sent for review</li>
        <li><strong>Photographers:</strong> Watermark PDF photo proofs with your studio name</li>
        <li><strong>Legal:</strong> Mark documents "PRIVILEGED AND CONFIDENTIAL"</li>
      </ul>

      <h2>Can Someone Remove a Watermark?</h2>
      <p>Text watermarks added over a PDF's content layer can potentially be edited out by someone with advanced PDF editing software. However, watermarks on scanned PDFs (image-based) are much harder to remove since the watermark is baked into the image pixels. For maximum protection, combine watermarking with <a href="../protect.html">password protection</a>.</p>

      <div class="cta-box">
        <h3>Add Watermark to PDF — Free</h3>
        <p>Text or image watermarks. Custom opacity. No sign-up required.</p>
        <a href="../watermark.html" class="cta-btn">Watermark PDF Now →</a>
      </div>
"""
    },
    {
        "slug": "how-to-do-pdf-ocr-free",
        "title": "PDF OCR: How to Convert Scanned PDF to Searchable Text Free",
        "meta_desc": "Learn how to use OCR to make scanned PDFs searchable and selectable. Free online PDF OCR guide — convert image-based PDFs to text without software.",
        "date": "March 29, 2026",
        "read_time": "6",
        "category": "How-To",
        "body": """
      <p>You've received a scanned PDF where you can't select, copy, or search any text. This happens because the document is stored as an image, not as machine-readable text. OCR (Optical Character Recognition) is the technology that converts these image-based PDFs into fully searchable, selectable documents.</p>

      <h2>What is OCR and Why Do You Need It?</h2>
      <p>OCR software analyzes the visual pattern of letters and words in an image and converts them into actual text characters. Without OCR:</p>
      <ul>
        <li>You can't search for words within the document</li>
        <li>You can't copy-paste any text from it</li>
        <li>Screen readers can't read it for accessibility</li>
        <li>PDF-to-Word converters produce blank or garbled output</li>
      </ul>
      <p>After OCR, all of the above work perfectly.</p>

      <h2>How to Do OCR on a PDF for Free</h2>
      <ol class="steps-box">
        <li>Go to <a href="../pdf-ocr.html">quickdopdf.com/pdf-ocr.html</a></li>
        <li>Upload your scanned PDF</li>
        <li>Select the document language (English, Hindi, etc.) for better accuracy</li>
        <li>Click <strong>"Run OCR"</strong></li>
        <li>Download the searchable PDF — now you can select and search text</li>
      </ol>

      <div class="tip-box"><strong>💡 After OCR:</strong> The output is a "searchable PDF" — it looks identical to the original scan, but has an invisible text layer underneath that makes search and copy-paste work perfectly.</div>

      <h2>OCR Accuracy Tips</h2>
      <ul>
        <li><strong>Scan quality matters most</strong> — 300 DPI or higher gives the best accuracy</li>
        <li><strong>Straight pages</strong> — skewed or angled scans reduce accuracy. Deskew the scan first.</li>
        <li><strong>Clear fonts</strong> — handwriting and decorative fonts are harder for OCR to read</li>
        <li><strong>Language selection</strong> — always select the correct language in the OCR tool</li>
        <li><strong>Review output</strong> — always check the recognized text, especially for numbers and similar-looking letters (1/l, 0/O)</li>
      </ul>

      <h2>Common Use Cases for PDF OCR</h2>
      <ul>
        <li>Bank statements and bills received as scanned PDFs</li>
        <li>Old contracts or legal documents scanned from paper</li>
        <li>Government certificates and ID documents</li>
        <li>Research papers from older journals scanned as images</li>
        <li>Handwritten notes you want to make searchable</li>
        <li>Invoices from vendors who send scanned bills</li>
      </ul>

      <h2>OCR vs PDF to Word — What's the Difference?</h2>
      <p><strong>OCR</strong> creates a searchable PDF — the document still looks like the scan but has invisible text. <strong>PDF to Word</strong> extracts the text from a (preferably already-searchable) PDF into an editable Word document. For scanned PDFs, you should run OCR first, then convert to Word if you need to edit the content.</p>

      <div class="cta-box">
        <h3>Make Your Scanned PDF Searchable — Free</h3>
        <p>Instant OCR. Supports English, Hindi, and 30+ languages. No sign-up.</p>
        <a href="../pdf-ocr.html" class="cta-btn">Run PDF OCR Free →</a>
      </div>
"""
    },
    {
        "slug": "how-to-delete-pages-from-pdf-free",
        "title": "How to Delete Pages from a PDF for Free (2026)",
        "meta_desc": "Learn how to remove specific pages from a PDF for free without software. Delete blank pages, unwanted covers, or confidential sections in seconds.",
        "date": "March 29, 2026",
        "read_time": "4",
        "category": "How-To",
        "body": """
      <p>Need to remove a blank page, a confidential section, or an unwanted cover page from a PDF without re-creating the whole document? Here's how to do it for free in seconds.</p>

      <h2>How to Delete Pages from a PDF (Step-by-Step)</h2>
      <ol class="steps-box">
        <li>Go to <a href="../delete-pages.html">quickdopdf.com/delete-pages.html</a></li>
        <li>Upload your PDF file</li>
        <li>You'll see a thumbnail preview of every page</li>
        <li>Click the pages you want to delete (they'll be highlighted)</li>
        <li>Click <strong>"Delete Selected Pages"</strong></li>
        <li>Download the clean PDF with those pages removed</li>
      </ol>

      <div class="tip-box"><strong>💡 Tip:</strong> You can select multiple non-consecutive pages at once. Click page 1, hold Ctrl (Windows) or Cmd (Mac), then click page 5, page 12, etc.</div>

      <h2>When Would You Delete PDF Pages?</h2>
      <ul>
        <li><strong>Remove blank pages</strong> — scanners often add empty pages at the end</li>
        <li><strong>Remove cover page</strong> — internal documents with external-facing covers</li>
        <li><strong>Remove confidential sections</strong> — before sharing with certain parties</li>
        <li><strong>Remove boilerplate</strong> — terms, disclaimers, or annexures not needed by recipient</li>
        <li><strong>Reduce file size</strong> — removing unnecessary pages makes the PDF smaller</li>
        <li><strong>Trim exam papers</strong> — keep only the sections you need to study</li>
      </ul>

      <h2>Delete Pages vs Split PDF — Which to Use?</h2>
      <p><strong>Delete Pages</strong> is best when you want to keep most of the document and remove a few specific pages.</p>
      <p><strong>Split PDF</strong> is better when you want to extract a specific range of pages into a separate file (e.g., pages 10-20 as a standalone document).</p>

      <h2>Will Quality Be Affected?</h2>
      <p>No. Deleting pages from a PDF is a structural operation — no re-rendering or re-encoding happens. The remaining pages are identical to the originals, with no quality loss at all.</p>

      <h2>Can I Undo After Deleting?</h2>
      <p>Our tool creates a new PDF — your original file is untouched. Always keep your original PDF safe before making changes, as deleted pages cannot be recovered from the output file.</p>

      <div class="cta-box">
        <h3>Delete PDF Pages — Free</h3>
        <p>Visual page picker. No quality loss. Your file never leaves your browser.</p>
        <a href="../delete-pages.html" class="cta-btn">Delete PDF Pages →</a>
      </div>
"""
    },
    {
        "slug": "how-to-rotate-pages-in-pdf-free",
        "title": "How to Rotate Pages in a PDF for Free (2026 Guide)",
        "meta_desc": "Rotate one or all pages in a PDF to portrait or landscape for free. Fix upside-down or sideways scans without re-scanning. Works in your browser.",
        "date": "March 29, 2026",
        "read_time": "4",
        "category": "How-To",
        "body": """
      <p>Scanned a document upside down? Got a PDF where some pages are sideways? Rotating PDF pages is free and takes under 30 seconds. Here's how.</p>

      <h2>How to Rotate Pages in a PDF</h2>
      <ol class="steps-box">
        <li>Go to <a href="../rotate.html">quickdopdf.com/rotate.html</a></li>
        <li>Upload your PDF file</li>
        <li>See a thumbnail preview of all pages</li>
        <li>Click individual pages to select them, or click <strong>"Select All"</strong></li>
        <li>Choose rotation: <strong>90° Right</strong>, <strong>90° Left</strong>, or <strong>180°</strong></li>
        <li>Click <strong>"Rotate"</strong> and download the fixed PDF</li>
      </ol>

      <div class="tip-box"><strong>💡 Pro Tip:</strong> You can rotate specific pages differently. For example: rotate pages 2, 5, and 8 by 90° right, while leaving all other pages unchanged.</div>

      <h2>When Do You Need to Rotate PDF Pages?</h2>
      <ul>
        <li>Scanned documents where some pages are sideways or upside down</li>
        <li>Photographs of documents taken with phone in wrong orientation</li>
        <li>Presentation slides that were exported in landscape but open as portrait</li>
        <li>Architecture or engineering drawings that need landscape orientation</li>
        <li>Mixed-orientation PDFs where some pages are portrait and some are landscape</li>
      </ul>

      <h2>Does Rotating Affect Quality?</h2>
      <p>For <strong>text-based PDFs</strong> (created digitally): No quality loss at all. Rotation is just a metadata change — no pixels are changed.</p>
      <p>For <strong>scanned PDFs</strong> (image-based): There is a very minor quality impact since the image pixels are rearranged, but it's imperceptible at normal viewing sizes.</p>

      <h2>Rotate All Pages vs Rotate Specific Pages</h2>
      <p>If your entire document scanned sideways, use "Select All" and rotate everything at once. If only certain pages need rotation (common in mixed-format documents), select just those specific pages.</p>

      <h2>Will the File Size Change?</h2>
      <p>Barely — rotating a text-based PDF changes only metadata, so the file size stays identical. Rotating a scanned PDF may cause a marginal size change (less than 1%) due to pixel rearrangement.</p>

      <div class="cta-box">
        <h3>Rotate PDF Pages — Free</h3>
        <p>Rotate any page, any angle. No quality loss. Works on any device.</p>
        <a href="../rotate.html" class="cta-btn">Rotate PDF Pages →</a>
      </div>
"""
    },
]

print("Creating today's new blog articles...")
for art in articles:
    fpath = os.path.join(BLOG, art['slug'] + '.html')
    content = TEMPLATE.format(**art)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Created: {art['slug']}.html")
print(f"\nTotal created: {len(articles)} articles")
