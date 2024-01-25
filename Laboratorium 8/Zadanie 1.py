import re

def sprawdz_liczba_ułamkowa(liczba):
    return True if re.match(r'^[-+]?\d*\.\d+$', str(liczba)) else False

if __name__ == '__main__':
    print("Sprawdzenie liczby 3.5: "+ str(sprawdz_liczba_ułamkowa(3.5)))
    print("Sprawdzenie liczby -3.5: " + str(sprawdz_liczba_ułamkowa(-3.5)))
    print("Sprawdzenie liczby 3: " + str(sprawdz_liczba_ułamkowa(3)))
    print("Sprawdzenie liczby -3: " + str(sprawdz_liczba_ułamkowa(-3)))