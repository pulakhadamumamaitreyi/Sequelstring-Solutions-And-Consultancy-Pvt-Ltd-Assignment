from openai import OpenAI

from app.core.config import settings
from app.rag.vector_store import VectorStore


class RAGGenerator:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

        self.vector_store = VectorStore()

    def ask(self, question):

        results = self.vector_store.search(
            question,
            top_k=5
        )

        documents = results["documents"][0]
        metadata = results["metadatas"][0]

        context = ""

        for i, doc in enumerate(documents):

            context += f"""

Page : {metadata[i]["page"]}

Content:

{doc}

"""

        prompt = f"""

You are an AI Research Assistant.

Answer ONLY using the supplied context.

If the answer is unavailable say:

"I could not find the answer from the uploaded documents."

Context:

{context}

Question:

{question}

"""

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.choices[0].message.content

        return {
            "answer": answer,
            "sources": metadata,
            "context": documents
        }
