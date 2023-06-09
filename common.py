import time
import RSA
import random
import matplotlib.pyplot as plt



def listToString(L): 
        text = "" 
        # traverse in the string  
        for char in L: 
            text += char  
        # return string  
        return text 

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]

def ConvertToInt(message_str):
    res = 0
    for i in range(len(message_str)):
        res = res * 256 + ord(message_str[i])
    return res


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