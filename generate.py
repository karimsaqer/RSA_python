import RSA 
 

public_key , private_key = RSA.keys_generator(158527,158537)


def get_public_key():
    return public_key

def get_private_key():
    return private_key

