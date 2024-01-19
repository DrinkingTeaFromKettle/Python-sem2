def funkcja_formatujaca(napisy):
    """
    Funkcja formatująca napis aby zaczynał się duża literą i kończył kropką
    :param napisy: napis do sformatowania
    :return: sformatowany napis
    """
    sformatuj = lambda napis: napis.capitalize() + ("" if napis[-1] == "." else ".")
    napisy = map(sformatuj, napisy)
    return list(napisy)

if __name__ == '__main__':
    napisy = ("napis", "Napis rozpoczety duza litera", "napis zakonczony kropka.")
    print(funkcja_formatujaca(napisy))