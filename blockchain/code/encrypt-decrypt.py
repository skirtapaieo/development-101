from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate a key pair of private and public keys
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

print("Private Key: ", binascii.hexlify(private_key.export_key()))
print("Public Key: ", binascii.hexlify(public_key.export_key()))

# Let's say we have a message, or in the case of a blockchain, a transaction
message = 'Hello, this is a test transaction'.encode('utf-8')

# Encrypt the message with the public key
encryptor = PKCS1_OAEP.new(public_key)
encrypted_msg = encryptor.encrypt(message)
print("Encrypted Message: ", binascii.hexlify(encrypted_msg))

# Decrypt the message with the private key
decryptor = PKCS1_OAEP.new(private_key)
decrypted_msg = decryptor.decrypt(encrypted_msg)
print("Decrypted Message: ", decrypted_msg)
