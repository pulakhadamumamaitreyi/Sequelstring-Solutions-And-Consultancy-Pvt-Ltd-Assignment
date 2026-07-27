from app.rag.pdf_loader import PDFLoader
from app.rag.text_cleaner import TextCleaner
from app.rag.chunker import TextChunker


class DocumentProcessor:

    @staticmethod
    def process(pdf_path):

        pages = PDFLoader.extract_text(pdf_path)

        chunker = TextChunker()

        all_chunks = []

        for page in pages:

            cleaned = TextCleaner.clean(
                page["text"]
            )

            chunks = chunker.split(cleaned)

            for chunk in chunks:

                all_chunks.append(
                    {
                        "page": page["page"],
                        "text": chunk
                    }
                )

        return all_chunks
