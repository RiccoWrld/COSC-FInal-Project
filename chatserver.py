import socket
import threading

# Change this to your public IP address if you're running this on a public server
HOST = '127.0.0.1'  # or use your public IP address (e.g., '198.51.100.1')
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind((HOST, PORT))
except socket.error as e:
    print(f"Error binding to {HOST}:{PORT}. Check if the port is in use.")
    exit()
server.listen()

clients = []
nicknames = []

def broadcast(message, sender):
    # Broadcast the message to all clients except the sender
    for client in clients:
        if client != sender:
            client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == '!exit':  # Check if the client wants to exit
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} left the chat!'.encode('ascii'), client)
                nicknames.remove(nickname)
                break  # Exit the loop and stop handling this client
            else:
                broadcast(message.encode('ascii'), client)  # Broadcast the message excluding the sender
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'), client)
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}!")
        broadcast(f"{nickname} joined the chat!".encode('ascii'), client)
        client.send("Connected to the server!".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()
