from threading import Thread
from urllib.request import urlopen
from time import time
#
# przed = time()
# for i in range(10):
#     with urlopen(f"https://www.metaweather.com/api/location/search/?query=Warsaw") as file:
#         print(file.read())
# po = time()
# czas1 = po - przed
# print(czas1)

class MyThread(Thread):

    def run(self):
        with urlopen(f"https://www.metaweather.com/api/location/search/?query=Warsaw") as plik:
            print(plik.read())

przed1 = time()

watki = []
for i in range(10):
    watek = MyThread()
    watek.start()
    watki.append(watek)

for watek in watki:
    watek.join()

po1 = time()
czas2 = po1-przed1
print(czas2)