import time
from datetime import datetime
from socket import socket
from threading import Thread

MAX_REQ = 5
TAM_BUFFER = 1000


def processar(conexao):
    conexao.sendall(b'oi')
    conexao.close()


def escutar(port):
    print(port)
    socket_bind_info = ('127.0.0.1', port)

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
                print("A mensagem: " + dados_client.decode("utf-8") + " foi recebida às " + datetime.now().strftime("%H:%M:%S, %m/%d/%Y"))
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
