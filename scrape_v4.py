from playwright.sync_api import sync_playwright
import json
import time

def run():
    print("Launching browser...")
    with sync_playwright() as p:
        # User headless=False to avoid bot detection and let user see what's happening if needed
        # args=['--start-maximized'] helps sometimes
        browser = p.chromium.launch(headless=False, args=["--no-sandbox"])
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        )
        page = context.new_page()
        
        # Try navigating to the new_index directly as seen in user state
        url = "https://www.gprocurement.go.th/new_index.html"
        print(f"Navigating to {url}...")
        
        try:
            page.goto(url, timeout=60000)
            page.wait_for_load_state("domcontentloaded")
            time.sleep(5) # Wait for JS to settle
            
            print(f"Title: {page.title()}")
            
            # Now we look for "บริการข้อมูล" (Information Service) -> "กฎหมายและระเบียบ" (Laws/Regulations) -> "ข้อหารือ"
            # Or "ศูนย์ข้อมูลความรู้"
            
            # Let's find all links and fuzzy match
            print("Scanning links...")
            links = page.evaluate("""() => {
                return Array.from(document.querySelectorAll('a')).map(a => ({txt: a.innerText, href: a.href}));
            }""")
            
            target_href = None
            
            # Priority 1: Direct "ข้อหารือ"
            for l in links:
                if "ข้อหารือ" in l['txt']:
                    print(f"Found 'ข้อหารือ' link: {l['txt']} -> {l['href']}")
                    target_href = l['href']
                    break
            
            # Priority 2: "กฎหมายและระเบียบ"
            if not target_href:
                for l in links:
                    if "กฎหมาย" in l['txt'] and "ระเบียบ" in l['txt']:
                        print(f"Found 'กฎหมาย' link: {l['txt']} -> {l['href']}")
                        target_href = l['href']
                        break
                        
            # Priority 3: "ข้อมูลความรู้"
            if not target_href:
                for l in links:
                     if "ความรู้" in l['txt']:
                        print(f"Found 'ความรู้' link: {l['txt']} -> {l['href']}")
                        target_href = l['href']
                        break

            if target_href:
                print(f"Clicking/Navigating to {target_href}...")
                page.goto(target_href)
                page.wait_for_load_state("domcontentloaded")
                time.sleep(3)
                
                # If we are at a submenu, look for "ข้อหารือ" again
                if "ข้อหารือ" not in page.title() and "ตอบข้อหารือ" not in page.title():
                    print("Checking for sub-link 'ข้อหารือ'...")
                    links = page.evaluate("""() => {
                        return Array.from(document.querySelectorAll('a')).map(a => ({txt: a.innerText, href: a.href}));
                    }""")
                    for l in links:
                        if "ตอบข้อหารือ" in l['txt'] or ("ข้อหารือ" in l['txt'] and "คณะกรรมการวินิจฉัย" in l['txt']):
                            print(f"Found sub-link: {l['txt']} -> {l['href']}")
                            page.goto(l['href'])
                            page.wait_for_load_state("domcontentloaded")
                            time.sleep(3)
                            break
            
            # Now assume we are on the list page.
            # We need to find Page 22.
            # Check if there is pagination
            print("Looking for pagination to Page 22...")
            
            # 1. Try to modify URL if it has page parameter (unlikely in complex apps, often POST or JS)
            # 2. Look for "Go to page" input
            
            # Let's verify we are on a list page by finding PDF links
            pdfs = page.evaluate("""() => {
                return Array.from(document.querySelectorAll('a'))
                    .filter(a => a.href.includes('.pdf') && a.href.includes('wcm/connect'))
                    .map(a => a.href);
            }""")
            print(f"Found {len(pdfs)} PDF links on current page.")
            
            if len(pdfs) == 0:
                print("No PDFs found. Dumping text to debug...")
                print(page.inner_text('body')[:500])
            else:
                # We have PDFs. Now we need to reach page 22.
                # If we can't find direct page jump, we might have to just dump all PDF links we see
                # and manual intervention might be needed if pagination is tricky.
                
                # But let's try to look for page input.
                # Common selector: input.wpc-results-page-input or similar
                
                # Try simple specific jump if possible
                pass
                
        except Exception as e:
            print(f"Error: {e}")
            page.screenshot(path="error.png")
            
        print("Closing browser...")
        browser.close()

if __name__ == "__main__":
    run()
