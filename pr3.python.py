

import hashlib

# Get user input
str = input("Enter the value to encode: ")

# Encode the input to bytes, then calculate the SHA-1 hash
result = hashlib.sha1(str.encode())

# Print the hexadecimal equivalent of the SHA-1 hash
print("The hexadecimal equivalent of SHA-1 is:")
print(result.hexdigest())
