import random
from math import gcd

def char_to_num(char):
    if char.isdigit():
        return int(char)
    elif char.islower():
        return ord(char) - ord('a') + 10
    else:
        return 36

def num_to_char(num):
    if 0 <= num <= 9:
        return str(num)
    elif 10 <= num <= 35:
        return chr(num - 10 + ord('a'))
    else:
        return ' '

def text_to_numbers(text):
    text = ''.join([' ' if not c.isalnum() else c.lower() for c in text])
    while len(text) % 5 != 0:
        text += ' '
    numbers = []
    for i in range(0, len(text), 5):
        group = text[i:i+5]
        num = sum(char_to_num(c) * (37 ** (4 - i)) for i, c in enumerate(group))
        numbers.append(num)
    return numbers

def numbers_to_text(numbers):
    text = []
    for num in numbers:
        group = []
        for i in range(4, -1, -1):
            c_num = num // (37 ** i)
            group.append(num_to_char(c_num))
            num %= (37 ** i)
        text.append(''.join(group))
    return ''.join(text)


def is_prime(n):
    if n <= 1:
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

def generate_prime(bits):
    while True:
        candidate = random.getrandbits(bits)
        if is_prime(candidate):
            return candidate

def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Inverse doesn't exist")
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def generate_keypair(bits):
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d = mod_inverse(e, phi)
    return (n, e), (n, d)

def encrypt(plaintext, public_key):
    n, e = public_key
    return [pow(num, e, n) for num in text_to_numbers(plaintext)]

def decrypt(ciphertext, private_key):
    n, d = private_key
    return numbers_to_text([pow(num, d, n) for num in ciphertext])


public_key,private_key = generate_keypair(20)
message='hello world'
encrypted_msg = encrypt(message,public_key)
# Decrypt message using private key
decrypted_msg = decrypt(encrypted_msg,private_key)

print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")
print(f"Encrypted Message: {encrypted_msg}")
print(f"Decrypted Message: {decrypted_msg}")