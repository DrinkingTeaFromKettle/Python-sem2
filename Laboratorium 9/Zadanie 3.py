import random
import threading


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

if __name__ == '__main__':
    teatr = Teatr(60)
    consumer_thread = []
    for i in range(30):
        consumer_thread.append(threading.Thread(target=teatr.zarezerwuj, args=[random.randint(1, 3)]))
    for t in consumer_thread:
        t.start()
    for t in consumer_thread:
        t.join()
