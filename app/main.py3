from fastapi import FastAPI

from app.api.document import router as document_router
from app.api.search import router as search_router
from app.api.chat import router as chat_router

from app.database.create_tables import create_tables

create_tables()

app = FastAPI(
    title="AI Research & Knowledge Assistant",
    version="1.0.0"
)

app.include_router(document_router)
app.include_router(search_router)
app.include_router(chat_router)


@app.get("/")
def root():

    return {
        "message": "AI Research Assistant Running"
    }
