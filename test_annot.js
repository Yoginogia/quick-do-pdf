const { PDFDocument, PDFName, PDFString } = require('pdf-lib');
const fs = require('fs');

async function test() {
    const pdfDoc = await PDFDocument.create();
    const page = pdfDoc.addPage([500, 500]);
    
    // Create Link
    const linkAnnot = pdfDoc.context.obj({
        Type: 'Annot', 
        Subtype: 'Link',
        Rect: [50, 50, 150, 100],
        Border: [0, 0, 2],
        F: 4, 
        P: page.ref,
        A: { Type: 'Action', S: 'URI', URI: PDFString.of('https://google.com') }
    });
    
    const linkRef = pdfDoc.context.register(linkAnnot);
    page.node.addAnnot(linkRef);
    
    fs.writeFileSync('test_annot.pdf', await pdfDoc.save({ useObjectStreams: false }));
}
test().catch(console.error);
