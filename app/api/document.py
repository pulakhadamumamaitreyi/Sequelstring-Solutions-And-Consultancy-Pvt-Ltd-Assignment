import os
import shutil

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.document_service import (
    save_document,
    list_documents,
    delete_document,
)

router = APIRouter(prefix="/documents", tags=["Documents"])

UPLOAD_FOLDER = "app/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    file_location = os.path.join(
        UPLOAD_FOLDER,
        file.filename,
    )

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document = save_document(
        db,
        file.filename,
        file_location,
    )

    return {
        "message": "Upload Successful",
        "document": document,
    }


@router.get("/")
def get_documents(
    db: Session = Depends(get_db),
):

    return list_documents(db)


@router.delete("/{document_id}")
def remove_document(
    document_id: int,
    db: Session = Depends(get_db),
):

    document = delete_document(
        db,
        document_id,
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found.",
        )

    return {
        "message": "Document deleted successfully."
    }
