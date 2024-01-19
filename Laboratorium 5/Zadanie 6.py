from Person_Class import Person

class WantedList:
    wanted_list = {}

    @classmethod
    def add_person(self, person, crime):
        self.wanted_list[person] = crime

def add_last_seen( person,wanted_list, last_seen):
    if person in wanted_list:
        setattr(person,'last_seen', last_seen)
    else:
        print(f"{person.name} nie znajduje się na liście poszukiwanych.")

if __name__ == '__main__':
    WantedList.add_person(person= Person("Jessie", "Rocket Team", "Kobieta", "94040547786"), crime= "Stealing pokemon")
    WantedList.add_person(person=Person("James", "Rocket Team", "Mężczyzna", "93031715797"), crime= "Being stupid")

    print("Lista osób na liście poszukiwanych:")
    for person in WantedList.wanted_list:
        add_last_seen(person, WantedList.wanted_list, "Yesterday")
        print(f'{person.name} {person.surname} - {WantedList.wanted_list[person]}, last seen: {getattr(person, "last_seen")}')



