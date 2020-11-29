from socket import socket

TAM_BUFFER = 1000


def requisicao(portas):
    try:
        mensagem = input()
        while mensagem != "exit":
            mensagem = input()
            for x in portas:
                sock = socket()
                server_info = ('127.0.0.1', x)
                sock.connect(server_info)
                sock.send(bytes(mensagem, "utf-8"))
            dados_recebidos = sock.recv(TAM_BUFFER)

            sock.close()
    except KeyboardInterrupt:
        print("Interrompido!")


if __name__ == '__main__':
    requisicao()
