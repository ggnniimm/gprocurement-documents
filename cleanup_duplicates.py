import os

DOWNLOAD_DIR = "/Users/mingsaksaengwilaipon/.gemini/antigravity/scratch/gprocurement_downloads"

# The 5 pairs I identified from the list:
# 1. 001_กวจ_16571_160463_ข้อหรือแนวทางปฏิบัติในการจัดซื้อจัดจ้างฯ+PDPA.pdf vs ...ข้อหารือ...
# 2. 01_กวจ_20694_030564_ข้อหรือแนวทางปฏิบัติกรณีการเบิกจ่ายเงินฯ.pdf vs ...ข้อหารือ...
# 3. 01_กวจ_21175_070564_ข้อหรือเกี่ยวกับการพิจารณาผลงานก่อสร้างฯ.pdf vs ...ข้อหารือ...
# 4. 01_กวจ_21382_110564_ข้อหรือการจัดซื้อจัดจ้างเกี่ยวกับการบำรุงรักษาพัสดุ.pdf vs ...ข้อหารือ...
# 5. 02_กวจ_21417_110564_ข้อหรือแนวทางการกําหนดกรอบระยะเวลาฯ.pdf vs ...ข้อหารือ...

duplicates = [
    "001_กวจ_16571_160463_ข้อหรือแนวทางปฏิบัติในการจัดซื้อจัดจ้างฯ+PDPA.pdf",
    "01_กวจ_20694_030564_ข้อหรือแนวทางปฏิบัติกรณีการเบิกจ่ายเงินฯ.pdf",
    "01_กวจ_21175_070564_ข้อหรือเกี่ยวกับการพิจารณาผลงานก่อสร้างฯ.pdf",
    "01_กวจ_21382_110564_ข้อหรือการจัดซื้อจัดจ้างเกี่ยวกับการบำรุงรักษาพัสดุ.pdf",
    "02_กวจ_21417_110564_ข้อหรือแนวทางการกําหนดกรอบระยะเวลาฯ.pdf"
]

print("Deleting 5 duplicate files with typo 'ข้อหรือ'...")
for f in duplicates:
    path = os.path.join(DOWNLOAD_DIR, f)
    if os.path.exists(path):
        os.remove(path)
        print(f"Deleted: {f}")
    else:
        print(f"Not found: {f}")

print("\nCleanup complete.")
files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith('.pdf')]
print(f"Total PDF files remaining: {len(files)}")
