#Importing library socket
import socket

objectConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket created with success")


host = "localhost"
port = 5432

objectConnection.bind((host, port)) # Bind = connection between client and server, with Host and Port
message = "\nServer: Hello Client"

while 1: # 1 = True (Value boolean)
    datas, address = objectConnection.recvfrom(4096)
    if datas:
        print("Server sending message...")
        objectConnection.sendto(datas + (message.encode()), address)
