import os
import re
import argparse

# Standardize Filenames Utility
# Fixes common encoding issues, spaces, and adds consistency to PDF names.

def clean_and_rename(data_dir, dry_run=False):
    files = sorted([f for f in os.listdir(data_dir) if f.endswith('.pdf') or f.endswith('_pdf')])
    print(f"Scanning {len(files)} files in {data_dir}...")
    
    renamed_count = 0
    
    for f in files:
        new_name = f
        
        # 1. Normalize Prefix (Padding Digits)
        prefix_match = re.search(r"^(\d+)", f)
        if prefix_match:
            digits = prefix_match.group(1)
            padded_digits = f"{int(digits):03d}"
            
            # Reconstruct trailing part
            rest = f[len(digits):]
            # Remove leading separators like . or _
            rest = re.sub(r"^[._]+", "", rest)
            
            new_name = f"{padded_digits}_{rest}"
            
            # Ensure proper separation for known prefixes like 'กวจ'
            if new_name.startswith(f"{padded_digits}กวจ"):
                 new_name = new_name.replace(f"{padded_digits}กวจ", f"{padded_digits}_กวจ")

        # 2. Fix extension issues (e.g. 12345_pdf -> 12345.pdf)
        if re.match(r"^\d+_pdf$", new_name):
             new_name = new_name.replace("_pdf", ".pdf")
        
        # 3. Clean up separators and PDPA
        # Replace + with _
        new_name = new_name.replace("+", "_").replace(" ", "_")
        
        # Normalize PDPA suffix
        new_name = re.sub(r"[\s_+]*\(?PDPA\)?", "_PDPA", new_name)
        
        # Fix double underscores
        while "__" in new_name:
            new_name = new_name.replace("__", "_")
            
        # Validation: Ensure it ends with .pdf
        if not new_name.lower().endswith(".pdf"):
            if new_name.lower().endswith("_pdf"):
                 new_name = new_name[:-4] + ".pdf"
            elif new_name.lower().endswith("pdf"): 
                 new_name = new_name[:-3] + ".pdf"
                 
        # Fix dot before pdf if messed up (e.g. _.pdf -> .pdf)
        new_name = new_name.replace("_.pdf", ".pdf")
        
        # Execute Rename
        if f != new_name:
            src = os.path.join(data_dir, f)
            dst = os.path.join(data_dir, new_name)
            
            if os.path.join(data_dir, f) == dst:
                continue

            if os.path.exists(dst):
                print(f"[SKIP] Target exists: {new_name}")
            else:
                if dry_run:
                    print(f"[DRY RUN] Would rename '{f}' -> '{new_name}'")
                else:
                    os.rename(src, dst)
                    # print(f"Renamed: '{f}' -> '{new_name}'")
                    renamed_count += 1

    print(f"Renamed {renamed_count} files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Standardize PDF Filenames")
    parser.add_argument("--dir", required=True, help="Directory containing files")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without executing")
    
    args = parser.parse_args()
    clean_and_rename(args.dir, args.dry_run)
