import os

BLOG = r'd:\Yogi\Yogesh\quick-do-pdf\blog'
ROOT = r'd:\Yogi\Yogesh\quick-do-pdf'

new_cards = """
            <!-- NEW ARTICLES March 29, 2026 -->
            <a href="how-to-extract-images-from-pdf.html" class="blog-card" data-category="howto">
                <div class="card-img-wrap"><img src="images/thumb_extract_images.png" class="card-img" alt="Extract images from PDF" onerror="this.src='images/thumb_howto.png'"></div>
                <div class="card-body">
                    <span class="tag tag-howto">How-To</span>
                    <p class="date">March 29, 2026</p>
                    <h2>How to Extract Images from a PDF for Free</h2>
                    <p>Extract photos, charts, and graphics from any PDF at original quality &mdash; no software needed. Works in your browser.</p>
                    <span class="read-more">Read Article &rarr;</span>
                </div>
            </a>
            <a href="how-to-add-watermark-to-pdf-free.html" class="blog-card" data-category="howto">
                <div class="card-img-wrap"><img src="images/thumb_watermark_pdf.png" class="card-img" alt="Add watermark to PDF" onerror="this.src='images/thumb_howto.png'"></div>
                <div class="card-body">
                    <span class="tag tag-howto">How-To</span>
                    <p class="date">March 29, 2026</p>
                    <h2>How to Add a Watermark to a PDF for Free</h2>
                    <p>Add "CONFIDENTIAL", "DRAFT" or your logo as a watermark to any PDF. Custom text, opacity, and position. No sign-up.</p>
                    <span class="read-more">Read Article &rarr;</span>
                </div>
            </a>
            <a href="how-to-do-pdf-ocr-free.html" class="blog-card" data-category="howto">
                <div class="card-img-wrap"><img src="images/thumb_pdf_ocr.png" class="card-img" alt="PDF OCR free" onerror="this.src='images/thumb_howto.png'"></div>
                <div class="card-body">
                    <span class="tag tag-howto">How-To</span>
                    <p class="date">March 29, 2026</p>
                    <h2>PDF OCR: Convert Scanned PDF to Searchable Text Free</h2>
                    <p>Make scanned PDFs searchable and selectable using free online OCR. Supports English, Hindi, and 30+ languages.</p>
                    <span class="read-more">Read Article &rarr;</span>
                </div>
            </a>
            <a href="how-to-delete-pages-from-pdf-free.html" class="blog-card" data-category="howto">
                <div class="card-img-wrap"><img src="images/thumb_delete_pages.png" class="card-img" alt="Delete PDF pages" onerror="this.src='images/thumb_howto.png'"></div>
                <div class="card-body">
                    <span class="tag tag-howto">How-To</span>
                    <p class="date">March 29, 2026</p>
                    <h2>How to Delete Pages from a PDF for Free</h2>
                    <p>Remove blank pages, confidential sections, or unwanted covers from any PDF instantly. No quality loss, no sign-up.</p>
                    <span class="read-more">Read Article &rarr;</span>
                </div>
            </a>
            <a href="how-to-rotate-pages-in-pdf-free.html" class="blog-card" data-category="howto">
                <div class="card-img-wrap"><img src="images/thumb_howto.png" class="card-img" alt="Rotate PDF pages"></div>
                <div class="card-body">
                    <span class="tag tag-howto">How-To</span>
                    <p class="date">March 29, 2026</p>
                    <h2>How to Rotate Pages in a PDF for Free</h2>
                    <p>Fix upside-down or sideways scanned pages in seconds. Rotate individual pages or the whole document &mdash; no software needed.</p>
                    <span class="read-more">Read Article &rarr;</span>
                </div>
            </a>
"""

idx = os.path.join(BLOG, 'index.html')
with open(idx, 'r', encoding='utf-8') as f:
    content = f.read()

MARKER = '<div class="blog-grid" id="blogGrid">'
content = content.replace(MARKER, MARKER + new_cards, 1)
with open(idx, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated blog/index.html')

new_entries = """  <url><loc>https://quickdopdf.com/blog/how-to-extract-images-from-pdf.html</loc><priority>0.8</priority><changefreq>monthly</changefreq><lastmod>2026-03-29</lastmod></url>
  <url><loc>https://quickdopdf.com/blog/how-to-add-watermark-to-pdf-free.html</loc><priority>0.8</priority><changefreq>monthly</changefreq><lastmod>2026-03-29</lastmod></url>
  <url><loc>https://quickdopdf.com/blog/how-to-do-pdf-ocr-free.html</loc><priority>0.8</priority><changefreq>monthly</changefreq><lastmod>2026-03-29</lastmod></url>
  <url><loc>https://quickdopdf.com/blog/how-to-delete-pages-from-pdf-free.html</loc><priority>0.8</priority><changefreq>monthly</changefreq><lastmod>2026-03-29</lastmod></url>
  <url><loc>https://quickdopdf.com/blog/how-to-rotate-pages-in-pdf-free.html</loc><priority>0.8</priority><changefreq>monthly</changefreq><lastmod>2026-03-29</lastmod></url>
</urlset>"""

sitemap = os.path.join(ROOT, 'sitemap.xml')
with open(sitemap, 'r', encoding='utf-8') as f:
    sm = f.read()
sm = sm.replace('</urlset>', new_entries)
with open(sitemap, 'w', encoding='utf-8') as f:
    f.write(sm)
print('Updated sitemap.xml')
print('Done!')
