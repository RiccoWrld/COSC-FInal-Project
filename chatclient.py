import socket
import threading

# Change this to the server's IP address if you're running this on a different machine
HOST = '127.0.0.1'  # Use the server's public IP if you're connecting from another machine
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Function to receive messages
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                nickname = input("Enter your nickname: ")
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

# Function to send messages
def send():
    while True:
        message = input()
        
        if message.lower() == '!exit':
            client.send('!exit'.encode('ascii'))  # Notify the server you're leaving
            client.close()  # Close the client socket
            break  # Exit the loop

        client.send(message.encode('ascii'))

# Start receiving and sending messages concurrently using threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
