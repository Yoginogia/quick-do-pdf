with open(r"d:\Yogi\Yogesh\quick-do-pdf\excel-to-pdf.html", "rb") as f:
    bytes_data = f.read(50)
    print("excel-to-pdf.html:")
    print(" ".join(f"{b:02x}" for b in bytes_data))

with open(r"d:\Yogi\Yogesh\quick-do-pdf\compress.html", "rb") as f:
    bytes_data = f.read(50)
    print("compress.html:")
    print(" ".join(f"{b:02x}" for b in bytes_data))
