class MathCalculations:
    @classmethod
    def sum_of_natural(cls, n):
        if n > 0:
            sum = 0
            for number in range(n+1):
                sum += number
            return sum
        else:
            return "Nie podano liczby naturalnej"
    @classmethod
    def factorial(cls, n):
        if n == 0 or n == 1:
            return f"Silnia z {n} wynosi: 1"
        if n > 1:
            fac = 1
            for number in range(2,n+1):
                fac *= number
            return fac
        else:
            return "Nie podano liczby wiekszej lub równej 0"

if __name__ == '__main__':
    print(f'Suma liczb od 1 do 5: {MathCalculations.sum_of_natural(5)}')
    print(f'Suma liczb od 1 do 5: {MathCalculations.factorial(5)}')

    print(f'Wynik funkcji sumy dla liczby ujemnej -5: {MathCalculations.sum_of_natural(-5)}')
    print(f'Wynik funkcji silni dla liczby ujemnej -5: {MathCalculations.factorial(-5)}')