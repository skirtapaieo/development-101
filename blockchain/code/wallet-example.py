import hashlib
import binascii
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

class Wallet:
    def __init__(self):
        """
        Initializes a new wallet with a new pair of private and public keys.
        """
        key = RSA.generate(2048)
        self.private_key = key
        self.public_key = key.publickey()

    def get_address(self):
        """
        Returns the wallet's address, which is the SHA-256 hash of the public key.
        """
        address = hashlib.sha256(self.public_key.export_key()).hexdigest()
        return address

    def sign_transaction(self, transaction):
        """
        Signs a transaction using the wallet's private key.
        """
        h = self._hash_transaction(transaction)
        signature = pkcs1_15.new(self.private_key).sign(h)
        return binascii.hexlify(signature)

    @staticmethod
    def _hash_transaction(transaction):
        """
        Returns a SHA-256 hash of the transaction data.
        """
        transaction_data = str(transaction).encode()
        h = hashlib.sha256(transaction_data)
        return h

    @staticmethod
    def verify_signature(transaction, signature, public_key):
        """
        Verifies a transaction signature against a given public key.
        """
        h = Wallet._hash_transaction(transaction)
        signature = binascii.unhexlify(signature)
        pubkey = RSA.import_key(public_key)
        try:
            pkcs1_15.new(pubkey).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False
