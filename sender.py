import socket
import RSA
import generate

# Define the IP address and port for the socket
HOST = '127.0.0.1'
PORT = 8000


# Define the private and public keys for the socket
# private = 0;
# public = 0;
private_key = generate.get_private_key()
print(private_key)


# Socket Object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket
server_socket.bind((HOST, PORT))

# Listening
server_socket.listen(1)


while True:
    client_socket, address = server_socket.accept()
    print(f"Connected with {address}")

    # Send a welcome message to the client
    client_socket.send(b"Welcome to the server! Send 'exit' to close the connection.")

    # loop to Receive and send data from the client
    while True:
        # Now receive the data from the client
        data = client_socket.recv(1024)
        if not data:
            break
        
        # Decoding the data
        message = data.decode()
        my_list = [int(x) for x in message.split(',')]
        print(f"Received message: {my_list}")
        decrypted_message = RSA.decrypt(my_list,private_key)
        print(f"Decrypted message: {decrypted_message}")

        # closing the connection 
        if message.strip().lower() == "exit":
            break

        # Send a message to the client
        # print("Enter your message: ")
        # new_message = input("> ")
        # encrypted_message = RSA.encrypt(new_message, public_key)
        # client_socket.send(f"You received: {new_message}".encode())

    # Close the connection
    print(f"Closing connection with {address}")
    client_socket.close()
    break