import requests
from bs4 import BeautifulSoup
import re
import urllib3
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(level=logging.INFO)

BASE_URL = "https://www.gprocurement.go.th"
START_URLS = [
    "https://www.gprocurement.go.th/go/front/enter/knowledge",
    "https://www.gprocurement.go.th/go/front/enter/law",
    "https://www.gprocurement.go.th/"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

visited = set()

def scan_page(url, depth=0):
    if depth > 2: return None
    if url in visited: return None
    visited.add(url)
    
    print(f"Scanning: {url}")
    try:
        r = requests.get(url, headers=headers, verify=False, timeout=15)
        soup = BeautifulSoup(r.content, 'html.parser')
        
        # Check for target links (our PDF pattern)
        # Pattern: wcm/connect and .pdf and maybe "กวจ"
        links = soup.find_all('a', href=True)
        pdf_links = []
        for a in links:
            href = a['href']
            if '.pdf' in href and 'wcm/connect' in href:
                pdf_links.append(href)
                
        if len(pdf_links) > 5:
            print(f"FOUND LIKELY LIST PAGE: {url} with {len(pdf_links)} PDF links")
            # Print sample
            for p in pdf_links[:3]:
                print(f" - {p}")
            return url

        # If not, look for navigation links
        # Keywords: ข้อหารือ, วินิจฉัย, คณะกรรมการวินิจฉัย
        nav_targets = []
        for a in links:
            txt = a.get_text().strip()
            href = a['href']
            if not href.startswith('http'):
                if href.startswith('/'):
                    href = BASE_URL + href
                else:
                    href = BASE_URL + '/' + href # simplistic
            
            if any(k in txt for k in ["ข้อหารือ", "วินิจฉัย", "knowledge", "law"]):
                if href not in visited and "wps" in href or "go/front" in href:
                    nav_targets.append(href)
        
        for t in nav_targets:
            res = scan_page(t, depth+1)
            if res: return res
            
    except Exception as e:
        print(f"Error scanning {url}: {e}")
    
    return None

for s in START_URLS:
    res = scan_page(s)
    if res:
        print(f"SUCCESS: Found list at {res}")
        break
