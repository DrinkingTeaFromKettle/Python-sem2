from statistics import mean, median

def funkcja_zad_4(*args):
    """
    Funkcja sprawdzająca typ argumentów i zwracająca średnią dla liczb,
    medianę długości dla napisów oraz komunikat dla innych typu
    :param args: liczby, napisy bądz inne elementy których typ zostanie sprawdzony
    :return: średnią dla liczb, medianę ilości znaków dla napisów oraz komunikat
    dla innych typów
    """
    if all((isinstance(a, int) or isinstance(a, float) ) for a in args):
        return mean(args)
    if all(isinstance(a, str) for a in args):
        return median(len(a) for a in args)
    return "Argumenty nie są liczbami ani napisami"

if __name__ == '__main__':
    print(funkcja_zad_4(1, 6, 3, -7, 2.8, -3.33333333333333333333333333333333333333))

    print(funkcja_zad_4("scholar", "hammer", "blade", "diet", "confront", "think"))

    print(funkcja_zad_4(4, "soldier", object))