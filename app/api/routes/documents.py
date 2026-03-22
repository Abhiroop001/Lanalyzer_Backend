from fastapi import APIRouter, UploadFile, File
import os, shutil

from app.utils.file_parser import extract_text
from app.utils.token_counter import count_tokens
from app.services.document_service import save_document

router = APIRouter()
UPLOAD_DIR = "uploads"

# Ensure the uploads directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    path = os.path.join(UPLOAD_DIR, file.filename)

    # Save file
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process file
    text = extract_text(path)
    tokens = count_tokens(text)
    data = {
        "filename": file.filename,
        "text": text,
        "tokens": tokens
    }

    document_id = save_document(data)
    return {
        "document_id": document_id,
        "tokens": tokens
    }
