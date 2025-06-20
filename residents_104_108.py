import os
import pytesseract
from PIL import Image
import re
import json

# CONFIGURATION
input_folder = r"C:\Users\E16\Downloads\1900"  
output_file = "residents_1900.json"
directory_name = "Minneapolis 1900"

# OCR config
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  

# Prepare result container
results = []

# Helper to parse a line of text into structured format
def parse_line(line, page_num):
    # Adjust this regex according to formats seen in your entries
    name_match = re.match(r"^([A-Z][a-zA-Z.]+(?: [A-Z][a-zA-Z.]+)*)\s+((?:Mrs|wid|Mr|Dr)\.?)?\s*(.*?)\s*(?:r|h|b)?\s*(\d{3,5})?\s*(.*)", line)
    if not name_match:
        return None

    first_last = name_match.group(1).strip().split()
    firstname = " ".join(first_last[:-1]) if len(first_last) > 1 else first_last[0]
    lastname = first_last[-1]
    
    occupation = name_match.group(3).strip()
    street_number = name_match.group(4)
    street_name = name_match.group(5).strip()

    return {
        "FirstName": firstname,
        "LastName": lastname,
        "Spouse": None,
        "Occupation": occupation if occupation else None,
        "CompanyName": None,
        "HomeAddress": {
            "StreetNumber": street_number,
            "StreetName": street_name,
            "ApartmentOrUnit": None,
            "ResidenceIndicator": None  # you can add logic for 'r', 'h', etc.
        },
        "WorkAddress": None,
        "Telephone": None,
        "DirectoryName": directory_name,
        "PageNumber": page_num,
        "RelatedPersons": []
    }

# LOOP through images
for filename in sorted(os.listdir(input_folder)):
    if filename.endswith(".png"):
        filepath = os.path.join(input_folder, filename)
        print(f"Processing {filename}...")

        # Extract page number from filename if embedded (or track manually)
        try:
            page_number = int(re.findall(r"\d+", filename)[0])
        except:
            page_number = None  # fallback if filename doesn't have page number

        # OCR
        image = Image.open(filepath)
        text = pytesseract.image_to_string(image)

        # Parse line by line
        for line in text.splitlines():
            line = line.strip()
            if line:
                entry = parse_line(line, page_number)
                if entry:
                    results.append(entry)

# SAVE JSON
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"✅ Done. Extracted {len(results)} entries to {output_file}")
