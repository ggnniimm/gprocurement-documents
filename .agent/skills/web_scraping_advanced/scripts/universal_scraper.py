from playwright.sync_api import sync_playwright
import os
import time
import urllib.request
import urllib.parse
import ssl
import re
import argparse
import sys

# Generalized Scraper for PDF documents using Playwright & URL Prediction
# Designed to be adaptable for G-Procurement and similar sites.

def get_ssl_context():
    """Create a permissive SSL context for legacy sites."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def clean_filename(filename):
    """Encodes standard filename cleaning logic (unquote, spaces, PDPA suffix)."""
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

def run_scraper(base_url_template, start_page, end_page, download_dir, selector_script=None):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        
    ctx = get_ssl_context()
    
    print(f"Launching scanner for Pages {start_page} to {end_page}...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--no-sandbox"])
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        )
        page = context.new_page()

        for page_num in range(start_page, end_page + 1):
            print(f"\n--- Processing Page {page_num} ---")
            
            # 1. URL Prediction
            target_url = base_url_template.replace("{}", str(page_num))
            
            try:
                print(f"Navigating to: {target_url[:60]}...")
                page.goto(target_url, timeout=60000)
                page.wait_for_load_state("domcontentloaded")
                time.sleep(5) # Wait for dynamic loading (DataTable, etc.)
                
                # 2. Extract Links
                # If no custom selector script is provided, use default heuristic:
                # Find all <a> tags with .pdf in href and 'wcm/connect' (common in G-Procurement)
                if selector_script:
                    pdfs = page.evaluate(selector_script)
                else:
                    # Default Heuristic
                    pdfs = page.evaluate("""() => {
                        return Array.from(document.querySelectorAll('a'))
                            .filter(a => a.href.includes('.pdf'))
                            .map(a => a.href);
                    }""")
                
                print(f"Found {len(pdfs)} PDF links on Page {page_num}.")
                
                if len(pdfs) == 0:
                    print(f"WARNING: No links found for Page {page_num}.")
                    # Optional: Inspect content if needed
                    # print(page.content()[:500])

                # 3. Download Loop
                dl_count = 0
                for url in pdfs:
                    try:
                        # Extract basic filename from URL
                        path_part = urllib.parse.urlparse(url).path
                        raw_name = os.path.basename(path_part)
                        
                        # Clean it
                        filename = clean_filename(raw_name)
                        filepath = os.path.join(download_dir, filename)
                        
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
                        print(f"  Failed to download {url[:30]}...: {e}")
                        
                print(f"Processed {dl_count}/{len(pdfs)} files for Page {page_num}.")
                
            except Exception as e:
                print(f"Error processing Page {page_num}: {e}")
                
        print("\nBatch processing complete.")
        browser.close()

if __name__ == "__main__":
    # Example usage:
    # python3 universal_scraper.py --url_template "http://site.com/page={}" --start 1 --end 5 --dir "./downloads"
    
    parser = argparse.ArgumentParser(description="Universal PDF Scraper")
    parser.add_argument("--url_template", required=True, help="URL with {} placeholder for page number")
    parser.add_argument("--start", type=int, required=True, help="Start page number")
    parser.add_argument("--end", type=int, required=True, help="End page number")
    parser.add_argument("--dir", default="./downloads", help="Download directory")
    
    args = parser.parse_args()
    
    run_scraper(args.url_template, args.start, args.end, args.dir)
