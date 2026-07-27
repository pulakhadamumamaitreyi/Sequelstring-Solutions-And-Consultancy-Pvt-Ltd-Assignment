import os
import fitz

from sqlalchemy.orm import Session

from app.models.document import Document

UPLOAD_FOLDER = "app/uploads"


def save_document(db: Session, filename: str, file_path: str):

    pdf = fitz.open(file_path)

    pages = len(pdf)

    pdf.close()

    document = Document(
        document_name=filename,
        file_path=file_path,
        total_pages=pages,
        processing_status="Uploaded"
    )

    db.add(document)

    db.commit()

    db.refresh(document)

    return document


def list_documents(db: Session):
    return db.query(Document).all()


def delete_document(db: Session, document_id: int):

    document = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if not document:
        return None

    if os.path.exists(document.file_path):
        os.remove(document.file_path)

    db.delete(document)

    db.commit()

    return document
