# AI-Powered Medical Report Simplifier (Backend)

This project is a **FastAPI-based backend** that takes medical reports (text or image) and produces **patient-friendly explanations**. It performs OCR for scanned images, normalizes test results, and generates summaries dynamically.

---

## 📂 Project Structure

medical-report-simplifier/
├── app.py                     # FastAPI main application
├── requirements.txt           # Python dependencies (libraries to install)
├── README.md                  # Project overview and instructions
├── temp.jpg                   # Temporary file placeholder
└── utils/
    ├── normalize.py           # Logic for handling reference ranges and test normalization
    ├── explain.py             # Logic for generating summary and explanations
    └── ocr.py                 # Core OCR functionality (using Tesseract)


---

## ⚙️ Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/kamalikamnnit/AI-Powered-Medical-Report-Simplifier.git
cd medical-report-simplifier

2.Create a virtual environment (recommended):

python -m venv venv
source venv/Scripts/activate   # Windows
# OR
source venv/bin/activate       # Linux/Mac

3.Install dependencies:

pip install -r requirements.txt

4.Install Tesseract OCR (Windows example):

Download and install from Tesseract GitHub

Set the path in utils/ocr.py:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

5.Run FastAPI server:
uvicorn app:app --reload

The server will run at http://127.0.0.1:8000/
To test endpoints: use http://127.0.0.1:8000/docs


Screenshots showing endpoints

1)
<img width="1778" height="854" alt="Screenshot 2025-10-04 124005" src="https://github.com/user-attachments/assets/702af5d0-908f-43eb-803e-3b4919cd63f2" />
shows output for testing text

2)
<img width="1759" height="829" alt="Screenshot 2025-10-04 124014" src="https://github.com/user-attachments/assets/f4c11d84-8dce-4de2-8be1-abc1e7c560d9" />
sows output for testing image

🏗️ Architecture

OCR (utils/ocr.py): Extracts text from uploaded images using Tesseract.

Normalization (utils/normalize.py): Extracts numeric values from text and interprets them using reference ranges.

Explanation (utils/explain.py): Generates dynamic summary and explanations based on abnormal test results.

FastAPI Endpoints (app.py): Handles both text and image uploads and returns JSON output.


🚀 API Endpoints
1. Analyze raw text

Endpoint: /analyze-text/
Method: POST
Form Data:

text (string): Medical report text

Example using curl (Git Bash):
curl -X POST "http://127.0.0.1:8000/analyze-text/" \
  -F "text=Hemoglobin 10.2 g/dL WBC 11200 /uL Platelet Count 140000 /uL"

Sample JSON Response:

{
  "analysis": {
    "Hemoglobin": {"raw_line": "Hemoglobin 10.2 g/dL", "value": 10.2, "outcome": "Low (Anemic)"},
    "WBC": {"raw_line": "WBC 11200 /uL", "value": 11200, "outcome": "High"},
    "Platelet Count": {"raw_line": "Platelet Count 140000", "value": 140000, "outcome": "Low (Low Platelets)"}
  },
  "summary": "Low (Anemic) Hemoglobin, High WBC, Low (Low Platelets) Platelet Count",
  "explanations": [
    "Low hemoglobin may relate to anemia.",
    "High WBC can occur with infections.",
    "Low platelet count may increase bleeding risk."
  ]
}


2. Analyze uploaded image

Endpoint: /upload-file/
Method: POST
Form Data:

file (file): Image of medical report (.png, .jpg, etc.)

Example using curl (Git Bash):

curl -X POST "http://127.0.0.1:8000/upload-file/" \
  -F "file=@/c/Users/rkama/OneDrive/Pictures/Screenshots/Screenshot\ 2025-10-03\ 202628.png"

  Response:

{
  "extracted_text": "Full text extracted from image...",
  "analysis": { ... same as text analysis ... },
  "summary": "Low (Anemic) Hemoglobin, High WBC, Low (Low Platelets) Platelet Count",
  "explanations": [
    "Low hemoglobin may relate to anemia.",
    "High WBC can occur with infections.",
    "Low platelet count may increase bleeding risk."
  ]

  "extracted_text":"Clinical Laboratory Report\n\nPatient Name Date Drawn Date Received Date of Report\nDOE, JOHN 12/20/99 12/20/99 12/22/99\nSex Age Client Name / Address LD.Number Account Number\nMt MEDICAL CENTER 7e0e7654 = 1243\nor n YOUR DOCTOR, M.D.\n“mn 4123 MAIN STREET a 4\n123094567 = -_ ‘Number ‘Drawn\n918273 11:00\nPatient |.D./Soc. Sec Number\nTEST NAME RESULT _UNITS.-——_«REFERENCE RANGE *\nCOMPLETE BLOOD COUNT W/ DIFF\nwee 52 Thousleumm 39-114\nRac 351 L Milcu.mm 420-570\nHGB (HEMOGLOBIN) 145 old 132-169\nHCT (HEMATOCRIT) 41.2 Percent 385-490\ncv 7 HA 80-97\nMCH 414 H pg 275-335\nce 35.3 Percent 320-360\nROW 118 Percent 110-150\nPLATELET COUNT 172 Thousleumm 140-390\nMPV 76 Af 75-115\nDIFFERENTIAL\nTOTAL NEUTROPHILS, % 40.1 Percent 38.0-80.0\nTOTAL LYMPHOCYTES, % 481 Percent 450-490\nMONOCYTES, % 129 Percent 00-130\nEOSINOPHILS, % os Percent 0.0-80\nBASOPHILS, % 03 Percent 0.0-20\nTOTAL NEUTROPHILS, ABSOLUTE (2085 Celis/cu.mm 1650 - 8000\nTOTAL LYMPHOCYTES, ABSOLUTE (2397 Celis/cu.mm 1000 - 3500\nMONOCYTES, ABSOLUTE ert Celis/cu.mm 40-900\nEOSINOPHILS, ABSOLUTE 31 Cals/oumm 30-600\nBASOPHILS, ABSOLUTE 16 Celis/cu.mm 0-125\n\n",

  "analysis":{"Hemoglobin":{"raw_line":"HGB (HEMOGLOBIN) 145 old 132-169","value":145.0,"outcome":"High"},"Platelet Count":{"raw_line":"PLATELET COUNT 172 Thousleumm 140-390","value":172.0,"outcome":"Low (Low Platelets)"}},

  "summary":"High Hemoglobin, Low (Low Platelets) Platelet Count",

  "explanations":["Low platelet count may increase bleeding risk."]
}

📝 Notes

1.All explanations and summaries are dynamic, based on the test values and reference ranges.

2.The backend does not diagnose — it provides patient-friendly explanations.

3.Supports both typed text and scanned images.
