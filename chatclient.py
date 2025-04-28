import socket
import threading


HOST = '127.0.0.1'  
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


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


def send():
    while True:
        message = input()
        
        if message.lower() == '!exit':
            client.send('!exit'.encode('ascii'))  
            client.close()  
            break 

        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
