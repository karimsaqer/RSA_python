import time
import RSA
import random
import matplotlib.pyplot as plt
import common


# Attacking Brute force (Knowing the plaintext and the algorithm)
def analyze_different_key_sizes(length_of_bits):
    key_sizes = []
    encryption_time = []
    for x in length_of_bits:
        key_sizes.append(x)
        start_time = time.time()
        public_key, private_key = common.generate_keypair(x)
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