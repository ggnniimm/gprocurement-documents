
import os
import re
import glob

DOWNLOAD_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement_downloads"
SCRIPTS_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement_downloads"

def analyze_script(script_path):
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try to find the list variable, usually page_X_links = [...]
    # We'll look for the list definition
    match = re.search(r'page_(\d+)_links\s*=\s*\[(.*?)\]', content, re.DOTALL)
    if not match:
        # Fallback for page 18 "complete" or others
        match = re.search(r'links\s*=\s*\[(.*?)\]', content, re.DOTALL)
        
    if not match:
        return None

    page_num_str = match.group(1) if 'page_' in match.group(0) else "unknown"
    # If we matched 'links =', try to guess page number from filename
    if page_num_str == "unknown":
        file_match = re.search(r'download_page(\d+)', os.path.basename(script_path))
        if file_match:
            page_num_str = file_match.group(1)

    links_content = match.group(2)
    # Count non-empty lines or quoted strings to estimate link count
    # A robust way is to find all "http..." strings
    urls = re.findall(r'"(https?://.*?)"', links_content)
    
    # Check which ones are downloaded
    downloaded_count = 0
    missing_files = []
    
    for url in urls:
        path = urllib.parse.urlparse(url).path
        filename_encoded = os.path.basename(path)
        filename = urllib.parse.unquote(filename_encoded)
        filename = filename.replace('\ufe6f', '').replace('%EF%B9%AF', '')
        
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        if os.path.exists(filepath):
            downloaded_count += 1
        else:
            missing_files.append(filename)
            
    return {
        "page": page_num_str,
        "total": len(urls),
        "downloaded": downloaded_count,
        "missing": missing_files,
        "script": os.path.basename(script_path)
    }

import urllib.parse

print(f"{'Page':<10} | {'Expected':<10} | {'Downloaded':<10} | {'Status':<15}")
print("-" * 55)

scripts = sorted(glob.glob(os.path.join(SCRIPTS_DIR, "download_page*.py")))
# Filter out older versions if newer exists? e.g. 11 vs 11_v2
# We'll map page number to script, keeping the one with "v2" or "complete" if duplicate or just latest
page_scripts = {}
for s in scripts:
    # heuristic: if we have page11 and page11_v2, take v2
    base = os.path.basename(s)
    # Extract number
    m = re.search(r'page(\d+)', base)
    if m:
        p = int(m.group(1))
        # Logic: if p not in dict, add. If in dict, prefer "complete" or "v2" or "retry"
        if p not in page_scripts:
            page_scripts[p] = s
        else:
            current = page_scripts[p]
            if "retry" in base or "complete" in base or "v2" in base:
                page_scripts[p] = s
            # simplistic override, could ideally check file mtime

sorted_pages = sorted(page_scripts.keys())

total_expected_sum = 0
total_downloaded_sum = 0

for p in sorted_pages:
    path = page_scripts[p]
    res = analyze_script(path)
    if res:
        print(f"Page {res['page']:<5} | {res['total']:<10} | {res['downloaded']:<10} | {'Complete' if res['total'] == res['downloaded'] else 'Incomplete'}")
        total_expected_sum += res['total']
        total_downloaded_sum += res['downloaded']
    else:
        print(f"Page {p:<5} | {'?':<10} | {'?':<10} | Copuld not parse")

print("-" * 55)
print(f"Total (9-20)| {total_expected_sum:<10} | {total_downloaded_sum:<10} |")
