# obliczająca sumę cyfr w liczbie,
def sumaCyfr(liczba: int) -> int:
    suma = 0
    for i in str(liczba):
        suma += int(i)
    return  suma


# obliczająca silnię liczby
def silnia(liczba: int) -> int:
    sil = 1
    for i in range(1, liczba + 1):
        sil *= i
    return sil