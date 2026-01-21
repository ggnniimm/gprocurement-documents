from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://www.gprocurement.go.th/wps/portal/egp/Regulation/Diagnosis_Diag_Committee/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziPTx8HA29nQ38LFwCTQ0CnYNcfFxMQ409_Uz1w8EKDHAARwP9KGL041EQhd_4cP0osBJfQ3cjQ2dnA19_TzdzA0dzUwPfAFNLAxMPYwwFYcZmQAUBvs7-gR4GBs6GUAV4LCnIDY0wyPRUBACGPToN/dz/d5/L0lDUmlTUSEhL3dHa0FKRnNBLzROV3FpQSEhL3Ro/p0/IZ7_HHLA1KC0N8DQ50QCRDLD5U3A07=CZ6_HHLA1KC0N8DQ50QCRDLD5U3IN5=MEns_Z7_HHLA1KC0N8DQFB50QFBCRDLD5U3A07_WCM_Page.57468948-8b65-47df-bc89-0af71aed3696!21=CTX!QCPegp_site_thQCPegpQCPRegulationQCPDiagnosis_Diagnosis_CommitteeQCP79f65263-0717-450c-9072-a5dad79c2abe=ns_Z7_HHLA1KC0N8DQFB50QFBCRDLD5U3A07_WCM_PreviousPageSize.57468948-8b65-47df-bc89-0af71aed3696!20=WCM_PI!1==/p0/IZ7_HHLA1KC0N8DQ50QCRDLD5U3A07=CZ6_HHLA1KC0N8DQ50QCRDLD5U3IN5=MEns_Z7_HHLA1KC0N8DQFB50QFBCRDLD5U3A07_WCM_Page.57468948-8b65-47df-bc89-0af71aed3696!22=CTX!QCPegp_site_thQCPegpQCPRegulationQCPDiagnosis_Diagnosis_CommitteeQCP79f65263-0717-450c-9072-a5dad79c2abe=WCM_PI!1==/#Z7_HHLA1KC0N8DQ50QCRDLD5U3A07"

def run():
    print("Launching browser (headless=False)...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--no-sandbox"])
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        )
        page = context.new_page()
        
        print(f"Navigating to provided URL...")
        try:
            page.goto(TARGET_URL, timeout=60000)
            page.wait_for_load_state("domcontentloaded")
            time.sleep(5)
            
            # Scroll to bottom
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            
            # Dump ALL links to see what we missed
            links = page.evaluate("""() => {
                return Array.from(document.querySelectorAll('a')).map(a => ({txt: a.innerText, href: a.href}));
            }""")
            
            print(f"Total links on page: {len(links)}")
            
            # Filter specifically for likely document files (pdf, doc, zip, etc or just wcm/connect)
            candidates = []
            for l in links:
                href = l['href']
                if 'wcm/connect' in href:
                    candidates.append(l)
            
            print(f"Found {len(candidates)} candidates with 'wcm/connect'.")
            for c in candidates:
                print(f" - {c['txt']} -> {c['href']}")

        except Exception as e:
            print(f"Error: {e}")
            
        print("Closing browser...")
        browser.close()

if __name__ == "__main__":
    run()
