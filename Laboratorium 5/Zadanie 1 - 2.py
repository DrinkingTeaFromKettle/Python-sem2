from Person_Class import Person

if __name__ == '__main__':
    person_dict = dict()
    Ola = Person("Aleksandra", "Szczepańska", "Kobieta", "99050801456")
    print(f'Wiek Oli: {Ola.getAge()}' )
    print(f'Ilość ludzi po dodaniu {Ola.name} : {Person.number_of_people}')
    person_dict[Person.number_of_people] = Ola
    Piotr = Person("Piotr", "Wyszkowski", "Mężczyzna", "70012737991")
    print(f'Wiek Piotra: {Piotr.getAge()}')
    print(f'Czy Piort ma nazwisko dwuczłonowe? : {Piotr.is_surname_two_part()}')
    print(f'Ilość ludzi po dodaniu {Piotr.name} : {Person.number_of_people}')
    person_dict[Person.number_of_people] = Piotr
    Mariola = Person("Mariola", "Gierska-Skoczkowska", "Kobieta", "03292451619")
    print(f'Wiek Marioli: {Mariola.getAge()}')
    print(f'Czy Mariola ma nazwisko dwuczłonowe?: {Mariola.is_surname_two_part()}')
    print(f'Ilość ludzi po dodaniu {Mariola.name} : {Person.number_of_people}')
    person_dict[Person.number_of_people] = Mariola

    print("Słownik osob:")
    for person in person_dict :
        print(f'{person}: {person_dict[person].name}')


