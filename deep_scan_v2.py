import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.gprocurement.go.th/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'th-TH,th;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1'
}

try:
    session = requests.Session()
    r = session.get(url, headers=headers, verify=False, timeout=20, allow_redirects=True)
    print(f"Status: {r.status_code}")
    print(f"Final URL: {r.url}")
    print(f"Content length: {len(r.content)}")
    
    soup = BeautifulSoup(r.content, 'html.parser')
    print(f"Title: {soup.title.string if soup.title else 'No title'}")
    
    # Try to find iframe if any
    iframes = soup.find_all('iframe')
    if iframes:
        print(f"Found {len(iframes)} iframes.")
        for i in iframes:
            print(f"Iframe src: {i.get('src')}")
            
    # Try to find meta refresh
    metas = soup.find_all('meta')
    for m in metas:
        if m.get('http-equiv') == 'refresh':
            print(f"Meta Refresh: {m.get('content')}")

except Exception as e:
    print(f"Error: {e}")
