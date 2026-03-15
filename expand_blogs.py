import os
import glob
import re

# Dictionary mapping file names to custom appended content
# We will inject 400-500 words of targeted "FAQs" and "Pro Tips" for AdSense

expansion_data = {
    "best-free-pdf-tools-2026.html": """
        <h2>Frequently Asked Questions About Free PDF Tools</h2>
        <h3>Are online PDF tools safe to use?</h3>
        <p>Security is the number one concern when using online software. Traditional PDF platforms mandate uploading your sensitive documents (like bank statements or medical records) to their remote servers for processing. This presents a massive privacy vulnerability. However, modern offline-first browser tools like QuickDoPDF solve this completely. By leveraging HTML5 Canvas and WebAssembly, QuickDoPDF processes your files locally on your own device's RAM. Your documents never leave your computer, ensuring 100% data safety and compliance with privacy standards.</p>
        
        <h3>Do I need to download software to compress a PDF?</h3>
        <p>In the past, users had to install heavy, expensive desktop software like Adobe Acrobat just to perform simple tasks like reducing file size. Today, you do not need to download any software. Browser-based tools operate directly within Google Chrome, Safari, or Microsoft Edge. QuickDoPDF specifically utilizes your browser's native engine to execute complex algorithms like DPI reduction and image resampling without requiring any external plugins or executables. This is faster, safer, and completely device-agnostic.</p>

        <h3>Why do some PDF tools add watermarks?</h3>
        <p>Many freemium platforms add intrusive watermarks to your documents to force you into buying their premium subscription plans. It is a common aggressive marketing tactic. At QuickDoPDF, we believe core utility should be accessible. Our entire suite of tools—from PDF merging to splitting and password unlocking—is proudly 100% watermark-free. You retain full ownership and a clean aesthetic on all your processed files.</p>

        <div class="pro-tip-box" style="background: rgba(var(--primary-rgb), 0.05); border-left: 4px solid var(--primary); padding: 20px; border-radius: 8px; margin-top: 30px;">
            <h3>💡 Pro Tip for 2026 Document Workflows</h3>
            <p>Always keep a local backup of your original, uncompressed PDF files. When applying heavy compression (like dropping a 20MB file to 100KB), raster images within the document will inevitably lose resolution. If you ever need to print the document in high quality later, you will want access to the original, uncompressed source file.</p>
        </div>
    """,
    "best-ways-to-compress-pdf.html": """
        <h2>Common Questions About PDF Compression</h2>
        <h3>How does PDF compression actually work?</h3>
        <p>PDF compression is a complex technical process that primarily targets the embedded multimedia elements within a document. Text and vector graphics take up very little space. The massive file sizes are almost always caused by high-resolution raster images (like scanned JPEGs) embedded inside the PDF. Compression algorithms work by strategically reducing the DPI (Dots Per Inch) of these images and stripping out unnecessary metadata, hidden font subsets, and invisible color profiles. QuickDoPDF uses an advanced client-side algorithm to achieve this intelligently, maintaining readability while aggressively shrinking the byte count.</p>
        
        <h3>Will compressing my PDF ruin the quality?</h3>
        <p>The short answer is: it depends on your goal. If you are uploading a document to a government portal or sending it via email, standard compression will likely be completely unnoticeable on a computer screen. Modern algorithms prioritize text clarity while slightly softening image details. QuickDoPDF allows you to control this balance. However, if your PDF is a high-end photography portfolio designed for physical billboard printing, you should avoid heavy compression, as the DPI reduction will cause visible pixelation in print.</p>

        <h3>Can I compress a PDF to an exact size, like 100KB?</h3>
        <p>Hitting an exact file size is mathematically challenging because every document has incredibly different internal architecture. A 10-page text document compresses differently than a 1-page high-resolution photograph. However, advanced tools like QuickDoPDF offer targeted compression presets (e.g., "Under 100KB", "Under 200KB"). These modes use aggressive heuristic loops to iteratively degrade the image quality until the total file payload falls beneath the strict megabyte or kilobyte threshold you requested.</p>

        <div class="pro-tip-box" style="background: rgba(var(--primary-rgb), 0.05); border-left: 4px solid var(--primary); padding: 20px; border-radius: 8px; margin-top: 30px;">
            <h3>💡 Pro Tip: The "Print to PDF" Hack</h3>
            <p>If automated algorithms are struggling to shrink a particularly stubborn, corrupted PDF file, try this archaic but effective operating system trick: Open the PDF in your Google Chrome browser, press Ctrl+P (or Cmd+P) to open the Print dialog, and select "Save as PDF" as your destination printer. This process essentially "flattens" the entire document, stripping away complex hidden layers and often resulting in a massively reduced file size without requiring third-party tools.</p>
        </div>
    """,
    # Fallback content for all other articles to ensure they hit the ~800 word mark for AdSense
    "generic": """
        <h2>Frequently Asked Questions</h2>
        <h3>Why is QuickDoPDF completely free and offline?</h3>
        <p>The PDF utility market is currently dominated by massive corporations that charge exorbitant monthly subscription fees for basic functionalities like merging, splitting, or compressing files. Furthermore, these traditional cloud-based platforms pose a significant privacy risk by requiring you to upload your sensitive personal data—such as tax returns, medical records, and legal contracts—to their remote servers. We built QuickDoPDF to disrupt this industry. By leveraging cutting-edge HTML5 Canvas, WebAssembly, and modern JavaScript APIs, we process every single document natively inside your device's RAM. This means zero server uploads, absolute privacy, and the ability to offer the service entirely for free since we have no heavy backend server costs.</p>
        
        <h3>How do I manage large PDF files effectively?</h3>
        <p>Managing large PDF files effectively requires a combination of smart compression and targeted splitting. When you encounter a 50MB PDF that refuses to attach to an email due to server limits, your first step should be our "Compress PDF" tool, which can often reduce file size by up to 90% without losing legible text quality. If the file is still too large, it is highly likely that only a few specific pages are actually relevant. Use the "Split PDF" tool to extract only the exact page ranges you need to share, discarding the redundant bulk. This dual approach guarantees you can bypass any institutional file-size restrictions.</p>

        <h3>Is it legal to unlock a password-protected PDF?</h3>
        <p>The legality of unlocking a protected PDF depends entirely on your intent and your ownership of the document. The "Unlock PDF" feature is designed explicitly for personal recovery. For example, banks frequently lock monthly e-statements with complex passwords (usually a combination of your name and date of birth). While secure, entering this password every single time you need to view your own financial record is incredibly tedious. Using our tool to strip the password from your own legally obtained documents is perfectly acceptable and legal. However, bypassing encryption on copyrighted intellectual property or confidential documents that you do not have authorized permission to view is strictly unethical and illegal.</p>

        <div class="pro-tip-box" style="background: rgba(var(--primary-rgb), 0.05); border-left: 4px solid var(--primary); padding: 20px; border-radius: 8px; margin-top: 30px;">
            <h3>💡 Workflow Pro Tip</h3>
            <p>Did you know you can chain our tools together for maximum efficiency? For instance, if you have three separate, heavily encrypted PDFs: First, run them all through the "Unlock PDF" tool to strip the passwords. Second, take the three unlocked files and combine them using "Merge PDF". Finally, take the massive merged output file and run it through "Compress PDF" to create a single, easy-to-share, lightweight document. By keeping the QuickDoPDF tab open, you can transform a messy digital filing cabinet into a streamlined, professional workflow in under 60 seconds.</p>
        </div>
    """
}

def inject_content(filepath):
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid double injection
    if "Frequently Asked Questions" in content or "FAQ" in content or "pro-tip-box" in content:
        print(f"Skipping {filename} (Already expanded)")
        return

    # Select the precise content string
    injection_text = expansion_data.get(filename, expansion_data["generic"])

    # Find the closing </article> tag and inject right before it
    if "</article>" in content:
        new_content = content.replace("</article>", f"\n\n        <!-- SEO Deepening Expansion -->\n        <div class='seo-content-expansion' style='margin-top: 50px; padding-top: 30px; border-top: 1px solid var(--border);'>\n            {injection_text}\n        </div>\n    </article>")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Expanded content in {filename}")
    else:
        print(f"Warning: No </article> tag found in {filename}")

if __name__ == "__main__":
    blog_htmls = glob.glob(os.path.join("d:\\Yogi\\Yogesh\\quick-do-pdf\\blog", "*.html"))
    for file in blog_htmls:
        if "blog-layout.css" in file or "index.html" in file:
            continue
        inject_content(file)
        
    print("SEO Blog Thin Content Expansion Complete.")
