from resources import srednia, sortuj, policzPuste

if __name__ == '__main__':
    print(" ##########################")
    print("Srednia i mediana listy")
    lista: list[int | float] = [4, 7, -3.55, 1.333333]
    print("Lista: ")
    print(lista)
    sr, med = srednia(lista)
    print("Srednia listy:")
    print(sr)
    print("Mediana listy:")
    print(med)
    print(" ##########################")
    print("Sortowanie listy")
    krotka = (7, 34, -9, 15555, 1, -47)
    print("Krotka:")
    print(krotka)
    print("Posortowana lista: ")
    print(sortuj(krotka))
    print(" ##########################")
    print("Liczenie pustych miejsc listy")
    lista :  list[list[int | None]] = [[4, 7, None , 1, None, 3, 2],[1, -6, 3 , 12, None, 6, None], [4, 7, None , 1, None, 3, 2], [1, -6, 3 , 12, None, 6, None]]
    puste = policzPuste(lista)
    print("Lista: ")
    print(lista)
    print("Ilość pustych miejsc w liście: ")
    print(puste)