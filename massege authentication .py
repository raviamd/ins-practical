from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii

# Generate RSA key pair
key_pair = RSA.generate(2048)

# Export the public and private keys
private_key = key_pair.export_key()
public_key = key_pair.publickey().export_key()

print("Public key:", public_key.decode('ascii'))
print("Private key:", private_key.decode('ascii'))

# Original and modified documents
original_document = b"This is the original document content."
modified_document = b"This is the modified document."

# Create SHA256 hash of the original document
original_hash = SHA256.new(original_document)

# Sign the original hash with the private key
signer = pkcs1_15.new(key_pair)
signature = signer.sign(original_hash)

# Now, let's verify the signature with the public key
try:
    # Hash the modified document
    modified_hash = SHA256.new(modified_document)
    
    # Create a new public key object
    public_key_object = RSA.import_key(public_key)
    
    # Verify the signature
    pkcs1_15.new(public_key_object).verify(original_hash, signature)
    print("Signature is valid.")
except (ValueError, TypeError):
    print("Signature is invalid.")
