from zeroconf import Zeroconf, ServiceBrowser, ServiceListener
from socket import socket
import msg_receiver
import msg_sender

TAM_BUFFER = 1000
NUM_REQ = 3

portas = []

class Listener(ServiceListener):

    def update_service(self, zc: 'Zeroconf', type_: str, name: str) -> None:
        print(f'Um serviço foi atualizado. Tipo: {type_} Nome: {name}')

    def remove_service(self, zc: 'Zeroconf', type_: str, name: str):
        print(f'Um serviço foi removido: ', portas[0])

    def add_service(self, zc: 'Zeroconf', type_: str, name: str):
        info = zc.get_service_info(type_, name)
        portas.append(info.port)
        print(f'Um servico foi encontrado. ', info)

def main():
    zeroconf = Zeroconf()
    listener = Listener()
    try:
        service_browser = ServiceBrowser(zeroconf, "_sd-chat-host._tcp.local.", listener)
        msg_sender.requisicao(portas)

    except KeyboardInterrupt:
        print("Interrompido!")
    finally:
        zeroconf.close()


if __name__ == '__main__':
    main()