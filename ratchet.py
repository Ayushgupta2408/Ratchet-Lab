import hmac
import hashlib
from cryptography.fernet import Fernet
import base64

class ChainKey:

    def __init__(self,key,index=0):
        self.key=key
        self.index=index

    def message_key(self):
        return hmac.new(
            self.key,
            b"\x01",
            hashlib.sha256
        ).digest()

    def next_chain_key(self):
        new_key=hmac.new(
            self.key,
            b"\x02",
            hashlib.sha256
        ).digest()

        return ChainKey(
            new_key,
            self.index+1
        )

    def get_fernet(self):
        mk = self.message_key()
        return Fernet(base64.urlsafe_b64encode(mk))