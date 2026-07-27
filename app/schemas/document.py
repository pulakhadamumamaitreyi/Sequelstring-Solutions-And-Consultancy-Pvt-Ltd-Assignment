from pydantic import BaseModel
from datetime import datetime


class DocumentResponse(BaseModel):
    id: int
    document_name: str
    file_path: str
    upload_time: datetime
    total_pages: int
    total_chunks: int
    processing_status: str
    category: str

    class Config:
        from_attributes = True
