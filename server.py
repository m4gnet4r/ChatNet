import socket
import threading
import rsa

host='127.0.0.1'
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen()

print("server is listening...")

clients=[]
nicknames=[]

with open('private.pem',"rb") as f:
    private_key=rsa.PrivateKey.load_pkcs1(f.read())
with open('public.pem',"rb") as f:
    public_key=rsa.PublicKey.load_pkcs1(f.read())


def broadcast(message):
    for client in clients:
        client.sendall(rsa.encrypt(message,public_key))

def dm(client):
    str1=(rsa.decrypt(client.recv(1024),private_key).decode()).split(': ')
    list1=(str1[1]).split(',')
    print(list1)
    message=client.recv(1024)
    for nickname in list1:
        index=nicknames.index(nickname)
        client1=clients[index]
        client1.sendall(message)

def handle(client):
    while True:
        index=clients.index(client)
        nickname=nicknames[index]
        try:
            message=rsa.decrypt(client.recv(1024),private_key)
            message1=message.decode()
            if message1 == f'{nickname}: quit' :
                clients.remove(client)
                client.close()
                nicknames.remove(nickname)
                broadcast(f'{nickname} has left the chat room.'.encode())
                break
            elif message1 == f'{nickname}: list':
                client.sendall(rsa.encrypt(('List of clients: '+', '.join(nicknames)).encode(),public_key))
            elif message1==f'{nickname}: dm':
                dm(client)
            else:
                broadcast(message)
        except:
            clients.remove(client)
            client.close()
            nicknames.remove(nickname)
            broadcast(f'{nickname} has left the chat room.'.encode())
            break

def recieve():
    while True:
        client,address=s.accept()
        print(f'server connected with {address}')
        client.sendall(rsa.encrypt('NICK'.encode(),public_key))
        nickname=rsa.decrypt(client.recv(1024),private_key).decode()
        clients.append(client)
        nicknames.append(nickname)

        print(f'nickname of the client is {nickname}')
        broadcast(f'{nickname} has joined the chat room.'.encode())

        thread=threading.Thread(target=handle,args=(client,))
        thread.start()

recieve()