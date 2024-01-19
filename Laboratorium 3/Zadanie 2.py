from collections import namedtuple
from dataclasses import dataclass

@dataclass
class productClass:
    name: str
    price: float
    weight: float

    def __str__(self):
        text = "Product name: {name}\n Price: {price: .2f} zl\n Weight: {weight: .3f}kg"
        return text.format(name = self.name, price = self.price, weight = self.weight)

    def specialOffer(self, percent):
        self.price = self.price*(1 - percent)


if __name__ == '__main__':
    print("NamedTuple: \n")
    ## Typ NamedTuple pozwala na ustawienie dowolnej nazwy obiektu oraz nazwy atrybutów
    ## jednakże jest też typem immutable, co oznacza, że nie można zmieiać wartości
    ## nadanych atrybutom bez zastąpienia całego obiektu
    productTuple = namedtuple("Product", ["name", "price", "weight"])
    parmigiano = productTuple("parmigiano reggiano", 30.99, 0.2)
    print(parmigiano)
    cheddar = productTuple("cheddar", 12.99, 0.3)
    print(cheddar)
    ## DataClass pozwala na wszystko co NamedTuple, a także na dodawanie i nadpisywanie funkcjonalności
    ## można przykładowo nadpisać metodę __str__ zwracjającą reprezentację obiektu aby umieścić dodatkowe informacje
    ## Dzięki tej możliwości pozwala na bardziej elastyczny i czytelny kod przy tworzeniu i operowaniu na wielu obiektach
    print("\nDataClass:\n")
    blue_cheese = productClass("Danish Blue Cheese", 15.00, 0.15)
    print(blue_cheese)
    ## DataClass pozwala też bezpośrednio podmienić wartość lub stworzyć funkcję zmieniającą wartość atrybutu
    blue_cheese.price = blue_cheese.price + 3.00
    print("Produkt po zmianie ceny")
    print(blue_cheese)
    ## przecenienie produktu
    print("Produkt po zmianie ceny na ofertę specjalną:")
    blue_cheese.specialOffer(0.15)
    print(blue_cheese)

