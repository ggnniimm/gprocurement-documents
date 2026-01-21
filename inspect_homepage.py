import urllib.request
import urllib.parse
import ssl
import re

url = "https://www.gprocurement.go.th/go/front/enter/knowledge_center"
# Trying to guess a likely URL for knowledge center or similar

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

def fetch(u):
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return str(e)

# 1. Fetch homepage
print("Fetching homepage...")
html = fetch("https://www.gprocurement.go.th/")
# Extract links that might be relevant
links = re.findall(r'href="([^"]+)"', html)

relevant = []
for l in links:
    if "wps" in l or "knowledge" in l.lower() or "download" in l.lower():
        relevant.append(l)

# print(f"Found {len(links)} links. Relevant: {len(relevant)}")
# for r in relevant[:10]:
#     print(r)

# 2. Search for "ข้อหารือ" text in html to see if there's a direct link
if "ข้อหารือ" in html:
    print("Found 'ข้อหารือ' on homepage.")
    # Try to find the link surrounding it
    # This is rough regex
    m = re.search(r'<a[^>]+href="([^"]+)"[^>]*>.*?ข้อหารือ.*?</a>', html, re.DOTALL)
    if m:
        print(f"Found link: {m.group(1)}")
else:
    print("Did not find 'ข้อหารือ' on homepage text.")

# 3. Try a known pattern for the knowledge page
# Often it's under "Information" -> "Legal" -> "Diagnosis"
# Try fetching the "Legal" page if we can find its link
