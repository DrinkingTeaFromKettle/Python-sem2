from Super_functions import *


if __name__ == '__main__':
    print("Ilość wyrazów w napisie: ")
    napis = "W tym napisie jest szesc wyrazów"
    print("Napis:" + napis)
    print("Ilość wyrazów: ")
    print(string_functions.iloscWyrazow(napis))
    print("########################")
    print("Odwrócenie kolejności wyrazów w napisie: ")
    napis = "Ten napis zostanie odwrócony "
    print("Napis:" + napis)
    print("Odwrócony napis: ")
    print(string_functions.odwrocKolejnosc(napis))
    print("########################")
    print("Usunięcie białych znaków w napisie: ")
    napis = ("Z tego napisu zostaną      usunięte\n  białe znaki")
    print("Napis:" + napis)
    print("Napis bez białych znaków: ")
    print(string_functions.usunBiale(napis))
    print("########################")
    print("Suma cyfr liczby: ")
    liczba = 123890
    print("Liczba:" )
    print(liczba)
    print("Suma cyfr liczby: ")
    print(numeric_functions.sumaCyfr(liczba))
    print("########################")
    print("Silnia liczby: ")
    liczba = 10
    print("Liczba:")
    print(liczba)
    print("Silnialiczby: ")
    print(numeric_functions.silnia(liczba))