import datetime

class Person:

    number_of_people = 0

    list_of_people = []

    def __init__(self, name, surname, gender, pesel):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.pesel = pesel
        Person.number_of_people += 1
        #print(f'Ilość ludzi po dodaniu {self.name} : {self.number_of_people}')
        Person.list_of_people.append(self)
        #print("Lista ludzi:")
        #for person in Person.list_of_people :
        #    print(person.name + " " + person.surname)


    def getAge(self):
        year = int(self.pesel[:2])
        month = int(self.pesel[2:4])
        if(month > 20):
            return datetime.datetime.now().year - 2000 - year
        else:
            return datetime.datetime.now().year - 2000 + (100 - year)

    def is_surname_two_part(self):
        return '-' in self.surname
