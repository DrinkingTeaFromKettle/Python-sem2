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
            time.sleep(random.random())



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
            time.sleep(random.random())


if __name__ == '__main__':
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
