from fastapi import APIRouter

from app.rag.search import SemanticSearch

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.post("/")
def search_documents(
    query: str
):

    results = SemanticSearch.search(
        query
    )

    return resultsfrom fastapi import APIRouter

from app.rag.search import SemanticSearch

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.post("/")
def search_documents(
    query: str
):

    results = SemanticSearch.search(
        query
    )

    return results
