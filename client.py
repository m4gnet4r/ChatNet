import socket
import threading
import rsa

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',12345))

with open('private.pem',"rb") as f:
    private_key=rsa.PrivateKey.load_pkcs1(f.read())
with open('public.pem',"rb") as f:
    public_key=rsa.PublicKey.load_pkcs1(f.read())

nickname=input("Choose a nickname: ")
if (rsa.decrypt(client.recv(1024),private_key).decode()=="NICK"):
    client.sendall(rsa.encrypt(nickname.encode(),public_key))

def recieve():
    while True:
        try:
            message=rsa.decrypt(client.recv(1024),private_key).decode()
            print(message)
        except:
            print("Error occured")
            client.close()
            break

def write():
     while True:
        message = f'{nickname}: {input("")}'
        client.sendall(rsa.encrypt(message.encode(),public_key))

recieve_thread=threading.Thread(target=recieve)
recieve_thread.start()

write=threading.Thread(target=write)
write.start()