from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair
key_pair = RSA.generate(1024)

# Export the public key
pubkey = key_pair.publickey()
n = hex(pubkey.n)
e = hex(pubkey.e)

print("Public key n:", n)
print("Public key e:", e)

# Export the private key
private_key = key_pair.export_key()
public_key = pubkey.export_key()

print("Public key (PEM format):")
print(public_key.decode('ascii'))

print("Private key (PEM format):")
print(private_key.decode('ascii'))

# Encrypt a message
message = b"Ismile Academy"
encryptor = PKCS1_OAEP.new(pubkey)
encrypted_message = encryptor.encrypt(message)

# Print the encrypted message in hexadecimal format
print("Encrypted message:", binascii.hexlify(encrypted_message).decode('ascii'))
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair
key_pair = RSA.generate(1024)

# Export the public key
pubkey = key_pair.publickey()
n = hex(pubkey.n)
e = hex(pubkey.e)

print("Public key n:", n)
print("Public key e:", e)

# Export the private key
private_key = key_pair.export_key()
public_key = pubkey.export_key()

print("Public key (PEM format):")
print(public_key.decode('ascii'))

print("Private key (PEM format):")
print(private_key.decode('ascii'))

# Encrypt a message
message = b"Ismile Academy"
encryptor = PKCS1_OAEP.new(pubkey)
encrypted_message = encryptor.encrypt(message)

# Print the encrypted message in hexadecimal format
print("Encrypted message:", binascii.hexlify(encrypted_message).decode('ascii'))
