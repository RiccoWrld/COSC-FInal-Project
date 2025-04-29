<<<<<<< HEAD
import asyncio
import websockets
import json

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    print("New client connected.")
    try:
        async for message in websocket:
            print(f"Received raw message: {message}")
            try:
                data = json.loads(message)  # Parse JSON message
                sender = data['sender']
                text = data['text']
                broadcast_message = json.dumps({ 'sender': sender, 'text': text })
                
                for client in connected_clients:
                    await client.send(broadcast_message)  # Send structured JSON
            except json.JSONDecodeError:
                print("Received non-JSON message. Ignored.")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected.")
    finally:
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 6789):
        print("WebSocket Server running on ws://localhost:6789")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
=======
import socket
import threading


HOST = '127.0.0.1'  
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
   
    for client in clients:
        if client != sender:
            client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == '!exit': 
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} left the chat!'.encode('ascii'), client)
                nicknames.remove(nickname)
                break  
            else:
                broadcast(message.encode('ascii'), client) 
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
>>>>>>> fd2cc6876221fa2c220a96d4f04d72ddf841a9c9
