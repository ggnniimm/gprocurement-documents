from playwright.sync_api import sync_playwright
import os
import time
import urllib.request
import urllib.parse
import ssl
import re

DOWNLOAD_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement-documents"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# SSL Context
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Base URL Template (We replace !26 with !{page_num})
BASE_URL_TEMPLATE = "https://www.gprocurement.go.th/wps/portal/egp/Regulation/Diagnosis_Diag_Committee/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziPTx8HA29nQ38LFwCTQ0CnYNcfFxMQ409_Uz1w8EKDHAARwP9KGL041EQhd_4cP0osBJfQ3cjQ2dnA19_TzdzA0dzUwPfAFNLAxMPYwwFYcZmQAUBvs7-gR4GBs6GUAV4LCnIDY0wyPRUBACGPToN/dz/d5/L0lDUmlTUSEhL3dHa0FKRnNBLzROV3FpQSEhL3Ro/p0/IZ7_HHLA1KC0N8DQ50QCRDLD5U3A07=CZ6_HHLA1KC0N8DQ50QCRDLD5U3IN5=MEns_Z7_HHLA1KC0N8DQFB50QFBCRDLD5U3A07_WCM_Page.57468948-8b65-47df-bc89-0af71aed3696!21=CTX!QCPegp_site_thQCPegpQCPRegulationQCPDiagnosis_Diagnosis_CommitteeQCP79f65263-0717-450c-9072-a5dad79c2abe=ns_Z7_HHLA1KC0N8DQFB50QFBCRDLD5U3A07_WCM_PreviousPageSize.57468948-8b65-47df-bc89-0af71aed3696!20=WCM_PI!1==/p0/IZ7_HHLA1KC0N8DQ50QCRDLD5U3A07=CZ6_HHLA1KC0N8DQ50QCRDLD5U3IN5=MEns_Z7_HHLA1KC0N8DQFB50QFBCRDLD5U3A07_WCM_Page.57468948-8b65-47df-bc89-0af71aed3696!{}=CTX!QCPegp_site_thQCPegpQCPRegulationQCPDiagnosis_Diagnosis_CommitteeQCP79f65263-0717-450c-9072-a5dad79c2abe=WCM_PI!1==/#Z7_HHLA1KC0N8DQ50QCRDLD5U3A07"

def clean_filename(filename):
    filename = urllib.parse.unquote(filename)
    filename = filename.replace('+', '_').replace(' ', '_').replace('__', '_')
    filename = re.sub(r"[\s_+]*\(?PDPA\)?", "_PDPA", filename)
    filename = filename.replace('\ufe6f', '').replace('%EF%B9%AF', '')
    
    # Ensure .pdf extension
    if not filename.lower().endswith('.pdf'):
        if filename.lower().endswith('_pdf'):
            filename = filename[:-4] + '.pdf'
        else:
             filename += '.pdf'
             
    filename = filename.replace("_.pdf", ".pdf")
    return filename

def run():
    print("Launching browser for batch processing Pages 27-31...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--no-sandbox"])
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        )
        page = context.new_page()

        for page_num in range(27, 32): # 27, 28, 29, 30, 31
            print(f"\n--- Processing Page {page_num} ---")
            target_url = BASE_URL_TEMPLATE.format(page_num)
            
            try:
                print(f"Navigating to Page {page_num}...")
                page.goto(target_url, timeout=60000)
                page.wait_for_load_state("domcontentloaded")
                time.sleep(5) # Wait for dynamic load
                
                # Check title
                # print(f"Title: {page.title()}")
                
                # Scrape Links
                pdfs = page.evaluate("""() => {
                    return Array.from(document.querySelectorAll('a'))
                        .filter(a => a.href.includes('.pdf') && a.href.includes('wcm/connect'))
                        .map(a => a.href);
                }""")
                
                print(f"Found {len(pdfs)} PDF links on Page {page_num}.")
                
                if len(pdfs) == 0:
                    print(f"WARNING: No links found for Page {page_num}. Stopping batch.")
                    break

                # Download Files
                dl_count = 0
                for url in pdfs:
                    try:
                        path_part = urllib.parse.urlparse(url).path
                        raw_name = os.path.basename(path_part)
                        filename = clean_filename(raw_name)
                        filepath = os.path.join(DOWNLOAD_DIR, filename)
                        
                        if os.path.exists(filepath):
                            print(f"  Skip (exists): {filename[:30]}...")
                            dl_count += 1
                            continue
                            
                        print(f"  DL: {filename[:30]}...")
                        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                        with urllib.request.urlopen(req, context=ctx, timeout=60) as r, open(filepath, 'wb') as f:
                            f.write(r.read())
                        dl_count += 1
                    except Exception as e:
                        print(f"  Failed: {url[:30]}... - {e}")
                        
                print(f"Successfully processed {dl_count}/{len(pdfs)} files for Page {page_num}.")
                
            except Exception as e:
                print(f"Error processing Page {page_num}: {e}")
                
        print("\nBatch processing complete.")
        browser.close()

if __name__ == "__main__":
    run()
