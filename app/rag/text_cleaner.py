import re


class TextCleaner:

    @staticmethod
    def clean(text: str):

        text = text.replace("\n", " ")

        text = re.sub(r"\s+", " ", text)

        text = text.strip()

        return text
