from collections import deque
from numpy import mean

#TODO:
# 1. nie do końca rozumiem zadania
def zapisz(ramka: tuple[int]):
    f = open("ramki.txt", "a")
    l = ramka[2:len(ramka)]
    for e in l:
        f.write("," + str(e))
    f.write(";" + str(mean(l)))

    f.write("\n")
    f.close()


if __name__ == '__main__'
    open('ramki.txt', 'w').close()
    ramki = deque(
        [(3, 7, 1, 6, 4, 3, 7, 3, 9, 0), (5, 2, 8, 6, 2, 1, 0, 5, 8, 4), (7, 3, 2, 3, 3, 7, 4, 8, 2, 8)]
    )

    for i in range(len(ramki)):
        zapisz(ramki.pop())




