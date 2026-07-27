from app.rag.process_document import DocumentProcessor

chunks = DocumentProcessor.process(
    "app/uploads/sample.pdf"
)

print("Total Chunks:", len(chunks))

print()

print(chunks[0])
