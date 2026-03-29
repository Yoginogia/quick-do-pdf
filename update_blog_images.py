import os, re

BLOG = r'd:\Yogi\Yogesh\quick-do-pdf\blog'

# Map: article href → new thumbnail filename
IMAGE_MAP = {
    'adobe-acrobat-vs-quickdopdf.html':           'thumb_adobe_vs_quickdo.png',
    'best-free-pdf-tools-2026.html':              'thumb_best_free_pdf_tools.png',
    'best-pdf-tools-for-students-2025.html':      'thumb_students_pdf.png',  # to be generated
    'best-ways-to-compress-pdf.html':             'thumb_compress_pdf.png',
    'compress-pdf-on-mobile.html':                'thumb_compress_mobile.png',
    'convert-pdf-without-losing-formatting.html': 'thumb_convert_formatting.png',
    'free-pdf-tools-without-signup.html':         'thumb_best_free_pdf_tools.png',
    'how-to-add-header-footer-page-numbers-pdf.html': 'thumb_howto.png',
    'how-to-add-signature-to-pdf-on-iphone.html':'thumb_sign_iphone.png',
    'how-to-compress-pdf-exactly-100kb.html':     'thumb_compress_pdf.png',
    'how-to-compress-pdf-mac-preview.html':       'thumb_compress_mobile.png',
    'how-to-compress-pdf.html':                   'thumb_compress_pdf.png',
    'how-to-convert-images-to-pdf.html':          'thumb_howto.png',
    'how-to-convert-pdf-to-excel-free.html':      'thumb_pdf_excel.png',
    'how-to-edit-pdf-without-software.html':      'thumb_best_free_pdf_tools.png',
    'how-to-extract-photos-from-pdf.html':        'thumb_howto.png',
    'how-to-extract-text-from-pdf-to-txt-html.html': 'thumb_howto.png',
    'how-to-fill-pdf-forms-online.html':          'thumb_howto.png',
    'how-to-fix-detached-arraybuffer-error-pdf.html': 'thumb_howto.png',
    'how-to-fix-pdf-text-mojibake-garbled.html':  'thumb_howto.png',
    'how-to-merge-multiple-jpg-to-one-pdf.html':  'thumb_merge_pdf.png',
    'how-to-merge-pdf-files-free.html':           'thumb_merge_pdf.png',
    'how-to-merge-pdf-files-on-android.html':     'thumb_merge_android.png',
    'how-to-merge-pdf-files.html':                'thumb_merge_pdf.png',
    'how-to-print-protected-pdf.html':            'thumb_protect_pdf.png',
    'how-to-protect-a-pdf-with-password.html':    'thumb_protect_pdf.png',
    'how-to-reduce-pdf-file-size-free.html':      'thumb_compress_pdf.png',
    'how-to-reduce-pdf-size-for-gmail.html':      'thumb_compress_mobile.png',
    'how-to-repair-corrupted-pdf-files.html':     'thumb_howto.png',
    'how-to-replace-text-in-pdf-free.html':       'thumb_howto.png',
    'how-to-sign-a-pdf-document-free.html':       'thumb_sign_pdf.png',
    'how-to-sign-pdf-document-online.html':       'thumb_sign_pdf.png',
    'how-to-translate-a-pdf-document-free.html':  'thumb_translate_pdf.png',
    'how-to-unlock-pdf-bank-statements.html':     'thumb_unlock_pdf.png',
    'how-to-unlock-secured-pdf.html':             'thumb_unlock_pdf.png',
    'ilovepdf-vs-smallpdf-comparison.html':       'thumb_adobe_vs_quickdo.png',
    'is-it-safe-to-unlock-pdf-online.html':       'thumb_unlock_pdf.png',
    'is-pdf-software-dying.html':                 'thumb_adobe_vs_quickdo.png',
    'pdf-to-word-conversion-guide.html':          'thumb_pdf_to_word.png',
    'pdf-tools-for-small-business-owners.html':   'thumb_business_pdf.png',
    'pdf-vs-docx-which-format-to-use.html':       'thumb_pdf_vs_docx.png',
    'pdf-vs-word-which-is-better.html':           'thumb_pdf_vs_docx.png',
    'top-5-offline-pdf-editors.html':             'thumb_adobe_vs_quickdo.png',
    'what-is-a-pdf-and-how-does-it-work.html':    'thumb_what_is_pdf.png',
    'what-is-pdf-a-compliance.html':              'thumb_what_is_pdf.png',
    'why-is-my-pdf-so-large.html':                'thumb_compress_pdf.png',
}

idx = os.path.join(BLOG, 'index.html')
with open(idx, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
for article, thumb in IMAGE_MAP.items():
    # Find card blocks that reference this article and update their img src
    # Pattern: href="ARTICLE" ... img src="images/OLD_THUMB"
    old_pattern = re.compile(
        r'(href="' + re.escape(article) + r'"[^>]*>.*?<img src="images/)([^"]+)(")',
        re.DOTALL
    )
    new_content = old_pattern.sub(r'\g<1>' + thumb + r'\3', content)
    if new_content != content:
        content = new_content
        count += 1

with open(idx, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Updated {count} image references in blog/index.html')
print('Done!')
