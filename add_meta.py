import os, re

# Meta descriptions for each tool page
META = {
    'merge.html': ('Merge PDF Online Free | Quick Do PDF', 'Combine multiple PDF files into one document instantly. Free, no watermark, no signup. Runs entirely in your browser.'),
    'split.html': ('Split PDF Online Free | Quick Do PDF', 'Split PDF into individual pages or extract specific page ranges. Free, fast, and works in your browser.'),
    'compress.html': ('Compress PDF Online Free | Quick Do PDF', 'Reduce PDF file size while keeping text readable and images clear. Free online compression, no upload needed.'),
    'pdf-to-word.html': ('PDF to Word Converter Free | Quick Do PDF', 'Convert PDF to editable Word (.docx) files online for free. Best-effort text and layout extraction, no signup required.'),
    'pdf-to-excel.html': ('PDF to Excel Converter Free | Quick Do PDF', 'Convert PDF tables to Excel (.xlsx) spreadsheets online for free. Extract data from invoices and reports instantly.'),
    'jpg-to-pdf.html': ('JPG to PDF Converter Free | Quick Do PDF', 'Convert JPG images to PDF documents online for free. Combine multiple images into one PDF, no signup needed.'),
    'pdf-to-jpg.html': ('PDF to JPG Converter Free | Quick Do PDF', 'Convert each PDF page to high-quality JPG images online for free. Download as ZIP, no signup required.'),
    'sign.html': ('Sign PDF Online Free | Quick Do PDF', 'Add your signature to PDF documents online for free. Draw, type, or upload your signature. No signup, works in browser.'),
    'protect.html': ('Password Protect PDF Free | Quick Do PDF', 'Add password protection to your PDF files online for free. Encrypt PDFs with AES encryption, no upload needed.'),
    'unlock.html': ('Unlock PDF Online Free | Quick Do PDF', 'Remove password protection from PDF files online for free. Unlock PDFs instantly in your browser.'),
    'rotate.html': ('Rotate PDF Pages Free | Quick Do PDF', 'Rotate PDF pages 90, 180, or 270 degrees online for free. Fix upside-down or sideways pages instantly.'),
    'crop.html': ('Crop PDF Pages Free | Quick Do PDF', 'Crop PDF pages to remove unwanted margins or white space online for free. Works in your browser.'),
    'watermark.html': ('Add Watermark to PDF Free | Quick Do PDF', 'Add text or image watermarks to PDF documents online for free. Protect your documents with custom watermarks.'),
    'word-to-pdf.html': ('Word to PDF Converter Free | Quick Do PDF', 'Convert Word (.docx) documents to PDF format online for free. Maintain formatting, no signup required.'),
    'page-numbers.html': ('Add Page Numbers to PDF Free | Quick Do PDF', 'Add page numbers to your PDF documents online for free. Customize position, font, and format.'),
    'delete-pages.html': ('Delete Pages from PDF Free | Quick Do PDF', 'Remove specific pages from PDF documents online for free. Select and delete unwanted pages instantly.'),
    'reorder.html': ('Reorder PDF Pages Free | Quick Do PDF', 'Drag and drop to rearrange PDF pages in any order. Free, visual page reordering in your browser.'),
    'flatten.html': ('Flatten PDF Free | Quick Do PDF', 'Flatten PDF form fields and annotations into static content. Prevent editing of filled forms, free online.'),
    'sanitize.html': ('Sanitize PDF Free | Quick Do PDF', 'Remove hidden metadata, scripts, and embedded objects from PDF files. Clean PDFs for safe sharing, free online.'),
    'grayscale.html': ('Convert PDF to Grayscale Free | Quick Do PDF', 'Convert color PDF to black and white (grayscale) online for free. Reduce file size and save on printing costs.'),
    'extract-text.html': ('Extract Text from PDF Free | Quick Do PDF', 'Extract all text content from PDF documents online for free. Copy text from scanned or digital PDFs.'),
    'extract-images.html': ('Extract Images from PDF Free | Quick Do PDF', 'Extract all images from PDF files online for free. Download images as JPG or PNG format.'),
    'pdf-ocr.html': ('PDF OCR - Text Recognition Free | Quick Do PDF', 'Convert scanned PDFs to searchable text using OCR technology online for free. Extract text from images.'),
    'compare-pdfs.html': ('Compare PDF Files Free | Quick Do PDF', 'Compare two PDF documents side by side online for free. Find differences between document versions.'),
    'add-background.html': ('Add Background to PDF Free | Quick Do PDF', 'Add color or image backgrounds to PDF pages online for free. Customize your documents with branded backgrounds.'),
    'invoice-generator.html': ('Free Invoice Generator PDF | Quick Do PDF', 'Create professional PDF invoices with itemized billing, tax calculations, and company branding. Free, no signup.'),
    'scan-to-pdf.html': ('Scan to PDF Free | Quick Do PDF', 'Scan documents using your phone camera and convert to PDF. Free mobile-friendly scanner, works in browser.'),
    'compress-pdf-100kb.html': ('Compress PDF to 100KB Free | Quick Do PDF', 'Reduce PDF file size to under 100KB for government forms, SSC, UPSC applications. Free online compression.'),
    'compress-pdf-200kb.html': ('Compress PDF to 200KB Free | Quick Do PDF', 'Reduce PDF file size to under 200KB for email attachments and online submissions. Free compression tool.'),
    'compress-pdf-for-email.html': ('Compress PDF for Email Free | Quick Do PDF', 'Reduce PDF size to fit email attachment limits (25MB Gmail, 20MB Outlook). Free online compression.'),
    'compress-pdf-under-1mb.html': ('Compress PDF Under 1MB Free | Quick Do PDF', 'Reduce PDF file size to under 1MB for online uploads and submissions. Free compression, no quality loss.'),
    'compress-pdf-without-losing-quality.html': ('Compress PDF Without Losing Quality | Quick Do PDF', 'Smart PDF compression that reduces file size while preserving text clarity and image quality. Free online.'),
    'merge-multiple-pdf-into-one.html': ('Merge Multiple PDFs Into One Free | Quick Do PDF', 'Combine 2 or more PDF files into a single document. Free, fast, no watermark. Works in your browser.'),
    'merge-pdf-without-watermark.html': ('Merge PDF Without Watermark Free | Quick Do PDF', 'Combine PDF files into one document without any watermarks. 100% free, no signup, no hidden fees.'),
    'pdf-to-word-editable.html': ('PDF to Editable Word Free | Quick Do PDF', 'Convert PDF to editable Word document. Extract text and formatting for easy editing. Free online tool.'),
    'split-pdf-by-page-number.html': ('Split PDF by Page Number Free | Quick Do PDF', 'Split PDF at specific page numbers or extract page ranges. Free, precise PDF splitting in your browser.'),
    'unlock-pdf-without-password.html': ('Unlock PDF Without Password Free | Quick Do PDF', 'Remove PDF restrictions like printing and copying without needing the password. Free online tool.'),
}

count = 0
for fname, (title, desc) in META.items():
    fpath = os.path.join('.', fname)
    if not os.path.exists(fpath):
        print(f'SKIP (not found): {fname}')
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'name="description"' in content:
        print(f'SKIP (already has meta): {fname}')
        continue
    
    # Insert meta description + title after <meta charset> or <meta name="viewport">
    # Find the <head> section and add after charset
    meta_tag = f'  <meta name="description" content="{desc}">\n  <meta name="author" content="Quick Do PDF">\n'
    
    # Try to insert after viewport meta
    if '<meta name="viewport"' in content:
        content = content.replace(
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' + meta_tag,
            1
        )
    elif '<meta charset="UTF-8">' in content:
        content = content.replace(
            '<meta charset="UTF-8">',
            '<meta charset="UTF-8">\n' + meta_tag,
            1
        )
    else:
        content = content.replace('<head>', '<head>\n' + meta_tag, 1)
    
    # Update title if generic
    title_match = re.search(r'<title>(.*?)</title>', content)
    if title_match:
        old_title = title_match.group(1)
        if 'Quick Do PDF' not in old_title or len(old_title) < 20:
            content = content.replace(f'<title>{old_title}</title>', f'<title>{title}</title>', 1)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    count += 1
    print(f'ADDED: {fname}')

print(f'\nDone! Added meta descriptions to {count} files.')
