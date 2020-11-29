import advertise
import discover
from threading import Thread

th = Thread(target=discover.main)
th.start()
th2 = Thread(target=advertise.main)
th2.start()