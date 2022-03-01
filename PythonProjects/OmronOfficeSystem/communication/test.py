import threading
import time


class AA:
    def __init__(self):
        self.a = 0

    def b(self):
        t = threading.Thread(target=self.handle2, args=(self.a, ))
        t.start()

    def handle(self):
        while True:
            print(self.a)
            time.sleep(1)

    def handle2(self, a):
        while True:
            print(a)
            time.sleep(1)

    def c(self):
        while True:
            self.a += 1
            time.sleep(1)


aa = AA()
aa.b()
aa.c()