from fastapi import FastAPI, File, UploadFile
from PyPDF2 import PdfReader

app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "PDF API is working"}

# Upload PDF and extract text
@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):

    # Read PDF
    reader = PdfReader(file.file)
    
    text = ""
    
    # Loop through pages
    for page in reader.pages:
        text += page.extract_text()

    # Simple keypoints (first 3 lines)
    lines = text.split("\n")
    keypoints = lines[:3]

    return {
        "filename": file.filename,
        "keypoints": keypoints,
        "full_text": text[:500]   # only first 500 characters
    }
