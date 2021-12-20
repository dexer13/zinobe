from app.src.util.encrypt import Encrypt


class TestEncrypt:
    def test_encrypt(self):
        key_encrypted = Encrypt.easy_encrypt(u'test_encrypt')
        assert key_encrypted == '0c1cc84bdf39932b292d7a93c3c619cf4d3c2bf2'