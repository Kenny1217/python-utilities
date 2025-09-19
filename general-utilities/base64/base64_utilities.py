import base64

class Base64Utils:

    @staticmethod
    def encode(text: str) -> str:
        return base64.b64encode(text.encode()).decode()

    @staticmethod
    def decode(encoded_text: str) -> str:
        return base64.b64decode(encoded_text.encode()).decode()
