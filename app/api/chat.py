from fastapi import APIRouter

from app.rag.generator import RAGGenerator

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


generator = RAGGenerator()


@router.post("/")
def chat(question: str):

    result = generator.ask(question)

    return result
