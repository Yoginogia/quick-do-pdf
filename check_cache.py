import urllib.request
url = "https://quickdopdf.com/edit-pdf.html"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')

if "pdfPage.drawRectangle({" in html and "opacity: 0.15" in html:
    print("LIVE SITE IS UPDATED!")
else:
    print("LIVE SITE IS STALE (CACHED)!")
