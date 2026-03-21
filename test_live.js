const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext();
    const page = await context.newPage();

    page.on('console', msg => console.log('BROWSER CONSOLE:', msg.text()));
    page.on('pageerror', error => console.error('BROWSER ERROR:', error));

    await page.goto('https://quickdopdf.com/edit-pdf.html?v=4', { waitUntil: 'networkidle' });

    console.log("Injecting dummy PDF...");
    await page.evaluate(async () => {
        // Generate dummy PDF using existing PDFLib
        const doc = await PDFLib.PDFDocument.create();
        doc.addPage([600, 800]);
        const bytes = await doc.save();
        const file = new File([bytes], "dummy.pdf", { type: "application/pdf" });

        // Trigger file input
        const input = document.getElementById('pdfInput');
        const dt = new DataTransfer();
        dt.items.add(file);
        input.files = dt.files;
        input.dispatchEvent(new Event('change'));
    });

    // Wait for the pdf to render
    await page.waitForSelector('.page-wrapper', { timeout: 10000 });
    console.log("PDF rendered. Adding Link...");

    // Create a link annotation programmatically
    await page.evaluate(() => {
        const layer = document.querySelector('.interaction-layer');
        addLinkElement(layer, 50, 50, 'https://example.com');
    });

    console.log("Exporting PDF...");
    
    // Catch the download
    const downloadPromise = page.waitForEvent('download');
    
    await page.evaluate(() => {
        exportEditedPDF();
    });

    const download = await downloadPromise;
    await download.saveAs('downloaded_test.pdf');
    console.log("Downloaded saved to downloaded_test.pdf");

    await browser.close();
})();
