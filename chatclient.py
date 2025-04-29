import socket
import threading

<<<<<<< HEAD
# Change this to the server's IP address if you're running this on a different machine
HOST = '127.0.0.1'  # Use the server's public IP if you're connecting from another machine
PORT = 55600
=======

HOST = '127.0.0.1'  
PORT = 55555
>>>>>>> fd2cc6876221fa2c220a96d4f04d72ddf841a9c9

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

<<<<<<< HEAD
# Function to receive messages
=======

>>>>>>> fd2cc6876221fa2c220a96d4f04d72ddf841a9c9
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

<<<<<<< HEAD
# Function to send messages
=======

>>>>>>> fd2cc6876221fa2c220a96d4f04d72ddf841a9c9
def send():
    while True:
        message = input()
        
        if message.lower() == '!exit':
<<<<<<< HEAD
            client.send('!exit'.encode('ascii'))  # Notify the server you're leaving
            client.close()  # Close the client socket
            break  # Exit the loop

        client.send(message.encode('ascii'))

# Start receiving and sending messages concurrently using threads
=======
            client.send('!exit'.encode('ascii'))  
            client.close()  
            break 

        client.send(message.encode('ascii'))


>>>>>>> fd2cc6876221fa2c220a96d4f04d72ddf841a9c9
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
