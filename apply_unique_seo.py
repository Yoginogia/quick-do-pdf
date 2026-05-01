import os
import glob
import re

target_dir = r"d:\Yogi\Yogesh\quick-do-pdf"

tools_to_enhance = {
    "index.html": """
    <section class="tool-seo-content" style="max-width: 900px; margin: 40px auto; line-height: 1.8; color: var(--text);">
        <h2 style="font-size: 2.5rem; margin-bottom: 20px; text-align: center; color: var(--primary);">Welcome to Quick Do PDF: Your Ultimate Document Command Center</h2>
        <p style="font-size: 1.1rem; margin-bottom: 20px;">In an era where digital paperwork dictates our daily operations, managing PDF files shouldn't require expensive software subscriptions or compromise your data privacy. <strong>Quick Do PDF</strong> is designed as a powerful, 100% free, and completely secure suite of tools tailored for students, professionals, and small businesses alike.</p>
        
        <h3 style="font-size: 1.8rem; margin-top: 30px; margin-bottom: 15px;">Why Client-Side Processing is the Future</h3>
        <p style="font-size: 1.1rem; margin-bottom: 20px;">Most online PDF utilities operate on a cloud-based architecture. When you compress a file or merge an invoice, your sensitive data is uploaded to a remote server, processed, and then downloaded back to your device. This creates a massive vulnerability for data interception and unauthorized retention.</p>
        <p style="font-size: 1.1rem; margin-bottom: 20px;">At <strong>Quick Do PDF</strong>, we utilize advanced WebAssembly (Wasm) and HTML5 technologies to process your documents directly inside your browser's local memory (RAM). Your files never leave your computer. This means:
        <ul style="font-size: 1.1rem; margin-left: 20px; list-style-type: disc; margin-bottom: 20px;">
            <li>Zero upload times, drastically improving processing speed on large documents.</li>
            <li>Absolute privacy. Even if our servers were compromised, your data wouldn't be there.</li>
            <li>No artificial file size limits imposed by server bandwidth constraints.</li>
        </ul></p>

        <h3 style="font-size: 1.8rem; margin-top: 30px; margin-bottom: 15px;">A Comprehensive Suite for Every Need</h3>
        <p style="font-size: 1.1rem; margin-bottom: 20px;">Whether you need to quickly <strong>merge multiple PDF files</strong> into a single cohesive report, <strong>compress heavy documents</strong> to bypass strict email attachment limits, or <strong>convert PDFs to editable Word/Excel formats</strong>, our platform has a dedicated utility for it.</p>
        <p style="font-size: 1.1rem; margin-bottom: 20px;">We've also integrated AI-powered tools such as our revolutionary Resume Builder and AI PDF Summarizer to help you extract insights and build professional profiles in seconds.</p>

        <h3 style="font-size: 1.8rem; margin-top: 30px; margin-bottom: 15px;">Commitment to Quality</h3>
        <p style="font-size: 1.1rem; margin-bottom: 20px;">Our mission is to democratize document management. We continuously update our algorithms to ensure that compressing a PDF doesn't ruin image quality, and converting to Word retains the exact layout and formatting of the original document. Explore our tools above and experience the difference of local, frictionless processing.</p>
    </section>
    """,

    "merge.html": """
    <section class="tool-seo-content" style="max-width: 800px; margin: 40px auto; padding: 20px; background: var(--surface); border-radius: 12px; border: 1px solid var(--border);">
        <h2 style="font-size: 2rem; margin-bottom: 15px;">How to Merge Multiple PDF Files Securely</h2>
        <p style="margin-bottom: 15px;">Dealing with fragmented documents like monthly invoices, multi-part academic papers, or scattered receipt scans can severely hinder productivity. Our <strong>Merge PDF</strong> tool acts as a digital binder, allowing you to combine an unlimited number of PDF files into one clean, continuous document.</p>
        
        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">The Privacy Advantage</h3>
        <p style="margin-bottom: 15px;">Confidentiality is paramount when combining legal contracts or financial statements. Because our tool relies purely on client-side internal JavaScript processing, your sensitive PDFs are never uploaded to the cloud. The merging happens locally within your device's RAM, ensuring rapid execution and impenetrable privacy.</p>

        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">Step-by-Step Guide:</h3>
        <ol style="margin-left: 20px; margin-bottom: 15px;">
            <li><strong>Select Files:</strong> Click the upload area or simply drag and drop the PDFs you wish to combine.</li>
            <li><strong>Preview and Order:</strong> Ensure your files are loaded. (Visual reordering functionality is currently in development to allow drag-and-drop sequencing).</li>
            <li><strong>Merge and Download:</strong> Hit the "Merge" button. Our engine will stitch the pages seamlessly without applying any watermarks or degrading the original quality.</li>
        </ol>
        <p>This tool is ideal for administrative professionals, accountants, and students who need a fast, reliable, and offline-equivalent solution to document consolidation.</p>
    </section>
    """,

    "split.html": """
    <section class="tool-seo-content" style="max-width: 800px; margin: 40px auto; padding: 20px; background: var(--surface); border-radius: 12px; border: 1px solid var(--border);">
        <h2 style="font-size: 2rem; margin-bottom: 15px;">Split Large PDFs into Manageable Sections</h2>
        <p style="margin-bottom: 15px;">When dealing with a 500-page corporate manual or a bulky e-book, sending the entire file is often impractical and unprofessional. The <strong>Split PDF</strong> utility is engineered to dissect enormous documents effortlessly, allowing you to extract only the specific pages or chapters you actually need.</p>
        
        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">Precision Document Slicing</h3>
        <p style="margin-bottom: 15px;">Using advanced PDF-rendering parsing, our tool allows you to specify exact page ranges to keep or discard. Whether you need to pull page 15, or save pages 20 through 50 as an independent file, the system handles it with zero quality loss.</p>

        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">Local Processing Guarantees Security</h3>
        <p style="margin-bottom: 15px;">Just like our merging suite, splitting documents happens purely via client-side architecture. This is critical for HR professionals splitting employee records or legal clerks distributing distinct appendices. No data is stored, cached, or transmitted externally.</p>
    </section>
    """,

    "compress.html": """
    <section class="tool-seo-content" style="max-width: 800px; margin: 40px auto; padding: 20px; background: var(--surface); border-radius: 12px; border: 1px solid var(--border);">
        <h2 style="font-size: 2rem; margin-bottom: 15px;">Compress PDFs Without Losing Quality</h2>
        <p style="margin-bottom: 15px;">Email clients, government portals, and university assignment upload systems often enforce strict file size limits (e.g., 2MB or 5MB). Submitting a high-resolution, graphic-heavy PDF can quickly trigger an error. Our <strong>Compress PDF</strong> tool intelligently reduces your document's file size while maintaining crisp typography and clear imagery.</p>
        
        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">How the Optimization Algorithm Works</h3>
        <p style="margin-bottom: 15px;">The tool achieves significant size reduction through several background processes:</p>
        <ul style="margin-left: 20px; margin-bottom: 15px;">
            <li><strong>Image Downsampling:</strong> It heuristically scans embedded graphics and resizes them to optimal web-friendly DPIs, eliminating unnecessary pixel data.</li>
            <li><strong>Metadata Stripping:</strong> Removes hidden document trails, revisions, and bloated tags that software like embedded editors often leave behind.</li>
            <li><strong>Resource Deduplication:</strong> Identifies redundant font or icon resources and optimizes them.</li>
        </ul>

        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">100% Privacy by Default</h3>
        <p>Because compressing a file locally using Wasm is vastly superior to waiting for slow internet uploads, our tool isn't just more secure—it's incredibly fast. Protect your proprietary information by avoiding cloud-based compressors.</p>
    </section>
    """,

    "pdf-to-word.html": """
    <section class="tool-seo-content" style="max-width: 800px; margin: 40px auto; padding: 20px; background: var(--surface); border-radius: 12px; border: 1px solid var(--border);">
        <h2 style="font-size: 2rem; margin-bottom: 15px;">Convert PDF to Editable Microsoft Word (DOCX)</h2>
        <p style="margin-bottom: 15px;">PDFs are universally preferred for viewing and printing because they lock the formatting in place. However, when you receive a report that requires structural edits, rewriting it from scratch is a massive waste of time. Our <strong>PDF to Word</strong> converter bridges this gap by transforming static PDFs into dynamic, editable DOCX files.</p>
        
        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">Layout Retention & Formatting</h3>
        <p style="margin-bottom: 15px;">A core challenge in document conversion is maintaining the visual integrity of the original file. Our extraction algorithm maps out paragraphs, headers, tables, and images, and translates them into corresponding Microsoft Word elements. This ensures that your converted document requires minimal manual formatting.</p>

        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">Seamless API Integration</h3>
        <p>This distinct feature utilizes our optimized backend endpoint to handle the complex structural conversion required for proprietary DOCX formatting. We strictly adhere to ephemeral processing—files are held temporarily in secure RAM only during the conversion process and are immediately shredded, guaranteeing zero retention.</p>
    </section>
    """,

    "word-to-pdf.html": """
    <section class="tool-seo-content" style="max-width: 800px; margin: 40px auto; padding: 20px; background: var(--surface); border-radius: 12px; border: 1px solid var(--border);">
        <h2 style="font-size: 2rem; margin-bottom: 15px;">Convert Microsoft Word to PDF Format</h2>
        <p style="margin-bottom: 15px;">While Microsoft Word is excellent for drafting and editing, sending a DOC or DOCX file to a client risks formatting chaos. Different software versions, missing fonts, or divergent operating systems can ruin your layout. Converting <strong>Word to PDF</strong> permanently locks your formatting, ensuring your recipient views exactly what you designed.</p>
        
        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">Universal Compatibility</h3>
        <p style="margin-bottom: 15px;">By transforming your text documents into the Portable Document Format (PDF), you ensure 100% compatibility across Windows, macOS, Linux, iOS, and Android devices. No special office software is required to view the final output—any modern web browser will suffice.</p>
        
        <p>Whether you're finalizing a professional resume, a legal contract, or an academic manuscript, our converter generates clean, fully standardized PDF vectors. This feature ensures that text remains sharp, selectable, and searchable.</p>
    </section>
    """,

    "edit-pdf.html": """
    <section class="tool-seo-content" style="max-width: 800px; margin: 40px auto; padding: 20px; background: var(--surface); border-radius: 12px; border: 1px solid var(--border);">
        <h2 style="font-size: 2rem; margin-bottom: 15px;">Comprehensive Online PDF Editor</h2>
        <p style="margin-bottom: 15px;">Until recently, editing a PDF required installing heavy, expensive desktop software. Our full-featured online <strong>PDF Editor</strong> brings desktop-level capabilities straight to your browser. You can modify texts, insert graphics, draw custom annotations, and manipulate specific pages.</p>
        
        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">Key Capabilities</h3>
        <ul style="margin-left: 20px; margin-bottom: 15px;">
            <li><strong>Text Annotation:</strong> Highlight, underline, or strike-through text seamlessly directly on the canvas.</li>
            <li><strong>Insert Elements:</strong> Add custom text boxes, embed images, or paste stamps and logos.</li>
            <li><strong>Freehand Drawing:</strong> Perfect for educators grading papers or teams collaborating on design mocks.</li>
            <li><strong>Form Filling:</strong> Easily input data into un-editable text fields for applications or tax submissions.</li>
        </ul>

        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">Why Use an Online Editor?</h3>
        <p>By leveraging HTML5 Canvas and advanced JavaScript libraries, the entire editor interface renders locally. Not only does this make the tool incredibly responsive with zero latency, but it also means confidential edits to contracts happen securely on your machine.</p>
    </section>
    """,

    "sign.html": """
    <section class="tool-seo-content" style="max-width: 800px; margin: 40px auto; padding: 20px; background: var(--surface); border-radius: 12px; border: 1px solid var(--border);">
        <h2 style="font-size: 2rem; margin-bottom: 15px;">Sign PDF Documents Digitally</h2>
        <p style="margin-bottom: 15px;">Gone are the days of printing a multi-page contract, signing it with a pen, and scanning it back into a computer. The <strong>Sign PDF</strong> utility allows you to execute legally binding document endorsements efficiently, saving both time and paper.</p>
        
        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">Multiple Signature Modes</h3>
        <ul style="margin-left: 20px; margin-bottom: 15px;">
            <li><strong>Draw:</strong> Use your mouse, trackpad, or touchscreen stylus to physically sketch your signature onto the page.</li>
            <li><strong>Type:</strong> Enter your name and let our system format it into a professional, cursive-style digital endorsement.</li>
            <li><strong>Upload Image:</strong> Import a pre-scanned PNG or JPEG of your actual signature (with a transparent background) and place it flawlessly on the signature line.</li>
        </ul>

        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">Security and Integrity</h3>
        <p>Once a signature is applied, we highly recommend using our flattening or protection tools to lock the file. Our local-processing guarantee ensures your signature image is never saved to a remote server, eliminating the risk of identity theft or signature forgery.</p>
    </section>
    """,

    "protect.html": """
    <section class="tool-seo-content" style="max-width: 800px; margin: 40px auto; padding: 20px; background: var(--surface); border-radius: 12px; border: 1px solid var(--border);">
        <h2 style="font-size: 2rem; margin-bottom: 15px;">Protect PDF with Military-Grade Password Encryption</h2>
        <p style="margin-bottom: 15px;">When sharing highly sensitive documents via email—such as tax returns, medical records, or confidential intellectual property—attaching a standard PDF is risky. Our <strong>Protect PDF</strong> utility allows you to encrypt your files, ensuring only intended recipients with the password can open them.</p>
        
        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">AES-256 Bit Encryption</h3>
        <p style="margin-bottom: 15px;">We utilize the Advanced Encryption Standard (AES) with a 256-bit key. This is the highest level of commercial security available and is identical to the cryptography standards used by banks, intelligence agencies, and the military. Without the password, brute-forcing the file is mathematically impossible.</p>
        
        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">How to Secure Your Document:</h3>
        <p>Simply upload your file, assign a robust password (we recommend using a combination of alphanumeric characters and symbols), and hit protect. The process generates a fully encrypted wrapper around your data payload.</p>
    </section>
    """,

    "unlock.html": """
    <section class="tool-seo-content" style="max-width: 800px; margin: 40px auto; padding: 20px; background: var(--surface); border-radius: 12px; border: 1px solid var(--border);">
        <h2 style="font-size: 2rem; margin-bottom: 15px;">Unlock PDF and Remove Password Restrictions</h2>
        <p style="margin-bottom: 15px;">Having to type a long, complex password every single time you open your own bank statement or wage slip becomes incredibly tedious. Alternatively, receiving a document that has artificial restrictions preventing you from copying text or printing can halt your workflow. Our <strong>Unlock PDF</strong> tool is designed to strip these barriers permanently.</p>
        
        <h3 style="font-size: 1.5rem; margin-top: 25px; margin-bottom: 10px;">User vs. Owner Passwords</h3>
        <p style="margin-bottom: 15px;">If a PDF is fully encrypted with a 'User Password', you must input the password once to prove ownership. After validation, our tool generates an unlocked clone. If the file merely has an 'Owner Password' (restricting editing or copying), our engine can often safely bypass these arbitrary flags instantly.</p>
    </section>
    """
}

def clean_and_inject():
    html_files = glob.glob(os.path.join(target_dir, "*.html"))
    
    # Regex to aggressively find and remove any block that starts with <section class="tool-seo-content" and ends with </section>
    seo_pattern = re.compile(r'<section\s+class="tool-seo-content"[^>]*>.*?</section>', re.DOTALL)
    
    cleaned_count = 0
    injected_count = 0

    for filepath in html_files:
        filename = os.path.basename(filepath)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()

        # Step 1: Remove all existing SEO content
        if seo_pattern.search(html):
            html = seo_pattern.sub('', html)
            cleaned_count += 1
            
        # Step 2: Inject specific rich content if it's in our top 10 list
        if filename in tools_to_enhance:
            injection = tools_to_enhance[filename]
            
            # Find injection point: before </main> or before <script> or before </body>
            if '</main>' in html:
                html = html.replace('</main>', f'\n{injection}\n  </main>')
            elif '<script>' in html:
                last_script_idx = html.rfind('<script')
                if last_script_idx != -1:
                    html = html[:last_script_idx] + f'\n{injection}\n  ' + html[last_script_idx:]
                else:
                    html = html.replace('</body>', f'\n{injection}\n</body>')
            else:
                html = html.replace('</body>', f'\n{injection}\n</body>')
            
            injected_count += 1
            print(f"Injected unique SEO content into: {filename}")
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
            
    print(f"Operation complete. Cleaned duplicate boilerplate from {cleaned_count} files.")
    print(f"Injected top-tier unique content into {injected_count} strategic pages.")

if __name__ == "__main__":
    clean_and_inject()
