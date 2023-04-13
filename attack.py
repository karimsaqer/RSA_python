import time
import RSA
import random
import matplotlib.pyplot as plt

# Some new functions

# To know if it is prime or not
def is_prime(n):
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Get the prime number
def generate_prime(bits):
    while True:
        candidate = random.getrandbits(bits)
        if is_prime(candidate):
            return candidate
        
# Generate the pair input of bits 
def generate_keypair(bits):
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = RSA.generate_random_e(phi)
    d = RSA.mod_inverse(e, phi)
    public_key = (n , e)
    private_key = (n , d)
    return public_key, private_key


# Attacking Brute force (Knowing the plaintext and the algorithm)
def analyze_different_key_sizes(length_of_bits):
    key_sizes = []
    encryption_time = []
    for x in length_of_bits:
        key_sizes.append(x)
        start_time = time.time()
        public_key, private_key = generate_keypair(x)
        plaintext = "Hello, world!"
        ciphertext = RSA.encrypt(plaintext, public_key)
        elapsed_time = time.time() - start_time
        encryption_time.append(elapsed_time)
        print(f"{x}-bit encryption: {elapsed_time:.2f} seconds")
        # Time for decryption
        start_time = time.time()
        decrypted_text = RSA.decrypt(ciphertext, private_key)
        print(f"{x}-bit decryption: {time.time() - start_time:.2f} seconds")
    
    return key_sizes, encryption_time

# The function call
key_sizes , encryption_time = analyze_different_key_sizes([50, 60, 100, 120])

# plotting 
plt.plot(key_sizes, encryption_time)
plt.xlabel('Key size (bits)')
plt.ylabel('Encryption time (seconds)')
plt.show()