import os
import urllib.request
import urllib.parse
import ssl

DOWNLOAD_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement-documents"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

page_26_links = [
"https://www.gprocurement.go.th/wps/wcm/connect/8dff6c05-1035-42d7-9f88-0d1c9caf7f13/048345.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-8dff6c05-1035-42d7-9f88-0d1c9caf7f13-mVAyvsW",
"https://www.gprocurement.go.th/wps/wcm/connect/b98c8ab7-badc-463a-9d8b-de73b95655fa/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-046703.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-b98c8ab7-badc-463a-9d8b-de73b95655fa-mVAy4T-",
"https://www.gprocurement.go.th/wps/wcm/connect/bd216a92-edc9-4b72-9ef1-143f17a7050d/046113.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-bd216a92-edc9-4b72-9ef1-143f17a7050d-mVAyAu6",
"https://www.gprocurement.go.th/wps/wcm/connect/bc4597b5-af97-4233-9bc4-57d2a7972361/044197.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-bc4597b5-af97-4233-9bc4-57d2a7972361-mVAyT6K",
"https://www.gprocurement.go.th/wps/wcm/connect/59ae9b5c-481d-48b5-8a5d-b33b01c4dd37/040332.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-59ae9b5c-481d-48b5-8a5d-b33b01c4dd37-mVAyZS.",
"https://www.gprocurement.go.th/wps/wcm/connect/6bdde034-fcf1-4836-b6d3-3b4c482a5518/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-039278.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-6bdde034-fcf1-4836-b6d3-3b4c482a5518-mVAzcj9",
"https://www.gprocurement.go.th/wps/wcm/connect/bb72143d-278d-447a-b9c6-645ae0bee8c8/%E0%B8%81%E0%B8%84%2B%28%E0%B8%81%E0%B8%A7%E0%B8%88%29%2B0405.2-037999.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-bb72143d-278d-447a-b9c6-645ae0bee8c8-mVAz4YA",
"https://www.gprocurement.go.th/wps/wcm/connect/c6e6fdef-1b1c-4a56-beb4-633d0f5da36f/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-038032.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-c6e6fdef-1b1c-4a56-beb4-633d0f5da36f-mVAzpUr",
"https://www.gprocurement.go.th/wps/wcm/connect/e8e805d2-867b-40d7-878b-3bd10ae556c1/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-038035.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-e8e805d2-867b-40d7-878b-3bd10ae556c1-mVAzjb7",
"https://www.gprocurement.go.th/wps/wcm/connect/fc762f81-822f-424b-9615-87b73aae2d1f/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-034489.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-fc762f81-822f-424b-9615-87b73aae2d1f-mVAzQFc",
"https://www.gprocurement.go.th/wps/wcm/connect/1a63116f-645a-435f-a8fe-5fbbed7b13f0/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-033417.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-1a63116f-645a-435f-a8fe-5fbbed7b13f0-mVAyicb",
"https://www.gprocurement.go.th/wps/wcm/connect/84dbdf0e-43a1-4b39-be61-25f3f5c1ac1e/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-033197.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-84dbdf0e-43a1-4b39-be61-25f3f5c1ac1e-mVAzwqL",
"https://www.gprocurement.go.th/wps/wcm/connect/49ef6eba-6946-4311-b70e-f7082e751abe/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-032216.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-49ef6eba-6946-4311-b70e-f7082e751abe-mVAzKsj",
"https://www.gprocurement.go.th/wps/wcm/connect/be01d00e-1444-4a4b-951d-c154780c8163/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-030679.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-be01d00e-1444-4a4b-951d-c154780c8163-mVAzCqq",
"https://www.gprocurement.go.th/wps/wcm/connect/60193b75-53b6-4f5a-bc72-b78c34871879/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-030184.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-60193b75-53b6-4f5a-bc72-b78c34871879-mVAzWPJ",
"https://www.gprocurement.go.th/wps/wcm/connect/d9f15498-58b9-42b2-a592-62b772ce7abe/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-028748.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-d9f15498-58b9-42b2-a592-62b772ce7abe-mVAA7Fd",
"https://www.gprocurement.go.th/wps/wcm/connect/00108df8-dd08-4f4c-9539-a9b745956752/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-028463.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-00108df8-dd08-4f4c-9539-a9b745956752-mVAA242",
"https://www.gprocurement.go.th/wps/wcm/connect/976a322f-4a19-4996-8223-ad89ba52fecc/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-028466.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-976a322f-4a19-4996-8223-ad89ba52fecc-mVAAdu3",
"https://www.gprocurement.go.th/wps/wcm/connect/31996585-43fb-4676-80b8-236e46dcae56/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-028035.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-31996585-43fb-4676-80b8-236e46dcae56-mVAqoMr",
"https://www.gprocurement.go.th/wps/wcm/connect/daf6b59d-65ce-4f0d-8f8f-fd9ad638e894/%E0%B8%81%E0%B8%84+%28%E0%B8%81%E0%B8%A7%E0%B8%88%29+0405.2-027707.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE-daf6b59d-65ce-4f0d-8f8f-fd9ad638e894-mVFbTZR"
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print(f"Downloading {len(page_26_links)} files from Page 26...")

success = 0
failed = 0
for url in page_26_links:
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

print(f"\nPage 26 done. Success: {success}, Failed: {failed}")
print()
print("Counting total PDF files...")
files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith('.pdf')]
print(f"Total PDF files: {len(files)}")
