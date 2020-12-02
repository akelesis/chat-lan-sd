import time
from datetime import datetime
from socket import socket
from threading import Thread

MAX_REQ = 5
TAM_BUFFER = 1000

ip = '192.168.5.4'

def processar(conexao):
    conexao.sendall(b'mensagem recebida com sucesso!')
    conexao.close()


def escutar(port):
    print(port)
    socket_bind_info = (ip, port)

    sock = socket()
    sock.bind(socket_bind_info)
    sock.listen()

    start = None
    try:
        count = 0
        while count < MAX_REQ:
            conexao, origem = sock.accept()
            dados_client = conexao.recv(TAM_BUFFER)
            if(dados_client):
                th = Thread(target=processar, args=(conexao,))
                th.start()
                print(dados_client.decode("utf-8") + " --> " + datetime.now().strftime("%H:%M:%S, %d/%m/%Y"))
            if start is None:
                start = datetime.now()

            count += 1
    except KeyboardInterrupt:
        print('Finalizado!')
    finally:
        sock.close()
    tempo_total = datetime.now() - start

    print(f'O servidor levou {tempo_total} para processar as requisições!')


if __name__ == '__main__':
    escutar()
