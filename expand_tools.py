import os
import glob
import re

# Specific SEO content mapped by tool filename
tool_seo_content = {
    "compress.html": """
    <section class="tool-seo-content">
        <h2>How to Compress PDF Files Online</h2>
        <p>Large PDF documents can be difficult to share via email or upload to government and corporate portals due to strict file size limitations (often 1MB or 2MB). Our free <strong>Compress PDF</strong> tool uses advanced heuristic algorithms to intelligently reduce your file's footprint without compromising visual quality.</p>
        
        <h3>Why Choose Client-Side Compression?</h3>
        <p>Unlike traditional online PDF compressors that require you to upload your sensitive financial or legal documents to a remote server, Quick Do PDF operates entirely within your web browser. This means your data never leaves your device, guaranteeing 100% privacy and security against server-side data breaches.</p>

        <h3>Features of Our Compressor:</h3>
        <ul>
            <li><strong>Multiple Compression Levels:</strong> Choose between Extreme (100KB target), Heavy (200KB target), Standard (Under 1MB), or High Quality.</li>
            <li><strong>Intelligent Downsampling:</strong> Automatically optimizes internal image DPIs while keeping text vectors sharp and legible.</li>
            <li><strong>Metadata Stripping:</strong> Removes hidden blobs of unnecessary document history that bloat file size.</li>
        </ul>
    </section>
    """,
    
    "merge.html": """
    <section class="tool-seo-content">
        <h2>Merge Multiple PDF Files Instantly</h2>
        <p>Managing dozens of separate PDF invoices, reports, or scanned receipts can be a nightmare. Our <strong>Merge PDF</strong> tool allows you to seamlessly combine multiple documents into a single, continuous, and organized file in a matter of seconds.</p>
        
        <h3>Offline Privacy Guaranteed</h3>
        <p>Because merging documents often involves highly confidential business or personal information, uploading them to a third-party website is a massive security risk. Quick Do PDF utilizes HTML5 capabilities to parse and merge your documents directly inside your computer's RAM. No strings attached, no files uploaded.</p>

        <h3>How to Combine PDFs:</h3>
        <ul>
            <li><strong>Drag and Drop:</strong> Simply drag the files you want to merge into the upload zone above.</li>
            <li><strong>Reorder Visually:</strong> (Coming soon) Our system automatically aligns the documents in the order they were selected.</li>
            <li><strong>No Watermarks:</strong> The merged output is completely clean and identical to the original pages, with no intrusive branding applied.</li>
        </ul>
    </section>
    """,

    "split.html": """
    <section class="tool-seo-content">
        <h2>Split PDF Documents with Precision</h2>
        <p>Sometimes you only need a specific chapter from a massive digital textbook, or a single page from a 50-page corporate report. Instead of sending the entire bulky document, use our <strong>Split PDF</strong> tool to extract exactly what you need.</p>
        
        <h3>Secure Document Slicing</h3>
        <p>Our browser-based slicing engine reads the PDF structure locally. Whether you need to split a document into individual single-page files, or extract a specific range (like pages 5 through 12), the process runs instantly on your own CPU.</p>

        <h3>Common Uses for PDF Splitting:</h3>
        <ul>
            <li>Removing blank or unnecessary pages from scanned documents to save space.</li>
            <li>Dividing large team reports into individual PDFs to send to respective department heads.</li>
            <li>Extracting standalone invoices from a massive monthly ledger file.</li>
        </ul>
    </section>
    """,

    "protect.html": """
    <section class="tool-seo-content">
        <h2>Protect PDF with Military-Grade Encryption</h2>
        <p>When sharing sensitive documents like tax returns, legal contracts, or confidential banking information over the internet, standard PDFs are inherently vulnerable. Our <strong>Protect PDF</strong> tool allows you to wrap your documents in robust cryptography before you email them.</p>
        
        <h3>How Our Encryption Works</h3>
        <p>We utilize industry-standard AES (Advanced Encryption Standard) 256-bit cryptography to lock your document locally. Because the password encryption is applied inside your browser, the unencrypted version of your document is never exposed to external servers or network sniffers.</p>

        <h3>Best Practices for Passwords:</h3>
        <ul>
            <li>Always use a strong combination of uppercase letters, numbers, and symbols.</li>
            <li>Do not send the password in the same email or messaging thread as the protected document. Use a secondary channel (like an SMS text) to communicate the password to the recipient.</li>
        </ul>
    </section>
    """,
    
    "unlock.html": """
    <section class="tool-seo-content">
        <h2>Unlock PDF Files Securely</h2>
        <p>There are few things more frustrating than being unable to print or edit an old document because it's locked, or having to type a complex password every time you open your own bank statements. Our <strong>Unlock PDF</strong> tool strips away these artificial restrictions instantly.</p>
        
        <h3>Removing Owner vs User Passwords</h3>
        <p>If a PDF is restricted from printing or copying (an Owner Password), our engine can often strip these arbitrary limits automatically without needing the password at all. If the document is fully encrypted (a User Password), you must enter the password once to prove ownership, after which our tool will generate a permanently unlocked version for your convenience.</p>

        <h3>100% Offline Unlocking</h3>
        <p>Unlocking highly sensitive financial records on cloud servers exposes you to massive privacy risks. Quick Do PDF decrypts the file entirely within your browser's memory, ensuring your private data and your passwords remain strictly confidential on your own device.</p>
    </section>
    """
}

generic_seo_content = """
    <section class="tool-seo-content">
        <h2>100% Offline, Secure PDF Processing</h2>
        <p>Welcome to Quick Do PDF's comprehensive document management suite. Most online utilities process your files by uploading them to remote servers, exposing your confidential data to potential breaches and privacy violations. We engineered our platform differently.</p>
        
        <h3>Why Browser-Based Tools are Better</h3>
        <p>Using advanced WebAssembly and HTML5 technology, this tool executes complex file manipulations entirely within your own web browser's local memory (RAM). This architectural breakthrough provides three distinct advantages:</p>
        <ul>
            <li><strong>Absolute Privacy:</strong> Your documents never leave your computer. We do not store, scan, or log any of your file contents.</li>
            <li><strong>Blazing Fast Speed:</strong> You do not have to wait for heavy files to upload or download from distant cloud servers. Processing is virtually instantaneous.</li>
            <li><strong>Completely Free:</strong> Because we don't have to pay massive cloud computing bills to process your files, we can offer premium-grade functionality without subscription paywalls, watermarks, or sign-up requirements.</li>
        </ul>
    </section>
"""

def process_tools():
    target_dir = "d:\\Yogi\\Yogesh\\quick-do-pdf"
    html_files = glob.glob(os.path.join(target_dir, "*.html"))
    
    # Exclude non-tool pages
    excludes = ["index.html", "404.html", "about.html", "contact.html", "privacy-policy.html", "terms.html", "disclaimer.html"]
    
    updated_count = 0
    
    for filepath in html_files:
        filename = os.path.basename(filepath)
        if filename in excludes:
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Check if already injected
        if 'class="tool-seo-content"' in html:
            continue
            
        # Select appropriate content
        content_to_inject = tool_seo_content.get(filename, generic_seo_content)
        
        # Determine injection point: right before </main> or right before <script> 
        if '</main>' in html:
            new_html = html.replace('</main>', f'\n{content_to_inject}\n  </main>')
        elif '<script>' in html:
            # Inject before the very last script tag block
            last_script_idx = html.rfind('<script')
            if last_script_idx != -1:
                new_html = html[:last_script_idx] + f'\n{content_to_inject}\n  ' + html[last_script_idx:]
            else:
                new_html = html.replace('</body>', f'\n{content_to_inject}\n</body>')
        else:
            new_html = html.replace('</body>', f'\n{content_to_inject}\n</body>')
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        updated_count += 1
        print(f"Injected SEO content into: {filename}")
        
    print(f"Total tools expanded: {updated_count}")

if __name__ == "__main__":
    process_tools()
