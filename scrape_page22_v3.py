from playwright.sync_api import sync_playwright
import json

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Try direct link
        url = "https://www.gprocurement.go.th/go/front/enter/knowledge_center"
        print(f"Navigating to {url}...")
        try:
            page.goto(url, timeout=30000)
            page.wait_for_load_state("networkidle")
            print(f"Title: {page.title()}")
            
            # Check if we are redirected to splash
            if "เข้าสู่" in page.inner_text('body'):
                 print("Redirected to splash. Clicking Enter...")
                 page.click('text=เข้าสู่เว็บไซต์', timeout=10000)
                 page.wait_for_load_state("networkidle")
            
            print(f"Post-Enter Title: {page.title()}")
            
            # Dump links
            links = page.evaluate("""() => {
                return Array.from(document.querySelectorAll('a')).map(a => ({txt: a.innerText, href: a.href}));
            }""")
            
            found_target = False
            for l in links:
                if "ข้อหารือ" in l['txt']:
                    print(f"FOUND: {l['txt']} -> {l['href']}")
                    found_target = True
            
            if not found_target:
                print("No 'ข้อหารือ' link found. Dumping first 20 links:")
                for l in links[:20]:
                    print(f" - {l['txt']} -> {l['href']}")
                    
        except Exception as e:
            print(f"Error: {e}")
            
        browser.close()

if __name__ == "__main__":
    run()
