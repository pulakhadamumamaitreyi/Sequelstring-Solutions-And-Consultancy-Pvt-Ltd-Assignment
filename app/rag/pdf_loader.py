import fitz


class PDFLoader:

    @staticmethod
    def extract_text(pdf_path: str):

        pdf = fitz.open(pdf_path)

        pages = []

        for page_number, page in enumerate(pdf):

            text = page.get_text()

            pages.append(
                {
                    "page": page_number + 1,
                    "text": text
                }
            )

        pdf.close()

        return pages
