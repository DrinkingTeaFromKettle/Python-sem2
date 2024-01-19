import csv

class Employee:
    def __init__(self, name, surname, gender, address, salary):
        self.name = name
        self.surname = surname
        self.__setgender(gender)
        self.address = address
        self.salary = salary

    def __getgender(self):
        return self.__gender

    def __setgender(self, gender):
        if gender in "K, M":
            self.__gender = gender
        else:
            print("Jako płeć podaj K lub M")

    @classmethod
    def load_from_csv(cls, file_path):
        employees_list = []
        file = open(file_path, newline='')
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            employee = Employee(row[0],row[1],row[2],row[3],float(row[4]))
            employees_list.append(employee)
        return employees_list

    @staticmethod
    def average_salary(employees_list):
        if not employees_list:
            return "Lista pracownikow jest pusta"
        total_salary = sum(employee.salary for employee in employees_list)
        average_salary = total_salary / len(employees_list)
        return f"Średnia pensja w firmie wynosi: {average_salary:.2f}"



if __name__ == '__main__':
    employee_list = Employee.load_from_csv("employees.csv")
    for employee in employee_list:
        print(f"{employee.name} {employee.surname}")
    print(Employee.average_salary(employee_list))
    print("Wynik wpisania płci pracownika jako 'Kobieta':")
    Kasia = Employee("Katarzyna", "Wiącek", "Kobieta", "Kormanice 73b", 5000)
