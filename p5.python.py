from random import randint

# Assuming P and G are defined
P = 23  # Example prime number
G = 5   # Example generator

# Alice's secret number
a = randint(1, P-1)
print("Secret Number for Alice is: %d" % a)

# Bob's secret number
b = randint(1, P-1)
print("Secret Number for Bob is: %d" % b)

# Compute the public keys
A = pow(G, a, P)  # Alice's public key
B = pow(G, b, P)  # Bob's public key

print('Public Key for Alice is: %d' % A)
print('Public Key for Bob is: %d' % B)

# Compute the secret keys
ka = pow(B, a, P)  # Secret key for Alice
kb = pow(A, b, P)  # Secret key for Bob

print('Secret Key for Alice is: %d' % ka)
print('Secret Key for Bob is: %d' % kb)
