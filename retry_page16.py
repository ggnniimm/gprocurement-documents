import os
import urllib.request
import urllib.parse
import ssl
import re

DOWNLOAD_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement_downloads"

retry_links = [
    # Timeout file
    "https://www.gprocurement.go.th/wps/wcm/connect/49d2c202-b3bf-4901-ba9b-443ed096e7f6/01_%E0%B8%81%E0%B8%A7%E0%B8%88_42685_230964_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%8A%E0%B8%B3%E0%B8%A3%E0%B8%B8%E0%B8%94%E0%B8%AF.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-49d2c202-b3bf-4901-ba9b-443ed096e7f6-nOnDKF-",
    # Bad filename file
    "https://www.gprocurement.go.th/wps/wcm/connect/cc788e69-bf5a-47f0-907b-cf6f22e6d70d/02_%E0%B8%81%E0%B8%A7%E0%B8%88_42306_220964_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B9%81%E0%B8%99%E0%B8%A7%E0%B8%97%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%8F%E0%B8%B4%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B8%95%E0%B8%B2%E0%B8%A1%E0%B8%81%E0%B8%8E%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B8%97%E0%B8%A3%E0%B8%A7%E0%B8%87%E0%B8%81%E0%B9%8D%E0%B8%B2%E0%B8%AB%E0%B8%99%E0%B8%94%E0%B8%9E%E0%B8%B1%E0%B8%AA%E0%B8%94%E0%B8%B8%EF%B9%AF.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-cc788e69-bf5a-47f0-907b-cf6f22e6d70d-nPaRcjb"
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def clean_filename(fname):
    # Remove specific problematic char encountered: \ufe6f (small vertical line)
    # Also remove any non-standard chars if needed, but let's be minimal first to preserve Thai text
    # The user specifically asked to remove problem chars.
    # Check for the specific char found in logs: \ufe6f
    
    # Python's unquote might keep it.
    # Let's simple remove known bad chars or strip non-printable
    
    fname = fname.replace('\ufe6f', '') # Replace the specific issue
    fname = fname.replace('%EF%B9%AF', '') # Just in case it's still url encoded
    
    # Generic cleanup for safe filenames
    # Remove chars that are definitely illegal in filesystem but keep Thai
    # Just removing explicit problem char reported
    return fname

print(f"Retrying {len(retry_links)} files...")

for url in retry_links:
    try:
        path = urllib.parse.urlparse(url).path
        filename_encoded = os.path.basename(path)
        filename = urllib.parse.unquote(filename_encoded)
        
        # Clean filename
        filename = clean_filename(filename)
        
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        
        print(f"DL: {filename[:40]}... (Path: {filepath})")
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=60) as r, open(filepath, 'wb') as f:
            f.write(r.read())
        print("Success.")
    except Exception as e:
        print(f"Failed: {filename[:30]}... - {e}")

print("\nRetry complete.")
