from ratchet import ChainKey

class Bob:

    def __init__(self,shared_secret):
        self.chain=ChainKey(shared_secret)

    def receive(self,encrypted):

        cipher=self.chain.get_fernet()

        message=cipher.decrypt(
            encrypted
        ).decode()

        self.chain=self.chain.next_chain_key()

        return message