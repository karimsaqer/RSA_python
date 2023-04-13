import random
from random import randint
from math import gcd

# public_one = 0
# public_two = 0


# Get Modular inverses
def mod_inverse(a, m):
    g, x, _ = extended_euclidean_algorithm(a, m)
    if g != 1:
        raise TypeError("No inverse")
    return x % m

# EE Algorithm
def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x_new, y_new = extended_euclidean_algorithm(b % a, a)
    x = y_new - (b // a) * x_new
    y = x_new
    return gcd, x, y

# This is the function of generating the public and private keys
# I will input the p and q parameters
def keys_generator(p,q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = generate_random_e(phi_n)
    d = mod_inverse(e, phi_n)
    # Keys with n 
    public_key = (n , e)
    private_key = (n , d)
    return public_key, private_key

def generate_random_e(phi_n):
    e = random.randrange(2, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randrange(2, phi_n)
    return e

# This function of encoding the characters to numbers
def encode_text(the_character):
    if the_character.isdigit():
        return int(the_character)
    elif the_character.isspace():
        return 36
    elif the_character.isalpha():
        return ord(the_character) - ord('a') + 10
    else: # Just if there is exception case
        return 36

# This function returns the number of characters
def decode_text(the_number):
    if 0 <= the_number < 10:
        return str(the_number)
    elif 10 <= the_number < 36:
        return chr(the_number - 10 + ord('a'))
    elif the_number == 36:
        return ' '
    else: # Just if there is exception case
        return ' '
    

# Encoding The plaintext 
def encoding_plaintext(plaintext):
    # Convert plaintext to lower case to Get The Order function 
    plaintext = plaintext.lower() 
    
    # Make sure that the plaintext is five letters
    # if len(plaintext) % 5 != 0:
    while len(plaintext) % 5 != 0:
        plaintext += ' '   
    
    # Encoding every group of characters (5) and add it to array
    numbers = []
    for i in range(0, len(plaintext), 5):
        group_of_five_chars = plaintext[i:i+5]
        # The Sum
        num = sum(encode_text(c) * (37 ** (4 - i)) for i, c in enumerate(group_of_five_chars))
        # Appending
        numbers.append(num)
    return numbers

# Decoding The ciphertext 
def decode_ciphertext(numbers):
    text = []
    for num in numbers:
        group = []
        for i in range(4, -1, -1):
            c_num = num // (37 ** i)
            group.append(decode_text(c_num))
            num %= (37 ** i)
        text.append(''.join(group))
    return ''.join(text)


# Encryption
def encrypt(plaintext, public_key):
    n, e = public_key
    # print('encrypt')
    list_of_encrypted = [pow(num, e, n) for num in encoding_plaintext(plaintext)]
    return list_of_encrypted

# Decryption
def decrypt(ciphertext, private_key):
    n, d = private_key
    # print('decrypt')
    plaintext = decode_ciphertext([pow(num, d, n) for num in ciphertext])
    return plaintext


# def set_public_one(public_key):
#     public_one = public_key

# def set_public_two(public_key):
#     public_two = public_key




#################################################################################################
# Test Case
# print(encoding_plaintext('hi s7'))
# print(decode_ciphertext(encoding_plaintext('hi s7')))


#  # will generate private and public keys with same input (p,q)
# public_key , private_key = keys_generator(7907,7919)
# # message
# message = input("> ")
# encrypted_msg = encrypt(message,public_key)

# # Decrypt message using private key
# decrypted_msg = decrypt([17585745],(62615533, 10394551))

# print(f"Public Key: {public_key}")
# print(f"Private Key: {private_key}")
# print(f"Encrypted Message: {encrypted_msg}")
# print(f"Decrypted Message: {decrypted_msg}")