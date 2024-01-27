import datetime
import queue
import random
import threading
import time

ilosc = 20
###### Zadanie wykonane z wykorzystaniem threading
class BuforTh:
    def __init__(self, max):
        self.bufor = queue.Queue(max)
        self.lock = threading.Lock()

buforth = BuforTh(3)
def zapisz_daneth(i):
        buforth.lock.acquire()
        if not buforth.bufor.full():
            buforth.bufor.put(f"Dana: {i} o czasie {datetime.datetime.now().time()}")
            buforth.lock.release()
        else:
            print("Bufor pełny, czekam pół sekundy")
            buforth.lock.release()
            time.sleep(0.5)

def wczytaj_daneth():
        with buforth.lock:
            if not buforth.bufor.empty():
                print(buforth.bufor.get())

def mainth():
    producer_thread = [threading.Thread(target=zapisz_daneth,args=[i]) for i in range(ilosc)]
    consumer_thread = [threading.Thread(target=wczytaj_daneth) for _ in range(ilosc)]
    for i in range(1,ilosc):
        producer_thread[i].start()
        consumer_thread[i].start()
    for i in range(1,ilosc):
        producer_thread[i].join()
        consumer_thread[i].join()


###### Zadanie wykonane z wykorzystaniem AsyncIO
import asyncio

class BuforAs:
    def __init__(self, max):
        self.bufor = queue.Queue(max)
        self.lock = asyncio.Lock()

buforas = BuforAs(3)
async def zapisz_daneas(i):
        async with buforas.lock:
            if not buforas.bufor.full():
                buforas.bufor.put(f"Dana: {i} o czasie {datetime.datetime.now().time()}")
                return i + 1
            else:
                print("Bufor pełny, czekam pół sekundy")
                await asyncio.sleep(0.5)
async def wczytaj_daneas():
        async with buforas.lock:
            if not buforas.bufor.empty():
                print(buforas.bufor.get())

async def mainas():
    producer_thread = []
    consumer_thread = []
    for i in range(ilosc):
        producer_thread.append(asyncio.create_task(zapisz_daneas(i)))
        consumer_thread.append(asyncio.create_task(wczytaj_daneas()))
    for i in range(ilosc):
        await producer_thread[i]
    for i in range(ilosc):
        await consumer_thread[i]


if __name__ == '__main__':
    ###### Threading
    start = time.perf_counter()
    mainth()
    stop = time.perf_counter()
    print(f"Czas wykonania zadania wersja threading {stop - start}s.")
    ###### AsyncIO
    start = time.perf_counter()
    asyncio.run(mainas())
    stop = time.perf_counter()
    print(f"Czas wykonania zadania wersja AsyncIO {stop - start}s.")

