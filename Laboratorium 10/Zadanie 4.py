import asyncio
import random
import threading
import time


class Magazyn:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.zajete_miejsce = 0
        self.lock = threading.Lock()
        self.empty_lock = threading.Condition(self.lock)
        self.full_lock = threading.Condition(self.lock)

    def usun(self, ilosc):
        with self.empty_lock:
            if self.zajete_miejsce - ilosc < 0:
                #print(f"Niewystarczająca liczba produktow w magazynie aby usunac {ilosc}, liczba produktów {self.zajete_miejsce}")
                while self.zajete_miejsce - ilosc < 0:
                    self.empty_lock.wait()
            self.zajete_miejsce -= ilosc
            print(f"Usunieto {ilosc} produktow.")
            print(f"Ilosc produktow w magaznie: {self.zajete_miejsce}")
            self.full_lock.notify()
            #time.sleep(0.1)



    def dodaj(self, ilosc):
        with self.full_lock:
            if self.zajete_miejsce + ilosc > self.pojemnosc:
                #print(f"Niewystarczająca pojemność magazynu aby dodac {ilosc}, dostepne miejsce {self.pojemnosc - self.zajete_miejsce}")
                while self.zajete_miejsce + ilosc > self.pojemnosc:
                    self.full_lock.wait()
            self.zajete_miejsce += ilosc
            print(f"Dodano {ilosc} produktow.")
            print(f"Ilosc produktow w magaznie: {self.zajete_miejsce}")
            self.empty_lock.notify()
            #time.sleep(0.1)

def main():
    magazyn = Magazyn(20)
    producer_thread = []
    consumer_thread = []
    for i in range(30):
        producer_thread.append(threading.Thread(target=magazyn.dodaj, args=[random.randint(1, 5)]))
        consumer_thread.append(threading.Thread(target=magazyn.usun, args=[random.randint(1, 5)]))

    for t in consumer_thread:
        t.start()
    for t in producer_thread:
        t.start()

    for t in consumer_thread:
        t.join()
    for t in producer_thread:
        t.join()


class MagazynAsync:
    def __init__(self, pojemnosc):
        self.pojemnosc = pojemnosc
        self.zajete_miejsce = 0
        self.lock = asyncio.Lock()
        self.empty_lock = asyncio.Condition(self.lock)
        self.full_lock = asyncio.Condition(self.lock)

    async def usun(self, ilosc): ta funkcja ma blad napraw to
        async with self.empty_lock:
            if self.zajete_miejsce - ilosc < 0:
                print(f"Niewystarczająca liczba produktow w magazynie aby usunac {ilosc}, liczba produktów {self.zajete_miejsce}")
                while self.zajete_miejsce - ilosc < 0:
                    await self.empty_lock.wait()
            self.zajete_miejsce -= ilosc
            print(f"Usunieto {ilosc} produktow.")
            print(f"Ilosc produktow w magaznie: {self.zajete_miejsce}")
            self.full_lock.notify_all()
            #asyncio.sleep(0.1)

    async def dodaj(self, ilosc):
        async with self.full_lock:
            if self.zajete_miejsce + ilosc > self.pojemnosc:
                print(f"Niewystarczająca pojemność magazynu aby dodac {ilosc}, dostepne miejsce {self.pojemnosc - self.zajete_miejsce}")
                while self.zajete_miejsce + ilosc > self.pojemnosc:
                    await self.full_lock.wait()
            self.zajete_miejsce += ilosc
            print(f"Dodano {ilosc} produktow.")
            print(f"Ilosc produktow w magaznie: {self.zajete_miejsce}")
            self.empty_lock.notify_all()
            #asyncio.sleep(0.1)


async def mainAsync():
    magazyn = MagazynAsync(20)
    producer_thread = []
    consumer_thread = []
    for i in range(30):
        producer_thread.append(asyncio.create_task(magazyn.dodaj(random.randint(1, 5))))
        consumer_thread.append(asyncio.create_task(magazyn.usun(random.randint(1, 5))))
    for i in range(30):
        await producer_thread[i]
        await consumer_thread[i]


if __name__ == '__main__':
    ###### Threading
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print(f"Czas wykonania zadania wersja threading {stop - start}s.")
    ###### AsyncIO
    start = time.perf_counter()
    asyncio.run(mainAsync())
    stop = time.perf_counter()
    print(f"Czas wykonania zadania wersja AsyncIO {stop - start}s.")
