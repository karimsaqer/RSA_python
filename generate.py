import RSA 
 

public_key , private_key = RSA.keys_generator(158527,158537)
# message = input("> ")
# encrypted_msg = RSA.encrypt(message,public_key)
# decrypted_msg = RSA.decrypt(encrypted_msg,private_key)

# print(f"Public Key: {public_key}")
# print(f"Private Key: {private_key}")
# print(f"Encrypted Message: {encrypted_msg}")
# print(f"Decrypted Message: {decrypted_msg}")

# public_key , private_key = RSA.keys_generator(158527,158537)
# public_key , private_key = RSA.keys_generator(9749,9833)

def get_public_key():
    return public_key

def get_private_key():
    return private_key

