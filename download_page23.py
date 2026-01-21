import os
import urllib.request
import urllib.parse
import ssl

DOWNLOAD_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement_downloads"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

page_23_links = [
"https://www.gprocurement.go.th/wps/wcm/connect/87974340-7c77-4c2c-9c9e-e878f2f19148/%E0%B8%AA%E0%B8%B3%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%9A%E0%B8%A3%E0%B8%B4%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%AB%E0%B8%99%E0%B8%B5%E0%B9%89%E0%B8%AA%E0%B8%B2%E0%B8%98%E0%B8%B2%E0%B8%A3%E0%B8%93%E0%B8%B0+%E0%B8%82%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B9%81%E0%B8%99%E0%B8%A7%E0%B8%97%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%97%E0%B8%B3%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2%E0%B9%83%E0%B8%99%E0%B8%A3%E0%B8%B0%E0%B8%9A%E0%B8%9A%E0%B8%AD%E0%B8%B4%E0%B9%80%E0%B8%A5%E0%B9%87%E0%B8%81%E0%B8%97%E0%B8%A3%E0%B8%AD%E0%B8%99%E0%B8%B4%E0%B8%81%E0%B8%AA%E0%B9%8C.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-87974340-7c77-4c2c-9c9e-e878f2f19148-noCp3vb",
"https://www.gprocurement.go.th/wps/wcm/connect/b518bcdc-457a-4b54-9bc4-7d20534450ff/%E0%B9%81%E0%B8%81%E0%B9%89%E0%B8%A5%E0%B8%87%E0%B9%80%E0%B8%A7%E0%B9%87%E0%B8%9A+%E0%B8%9E%E0%B8%B5%E0%B9%88%E0%B8%A3%E0%B8%B4%E0%B8%99.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-b518bcdc-457a-4b54-9bc4-7d20534450ff-nmRBs-r",
"https://www.gprocurement.go.th/wps/wcm/connect/3caabd2a-7dee-40c6-96eb-1f41e40b3134/%E0%B9%81%E0%B8%81%E0%B9%89%E0%B8%A5%E0%B8%87%E0%B9%80%E0%B8%A7%E0%B9%87%E0%B8%9A+%E0%B9%81%E0%B8%AD%E0%B8%A3%E0%B9%8C.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-3caabd2a-7dee-40c6-96eb-1f41e40b3134-nmRBIzJ",
"https://www.gprocurement.go.th/wps/wcm/connect/77a98de7-3cd4-4d9e-b8ce-5b27ac571f34/%E0%B9%81%E0%B8%99%E0%B8%A7%E0%B8%95%E0%B8%AD%E0%B8%9A%E0%B8%81%E0%B8%A3%E0%B8%93%E0%B8%B5%E0%B9%80%E0%B8%8A%E0%B9%88%E0%B8%B2%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%97%E0%B8%B3%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%95%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%97%E0%B8%B3%E0%B8%95%E0%B8%B2%E0%B8%A1%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B9%80%E0%B8%8A%E0%B9%88%E0%B8%B2%E0%B8%95%E0%B8%B2%E0%B8%A1%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A8+%E0%B8%81%E0%B8%99%E0%B8%9A.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-77a98de7-3cd4-4d9e-b8ce-5b27ac571f34-nmcnDfc",
"https://www.gprocurement.go.th/wps/wcm/connect/42441e39-32e7-44ef-9f9e-6cf285c0e6e6/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A7%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%84%E0%B8%B7%E0%B8%99%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%81%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2+0405.4_39563.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-42441e39-32e7-44ef-9f9e-6cf285c0e6e6-nOmEmmO",
"https://www.gprocurement.go.th/wps/wcm/connect/d84b6863-e9bf-42aa-968d-fa0acbdccba1/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%95%E0%B8%B1%E0%B8%94%E0%B8%88%E0%B8%B3%E0%B8%AB%E0%B8%99%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%84%E0%B8%AD%E0%B8%A1%E0%B8%9E%E0%B8%B4%E0%B8%A7%E0%B9%80%E0%B8%95%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%AA%E0%B9%88%E0%B8%A7%E0%B8%99%E0%B8%9A%E0%B8%B8%E0%B8%84%E0%B8%84%E0%B8%A5.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-d84b6863-e9bf-42aa-968d-fa0acbdccba1-nOmDQq9",
"https://www.gprocurement.go.th/wps/wcm/connect/9110c3cd-a043-4074-b992-68fc57df3ba3/001_%E0%B8%81%E0%B8%A7%E0%B8%88_16571_160463_%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B9%81%E0%B8%99%E0%B8%A7%E0%B8%97%E0%B8%B2%E0%B8%87%E0%B8%9B%E0%B8%8F%E0%B8%B4%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B9%83%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%8B%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%88%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%AF+PDPA.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-9110c3cd-a043-4074-b992-68fc57df3ba3-piXL0kL",
"https://www.gprocurement.go.th/wps/wcm/connect/3322f661-3a8e-43fe-bed8-9412f7d706c6/%E0%B8%A5%E0%B8%87%E0%B9%80%E0%B8%A7%E0%B9%87%E0%B8%9A%E0%B9%81%E0%B8%81%E0%B9%89+%E0%B9%81%E0%B8%9A%E0%B9%88%E0%B8%87%E0%B8%8B%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B9%81%E0%B8%9A%E0%B9%88%E0%B8%87%E0%B8%88%E0%B9%89%E0%B8%B2%E0%B8%87.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-3322f661-3a8e-43fe-bed8-9412f7d706c6-ngvqSD.",
"https://www.gprocurement.go.th/wps/wcm/connect/d663b36f-1ea0-4e01-929f-f3429d8440e4/%E0%B8%A1.%E0%B8%AD%E0%B8%B5%E0%B8%AA%E0%B8%B2%E0%B8%99%2Bpdf.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-d663b36f-1ea0-4e01-929f-f3429d8440e4-n1W68Tr",
"https://www.gprocurement.go.th/wps/wcm/connect/5a734d6b-7378-472c-befb-27b2b1b7b4bc/PDF%2B%E0%B8%95%E0%B8%AD%E0%B8%9A%2B%E0%B8%AA%E0%B8%9B.%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B8%97%E0%B8%A3%E0%B8%A7%E0%B8%87%E0%B8%97%E0%B8%A3%E0%B8%B1%E0%B8%9E%E0%B8%A2%E0%B8%B2%E0%B8%81%E0%B8%A3%E0%B8%98%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%8A%E0%B8%B2%E0%B8%95%E0%B8%B4%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%AA%E0%B8%B4%E0%B9%88%E0%B8%87%E0%B9%81%E0%B8%A7%E0%B8%94%E0%B8%A5%E0%B9%89%E0%B8%AD%E0%B8%A1.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-5a734d6b-7378-472c-befb-27b2b1b7b4bc-n1W7jOY",
"https://www.gprocurement.go.th/wps/wcm/connect/8a471a93-d138-4292-9a15-a8199dd3b07e/%E0%B9%81%E0%B8%81%E0%B9%89%E0%B8%A5%E0%B8%87%E0%B9%80%E0%B8%A7%E0%B9%87%E0%B8%9A+%E0%B8%84%E0%B8%B8%E0%B8%93%E0%B8%AA%E0%B8%A1%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%A2%E0%B8%B7%E0%B9%88%E0%B8%99%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B9%80%E0%B8%AA%E0%B8%99%E0%B8%AD.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-8a471a93-d138-4292-9a15-a8199dd3b07e-ngvrmgZ",
"https://www.gprocurement.go.th/wps/wcm/connect/1e8eef83-8c0d-4bab-ad9c-f1f04aad6e88/1780.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-1e8eef83-8c0d-4bab-ad9c-f1f04aad6e88-nOmCJJi",
"https://www.gprocurement.go.th/wps/wcm/connect/b7dcce4e-0d1e-4e2a-a842-b06d4524ed61/%E0%B8%AB%E0%B8%99%E0%B8%B1%E0%B8%87%E0%B8%AA%E0%B8%B7%E0%B8%AD%E0%B8%95%E0%B8%AD%E0%B8%9A.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-b7dcce4e-0d1e-4e2a-a842-b06d4524ed61-nOmBJsr",
"https://www.gprocurement.go.th/wps/wcm/connect/2be52c84-049f-43b3-a6ff-891f54e797f9/59970.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-2be52c84-049f-43b3-a6ff-891f54e797f9-nOmGnf-",
"https://www.gprocurement.go.th/wps/wcm/connect/c8b76191-940f-4355-a68e-b94d2c921d96/59627.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-c8b76191-940f-4355-a68e-b94d2c921d96-nOmFHhg",
"https://www.gprocurement.go.th/wps/wcm/connect/6e7451d7-10d3-4a5b-9cc7-80c1177fa098/25620430753_V1.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-6e7451d7-10d3-4a5b-9cc7-80c1177fa098-mYThH7p",
"https://www.gprocurement.go.th/wps/wcm/connect/f33a3c34-af61-4772-b70d-88f0af68e4e9/25620425187_V1+%281%29.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-f33a3c34-af61-4772-b70d-88f0af68e4e9-mYThZ5j",
"https://www.gprocurement.go.th/wps/wcm/connect/1762bce1-18bb-4f3d-b304-e2ab5bb69d4a/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%81%E0%B8%B3%E0%B8%AB%E0%B8%99%E0%B8%94%E0%B8%84%E0%B9%88%E0%B8%B2%E0%B8%9B%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B9%83%E0%B8%99%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2%E0%B8%88%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B9%88%E0%B8%AD%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87+%28%E0%B8%A5%E0%B8%B4%E0%B8%82%E0%B8%B4%E0%B8%95%29.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-1762bce1-18bb-4f3d-b304-e2ab5bb69d4a-mYTiphp",
"https://www.gprocurement.go.th/wps/wcm/connect/67653f7d-5a67-4881-bc23-3a17399231da/%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B7%E0%B8%AD%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%94%E0%B8%B3%E0%B9%80%E0%B8%99%E0%B8%B4%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%88%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%9B%E0%B8%A3%E0%B8%B6%E0%B8%81%E0%B8%A9%E0%B8%B2+%E0%B8%95%E0%B8%B2%E0%B8%A1%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%9A%E0%B8%B5%E0%B8%A2%E0%B8%9A%E0%B8%81%E0%B8%A3%E0%B8%B0%E0%B8%97%E0%B8%A3%E0%B8%A7%E0%B8%87%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%84%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B8%A7%E0%B9%88%E0%B8%B2%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%8B%E0%B8%B7%E0%B9%89%E0%B8%AD%E0%B8%88%E0%B8%B1%E0%B8%94%E0%B8%88%E0%B9%89%E0%B8%B2%E0%B8%87%E0%B8%AF.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-67653f7d-5a67-4881-bc23-3a17399231da-mYTiQX0"
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print(f"Downloading {len(page_23_links)} files from Page 23...")

success = 0
failed = 0
for url in page_23_links:
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

print(f"\nPage 23 done. Success: {success}, Failed: {failed}")
print()
print("Counting total files in download directory...")
files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith('.pdf')]
print(f"Total PDF files: {len(files)}")
