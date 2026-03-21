import re
with open('test_annot.pdf', 'rb') as f:
    data = f.read().decode('latin-1')
print("Annots exists in PDF?", '/Annots' in data)
print("Link exists?", '/Link' in data)
print("Annot exists?", '/Annot' in data)
matches = re.findall(r'<<[^>]*?/Annots.*?>', data, re.DOTALL)
print("Matches for Annots dicts:")
for m in matches: print(m)
