import csv
from collections import namedtuple
import re

class NameException(Exception):
    pass
class EmailException(Exception):
    pass
class indexException(Exception):
    pass
class GradeException(Exception):
    pass
class Student:
    studenci = []
    def __init__(self, imie, nazwisko, numer_indeksu, email, oceny):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.email = email
        self.oceny = oceny

ocena_tuple = namedtuple("Przedmiot", ("nazwa", "ocena"))

def wczytaj_studentow(sciezka):
    try:
        plik = open(sciezka, 'r')
        czytnik = csv.reader(plik, delimiter= ';')
    except OSError:
        print("Nie można otworzyć pliku")
    else:
        for row in czytnik:
            oceny_tab = []
            imie, nazwisko, numer_indeksu, email, *oceny = row
            for o in oceny:
                try:
                    o = eval(o)
                except SyntaxError:
                    print("Niepoprawny format ocen")
                else:
                    ocena = ocena_tuple(o[0],o[1])
                    oceny_tab.append(ocena)
            Student.studenci.append(Student(imie, nazwisko, numer_indeksu, email, oceny_tab))
        return Student.studenci

def wyswietl_student(student):
    print(f"Imie: {student.imie}, Nazwisko: {student.nazwisko}, Nr. Indeksu:  {student.numer_indeksu}, email: {student.email}, Oceny: {student.oceny}.2f")

def zapisz_studenta(sciezka, imie, nazwisko, numer_indeksu, email, oceny):
    if not nazwisko[0].isupper() or not imie[0].isupper():
        raise NameException("Imie i nazwisko studenta musi zaczanac sie od duzej litery")
    if not email.endswith('@pollub.edu.pl'):
        raise EmailException("Email musi byc zakonczony '@pollub.edu.pl'")
    if int(numer_indeksu) < 0:
        raise indexException("Indeks studenta nie moze byc ujemny")
    try:
        plik = open(sciezka, 'a')
    except OSError:
        print("Nie można otworzyć pliku")
    else:
        plik.write(f"\n{imie};{nazwisko};{numer_indeksu};{email}")
        for o in oceny:
            plik.write(f";('{o.nazwa}',{o.ocena})")
        student = Student(imie, nazwisko, numer_indeksu, email, oceny)
        wyswietl_student(student)
        Student.studenci.append(student)

def wyswietl_oceny(nazwisko):
    if not nazwisko[0].isupper():
        raise NameException("Nazwisko studenta musi zaczanac sie od duzej litery")
    for student in Student.studenci:
        if student.nazwisko == nazwisko:
            print(f"\nOceny {student.nazwisko}: {student.oceny}")
            return
    print(f"Student o nazwisku {nazwisko} nie istnieje w bazie.")

def srednia_ocen(oceny):
    suma = 0
    for o in oceny:
        suma += float(o.ocena)
    return suma/len(oceny)


def posortuj_po_sredniej():
    studenci_temp = Student.studenci
    for s in studenci_temp:
        s.srednia = srednia_ocen(s.oceny)
    posortowani_studenci = sorted(Student.studenci, key=lambda student: student.srednia, reverse=True)
    print("\nPosortowana lista studentów:")
    for student in posortowani_studenci:
        wyswietl_student(student)
        print("Srednia: " + str(student.srednia))

if __name__ == '__main__':
    sciezka = ""

    while True:
        print("a. Wczytaj listę studentów z pliku CSV")
        print("b. Zapisz nowego studenta")
        print("c. Wyświetl oceny studenta (należy najpierw wczytać studentów z pliku)")
        print("d. Wyświetl posortowaną listę studentów")
        print("e. Wyjście z programu")
        wybor = input("Wybór: ")
        match wybor:
            case "a":
                if sciezka == "":
                    sciezka = input("Podaj ścieżkę do pliku CSV: ")
                wczytaj_studentow("studenci.csv")
                for s in Student.studenci:
                    wyswietl_student(s)
            case "b":
                if sciezka == "":
                    sciezka = input("Podaj ścieżkę do pliku CSV: ")
                imie = input("Podaj imie studenta: ")
                nazwisko = input("Podaj nazwisko studenta: ")
                numer_indeksu = int(input("Podaj numer indeksu: "))
                email = input("Podaj adres email w domenie @pollub.edu.pl: ")
                number = input("Ile ocen chcesz podać?: ")
                oceny = []
                for i in range(number):
                    p = input("Podaj przedmiot: ")
                    o = input("Podaj ocenę: ")
                    if not isinstance(o, int) and not isinstance(o, float):
                        raise GradeException("Ocena musi być wartością numeryczną")
                    ocena = ocena_tuple(o[0], o[1])
                    oceny.append(ocena)
                nowy_student = zapisz_studenta(sciezka, imie, nazwisko, numer_indeksu, email, oceny)
            case "c":
                nazwisko = input("Podaj nazwisko studenta, którego oceny chcesz wyświetlić: ")
                wyswietl_oceny(nazwisko)
            case "d":
                posortuj_po_sredniej()
            case "e": break
