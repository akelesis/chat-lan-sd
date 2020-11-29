import time

from random import seed
from random import randint
from socket import inet_aton
from random import gauss
from zeroconf import Zeroconf, ServiceInfo
import msg_receiver

def main():
    seed(gauss(0, 1))

    service_info = ServiceInfo(
        type_='_sd-chat-host._tcp.local.',
        name='host' + str(randint(0, 99)) + '._sd-chat-host._tcp.local.',
        port=int('50' + str(randint(0, 99))),
        addresses=[inet_aton('192.168.15.20')]
    )
    zeroconf = Zeroconf()
    zeroconf.register_service(service_info)
    print(f'Serviço Anunciado... Nome: {service_info.name}')
    msg_receiver.escutar(service_info.port)
    
    """ time.sleep(30)
    zeroconf.unregister_service(service_info) """


if __name__ == '__main__':
    main()