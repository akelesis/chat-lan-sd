from socket import socket

TAM_BUFFER = 1000

ip = '192.168.5.4'

def requisicao(portas, port):
    try:
        mensagem = input()
        while mensagem != "exit":
            for x in portas:
                if x != port:
                    sock = socket()
                    server_info = (ip, x)
                    sock.connect(server_info)
                    sock.send(bytes(str(port) + " - " + mensagem, "utf-8"))
            dados_recebidos = sock.recv(TAM_BUFFER)
            print(dados_recebidos)

            sock.close()
            mensagem = input()
    except KeyboardInterrupt:
        print("Interrompido!")

if __name__ == '__main__':
    requisicao()
