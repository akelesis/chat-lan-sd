import advertise
import discover
from threading import Thread
from random import seed
from random import randint
from random import gauss

def main():
    seed(gauss(0, 1))
    port = int('50' + str(randint(0, 99)))

    th = Thread(target=discover.main, args=(port,))
    th.start()
    th2 = Thread(target=advertise.main, args=(port,))
    th2.start()