import os
import re

extra_about = """
        <h2>Our Mission and Vision</h2>
        <p>At Quick Do PDF, our primary mission is to democratize digital document management. For decades, manipulating PDF files required expensive, heavy desktop software subscriptions or forced users to upload their sensitive and confidential data to remote cloud servers. We believe that privacy is a fundamental human right, and that document processing should be accessible to everyone, regardless of technical skill or financial status. Our vision is a web where users can fully control their data locally without compromising on power or utility.</p>
        
        <h2>How We Built Quick Do PDF</h2>
        <p>Built by a dedicated team of web developers and privacy advocates based in New Delhi, India, Quick Do PDF utilizes cutting-edge web technologies like HTML5 Canvas and WebAssembly. These modern browser APIs allow us to run complex arithmetic and file conversions directly inside your device's RAM. Because the heavy lifting happens locally, we have managed to completely eliminate the need for costly backend processing servers. This extraordinary efficiency is exactly why we can offer our entire premium suite of over 20 PDF tools completely for free, forever.</p>

        <h2>Why Trust Us?</h2>
        <p>In a digital era plagued by data breaches and unauthorized data harvesting, trust is paramount. Quick Do PDF was engineered with a "Privacy First" architecture. We categorically state that we do not upload, scan, or retain copies of your documents. You do not need to register an account, provide an email address, or link your social media profiles to use our service. Whether you are merging confidential financial ledgers or shrinking family photos, your files never leave your computer. We are sustained transparently through non-intrusive advertising, ensuring our incentives remain perfectly aligned with user satisfaction and data security.</p>
"""

extra_contact = """
        <h2>Business Inquiries & Partnerships</h2>
        <p>Our team at Quick Do PDF is always open to collaborative opportunities, media inquiries, and potential API integrations. If you represent an educational institution, a non-profit organization, or a fellow technology start-up looking to integrate local-first PDF processing into your workflow, we would love to connect. Please clearly state "Partnership Inquiry" in your subject line to ensure your message is routed to our business development team promptly. We operate Monday through Friday, from 9:00 AM to 6:00 PM IST.</p>
        
        <h2>Technical Support Guidelines</h2>
        <p>Because Quick Do PDF operates entirely inside your local web browser, technical issues are often related to specific device configurations. To help us resolve your issue as quickly as possible, please include the following details in your message:</p>
        <ul style="color: var(--muted); margin-left: 20px; margin-bottom: 20px;">
            <li>Your Operating System (e.g., Windows 11, macOS Sonoma, Android 14)</li>
            <li>Your Web Browser and Version (e.g., Google Chrome v120, Safari v17)</li>
            <li>The specific tool you were using (e.g., Merge PDF, Compress PDF 100kb)</li>
            <li>A brief description of the file size or type causing the issue</li>
        </ul>
        <p>We actively monitor our support inbox and strive to patch bugs and browser incompatibilities within 48 hours of a confirmed report.</p>

        <h2>Mailing Address</h2>
        <p>While we operate as a remote-first digital team, our primary corporate correspondence can be directed to our headquarters:<br>
        <strong>Quick Do PDF Operations</strong><br>
        New Delhi, Delhi 110001<br>
        India<br>
        <em>Please Note: We do not accept physical document submissions or walk-in technical support at this address.</em></p>
"""

extra_privacy = """
        <h2>3. Third-Party Advertising and Cookies</h2>
        <p>To keep Quick Do PDF 100% free for all users globally, we monetize our website using third-party advertising networks, specifically Google AdSense. Google AdSense uses cookies to serve ads based on a user's prior visits to our website or other websites across the Internet. Google's use of advertising cookies enables it and its partners to serve targeted advertisements to our users based on their browsing history. You may opt out of personalized advertising by visiting the <a href="https://myadcenter.google.com/" style="color:var(--a1)">Google Ads Settings</a> page.</p>

        <h2>4. Analytics and Usage Tracking</h2>
        <p>We utilize standard web analytics tools, such as Google Analytics, to understand broad traffic patterns and improve our website's user interface. These tools collect aggregate, anonymous data such as the browser type (e.g., Chrome, Firefox), the operating system (e.g., Windows, iOS), the referring website, and the specific tools accessed. This data cannot be used to identify you personally, and crucially, it does not scan or read the contents of the PDF files you process locally.</p>

        <h2>5. California Consumer Privacy Act (CCPA) Rights</h2>
        <p>If you are a resident of California, you hold specific rights under the CCPA regarding your personal data. Because our application is strictly client-side and does not collect or store users' personal data or documents, we naturally comply with the core tenets of the CCPA. We do not sell your personal information. If you wish to query any generalized log data regarding your IP address, you may contact us via our Contact Page.</p>

        <h2>6. General Data Protection Regulation (GDPR)</h2>
        <p>For our users residing in the European Economic Area (EEA), please note that our service design inherently aligns with GDPR principles, specifically "Data Minimization" and "Privacy by Design." Your documents are processed locally, meaning we are legally neither a "Data Controller" nor a "Data Processor" of your PDF files. For the ad-related cookies mentioned in Section 3, you are prompted with a consent banner upon your first visit, in full compliance with EU regulations.</p>
"""

extra_terms = """
        <h2>4. Permitted and Prohibited Use</h2>
        <p>You are granted a non-exclusive, non-transferable right to access and use Quick Do PDF for your personal or internal business purposes. However, you strictly agree NOT to use the Service to:</p>
        <ul style="color: var(--muted); margin-left: 20px; margin-bottom: 20px;">
            <li>Process, distribute, or unlock illegal, non-consensual, or illicit materials.</li>
            <li>Bypass Digital Rights Management (DRM) or passwords on copyrighted intellectual property that you do not legally own or have express permission to access.</li>
            <li>Automate requests to our website using scraping bots, headless browsers, or unofficial API wrappers that degrade the performance of our frontend servers.</li>
            <li>Attempt to reverse-engineer, decompile, or copy the proprietary WebAssembly or JavaScript bundles that power the Quick Do PDF engine.</li>
        </ul>

        <h2>5. Intellectual Property Rights</h2>
        <p>All content present on this website—including the Quick Do PDF logo, the UI/UX design, custom graphics, written blog articles, and original programming code—is the exclusive intellectual property of Quick Do PDF and is protected by international copyright laws. You may not reproduce, redistribute, or create derivative works from our website layout or code without explicit written authorization from our team.</p>

        <h2>6. Limitation of Liability</h2>
        <p>Quick Do PDF is provided on an "AS IS" and "AS AVAILABLE" basis. While we strive for perfection in our document rendering algorithms, edge cases exist. In no event shall Quick Do PDF, its founders, or affiliates be liable for any direct, indirect, incidental, consequential, or punitive damages arising from your use of the service. This includes, but is not limited to, data loss, corruption of files during compression, formatting errors during Word conversion, or any subsequent financial loss resulting from reliance on the processed documents. It is your sole responsibility to maintain backups of your original, unedited files.</p>
"""

def inject(filename, search_text, content_to_add):
    path = os.path.join("d:\\Yogi\\Yogesh\\quick-do-pdf", filename)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # If already injected, skip
    if "Our Mission and Vision" in html or "Technical Support Guidelines" in html or "Third-Party Advertising" in html or "Permitted and Prohibited Use" in html:
        print(f"Skipping {filename}, already expanded.")
        return

    # find the end of the standard content to inject before the footer links
    footer_idx = html.find('<div class="footer-links">')
    if footer_idx == -1:
        print(f"Error: Could not find footer in {filename}")
        return
        
    new_html = html[:footer_idx] + content_to_add + "\n" + html[footer_idx:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Successfully expanded {filename}")

if __name__ == "__main__":
    inject("about.html", "", extra_about)
    inject("contact.html", "", extra_contact)
    inject("privacy-policy.html", "", extra_privacy)
    inject("terms.html", "", extra_terms)
