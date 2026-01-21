import os
import urllib.request
import urllib.parse
import ssl

DOWNLOAD_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement_downloads"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

page_22_links = [
"https://www.gprocurement.go.th/wps/wcm/connect/292a327a-23e7-4190-8d9d-05d3b394e50f/02_%E0%B8%81%E0%B8%A7%E0%B8%88_21417_110564_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B9%81%E0%B8%99%E0%B8%A7%E0%B8%97%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B9%8D%E0%B8%B2%E0%B8%AB%E0%B8%99%E0%B8%94%E0%B8%81%E0%B8%A3%E0%B8%AD%E0%B8%9A%E0%B8%A3%E0%B8%B0%E0%B8%A2%E0%B8%B0%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AF.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-292a327a-23e7-4190-8d9d-05d3b394e50f-nT2bFtU",
"https://www.gprocurement.go.th/wps/wcm/connect/22a15bcc-d882-424e-9255-bfb0bfd73cfb/01_%E0%B8%81%E0%B8%A7%E0%B8%88_21382_110564_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%8B%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%88%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A7%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9A%E0%B8%B3%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B8%A3%E0%B8%B1%E0%B8%81%E0%B8%A9%E0%B8%B2%E0%B8%9E%E0%B8%B1%E0%B8%AA%E0%B8%94%E0%B8%B8.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-22a15bcc-d882-424e-9255-bfb0bfd73cfb-nSOy1ie",
"https://www.gprocurement.go.th/wps/wcm/connect/972649fe-08fb-4516-8a0a-b75676d7ec7c/01_%E0%B8%81%E0%B8%A7%E0%B8%88_21175_070564_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A7%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9E%E0%B8%B4%E0%B8%88%E0%B8%B2%E0%B8%A3%E0%B8%93%E0%B8%B2%E0%B8%9C%E0%B8%A5%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%81%E0%B9%88%E0%B8%AD%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%AF.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-972649fe-08fb-4516-8a0a-b75676d7ec7c-nOhjT9F",
"https://www.gprocurement.go.th/wps/wcm/connect/19bd24cf-220c-4a8c-8f87-665e584dc3e5/01_%E0%B8%81%E0%B8%A7%E0%B8%88_20694_030564_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B9%81%E0%B8%99%E0%B8%A7%E0%B8%97%E0%B8%B2%E0%B8%87%E0%B8%9B%E0%B8%8F%E0%B8%B4%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B8%81%E0%B8%A3%E0%B8%93%E0%B8%B5%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%9A%E0%B8%B4%E0%B8%81%E0%B8%88%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%87%E0%B8%B4%E0%B8%99%E0%B8%AF.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-19bd24cf-220c-4a8c-8f87-665e584dc3e5-nXywVYl",
"https://www.gprocurement.go.th/wps/wcm/connect/27f75dca-d624-4043-a7cd-f1fc8beec699/0405.4_16439.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-27f75dca-d624-4043-a7cd-f1fc8beec699-ny2bMI1",
"https://www.gprocurement.go.th/wps/wcm/connect/4749ab58-931e-488f-9b05-fd5c13c235d2/0405.4_9630.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-4749ab58-931e-488f-9b05-fd5c13c235d2-nvcF3-i",
"https://www.gprocurement.go.th/wps/wcm/connect/a32f148d-2dfc-497b-9983-ba7a33cc0ab4/%E0%B8%9B%E0%B8%95%E0%B8%97.%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD+%E0%B8%A1%E0%B8%B2%E0%B8%95%E0%B8%A3%E0%B8%B24.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-a32f148d-2dfc-497b-9983-ba7a33cc0ab4-npwiZSe",
"https://www.gprocurement.go.th/wps/wcm/connect/3b897178-94a1-4357-b3b1-db111c3de6a1/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%88%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%A3%E0%B8%B6%E0%B8%81%E0%B8%A9%E0%B8%B2+%E0%B8%81%E0%B8%A3%E0%B8%A1%E0%B8%8A%E0%B8%A5%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%97%E0%B8%B2%E0%B8%99+60355.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-3b897178-94a1-4357-b3b1-db111c3de6a1-noIypL4",
"https://www.gprocurement.go.th/wps/wcm/connect/3bb9ff1b-fa9f-47a8-b165-169e51c75a68/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%87%E0%B8%94%E0%B8%A5%E0%B8%94+%E0%B8%AD%E0%B8%9A%E0%B8%88.%E0%B8%AA%E0%B8%B8%E0%B8%A3%E0%B8%B4%E0%B8%99%E0%B8%97%E0%B8%A3%E0%B9%8C+60370.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-3bb9ff1b-fa9f-47a8-b165-169e51c75a68-noIxEA.",
"https://www.gprocurement.go.th/wps/wcm/connect/967f86d7-2cb8-4de4-8be6-a35cf4e93adb/%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%9C%E0%B8%A5%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B8%97%E0%B8%9A%E0%B9%82%E0%B8%84%E0%B8%A7%E0%B8%B4%E0%B8%94+%E0%B8%AD%E0%B8%9A%E0%B8%88.%E0%B9%81%E0%B8%9E%E0%B8%A3%E0%B9%88+60077.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-967f86d7-2cb8-4de4-8be6-a35cf4e93adb-noDdf98",
"https://www.gprocurement.go.th/wps/wcm/connect/4af2ee2c-8f89-49fc-80db-e830a61e2d4d/%E0%B9%80%E0%B8%97%E0%B8%A8%E0%B8%9A%E0%B8%B2%E0%B8%A5%E0%B8%95%E0%B8%B3%E0%B8%9A%E0%B8%A5%E0%B8%9E%E0%B8%A3%E0%B8%B0%E0%B8%9A%E0%B8%B8+%E0%B8%82%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B9%81%E0%B8%99%E0%B8%A7%E0%B8%97%E0%B8%B2%E0%B8%87%E0%B8%9B%E0%B8%8F%E0%B8%B4%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B9%83%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%84%E0%B8%B7%E0%B8%99%E0%B8%84%E0%B9%88%E0%B8%B2%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%AD%E0%B8%81%E0%B8%AA%E0%B8%B2%E0%B8%A3%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%A7%E0%B8%94%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B9%80%E0%B8%A5%E0%B9%87%E0%B8%81%E0%B8%97%E0%B8%A3%E0%B8%AD%E0%B8%99%E0%B8%B4%E0%B8%81%E0%B8%AA%E0%B9%8C+60070.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-4af2ee2c-8f89-49fc-80db-e830a61e2d4d-noCMfbn",
"https://www.gprocurement.go.th/wps/wcm/connect/ba9f7553-88a1-4bc1-ad81-8233187a1c71/%E0%B8%95%E0%B8%AD%E0%B8%9A%E0%B8%A3%E0%B8%B2%E0%B8%8A%E0%B8%A0%E0%B8%B1%E0%B8%8E%E0%B9%80%E0%B8%A5%E0%B8%A2+59140.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-ba9f7553-88a1-4bc1-ad81-8233187a1c71-noCi-tA",
"https://www.gprocurement.go.th/wps/wcm/connect/0e736be9-1911-4f61-9cec-b4c464a37883/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%84%E0%B8%AB%E0%B8%B0+59133.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-0e736be9-1911-4f61-9cec-b4c464a37883-noCjBn.",
"https://www.gprocurement.go.th/wps/wcm/connect/ad462c42-56a1-405f-95d9-e5bdafcb333f/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%A3%E0%B8%B1%E0%B8%9A+%E0%B8%A1.%E0%B8%99%E0%B9%80%E0%B8%A3%E0%B8%A8%E0%B8%A7%E0%B8%A3+59101.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-ad462c42-56a1-405f-95d9-e5bdafcb333f-noCjPgj",
"https://www.gprocurement.go.th/wps/wcm/connect/abc9244e-400e-4e01-a6d1-991ffacebed5/%E0%B8%95%E0%B8%AD%E0%B8%9A%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD+%E0%B8%99%E0%B8%A2.%E0%B8%97%E0%B8%A1.%E0%B8%9E%E0%B8%B1%E0%B8%87%E0%B8%87%E0%B8%B2+59137.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-abc9244e-400e-4e01-a6d1-991ffacebed5-noCmYuo",
"https://www.gprocurement.go.th/wps/wcm/connect/5f26180a-413a-452c-8f02-a0743b29f544/%E0%B8%95%E0%B8%AD%E0%B8%9A%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD+%E0%B8%AD%E0%B8%9A%E0%B8%95.%E0%B8%9A%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%9E%E0%B8%A3%E0%B8%B4%E0%B8%81.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-5f26180a-413a-452c-8f02-a0743b29f544-noCny5d",
"https://www.gprocurement.go.th/wps/wcm/connect/7481d215-8027-442b-b46b-8cde6b2d42ae/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%A3%E0%B8%93%E0%B8%B5%E0%B8%88%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%84%E0%B8%9F%E0%B8%9F%E0%B9%89%E0%B8%B2%E0%B8%AA%E0%B9%88%E0%B8%A7%E0%B8%99%E0%B8%A0%E0%B8%B9%E0%B8%A1%E0%B8%B4%E0%B8%A0%E0%B8%B2%E0%B8%84+58348.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-7481d215-8027-442b-b46b-8cde6b2d42ae-noCnPHe",
"https://www.gprocurement.go.th/wps/wcm/connect/4071c4f5-9c50-47f1-a066-d144235becd0/%E0%B8%95%E0%B8%AD%E0%B8%9A%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD+%E0%B8%81%E0%B8%A3%E0%B8%A1%E0%B8%97%E0%B8%A3%E0%B8%B1%E0%B8%9E%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B8%A3%E0%B8%97%E0%B8%B0%E0%B9%80%E0%B8%A5+56931.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-4071c4f5-9c50-47f1-a066-d144235becd0-noCo7nt"
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print(f"Downloading {len(page_22_links)} files from Page 22...")

success = 0
failed = 0
for url in page_22_links:
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
            
        print(f"DL: {translate_filename(filename)[:40] if 'translate_filename' in globals() else filename[:40]}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=60) as r, open(filepath, 'wb') as f:
            f.write(r.read())
        success += 1
    except Exception as e:
        print(f"Failed: {filename[:30]}... - {e}")
        failed += 1

print(f"\nPage 22 done. Success: {success}, Failed: {failed}")
print()
print("Counting total files in download directory...")
files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith('.pdf')]
print(f"Total PDF files: {len(files)}")
