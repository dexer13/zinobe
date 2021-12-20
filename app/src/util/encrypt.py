import hashlib


class Encrypt:
    @staticmethod
    def easy_encrypt(value: str) -> str:
        return hashlib.sha1(value.encode('utf-8')).hexdigest()
