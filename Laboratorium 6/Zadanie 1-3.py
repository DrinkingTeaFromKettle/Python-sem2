from abc import ABC, abstractmethod


class Product(ABC):
    """
    Klasa abstrakcyjna opisująca produkty
    Attributes
    ----------
    name: str
        nazwa produktu
    price: float
        cena pojedynczej sztuki produktu
    stock: int
        ilość produktu w magazynie
    Methods
    -------
    calculate_discount():
        abstrakcyjna metoda zwracająca cenę po obniżce
    display_info():
        metoda wyświetlająca informację o produkcie
    __add__():
        metoda napisująca operator '+'
        metoda zwiększa ilość sztuk produktu w magazynie o podaną ilość
        :param number: ilość sztuk do dodania
    __sub__():
        metoda napisująca operator '-'
        metoda zmniejsza ilość sztuk produktu w magazynie o podaną ilość
        :param number: ilość sztuk do odjęcia
    """
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    @abstractmethod
    def calculate_discount(self):
        pass
    def display_info(self):
        print(f'Produkt: {self.name}, cena: {self.price}zl , ilość: {self.stock}')

    def __add__(self, number):
        self.stock += number
        return self

    def __sub__(self, number):
        if self.stock >= number:
            self.stock -= number
            return self
        else:
            print("Nie ilosc produktow do zmniejszenia stanu jest wieksza niz ilosc produktow w magazynie")

class Book(Product):
    """
    Klasa opisująca książkę dziedzicząca po klasie Produkt
    Attributes
    ----------
    author: str
        autor książki
    genre: str
        gatunek książki
    pages: int
        ilość stron w książce
    Methods
    -------
    calculate_discount():
        metoda przysłaniająca metodę z klasy nadrzędnej zwracająca cenę książki po obniżce
    display_info():
        metoda przysłaniająca metodę z klasy nadrzędnej wyświetlająca informacje o książce
    """
    def __init__(self, name, price, stock, author, genre, pages):
        Product.__init__(self, name, price, stock)
        self.author = author
        self.genre = genre
        self.pages = pages

    def calculate_discount(self):
        return 0.9 * self.price

    def display_info(self):
        Product.display_info(self)
        print(f'Autor: {self.author}, gatunek: {self.genre}, liczba stron: {self.pages} ')

class ElectronicDevice(Product):
    """
    Klasa opisująca urządzenie elektryczne dziedzicząca po klasie Produkt
    Attributes
    ----------
    brand: str
        firma produkująca urządzenie
    warranty: str
        czas gwarancji
    power: int
        moc urządzenia w watach
    Methods
    -------
    calculate_discount():
        metoda przysłaniająca metodę z klasy nadrzędnej zwracająca cenę urządzenia po obniżce
    display_info():
        metoda przysłaniająca metodę z klasy nadrzędnej wyświetlająca informacje o urządzeniu
    """
    def __init__(self, name, price, stock, brand, warranty, power):
        Product.__init__(self, name, price, stock)
        self.brand = brand
        self.warranty = warranty
        self.power = power

    def calculate_discount(self):
        return 0.95 * self.price

    def display_info(self):
        Product.display_info(self)
        print(f'Firma: {self.brand}, gwarancja: {self.warranty}, moc: {self.power} watt')




def check_stock(products):
    """
    Metoda sprawdzająca czy zamawiane produkty są w magazynie oraz zapisująac szczegóły zamówienia
    do pliku order_details.txt
    :param products: słownik produktów (klucz – produkt, wartość – liczba sztuk)
    :return: Odpowiedni komunikat
    """
    total_price = 0
    order = open('order_details.txt', 'w')
    order.write("Szczegoly zamowienia: \n")
    for product in products:
        if product.stock >= products[product]:
            price_of_products = products[product]*product.price
            order.write(f'{product.name} : {price_of_products} zl za {products[product]} sztuk ({product.price}zl sztuka) \n')
            total_price += price_of_products
        else:
            order.write(f'Nie ma wystarczającej ilosci produktu o nazwie {product.name} w magazynie \n')
            return f"Nie ma wystarczającej ilosci produktu o nazwie {product.name} w magazynie"
        order.write( f"Pelna wartosc zamowienia: {total_price} \n")
    order.close()
    return f"Pelna wartosc zamowienia: {total_price}"


if __name__ == '__main__':
    book = Book("Dom z lisci" , 60, 10, "Mark Z. Danielewski", "Horror" ,736)
    smartphone = ElectronicDevice("IPhone 15", 4699, 500, "Apple", "1 rok", 10)
    print("Produkty:")
    print("Książka")
    book.display_info()
    print(f'Cena książki po obniżce: {book.calculate_discount()}')
    print("Urządzenie elektryczne")
    smartphone.display_info()
    print(f'Cena smartphonu po obniżce: {smartphone.calculate_discount()}')

    products = {smartphone: 50}
    products[book] = 10
    check_stock(products)

    print(f'Ilosc ksiazek w magazynie przed zmniejszeniem stanu magazynu: {book.stock}')
    book -= 2
    print(f'Ilosc ksiazek w magazynie po zmniejszeniu stanu magazynu: {book.stock}')


