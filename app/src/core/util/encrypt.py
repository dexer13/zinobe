import hashlib


class Encrypt:
    @staticmethod
    def easy_encrypt(value) -> str:
        return hashlib.sha1(value).hexdigest()
