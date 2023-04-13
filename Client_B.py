import socket
import threading
import RSA
import test



public_key= test.get_public_key()
private_key = test.get_private_key()

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the local machine name
host = socket.gethostname()

# specify a port number for the client to connect to
port = 9999

# connect to the server
client_socket.connect((host, port))

# define a function to handle receiving messages from the server
def receive_messages():
    while True:
        data = client_socket.recv(1024)
        message = data.decode()
        cipher = [int(x) for x in message.split(',')]
        print(f"Received message: {cipher}")
        decrypted_message = RSA.decrypt(cipher,private_key)
        print(f"Decrypted message: {decrypted_message}")

# start a new thread to handle receiving messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# start the main chat loop
while True:
    # get input from the user and send it to the server
    message = input("> ")
    encrypted_message = RSA.encrypt(message,public_key)
    # print(encrypted_message)
    cipher = ','.join(str(x) for x in encrypted_message)
    client_socket.send(cipher.encode())
    if message.strip().lower() == "exit":
        break