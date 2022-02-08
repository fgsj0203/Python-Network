#Required importing library "socket" for relationship between board network and SO
import socket #Library
import sys

#creating function

def main():
    try:
        objectConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #passando como parâmetro o tipo de conexão que queremos

    except socket.error as erro:
        print("A conexão falhou!!!")
        print("Erro: {}".format(erro))
        sys.exit()
    print("Socket criado com sucesso")

    #definir o host alvo (o que será conectado)
    hostAlvo = input("Digite o host ou Ip a ser conectado: ")
    portaAlvo = input("Digite a porta a ser conectada: ")

    try:
        objectConnection.connect((hostAlvo, int(portaAlvo)))
        print("Cliente TCP conectado com sucesso no host: "+hostAlvo+" e na porta: "+portaAlvo)
        objectConnection.shutdown(2)
    except socket.error as erro:
        print("Não foi possível conectar o host: "+hostAlvo+ " Porta: " + portaAlvo)
        print("Erro: {}".format(erro))
        sys.exit()


#Chamando a função main
if __name__ == "__main__":
    main()
