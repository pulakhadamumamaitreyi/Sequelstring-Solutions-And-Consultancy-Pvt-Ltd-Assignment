from app.rag.process_document import DocumentProcessor
from app.rag.vector_store import VectorStore


class DocumentIndexer:

    @staticmethod
    def index(
        document_id,
        pdf_path
    ):

        chunks = DocumentProcessor.process(
            pdf_path
        )

        vector_store = VectorStore()

        vector_store.add_chunks(
            document_id,
            chunks
        )

        return len(chunks)
