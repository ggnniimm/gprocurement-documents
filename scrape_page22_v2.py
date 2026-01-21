from playwright.sync_api import sync_playwright
import re
import time
import json

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # Set to True for speed/headless
        page = browser.new_page()
        
        print("Navigating to homepage...")
        page.goto("https://www.gprocurement.go.th/", timeout=60000)
        page.wait_for_load_state("networkidle")
        
        # Check if splash page
        if "เข้าสู่" in page.inner_text('body'):
            print("Found Splash Page. Clicking Enter...")
            try:
                # Click the link that contains "เข้าสู่"
                with page.expect_navigation():
                    page.click('text=เข้าสู่เว็บไซต์', timeout=10000)
                print("Entered site.")
            except Exception as e:
                print(f"Error clicking enter: {e}. Dumping links:")
                links = page.evaluate("Array.from(document.querySelectorAll('a')).map(a => ({txt: a.innerText, href: a.href}))")
                for l in links:
                    if "เข้าสู่" in l['txt']:
                        print(f" - {l['txt']} -> {l['href']}")
                        page.goto(l['href'])
                        break
        
        page.wait_for_load_state("networkidle")
        print(f"Page Title: {page.title()}")
        
        # Now searching for "บริการข้อมูล" or "กฎหมาย" or "ข้อหารือ"
        # Often under "บริการข้อมูล" (Information Service) -> "กฎหมายและระเบียบ" (Laws/Regs) -> "ข้อหารือ" (Consultation)
        
        # Let's try to click "บริการข้อมูล" if present
        try:
             # Use a selector that matches text roughly
             pass
        except:
             pass

        # Use the scraping approach to find the link
        print("Scanning for 'ข้อหารือ' link...")
        links = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('a')).map(a => ({txt: a.innerText, href: a.href}));
        }""")
        
        target_link = None
        for l in links:
             if "ข้อหารือ" in l['txt'] or "ตอบข้อหารือ" in l['txt']:
                 target_link = l['href']
                 print(f"Found match: {l['txt']} -> {target_link}")
                 break
        
        if target_link:
            print(f"Navigating to {target_link}")
            page.goto(target_link)
            page.wait_for_load_state("networkidle")
            
            # Now we are on the list page.
            # Need to paginate to Page 22.
            # Assuming there's a pagination input or links.
            print("Looking for pagination...")
            
            # Take a screenshot to verify where we are (saved to disk, user won't see unless I embed)
            # page.screenshot(path="page_view.png")
            
            # Simple dumb wait to let JS load
            time.sleep(5)
            
            # Try to grab ALL PDF links on this page
            pdfs = page.evaluate("""() => {
                return Array.from(document.querySelectorAll('a'))
                    .filter(a => a.href.includes('.pdf') && a.href.includes('wcm/connect'))
                    .map(a => a.href);
            }""")
            print(f"Found {len(pdfs)} PDFs on first page.")
            
            # If we need Page 22, we need to paginate.
            # Let's try to set the page number if there is an input box.
            # Selector guess: input[title='Page Number'] or similar
            
            # For now, just print the PDF links of page 1 to prove it works.
            # Then I will refine.
            print(json.dumps(pdfs))
            
        else:
            print("Could not find 'ข้อหารือ' link.")
            # Print menu items
            print("Menu items found:")
            for l in links[:20]:
                print(f" - {l['txt']}")

        browser.close()

if __name__ == "__main__":
    run()
