import urllib.request
import ssl
import os

url = "https://www.gprocurement.go.th/wps/wcm/connect/a887951a-9fa5-43df-863f-5f42b727ffb0/02_%E0%B8%81%E0%B8%A7%E0%B8%88_24257_280564_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%8F%E0%B8%B4%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B8%81%E0%B8%A3%E0%B8%93%E0%B8%B5%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%8B%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%94%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%A2%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B9%80%E0%B8%89%E0%B8%9E%E0%B8%B2%E0%B8%B0%E0%B9%80%E0%B8%88%E0%B8%B2%E0%B8%B0%E0%B8%88%E0%B8%87.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-a887951a-9fa5-43df-863f-5f42b727ffb0-nOn.2SK"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    print(f"Testing download from {url[:50]}...")
    with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
        data = r.read()
        print(f"Downloaded {len(data)} bytes.")
except Exception as e:
    print(f"Download failed: {e}")
