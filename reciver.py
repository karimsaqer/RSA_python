import socket
import RSA
import generate
import pickle

# Define the IP address and port for the socket
HOST = '127.0.0.1'
PORT = 8000

# Define the private and public keys for the socket
# private = 0;
# public = 0;
public_key= generate.get_public_key()
print(public_key)


# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Receive the welcome message from the server
welcome_message = client_socket.recv(1024)
print(welcome_message.decode())
# public_key = welcome_message.decode()

# Loop for Send and receive data
while True:
    # Get input from the user
    print("Enter your message: ")
    message = input("> ")
    print(message)
    encrypted_message = RSA.encrypt(message,public_key)
    print(encrypted_message)
    cipher = ','.join(str(x) for x in encrypted_message)
    # encrypted_message_bytes = pickle.dumps(encrypted_message)
    # Send the message to the server
    client_socket.send(cipher.encode())

    # If the user typed "exit", close the connection
    if message.strip().lower() == "exit":
        client_socket.close()
        break
