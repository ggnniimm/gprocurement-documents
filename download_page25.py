import os
import urllib.request
import urllib.parse
import ssl

DOWNLOAD_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement-documents"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

page_25_links = [
"https://www.gprocurement.go.th/wps/wcm/connect/42bfc41c-575e-471a-a727-49b0fa57cf20/10515.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-42bfc41c-575e-471a-a727-49b0fa57cf20-mVAuQkb",
"https://www.gprocurement.go.th/wps/wcm/connect/17336178-942f-4b68-8457-a42f49b8bb76/9619.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-17336178-942f-4b68-8457-a42f49b8bb76-mVAuKhV",
"https://www.gprocurement.go.th/wps/wcm/connect/003bb1a9-de52-4817-90c5-268e296dc6c8/9616.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-003bb1a9-de52-4817-90c5-268e296dc6c8-mVAuZ7x",
"https://www.gprocurement.go.th/wps/wcm/connect/253295b7-a1fe-441f-be7e-95e374b328b6/25620058452_V1.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-253295b7-a1fe-441f-be7e-95e374b328b6-nOmBeEU",
"https://www.gprocurement.go.th/wps/wcm/connect/09de5151-c059-4f2f-9c9b-c99ef0c07f6d/25620058420_V1.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-09de5151-c059-4f2f-9c9b-c99ef0c07f6d-nOmyLkx",
"https://www.gprocurement.go.th/wps/wcm/connect/3112b9b9-25f2-4499-b77e-b798f8f2b668/5875.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-3112b9b9-25f2-4499-b77e-b798f8f2b668-mVAtFm3",
"https://www.gprocurement.go.th/wps/wcm/connect/a9d68a74-e825-4e31-a14e-fd956a3ad26b/25620027364_V1.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-a9d68a74-e825-4e31-a14e-fd956a3ad26b-nOmvcPI",
"https://www.gprocurement.go.th/wps/wcm/connect/8d0b3d92-c7ee-4c68-ac91-1e46903f30fd/3315.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-8d0b3d92-c7ee-4c68-ac91-1e46903f30fd-mVAudUd",
"https://www.gprocurement.go.th/wps/wcm/connect/79517b7e-ae22-42f4-966c-b312041af4d7/3211.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-79517b7e-ae22-42f4-966c-b312041af4d7-mVAv3GW",
"https://www.gprocurement.go.th/wps/wcm/connect/d3bbceff-0913-4244-ab8a-d5621e2e8b8e/25610410015_V1.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-d3bbceff-0913-4244-ab8a-d5621e2e8b8e-nOmxM1e",
"https://www.gprocurement.go.th/wps/wcm/connect/cb88d0ed-4d27-4b9b-94c3-0738624acd6c/25610409058_V1.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-cb88d0ed-4d27-4b9b-94c3-0738624acd6c-nOmy5fb",
"https://www.gprocurement.go.th/wps/wcm/connect/76e5aba4-89e0-44f2-a167-fc27d3683b79/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-053926.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-76e5aba4-89e0-44f2-a167-fc27d3683b79-mVAxwaM",
"https://www.gprocurement.go.th/wps/wcm/connect/4a2f2b06-11ab-40ef-918e-faee452759b6/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-051679.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-4a2f2b06-11ab-40ef-918e-faee452759b6-mVA4B.8",
"https://www.gprocurement.go.th/wps/wcm/connect/d3beda1e-4925-447c-9457-381b1bf03b94/051687.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-d3beda1e-4925-447c-9457-381b1bf03b94-mVAxCBP",
"https://www.gprocurement.go.th/wps/wcm/connect/064fd21f-6f11-4eb5-b139-7fa157be9d74/051670..pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-064fd21f-6f11-4eb5-b139-7fa157be9d74-mVAxKts",
"https://www.gprocurement.go.th/wps/wcm/connect/81977a3a-22b1-48cf-b6a8-0f591a1295d9/051459.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-81977a3a-22b1-48cf-b6a8-0f591a1295d9-mVAxRKV",
"https://www.gprocurement.go.th/wps/wcm/connect/e2e1a0c7-241c-4357-8a31-2722746ea879/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-049571.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-e2e1a0c7-241c-4357-8a31-2722746ea879-mVAxZ8E",
"https://www.gprocurement.go.th/wps/wcm/connect/fe60a607-70e5-497b-b105-5c48a1c98694/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-049049.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-fe60a607-70e5-497b-b105-5c48a1c98694-mVAyp58",
"https://www.gprocurement.go.th/wps/wcm/connect/d014b864-c0a3-491e-9768-df60fa84b9a2/048797.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-d014b864-c0a3-491e-9768-df60fa84b9a2-mVAy9P9",
"https://www.gprocurement.go.th/wps/wcm/connect/5e918039-a125-47e8-bb0e-62519b5d5ecb/048748.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-5e918039-a125-47e8-bb0e-62519b5d5ecb-mVAyLEw"
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print(f"Downloading {len(page_25_links)} files from Page 25...")

success = 0
failed = 0
for url in page_25_links:
    try:
        path = urllib.parse.urlparse(url).path
        filename_encoded = os.path.basename(path)
        filename = urllib.parse.unquote(filename_encoded)
        
        # Consistent sanitization
        filename = filename.replace('+', '_').replace(' ', '_').replace('__', '_')
        filename = filename.replace('(PDPA)', '_PDPA').replace('_PDPA.pdf', '_PDPA.pdf') # Just in case
        
        # Also simple chars
        filename = filename.replace('\ufe6f', '').replace('%EF%B9%AF', '')
        
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        
        if os.path.exists(filepath):
            print(f"Skip (exists): {filename[:40]}...")
            success += 1
            continue
            
        print(f"DL: {filename[:40]}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=60) as r, open(filepath, 'wb') as f:
            f.write(r.read())
        success += 1
    except Exception as e:
        print(f"Failed: {filename[:30]}... - {e}")
        failed += 1

print(f"\nPage 25 done. Success: {success}, Failed: {failed}")
print()
print("Counting total PDF files...")
files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith('.pdf')]
print(f"Total PDF files: {len(files)}")
