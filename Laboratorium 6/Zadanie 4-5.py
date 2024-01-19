import types
from abc import ABC, abstractmethod
import random

class Animal(ABC):
    """
    Klasa abstrakcyjna reprezentująca zwierzę
    Attributes
    ----------
    name: str
        nazwa zwierzęcia
    occurence: lista str
        miejsca występowania
    is_protected: boolean
        czy zwierze jest pod ochroną
    Methods
    -------
    info()
     abstrakcyjna metoda wyświetlająca informacje o zwierzęciu
    """
    def __init__(self, name, occurrence, is_protected):
        self.name = name
        self.occurrence = occurrence
        self.is_protected = is_protected

    @abstractmethod
    def info(self):
        pass

class Predator(Animal):
    """
    Klasa opisująca mięsożercę, która dziedziczy po klasie Animal
    Attributes
    ----------
    hunting_time: str
        czas, w którym zwierzę poluje
       Methods
    -------
    info()
        Metoda wyświetlająca informacje o mięsożercy
    hunt()
        Metoda wyślwietlająca informację, że mięsożerca rozpoczyna polowanie
    """
    def __init__(self, name, occurrence, is_protected, hunting_time):
        Animal.__init__(self, name, occurrence, is_protected)
        self.hunting_time = hunting_time

    def info(self):
        print(f"Nazwa zwierzęcia: {self.name}\nWystępowanie: {', '.join(self.occurrence)}\nChroniony: {self.is_protected}\nCzas polowania : {self.hunting_time}")

    def hunt(self):
        print(f"{self.name} rozpoczyna polowanie")

class Herbivore(Animal):
    """
    Klasa opisująca roślinożercę, która dziedziczy po klasie Animal
    Attributes
    ----------
    favourite_plants: lista str
        lista ulubionych roślin do jedzenia
       Methods
    -------
    info()
        Metoda wyświetlająca informacje o roślinożercy
    search()
        Metoda wyświetlająca informację o rozpoczęciu poszukiwania losowej ulubionej rośliny
    """
    def __init__(self, name, occurrence, is_protected, favourite_plants):
        Animal.__init__(self, name, occurrence, is_protected)
        self.favourite_plants = favourite_plants

    def info(self):
        print(f"Nazwa zwierzęcia: {self.name}\nWystępowanie: {', '.join(self.occurrence)}\nChroniony: {self.is_protected}\nUlubione rośliny: {', '.join(self.favourite_plants)}")

    def search(self):
        chosen_plant = random.choice(self.favourite_plants)
        print(f"{self.name} rozpoczyna poszukiwanie {chosen_plant}")

class Omnivore(Predator, Herbivore):
    """
    Klasa opisująca wszystkożercę, która dziedziczy po klasach Herbivore i Predator
       Methods
    -------
    info()
        Metoda wyświetlająca informacje o wszystkożercy
    """
    def __init__(self, name, occurrence, is_protected, hunting_time, favourite_plants):
        Predator.__init__(self, name, occurrence, is_protected, hunting_time)
        Herbivore.__init__(self, name, occurrence, is_protected, favourite_plants)

    def info(self):
        print(f"Nazwa zwierzęcia: {self.name}\nWystępowanie: {', '.join(self.occurrence)}\nChroniony: {self.is_protected}\nUlubione rośliny: {', '.join(self.favourite_plants)}\nCzas polowania : {self.hunting_time}")

def feeding_routine(self, time_of_day):
    """
    Funkcja wybierająca sposób zdobywania pożywienia na podstawie pory dnia
    :param self: obiekt klasy Omnivore
    :param time_of_day: pora dnia przekazana jako string
    """
    if time_of_day.lower() in ["dzien", "ranek"]:
        self.search()
    elif time_of_day.lower() in ["noc","wieczor"]:
        self.hunt()
    else:
        print("Niepoprawna pora dnia")

if __name__ == '__main__':
    horse = Herbivore('Szwedzki koń gorącokrwisty', ['Środkowa Szwecja', 'Południowa Szwecja'], False, ['Marchew', 'Jabklo', 'Banan'])
    print(horse.info())
    leopard = Predator('Lampart amurski', ['Rosyjski Daleki Wschód', 'Północno-Wschodnie Chiny'], True, 'Późny wieczór i noc')
    print(leopard.info())
    crow = Omnivore('Wrona siwa', ['Europa', 'Azja'], False, 'Dzień', ['Jagody'])
    crow.info()

    crow.feeding_routine = types.MethodType(feeding_routine, crow)

    crow.feeding_routine("dzien")