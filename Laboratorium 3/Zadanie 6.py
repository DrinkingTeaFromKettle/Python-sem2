from collections import deque
from dataclasses import dataclass


@dataclass
class Patient:
    name: str
    surname: str
    age: int
    disease: str

    def __str__(self):
        return "Imię: " + self.name + "\nNazwisko: " + self.surname + "\nWiek: " + str(self.age) + "\nChoroba: "+ self.disease
def sortPatients(patients, sortType):
    match sortType:
        case "name":
            return deque(sorted(patients, key= lambda x: (x.surname, x.name, x.age)))
        case "age":
            return deque(sorted(patients, key=lambda x: (x.age, x.surname, x.name)))
        case _:
            return "Zły typ sortu"


if __name__ == '__main__':
    queue = deque([
        Patient("Katarzyna", "Alinowska", 29, "Grypa"),
        Patient("Alina", "Alinowska", 29, "Grypa"),
        Patient("Michał", "Michałowksi", 19, "Angina"),
        Patient("Jakub", "Jakubowksi", 42, "Migrena")
    ])
    while len(queue) > 0:
        print("Pacjenci")
        for i in queue:
            print(i)
            print("################")
        action = input("Jaką akcję chcesz podjąć: \n 1. Posortować pacjentów względem imienia i nazwiska\n 2. Posortować pacjentów względem wieku\n3. Przyjąć pacjenta (Pierwszy w kolejce)" )
        match action:
            case "1": queue = sortPatients(queue, "name")
            case "2": queue = sortPatients(queue, "age")
            case "3": queue.popleft()
            case _: print("Nie ma takiej akcji")


    print("Koniec przyjęć")
