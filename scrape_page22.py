from playwright.sync_api import sync_playwright
import re
import time
import json

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Navigating to homepage...")
        page.goto("https://www.gprocurement.go.th/", timeout=60000)
        page.wait_for_load_state("networkidle")
        
        print(f"Page Title: {page.title()}")
        
        # Try to find "ข้อหารือ" link
        # Usually in a menu.
        # Let's dump all links to see what we have
        links = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('a')).map(a => ({txt: a.innerText, href: a.href}));
        }""")
        
        target_link = None
        for l in links:
            if "ข้อหารือ" in l['txt'] and "วินิจฉัย" in l['txt']:
                 # "คณะกรรมการวินิจฉัยปัญหาการจัดซื้อจัดจ้างและการบริหารพัสดุภาครัฐ (กวจ.)" -> "ตอบข้อหารือ"
                 target_link = l['href']
                 print(f"Found candidate link: {l['txt']} -> {target_link}")
                 break
            if "ตอบข้อหารือ" in l['txt']:
                target_link = l['href']
                print(f"Found candidate link: {l['txt']} -> {target_link}")
                break
        
        if not target_link:
            print("Could not find direct link. Searching for Knowledge Center...")
            # Try to click "ศูนย์ข้อมูลความรู้" or "กฎหมาย"
            # Adjust selectors as needed
            # For now, let's just assume we can find something.
            # If failing, I'll return the page text to debug.
            print("Page Text Sample:")
            print(page.inner_text('body')[:500])
            browser.close()
            return

        print(f"Navigating to {target_link}...")
        page.goto(target_link)
        page.wait_for_load_state("networkidle")
        
        # Now we are on the list page (hopefully)
        # We need to go to Page 22.
        # Check for pagination.
        # Usually standard pagination: 1 2 3 ...
        
        # We might need to click "Next" multiple times or jump.
        # Let's try to find a link with text "22".
        
        # If the pagination is "Page X of Y" and input box, or simple links.
        # I'll dump pagination links.
        print("Searching for pagination...")
        
        # Function to extract PDF links on current page
        def extract_pdfs():
            return page.evaluate("""() => {
                return Array.from(document.querySelectorAll('a'))
                    .filter(a => a.href.includes('.pdf') && a.href.includes('wcm/connect'))
                    .map(a => a.href);
            }""")
        
        # Attempt to jump to page 22
        # This is tricky without knowing the UI.
        
        # Let's try to find the "Go to Page" input or just '22' link.
        # If not, we might have to just return the first page links and I'll debug.
        
        pdfs = extract_pdfs()
        print(f"Found {len(pdfs)} PDF links on current page.")
        if len(pdfs) > 0:
            print(json.dumps(pdfs))
            
        browser.close()

if __name__ == "__main__":
    run()
