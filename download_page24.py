import os
import urllib.request
import urllib.parse
import ssl

DOWNLOAD_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement_downloads"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

page_24_links = [
"https://www.gprocurement.go.th/wps/wcm/connect/ddcb111b-42f2-4476-a719-296702910f8e/25620416516_V1.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-ddcb111b-42f2-4476-a719-296702910f8e-mYTiYqE",
"https://www.gprocurement.go.th/wps/wcm/connect/9f7375a3-b4c7-4414-900f-3c71f6f13414/25620185559_V1.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-9f7375a3-b4c7-4414-900f-3c71f6f13414-nOmwgSS",
"https://www.gprocurement.go.th/wps/wcm/connect/f85accf3-9083-4a49-b4f2-2719daeaa67b/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%9E%29+0405.4-56635.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-f85accf3-9083-4a49-b4f2-2719daeaa67b-mYTj4PT",
"https://www.gprocurement.go.th/wps/wcm/connect/de19e770-466e-4097-b1b1-c69214e1acad/25620290673_V1.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-de19e770-466e-4097-b1b1-c69214e1acad-mYTix57",
"https://www.gprocurement.go.th/wps/wcm/connect/e0ddcac6-80f1-484a-85a5-632eaabfee16/25620221079_V1.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-e0ddcac6-80f1-484a-85a5-632eaabfee16-mYThQ3o",
"https://www.gprocurement.go.th/wps/wcm/connect/f4dcf5b4-36d2-4f42-b8e6-b83ebe4b6bc7/25620143422_V1.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-f4dcf5b4-36d2-4f42-b8e6-b83ebe4b6bc7-mYTi3xx",
"https://www.gprocurement.go.th/wps/wcm/connect/dde5d700-4d23-45c5-bb62-17a52f229cff/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-16743.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-dde5d700-4d23-45c5-bb62-17a52f229cff-mVABFpQ",
"https://www.gprocurement.go.th/wps/wcm/connect/efa701e0-3514-4217-9adf-941774667125/%E0%B8%81%E0%B8%84%28%E0%B8%81%E0%B8%A7%E0%B8%88%290405.2-16645.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-efa701e0-3514-4217-9adf-941774667125-mVArMk0",
"https://www.gprocurement.go.th/wps/wcm/connect/76f42eee-5a11-4798-923b-eb7a06d067fd/%E0%B8%81%E0%B8%84%28%E0%B8%81%E0%B8%A7%E0%B8%88%290405.2-16641.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-76f42eee-5a11-4798-923b-eb7a06d067fd-mVArTSN",
"https://www.gprocurement.go.th/wps/wcm/connect/3c93e8fc-2911-4f66-aa58-a960f703ae9c/16328.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-3c93e8fc-2911-4f66-aa58-a960f703ae9c-mVAtrRJ",
"https://www.gprocurement.go.th/wps/wcm/connect/1f246bab-5fba-418d-aaab-29f7ce941ed1/%E0%B8%81%E0%B8%84%28%E0%B8%81%E0%B8%A7%E0%B8%88%290405.2-16104.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-1f246bab-5fba-418d-aaab-29f7ce941ed1-mVAryzG",
"https://www.gprocurement.go.th/wps/wcm/connect/bcf881ec-d3d7-442a-9fc4-743400fd814c/%E0%B8%81%E0%B8%84%28%E0%B8%81%E0%B8%A7%E0%B8%88%290405.2-16101.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-bcf881ec-d3d7-442a-9fc4-743400fd814c-mVAs0hY",
"https://www.gprocurement.go.th/wps/wcm/connect/fd2fa16a-de80-4215-a032-7450093b9265/%E0%B8%81%E0%B8%84%28%E0%B8%81%E0%B8%A7%E0%B8%88%290405.2-16112.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-fd2fa16a-de80-4215-a032-7450093b9265-mVArqB1",
"https://www.gprocurement.go.th/wps/wcm/connect/49d78dfe-a130-482b-996e-339861938004/%E0%B8%81%E0%B8%84%28%E0%B8%81%E0%B8%A7%E0%B8%88%290405.2-015891.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-49d78dfe-a130-482b-996e-339861938004-mVArhcL",
"https://www.gprocurement.go.th/wps/wcm/connect/d2aa4365-7686-44f3-bafd-9cf8b4e7a957/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-15231.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-d2aa4365-7686-44f3-bafd-9cf8b4e7a957-mVAq-.1",
"https://www.gprocurement.go.th/wps/wcm/connect/c6d77bb7-f219-4886-aa3a-ba4ac35349dc/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%290405.2-15227.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-c6d77bb7-f219-4886-aa3a-ba4ac35349dc-mVAs7Nc",
"https://www.gprocurement.go.th/wps/wcm/connect/0eb7fe75-0373-4965-a568-a94bc1d0e40f/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-15230.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-0eb7fe75-0373-4965-a568-a94bc1d0e40f-mVAsdXV",
"https://www.gprocurement.go.th/wps/wcm/connect/9033b207-4e0b-4f8b-8488-6e81e0e31551/11688.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-9033b207-4e0b-4f8b-8488-6e81e0e31551-mVAuty5",
"https://www.gprocurement.go.th/wps/wcm/connect/668b86b2-de67-4ff5-bfb9-1532ab9c6a84/11673.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-668b86b2-de67-4ff5-bfb9-1532ab9c6a84-mVAuziS",
"https://www.gprocurement.go.th/wps/wcm/connect/c5fc5778-9720-4eed-a514-ac9e0e0d9c73/11498.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-c5fc5778-9720-4eed-a514-ac9e0e0d9c73-mVAulFa"
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print(f"Downloading {len(page_24_links)} files from Page 24...")

success = 0
failed = 0
for url in page_24_links:
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

print(f"\nPage 24 done. Success: {success}, Failed: {failed}")
print()
print("Counting total files in download directory...")
files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith('.pdf')]
print(f"Total PDF files: {len(files)}")
