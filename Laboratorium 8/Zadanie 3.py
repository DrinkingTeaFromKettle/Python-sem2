import re

class InitException(Exception):
    pass
class Zamowienie:
    @staticmethod
    def sprawdz_imie(imie):
        if not imie[0].isupper():
            raise InitException("Imie musi się zaczynać od dużel litery")
        return True

    @staticmethod
    def sprawdz_nazwisko(nazwisko):
        r = re.compile(r"[A-ZŁŹŻĆŚŃ][a-złźćśńąęóż]+(-[A-ZŁŹŻĆŚŃ][a-złźćśńąęóż])?")
        if not r.match(nazwisko):
            raise InitException("Niepoprawny format nazwiska")
        return True

    @staticmethod
    def sprawdz_adres( adres):
        r = re.compile(r'^[A-Z][a-z]+\s\d+(/\d+)?$')
        if not r.match(adres):
            raise InitException("Niepoprawny format adresu")
        return True

    @staticmethod
    def sprawdz_kod(kod):
        r = re.compile(r'^\d{2}-\d{3}$')
        if not r.match(kod):
            raise InitException("Niepoprawny format kodu pocztowego")
        return True
    def __init__(self, imie, nazwisko, adres, kod_pocztowy):
        if Zamowienie.sprawdz_imie(imie):
            self.imie = imie
        if Zamowienie.sprawdz_nazwisko(nazwisko):
            self.nazwisko = nazwisko
        if Zamowienie.sprawdz_adres(adres):
            self.adres = adres
        if Zamowienie.sprawdz_kod(kod_pocztowy):
            self.kod_pocztowy = kod_pocztowy



if __name__ == '__main__':
    # Niepoprawne dane
    #z = Zamowienie("man", "Man", "Street 13", "31-234")
    #z = Zamowienie("Man", "Man-Man", "Street13", "31-234")
    #z = Zamowienie("Man", "Man-Man", "Street 13", "31-2346")

    #Poprawne dane
    z = Zamowienie("Man", "Man-Man", "Street 13", "31-234")
    print(f"{z.imie} {z.nazwisko}, {z.adres} {z.kod_pocztowy}")