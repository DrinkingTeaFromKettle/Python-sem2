import asyncio
import random
import threading
import time


class Teatr:
    def __init__(self, miejsca):
        self.dostepne_miejsca = miejsca
        self.semafor = threading.Semaphore(10)

    def zarezerwuj(self, ilosc):
        with self.semafor:
            if self.dostepne_miejsca - ilosc >= 0:
                self.dostepne_miejsca -= ilosc
                print(f"Zarezerwowano {ilosc} miejsc.")
            else:
                print(f"Niewystarczająca liczba wolnych miesjc")
            print(f"Liczba dostępnych miejsc: {self.dostepne_miejsca}")

def main():
    teatr = Teatr(60)
    consumer_thread = []
    for i in range(30):
        consumer_thread.append(threading.Thread(target=teatr.zarezerwuj, args=[random.randint(1, 3)]))
    for t in consumer_thread:
        t.start()
    for t in consumer_thread:
        t.join()

class TeatrAsync:
    def __init__(self, miejsca):
        self.dostepne_miejsca = miejsca
        self.semafor = asyncio.Semaphore(10)

    async def zarezerwuj(self, ilosc):
        async with self.semafor:
            if self.dostepne_miejsca - ilosc >= 0:
                self.dostepne_miejsca -= ilosc
                print(f"Zarezerwowano {ilosc} miejsc.")
            else:
                print(f"Niewystarczająca liczba wolnych miesjc")
            print(f"Liczba dostępnych miejsc: {self.dostepne_miejsca}")

async def mainAsync():
    teatr = TeatrAsync(60)
    consumer_thread = []
    for i in range(30):
        consumer_thread.append(asyncio.create_task(teatr.zarezerwuj(random.randint(1, 3))))
    for i in range(30):
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


