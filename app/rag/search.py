from app.rag.vector_store import VectorStore


class SemanticSearch:

    @staticmethod
    def search(
        query,
        top_k=5
    ):

        vector_store = VectorStore()

        results = vector_store.search(
            query,
            top_k
        )

        return resultsfrom app.rag.vector_store import VectorStore


class SemanticSearch:

    @staticmethod
    def search(
        query,
        top_k=5
    ):

        vector_store = VectorStore()

        results = vector_store.search(
            query,
            top_k
        )

        return results
