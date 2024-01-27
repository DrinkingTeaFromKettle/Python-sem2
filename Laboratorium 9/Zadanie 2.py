import datetime
import queue
import threading
import time


class Bufor:
    def __init__(self, max):
        self.bufor = queue.Queue(max)
        self.lock = threading.Lock()

bufor = Bufor(3)

zatrzymaj = False
def zapisz_dane():
    i = 1
    while not zatrzymaj:
        with bufor.lock:
            if not bufor.bufor.full():
                bufor.bufor.put(f"Dana: {i} o czasie {datetime.datetime.now().time()}")
                i += 1
            else:
                print("Bufor pełny, czekam pół sekundy")
                time.sleep(0.5)
        time.sleep(0.3)
def wczytaj_dane():
    while not zatrzymaj:
        with bufor.lock:
            if not bufor.bufor.empty():
                print(bufor.bufor.get())
        time.sleep(0.4)

if __name__ == '__main__':
    producer_thread = threading.Thread(target=zapisz_dane, args=[])
    consumer_thread = threading.Thread(target=wczytaj_dane, args=[])

    producer_thread.start()
    consumer_thread.start()

    time.sleep(10)
    zatrzymaj = True

    producer_thread.join()
    consumer_thread.join()