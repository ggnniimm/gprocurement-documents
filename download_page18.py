import os
import urllib.request
import urllib.parse
import ssl

DOWNLOAD_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement_downloads"

# Page 18 links (First 10)
page_18_links = [
    "https://www.gprocurement.go.th/wps/wcm/connect/f8ce6bfd-8c10-4af7-8e76-6def7bc9383f/01_%E0%B8%81%E0%B8%A7%E0%B8%88_28591_280664_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A3%E0%B8%B4%E0%B8%9A%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%81%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2%E0%B8%8B%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%82%E0%B8%A2.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-f8ce6bfd-8c10-4af7-8e76-6def7bc9383f-nOhGj8J",
    "https://www.gprocurement.go.th/wps/wcm/connect/91a09a4f-280f-4a21-bb11-49708cabd13d/01_%E0%B8%81%E0%B8%A7%E0%B8%88_28126_230664_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%9B%E0%B8%A5%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%99%E0%B9%81%E0%B8%9B%E0%B8%A5%E0%B8%87%E0%B8%AA%E0%B8%96%E0%B8%B2%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%81%E0%B9%88%E0%B8%AD%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-91a09a4f-280f-4a21-bb11-49708cabd13d-nOhqzQ4",
    "https://www.gprocurement.go.th/wps/wcm/connect/47298b69-5153-49e0-9b50-f77b0f38ed98/02_%E0%B8%81%E0%B8%A7%E0%B8%88_28122_230664_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%A1%E0%B8%B5%E0%B8%AD%E0%B8%B3%E0%B8%99%E0%B8%B2%E0%B8%88%E0%B8%AD%E0%B8%99%E0%B8%B8%E0%B8%A1%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B9%81%E0%B8%81%E0%B9%89%E0%B9%84%E0%B8%82%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-47298b69-5153-49e0-9b50-f77b0f38ed98-nOngJHZ",
    "https://www.gprocurement.go.th/wps/wcm/connect/0e9d3621-7645-461a-bffa-4f145c48136c/01_%E0%B8%81%E0%B8%A7%E0%B8%88_27975_220664_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%A3%E0%B8%93%E0%B8%B5%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%B4%E0%B8%88%E0%B8%B2%E0%B8%A3%E0%B8%93%E0%B9%8C%E0%B8%A3%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B8%82%E0%B8%AD%E0%B8%9B%E0%B9%80%E0%B8%82%E0%B8%95%E0%B8%AF.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-0e9d3621-7645-461a-bffa-4f145c48136c-nT1y2N8",
    "https://www.gprocurement.go.th/wps/wcm/connect/89920781-2c0f-430c-9572-7d127b36d5e1/02_%E0%B8%81%E0%B8%A7%E0%B8%88_27458_180664_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A7%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%AD%E0%B8%AD%E0%B8%AB%E0%B8%82%E0%B8%B2%E0%B8%9A%E0%B8%B1%E0%B8%87%E0%B8%84%E0%B8%B1%E0%B8%9A%EF%B9%AF.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-89920781-2c0f-430c-9572-7d127b36d5e1-nT6CUfM",
    "https://www.gprocurement.go.th/wps/wcm/connect/8276f492-dbee-44b7-a029-42caeca1d873/01_%E0%B8%81%E0%B8%A7%E0%B8%88_27173_170664_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B9%81%E0%B8%99%E0%B8%A7%E0%B8%97%E0%B8%B2%E0%B8%87%E0%B8%9B%E0%B8%8F%E0%B8%B4%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B8%95%E0%B8%B2%E0%B8%A1%E0%B8%9E%E0%B8%A3%E0%B8%B2%E0%B8%8A%E0%B8%9A%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B1%E0%B8%95%E0%B8%B4%EF%B9%AF.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-8276f492-dbee-44b7-a029-42caeca1d873-nT6GsNf",
    "https://www.gprocurement.go.th/wps/wcm/connect/8920a940-6bb2-4cd7-852b-64b0ef31b755/02_%E0%B8%81%E0%B8%A7%E0%B8%88_27094_160664_%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%82%E0%B8%AD%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B8%A7%E0%B8%B4%E0%B8%99%E0%B8%B4%E0%B8%88%E0%B8%89%E0%B8%B1%E0%B8%A2%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%8A%E0%B8%AD%E0%B8%9A%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%81%E0%B8%AB%E0%B8%A1%E0%B8%B2%E0%B8%A2%E0%B8%20%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-8920a940-6bb2-4cd7-852b-64b0ef31b755-nOhqlme",
    "https://www.gprocurement.go.th/wps/wcm/connect/0859d775-7a70-4eac-97fb-f065b66f8ec2/01_%E0%B8%81%E0%B8%A7%E0%B8%88_27093_160664_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%A3%E0%B8%93%E0%B8%B5%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%81%E0%B8%88%E0%B9%89%E0%B9%84%E0%B8%82%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-0859d775-7a70-4eac-97fb-f065b66f8ec2-nRru.Gg",
    "https://www.gprocurement.go.th/wps/wcm/connect/828c9801-5126-4fc5-a184-a98d99da1a99/02_%E0%B8%81%E0%B8%A7%E0%B8%88_26870_150664_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B9%81%E0%B8%99%E0%B8%A7%E0%B8%97%E0%B8%B2%E0%B8%87%E0%B8%9B%E0%B8%8F%E0%B8%B4%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A7%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9E%E0%B8%B4%E0%B8%88%E0%B8%B2%E0%B8%A3%E0%B8%93%E0%B8%B2%E0%B8%87%E0%B8%94%E0%B8%AB%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%A5%E0%B8%94%E0%B8%84%E0%B9%88%E0%B8%B2%E0%B8%9B%E0%B8%A3%E0%B8%B1%E0%B8%9B%EF%B9%AF.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-828c9801-5126-4fc5-a184-a98d99da1a99-nXyGsIZ",
    "https://www.gprocurement.go.th/wps/wcm/connect/92668abc-4f43-4ded-b6e3-8dbf1ac8a198/01_%E0%B8%81%E0%B8%A7%E0%B8%88_26754_150664_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%84%E0%B8%B8%E0%B8%93%E0%B8%AA%E0%B8%A1%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%A2%E0%B8%B7%E0%B9%88%E0%B8%99%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B9%80%E0%B8%AA%E0%B8%99%E0%B8%AD%EF%B9%AF.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-92668abc-4f43-4ded-b6e3-8dbf1ac8a198-nOhGpCI"
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print(f"Downloading {len(page_18_links)} files from Page 18 (Batch 1)...")

success = 0
failed = 0
for url in page_18_links:
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
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r, open(filepath, 'wb') as f:
            f.write(r.read())
        success += 1
    except Exception as e:
        print(f"Failed: {filename[:30]}... - {e}")
        failed += 1

print(f"\nPage 18 (Batch 1) done. Success: {success}, Failed: {failed}")
print()
print("Counting total files in download directory...")
files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith('.pdf')]
print(f"Total PDF files: {len(files)}")
