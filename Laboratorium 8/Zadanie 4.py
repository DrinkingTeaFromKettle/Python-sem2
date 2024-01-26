import csv
import re
class Produkt:
    wymiana_walut = {
        ('zl', '$'): 0.27,
        ('zl', 'eur'): 0.23,
        ('$', 'zl'): 3.69,
        ('$', 'eur'): 0.89,
        ('eur', 'zl'): 4.32,
        ('eur', '$'): 1.12,
    }

    produkty = []
    def __init__(self, id, cena, stan):
        Produkt.sprawdz_id(id)
        self.id = id
        Produkt.sprawdz_cena(cena)
        self.cena = cena
        Produkt.sprawdz_stan(stan)
        self.stan = stan

    def __repr__(self):
        return f"ID: {self.id}, Cena: {self.cena}, Stan magazynu: {self.stan} sztuk"

    @staticmethod
    def oblicz_cene_waluta(cena, waluta):
        currency = re.compile(r"(\$|(zl)|(eur))$")
        search = currency.search(cena)
        cena_t: list = re.findall( r"(([1-9]\d{0,2} (\d{3})*)|\d{1,3})(\.\d{1,2})?",cena)
        if len(cena_t) > 0 and search and waluta in ('$','zl','eur'):
            współczynnik_konwersji = Produkt.wymiana_walut.get((search.group(), waluta))
            nowa_cena = float(cena_t[0][0].replace(" ", ""))*współczynnik_konwersji
            return str(nowa_cena)+waluta
        else:
            raise ValueError("Wprowadzono nieporawną cenę lub walutę")
    @staticmethod
    def sprawdz_id(id):
        r = re.compile(r'#(\d{8}[SO])')
        if not r.match(id):
            raise ValueError("Niepoprawny format ceny")
    @staticmethod
    def sprawdz_cena(cena):
        currency = re.compile(r"(([1-9]\d{0,2} (\d{3})*)|\d{1,3})(\.\d{1,2})?(\$|(zl)|(eur))$")
        match = currency.match(cena)
        if not match:
            raise ValueError("Niepoprawny format ceny")
    @staticmethod
    def sprawdz_stan(stan):
        if not int(stan) >= 0:
            raise ValueError("Stan magazynów musi być nieujemny")


    @classmethod
    def posortuj_produkty(cls):
        if len(Produkt.produkty) > 0:
            Produkt.produkty = sorted(Produkt.produkty, key=lambda x: float(re.findall( r"(([1-9]\d{0,2} (\d{3})*)|\d{1,3})(\.\d{1,2})?",x.cena)[0][0].replace(" ", "")))
        else:
            print("Lista produktów jest pusta")

def wczytaj_produkty(sciezka):
    try:
        plik = open(sciezka, 'r')
        czytnik = csv.reader(plik, delimiter= ';')
    except OSError:
        print("Nie można otworzyć pliku")
    else:
        for row in czytnik:
            id, cena, stan = row
            pr = Produkt(id, cena, stan)
            Produkt.produkty.append(pr)
        Produkt.posortuj_produkty()
        for pr in Produkt.produkty:
            print(pr)


if __name__ == '__main__':
    wczytaj_produkty("produkty.csv")