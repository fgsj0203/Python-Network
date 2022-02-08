"""
Author: Francisco Gomes
Date: 08/02/2022
Objective: Create code connection network for development client using protocol UDP
"""

# First importing libraries
# Required importing library "socket" for relationship between board network and SO
import socket
# ------------------------------------------------------------
#Create object of connection
objectConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP is protocol datagram of user
print("Client socket created is success!")

#Host, port and message of send
host = "localhost"
port = 5433 # Client
message = "Hello server, is good?"

try:
    print("Client: " + message)
    objectConnection.sendto(message.encode(), (host, 5432)) # Encoding this is packing datas and send message, 5432 is port of server

    datas, server = objectConnection.recvfrom(4096) # Datas and server is receiving of objectConnection response with  size 4096 Bytes
    datas = datas.decode() # Unpacking datas received
    print("Client: "+datas)
finally:
    print("Client: Closing a connection")
    objectConnection.close()

