from ratchet import ChainKey

class Alice:

    def __init__(self,shared_secret):
        self.chain=ChainKey(shared_secret)

    def send(self,message):

        cipher=self.chain.get_fernet()

        encrypted=cipher.encrypt(
            message.encode()
        )

        self.chain=self.chain.next_chain_key()

        return encrypted