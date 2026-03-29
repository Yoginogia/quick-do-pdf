import os

BLOG = r'd:\Yogi\Yogesh\quick-do-pdf\blog'
ROOT = r'd:\Yogi\Yogesh\quick-do-pdf'

new_cards = """
            <!-- NEW ARTICLES March 2026 (batch 2) -->
            <a href="how-to-convert-pdf-to-excel-free.html" class="blog-card" data-category="howto">
                <div class="card-img-wrap"><img src="images/thumb_howto.png" class="card-img" alt="PDF to Excel"></div>
                <div class="card-body">
                    <span class="tag tag-howto">How-To</span>
                    <p class="date">March 29, 2026</p>
                    <h2>How to Convert PDF to Excel for Free</h2>
                    <p>Extract tables and data from any PDF into an Excel spreadsheet instantly &mdash; no software, no sign-up, works on any device.</p>
                    <span class="read-more">Read Article &rarr;</span>
                </div>
            </a>
            <a href="how-to-add-signature-to-pdf-on-iphone.html" class="blog-card" data-category="howto">
                <div class="card-img-wrap"><img src="images/thumb_howto.png" class="card-img" alt="Sign PDF iPhone"></div>
                <div class="card-body">
                    <span class="tag tag-howto">How-To</span>
                    <p class="date">March 28, 2026</p>
                    <h2>How to Add a Signature to a PDF on iPhone (Free)</h2>
                    <p>Sign any PDF on iPhone without an app &mdash; use the built-in Files app or open in Safari. Step-by-step guide for iOS users.</p>
                    <span class="read-more">Read Article &rarr;</span>
                </div>
            </a>
            <a href="how-to-merge-pdf-files-on-android.html" class="blog-card" data-category="howto">
                <div class="card-img-wrap"><img src="images/thumb_howto.png" class="card-img" alt="Merge PDF Android"></div>
                <div class="card-body">
                    <span class="tag tag-howto">How-To</span>
                    <p class="date">March 27, 2026</p>
                    <h2>How to Merge PDF Files on Android for Free</h2>
                    <p>Combine multiple PDFs on any Android phone without downloading an app. Works directly in Chrome in under 30 seconds.</p>
                    <span class="read-more">Read Article &rarr;</span>
                </div>
            </a>
            <a href="how-to-translate-a-pdf-document-free.html" class="blog-card" data-category="guide">
                <div class="card-img-wrap"><img src="images/thumb_guide.png" class="card-img" alt="Translate PDF"></div>
                <div class="card-body">
                    <span class="tag tag-guide">Guide</span>
                    <p class="date">March 26, 2026</p>
                    <h2>How to Translate a PDF Document for Free</h2>
                    <p>Translate any PDF to English, Hindi, Spanish or 100+ languages free. No software needed &mdash; works directly in your browser.</p>
                    <span class="read-more">Read Article &rarr;</span>
                </div>
            </a>
            <a href="pdf-tools-for-small-business-owners.html" class="blog-card" data-category="tips">
                <div class="card-img-wrap"><img src="images/thumb_tips.png" class="card-img" alt="PDF tools for business"></div>
                <div class="card-body">
                    <span class="tag tag-tips">Tips</span>
                    <p class="date">March 25, 2026</p>
                    <h2>7 PDF Tools Every Small Business Owner Needs</h2>
                    <p>Free PDF tools for invoices, contracts, tax documents &mdash; save thousands on Adobe Acrobat subscriptions every year.</p>
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

new_entries = """  <url><loc>https://quickdopdf.com/blog/how-to-convert-pdf-to-excel-free.html</loc><priority>0.8</priority><changefreq>monthly</changefreq><lastmod>2026-03-29</lastmod></url>
  <url><loc>https://quickdopdf.com/blog/how-to-add-signature-to-pdf-on-iphone.html</loc><priority>0.8</priority><changefreq>monthly</changefreq><lastmod>2026-03-28</lastmod></url>
  <url><loc>https://quickdopdf.com/blog/how-to-merge-pdf-files-on-android.html</loc><priority>0.8</priority><changefreq>monthly</changefreq><lastmod>2026-03-27</lastmod></url>
  <url><loc>https://quickdopdf.com/blog/how-to-translate-a-pdf-document-free.html</loc><priority>0.8</priority><changefreq>monthly</changefreq><lastmod>2026-03-26</lastmod></url>
  <url><loc>https://quickdopdf.com/blog/pdf-tools-for-small-business-owners.html</loc><priority>0.8</priority><changefreq>monthly</changefreq><lastmod>2026-03-25</lastmod></url>
</urlset>"""

sitemap = os.path.join(ROOT, 'sitemap.xml')
with open(sitemap, 'r', encoding='utf-8') as f:
    sm = f.read()
sm = sm.replace('</urlset>', new_entries)
with open(sitemap, 'w', encoding='utf-8') as f:
    f.write(sm)
print('Updated sitemap.xml')
print('All done!')
