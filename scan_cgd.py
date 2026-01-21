from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # CGD website
        url = "https://www.cgd.go.th/"
        print(f"Navigating to {url}...")
        try:
            page.goto(url, timeout=30000)
            page.wait_for_load_state("networkidle")
            
            print(f"Title: {page.title()}")
            
            # Search for link to gprocurement consultation
            links = page.evaluate("""() => {
                return Array.from(document.querySelectorAll('a')).map(a => ({txt: a.innerText, href: a.href}));
            }""")
            
            for l in links:
                if "ข้อหารือ" in l['txt'] or "วินิจฉัย" in l['txt']:
                    print(f"FOUND candidate on CGD: {l['txt']} -> {l['href']}")
                    
        except Exception as e:
            print(f"Error: {e}")
            
        browser.close()

if __name__ == "__main__":
    run()
