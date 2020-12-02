from threading import Thread
import user

th = Thread(target=user.main)
th.start()