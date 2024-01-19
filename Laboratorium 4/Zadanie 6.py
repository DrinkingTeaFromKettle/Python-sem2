import datetime

def zapisz_log(func):
    """
    Funkcja nadrzędna do funkcji dekorującej

    :param func: funkcja która zostanie udekorowana
    :return: Funkcję dekorującą
    """
    def zapisz_log_dekorator(*args, **kwargs):
        """
        Funkcja dekorujaca zapisująca nazwę funkcji, datę i godzinę
                 wywowałnia funkcji którą dekoruje oraz argumentów przez nią wywoływanych
                 do pliku o nazwie log.txt

        :param args:
        :param kwargs:
        """
        log = open('log.txt', 'a')
        log.write("Nazwa: " + func.__name__)
        log.write("\nData: " + str(datetime.datetime.now().date()))
        log.write("\nGodzina: " + str(datetime.datetime.now().hour))
        log.write("\nArgumenty: " + str(args) + str(kwargs))
    return zapisz_log_dekorator

@zapisz_log
def funkcja(*args, **kwargs):
    """
    Funkcja wyświetlająca przekazane do niej wartości

    :param args:
    :param kwargs:
    """
    print("Jestem funkcja z argumentami: " + str(args) + str(kwargs))

if __name__ == '__main__':
    funkcja('argument 1', 2, object)
