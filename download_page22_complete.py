import os
import urllib.request
import urllib.parse
import ssl

DOWNLOAD_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement_downloads"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Read links from file
links = []
with open("page22_links.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "|||" in line:
            parts = line.split("|||")
            if len(parts) >= 2:
                url = parts[1].strip()
                if ".pdf" in url and "wcm/connect" in url:
                    links.append(url)

# Remove duplicates
unique_links = sorted(list(set(links)))

print(f"Found {len(unique_links)} unique PDF links in file.")

success = 0
failed = 0
for url in unique_links:
    try:
        path = urllib.parse.urlparse(url).path
        filename_encoded = os.path.basename(path)
        filename = urllib.parse.unquote(filename_encoded)
        
        # Simple sanitization
        filename = filename.replace('\ufe6f', '').replace('%EF%B9%AF', '')
        
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        
        if os.path.exists(filepath):
            print(f"Skip (exists): {filename[:40]}...")
            success += 1
            continue
            
        print(f"DL: {filename[:40]}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=60) as r, open(filepath, 'wb') as f:
            f.write(r.read())
        success += 1
    except Exception as e:
        print(f"Failed: {filename[:30]}... - {e}")
        failed += 1

print(f"\nPage 22 Complete Run done. Success: {success}, Failed: {failed}")
print()
print("Counting total PDF files in download directory...")
files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith('.pdf')]
print(f"Total PDF files: {len(files)}")
