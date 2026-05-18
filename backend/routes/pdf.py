from fastapi import APIRouter, UploadFile, File
import shutil
from backend.rag.rag_pdf import ingest_pdf

router = APIRouter()

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    path = f"temp_{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_pdf(path)

    return {"message": "PDF uploaded successfully"}