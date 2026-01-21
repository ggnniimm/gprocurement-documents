import os
import re

DATA_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement-documents"
files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith('.pdf')])

print(f"Total files to process: {len(files)}")

renamed_count = 0

for f in files:
    new_name = f
    
    # 1. Normalize Prefix: NNN_กวจ or NN_กวจ or N.กวจ
    # Capture digits at start
    prefix_match = re.search(r"^(\d+)", f)
    if prefix_match:
        digits = prefix_match.group(1)
        # Pad to 3 digits
        padded_digits = f"{int(digits):03d}"
        
        # Check what follows: . or _ or text
        # We want to enforce: NNN_กวจ
        
        # If followed by 'กวจ' or '.กวจ' or '_กวจ'
        rest = f[len(digits):]
        
        # Remove leading separators from 'rest'
        rest = re.sub(r"^[._]+", "", rest)
        
        # If 'rest' DOES NOT start with 'กวจ', maybe it's just a number + text?
        # But looking at file list, most start with 'กวจ' after prefix.
        # Some are '1.Website', etc.
        
        # Special case: 1.Website_... -> 001_Website_... (User might want this, or maybe not website)
        # Actually, let's look at the sample output: 1.กวจ -> 001_กวจ
        
        new_name = f"{padded_digits}_{rest}"
        
        # Ensure 'กวจ' is separated if it exists
        if new_name.startswith(f"{padded_digits}กวจ"):
             new_name = new_name.replace(f"{padded_digits}กวจ", f"{padded_digits}_กวจ")
             
    # 2. Fix extension issues (e.g. 12345_pdf -> 12345.pdf)
    # If the file ended up as "DIGITS_pdf", revert to "DIGITS.pdf"
    if re.match(r"^\d+_pdf$", new_name):
         new_name = new_name.replace("_pdf", ".pdf")
    
    # 3. Clean up separators and PDPA
    # Replace + with _
    new_name = new_name.replace("+", "_").replace(" ", "_")
    
    # Normalize PDPA
    new_name = re.sub(r"[\s_+]*\(?PDPA\)?", "_PDPA", new_name)
    
    # Fix double underscores
    while "__" in new_name:
        new_name = new_name.replace("__", "_")
        
    # Validation: Ensure it ends with .pdf
    if not new_name.lower().endswith(".pdf"):
        if new_name.lower().endswith("_pdf"):
             new_name = new_name[:-4] + ".pdf"
        elif new_name.lower().endswith("pdf"): # e.g. .pdf -> pdf
             new_name = new_name[:-3] + ".pdf"
             
    # Fix dot before pdf if messed up (e.g. _.pdf -> .pdf)
    new_name = new_name.replace("_.pdf", ".pdf")
    
    # Perform Rename
    if f != new_name:
        src = os.path.join(DATA_DIR, f)
        dst = os.path.join(DATA_DIR, new_name)
        
        # Handle collision (e.g. if new_name already exists)
        if os.path.exists(dst):
            print(f"Skipping rename '{f}' -> '{new_name}' (Target exists)")
        else:
            os.rename(src, dst)
            # print(f"Renamed: '{f}' -> '{new_name}'")
            renamed_count += 1

print(f"Renamed {renamed_count} files.")
