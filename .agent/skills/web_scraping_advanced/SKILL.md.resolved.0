---
name: Advanced Web Scraping
description: A robust workflow for scraping modern, dynamic websites using Playwright and Python. best suited for sites with anti-scraping measures, dynamic content types (React/Angular), or predictable URL patterns.
---

# Advanced Web Scraping Skill

This skill provides a standardized approach to scraping challenging websites, extracting file links (like PDFs), and downloading them with consistent naming. It is designed to handle:
*   **Dynamic Content**: Uses `Playwright` to render JavaScript and wait for DOM readiness.
*   **Anti-Bot Measures**: Uses a real browser instance (headless or headed) to bypass basic static analysis.
*   **URL Prediction**: efficiently iterates through page numbers when navigation patterns are known.
*   **Robust Downloading**: Handles basic network errors, SSL issues, and existing file skipping.
*   **Clean Naming**: Enforces a strict filename convention to avoid shell issues and duplicates.

## Directory Structure
```
web_scraping_advanced/
├── SKILL.md                # This file
├── scripts/
│   ├── universal_scraper.py      # Main scraping script
│   └── standardize_filenames.py  # Utility to clean filenames
```

## Usage

### 1. Scraping & Downloading
The `universal_scraper.py` script is the core tool. You need to configure it (or pass arguments if adapted) for the target site.

**Key Parameters to Configure in Script:**
*   `BASE_URL_TEMPLATE`: The URL with a placeholder `{}` for logic (e.g., page IDs).
*   `DOWNLOAD_DIR`: Where files go.
*   `SELECTOR_LOGIC`: The `page.evaluate` function that finds links.

**Run Command:**
```bash
python3 scripts/universal_scraper.py
```

### 2. Standardization
After downloading, run the standardization script to clean up messy filenames (URL encoded characters, spaces, special chars).

**Run Command:**
```bash
python3 scripts/standardize_filenames.py
```

## Best Practices
1.  **Always Wait**: Use `page.wait_for_load_state("domcontentloaded")` and `time.sleep()` if necessary for AJAX tables to load.
2.  **Predict URLs**: If you can guess the URL of the next page (e.g., `!26=CTX`), favor that over clicking "Next" buttons, which is often flaky.
3.  **Headless=False for Debugging**: If a site blocks you, try `headless=False` to see if a CAPTCHA or splash page is the cause.
4.  **SSL Context**: For government/legacy sites, you often need `ssl.CERT_NONE`.

## Dependencies
*   `playwright`
*   `beautifulsoup4` (optional, if offline parsing needed)
*   `requests` (optional)
*   Standard libs: `os`, `re`, `urllib`, `ssl`, `json`, `time`

To install:
```bash
pip install playwright
playwright install chromium
```
