# minneapolis-1900-directory
Structured OCR data from the 1900 Minneapolis City Directory
# Minneapolis 1900 City Directory – Structured Resident Data

This repository contains structured OCR output from the **Minneapolis 1900 City Directory**, focused on residential entries between pages 30–108. Each record has been cleaned, parsed, and formatted into standardized JSON for archival, analysis, and research use.

## 📦 File Included

- `clean_residents_1900_directory.json`:  
  A machine-readable JSON file containing individual resident entries with detailed fields like name, occupation, company, address, and source metadata.

## 🔎 JSON Format

Each record follows this structure:

```json
{
  "FirstName": "Peter D",
  "LastName": "Aadland",
  "Spouse": "Pearl R",
  "Occupation": "Salesman",
  "CompanyName": "Lifetime Sls",
  "HomeAddress": {
    "StreetNumber": "2103",
    "StreetName": "Bryant av S",
    "ApartmentOrUnit": "apt 1",
    "ResidenceIndicator": "h"
  },
  "WorkAddress": null,
  "Telephone": null,
  "DirectoryName": "Minneapolis 1900",
  "PageNumber": 32,
  "RelatedPersons": []
}


🔁 Notes on Parsing
OCR was manually verified and cleaned where needed.

Multi-person households are tracked via RelatedPersons (with roles like "widow", "student", etc.).

Address fields are split for more structured analysis.

Page numbers reflect the original source location in the scanned directory.

📚 Use Cases
Historical residency tracking

Genealogy and archival projects

Urban development and migration analysis

👤 Maintainer
Ada Tuana Dönmez – github.com/AdaTuanaDonmez

📄 License
This dataset is derived from public domain historical materials and is shared freely for academic and non-commercial use.


