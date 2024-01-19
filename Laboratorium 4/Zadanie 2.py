def sortuj_wedlug_liczby_cyfr(lista):
    """
    Funkcja sortująca listę liczb względem liczby cyfr w liczbie
    oraz wyświetlająca liczbę z najmniejszą i największą ilością cyfr
    :param lista: lista liczb do posortowania
    """
    lista_sorted = sorted(lista, key=lambda num: len(str(num)))
    print("Posortowana lista:" + str(lista_sorted))
    wyswietl = lambda lista: print(
        "najmniejsza liczba cyfr: " + str(min(lista, key= lambda num: len(str(num))))
        + ", najwieksza liczba cyfr: " + str(max(lista, key= lambda num: len(str(num)))))
    wyswietl(lista)

if __name__ == '__main__':
    lista = [666666,333,4444,22,7777777,333]
    sortuj_wedlug_liczby_cyfr(lista)
