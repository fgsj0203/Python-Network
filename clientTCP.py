"""
Author: Francisco Gomes
Date: 08/02/2022
Objective: Create code connection network for development client using protocol TCP/IP
"""

# First importing libraries

# Required importing library "socket" for relationship between board network and SO
import socket
# The module sys of manipulate variables of environment execution language Python
import sys

# creating function principal
def main():
    try:
        # Creating object of connection using methods in library socket
        # AF_INET = using Protocol IP / SOCK_STREAM = using Protocol TCP / number = 0 (Protocol TCP)
        objectConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as erro:
        print("The connection failed!")
        print("Error: {}".format(erro))
        sys.exit()
    print("Socket created success")

    # Identify host and port using for connection
    hostTarget = input("Input Host or IP for connection: ")
    portTarget = input("Input Port for connection: ")

    try:
        objectConnection.connect((hostTarget, int(portTarget)))
        print("Client TCP connected success in host: " + hostTarget + " and Port: " + portTarget)
        objectConnection.shutdown(2)
    except socket.error as erro:
        print("Not possible connect with  host: " + hostTarget + " Port: " + portTarget)
        print("Error: {}".format(erro))
        sys.exit()


# Calling function main
if __name__ == "__main_ _":
    main()
