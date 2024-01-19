import random
from collections import deque

def losowanie(n: int):
    """
    Funkcja losująca liczby z przedziału <-100,100> i wstawiająca je do listy
    w taki sposób, aby listy dodatnie i równe 0 były na początku listy
    a na końcu listy liczby ujemne
    :param n: ilość liczb do wylosowania
    :return: lista odpowiednio posortowanych liczb
    """
    lista = deque()
    for i in range(n):
        number = random.randint(-100,100)
        if(number >= 0):
            lista.appendleft(number)
        else:
            lista.append(number)
    lista = list(lista)
    print(lista)
    #lista.sort(reverse=True)
    return lista

if __name__ == '__main__':
    losowanie(6)


