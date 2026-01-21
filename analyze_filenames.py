import os
import re

DATA_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement-documents"
files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith('.pdf')])

patterns = {}

def get_pattern(filename):
    # Try to capture the prefix part
    # 001_XXX, 01_XXX, 1.XXX, etc.
    match = re.match(r"^(\d+)[._](.+)", filename)
    if match:
        return "digit_prefix"
    match = re.match(r"^Website_(.+)", filename)
    if match:
        return "website_prefix"
    match = re.match(r"^(\d+)กวจ(.+)", filename) # 001กวจ
    if match:
        return "digit_no_sep"
    return "other"

print(f"Total files: {len(files)}")
print("Sample inconsistencies:")

# Analyze and print suggestions
for f in files:
    new_name = f
    
    # 1. Normalize Prefix Separators and Padding
    # Case: 01_กวจ, 001_กวจ, 1.กวจ, 001กวจ
    
    # Regex for "Start with digits, then separator or 'กวจ'"
    # Group 1: Digits
    # Group 2: Separator or immediate text
    match = re.match(r"^(\d+)([_.]|(?=กวจ))(.*)", f)
    if match:
        num = match.group(1)
        sep = match.group(2)
        rest = match.group(3)
        
        # Pad to 3 digits
        num_padded = f"{int(num):03d}"
        
        # Force separator to _
        new_name = f"{num_padded}_{rest}"
        
    # Case: Website_ -> maybe keep or change? Let's keep consistent strict structure if mostly digits?
    # User just said "same format".
    
    # Clean up + vs _ vs space
    new_name = new_name.replace("+", "_").replace(" ", "_").replace("__", "_")
    
    # Remove PDPA suffix variations if needed, or normalize them? 
    # USER didn't ask to remove, just "same format".
    # But usually (PDPA), +PDPA, _PDPA -> _PDPA
    new_name = re.sub(r"[+_\s]*\(?PDPA\)?", "_PDPA", new_name)
    
    if f != new_name:
         print(f"'{f}'  ->  '{new_name}'")
