from collections import Counter

if __name__ == '__main__':
    sciezka = input("Podaj sciezke:")
    f = open("slowa.txt", "r")
    wiersz = f.read()
    print(wiersz)
    slowa = Counter(wiersz.split())
    while 1:
        slowo = input("Podaj slowo do zliczenia:")
        print(slowa[slowo])
