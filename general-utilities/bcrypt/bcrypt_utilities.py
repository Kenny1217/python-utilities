import bcrypt

class BcryptUtils:

    @staticmethod
    def hash(str1: str) -> str:
        str1_bytes = str1.encode('utf-8')
        salt = bcrypt.gensalt()
        str1_hashed = bcrypt.hashpw(str1_bytes, salt)
        return str1_hashed.decode('utf-8')

    @staticmethod
    def verify(str1: str, hashed_str1: str) -> bool:
        str1_bytes = str1.encode('utf-8')
        hashed_str1_bytes = hashed_str1.encode('utf-8')
        return bcrypt.checkpw(str1_bytes, hashed_str1_bytes)
