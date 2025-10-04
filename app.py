from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import uvicorn

from utils.explain import parse_medical_report
from utils.ocr import extract_text_from_image

app = FastAPI()

@app.post("/analyze-text/")
async def analyze_text(text: str = Form(...)):
    results, summary, explanations = parse_medical_report(text)
    return JSONResponse(content={
        "analysis": results,
        "summary": summary,
        "explanations": explanations
    })

@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        extracted_text = extract_text_from_image(image_bytes)
        results, summary, explanations = parse_medical_report(extracted_text)

        return JSONResponse(content={
            "extracted_text": extracted_text,
            "analysis": results,
            "summary": summary,
            "explanations": explanations
        })
    except Exception as e:
        return JSONResponse(content={"status": "error", "reason": str(e)})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
