import socket
import threading

host='127.0.0.1'
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen()

print("server is listening...")

clients=[]
nicknames=[]


def broadcast(message):
    for client in clients:
        client.sendall(message)

def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            nicknames.remove(nickname)
            broadcast(f'{nickname} has left the chat room.'.encode())
            break

def recieve():
    client,address=s.accept()
    print(f'server connected with {address}')
    client.sendall('NICK'.encode())
    nickname=client.recv(1024).decode()
    clients.append(client)
    nicknames.append(nickname)

    print(f'nickname of the client is {nickname}')
    broadcast(f'{nickname} has joined the chat room.'.encode())

    thread=threading.Thread(target=handle,args=(client,))
    thread.start()

recieve()