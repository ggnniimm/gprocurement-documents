import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.gprocurement.go.th/"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    r = requests.get(url, headers=headers, verify=False, timeout=20)
    print(f"Status: {r.status_code}")
    print(f"Content length: {len(r.content)}")
    soup = BeautifulSoup(r.content, 'html.parser')
    print(f"Title: {soup.title.string if soup.title else 'No title'}")
    
    links = soup.find_all('a')
    print(f"Found {len(links)} links.")
    for a in links[:20]:
        print(f" - {a.get_text().strip()} -> {a.get('href')}")
        
except Exception as e:
    print(f"Error: {e}")
