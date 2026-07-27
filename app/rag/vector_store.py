import chromadb

from app.core.config import settings

from app.rag.embedding import EmbeddingModel


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_DB
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

        self.embedding_model = EmbeddingModel()

    def add_chunks(
        self,
        document_id,
        chunks
    ):

        ids = []
        documents = []
        metadatas = []
        embeddings = []

        for index, chunk in enumerate(chunks):

            ids.append(
                f"{document_id}_{index}"
            )

            documents.append(
                chunk["text"]
            )

            metadatas.append(
                {
                    "document_id": document_id,
                    "page": chunk["page"]
                }
            )

            embeddings.append(
                self.embedding_model.encode(
                    chunk["text"]
                )[0]
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings
        )

    def search(
        self,
        query,
        top_k=5
    ):

        query_embedding = self.embedding_model.encode(
            query
        )[0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results
