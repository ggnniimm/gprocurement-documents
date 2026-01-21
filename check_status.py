import os
import re
import glob
import urllib.parse

# Use current directory
DOWNLOAD_DIR = os.getcwd()
SCRIPTS_DIR = os.getcwd()

def analyze_script(script_path):
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try to find the list variable, usually page_X_links = [...]
    match = re.search(r'page_(\d+)_links\s*=\s*\[(.*?)\]', content, re.DOTALL)
    if not match:
        match = re.search(r'links\s*=\s*\[(.*?)\]', content, re.DOTALL)
        
    if not match:
        return None

    page_num_str = match.group(1) if 'page_' in match.group(0) else "unknown"
    if page_num_str == "unknown":
        file_match = re.search(r'download_page(\d+)', os.path.basename(script_path))
        if file_match:
            page_num_str = file_match.group(1)

    links_content = match.group(2)
    urls = re.findall(r'"(https?://.*?)"', links_content)
    
    downloaded_count = 0
    missing_files = []
    
    for url in urls:
        path = urllib.parse.urlparse(url).path
        filename_encoded = os.path.basename(path)
        filename = urllib.parse.unquote(filename_encoded)
        # Handle the specific replacement logic seen in original script if needed, 
        # but standardized unquote should work for most.
        # The original script had: filename = filename.replace('\ufe6f', '').replace('%EF%B9%AF', '')
        # We'll include it just in case.
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

print(f"{'Page':<10} | {'Expected':<10} | {'Downloaded':<10} | {'Status':<15}")
print("-" * 55)

scripts = sorted(glob.glob(os.path.join(SCRIPTS_DIR, "download_page*.py")))
page_scripts = {}

for s in scripts:
    base = os.path.basename(s)
    # Skip the summarize script itself and check_status
    if base in ["summarize_downloads.py", "check_status.py"]:
        continue
        
    m = re.search(r'page(\d+)', base)
    if m:
        p = int(m.group(1))
        if p not in page_scripts:
            page_scripts[p] = s
        else:
            # Prefer v2 or complete or retry
            current = page_scripts[p]
            kw_new = ["retry", "complete", "v2"]
            if any(k in base for k in kw_new):
                page_scripts[p] = s

sorted_pages = sorted(page_scripts.keys())

total_expected_sum = 0
total_downloaded_sum = 0
last_page = 0

for p in sorted_pages:
    path = page_scripts[p]
    res = analyze_script(path)
    if res:
        print(f"Page {res['page']:<5} | {res['total']:<10} | {res['downloaded']:<10} | {'Complete' if res['total'] == res['downloaded'] else 'Incomplete'}")
        total_expected_sum += res['total']
        total_downloaded_sum += res['downloaded']
        last_page = p
    else:
        print(f"Page {p:<5} | {'?':<10} | {'?':<10} | Could not parse")

print("-" * 55)
print(f"Total Pages Checked: {len(sorted_pages)}")
print(f"Last Page Checked: {last_page}")
