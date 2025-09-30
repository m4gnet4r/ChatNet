import socket
import threading

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',12345))

nickname=input("Choose a nickname: ")
if (client.recv(1024).decode()=="NICK"):
    client.sendall(nickname.encode())

def recieve():
    while True:
        try:
            message=client.recv(1024).decode()
            print(message)
        except:
            print("Error occured")
            client.close()
            break

def write():
     while True:
        message = f'{nickname}: {input("")}'
        client.sendall(message.encode())

recieve_thread=threading.Thread(target=recieve)
recieve_thread.start()

write=threading.Thread(target=write)
write.start()