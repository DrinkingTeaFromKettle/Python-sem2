from dataclasses import dataclass

@dataclass
class ksiazka:
    tytul: str
    autor: str
    isbn: str


class biblioteka:

    def __int__(self):
        self.ksiazki = []

    def __add__(self, k:ksiazka):
        self.ksiazki.append(k)

    def __sub__(self, k: ksiazka):
        self.ksiazki.remove(ksiazka)

    def __getitem__(self, str) -> ksiazka:




if __name__ == '__main__':
