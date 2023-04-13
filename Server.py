import socket
import threading

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the local machine name
host = socket.gethostname()

# specify a port number for the server to listen on
port = 9999

# bind the socket to a specific address and port
server_socket.bind((host, port))

# set the server to listen for incoming connections
server_socket.listen(2)  # allow up to 2 clients to connect

print('Waiting for clients to connect...')

# define a function to handle receiving messages from a client
def receive_messages(client_socket, client_name):
    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        print(f"{client_name}: {message.decode()}")

        # send the message to the other client
        other_client_socket = client_sockets[1] if client_socket == client_sockets[0] else client_sockets[0]
        other_client_socket.send(message)

    client_socket.close()

# accept incoming connections from clients
client_sockets = []
client_names = []
for i in range(2):
    client_socket, client_address = server_socket.accept()
    print(f"Client {i+1} ({client_address[0]}) connected.")
    # client_socket.send(b"Connected to server.")
    client_sockets.append(client_socket)

    # ask for the client's name
    client_name = input(f"What is the name of Client {i+1}? ")
    client_names.append(client_name)

    # start a new thread to handle receiving messages from the client
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket, client_name))
    receive_thread.start()

# start the chat loop
while True:
    pass  # do nothing, just keep the server running