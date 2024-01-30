import mysql.connector as mysql
from Employee import EmployeeDB
from Product import Product

def connect_to_db(db_name):
    try:
        connection = mysql.connect(host="localhost",
                                   user="root",
                                   passwd="",
                                   database=db_name)
        print("Połączono z bazą danych MySQL")
        return connection
    except mysql.Error as e:
        return None
        print(f"Błąd połączenia: {e}")

def create_employees(connection):
    if connection and connection.is_connected():
        cursor = connection.cursor()
        query = r"""
                CREATE TABLE IF NOT EXISTS employees (
                id INT NOT NULL AUTO_INCREMENT,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                department TEXT NOT NULL,
                PRIMARY KEY (id)
                ) ENGINE = InnoDB;
                """
        try:
            cursor.execute(query)
            connection.commit()
            print("Utworzono tablice")
        except mysql.Error as e:
            cursor.close()
            print(f"Nie udało się utworzyć tablicy: {e}")

def create_products(connection):
    if connection and connection.is_connected():
        cursor = connection.cursor()
        query = r"""
                CREATE TABLE IF NOT EXISTS products (
                id INT NOT NULL AUTO_INCREMENT,
                name TEXT NOT NULL,
                price FLOAT NOT NULL,
                category TEXT NOT NULL,
                PRIMARY KEY (id)
                ) ENGINE = InnoDB;
                """
        try:
            cursor.execute(query)
            connection.commit()
            print("Utworzono tablice")
        except mysql.Error as e:
            cursor.close()
            print(f"Nie udało się utworzyć tablicy: {e}")

def insert_employee(connection, employee):
    if connection and connection.is_connected():
        cursor = connection.cursor()
        query = """
                INSERT INTO employees (name, position, department)
                VALUES (%s, %s, %s);
                
                """
        val = (employee.name, employee.position, employee.department)
        try:
            cursor.execute(query, val)
            connection.commit()
            print("Wstawiono dane do tab")
        except mysql.Error as e:
            cursor.close()
            print(f"Nie udało się dodać rekordów: {e}")


def insert_product(connection, product):
    if connection and connection.is_connected():
        cursor = connection.cursor()
        query = """
                INSERT INTO products (name, price, category)
                VALUES (%s, %s, %s);

                """
        val = (product.name, product.price, product.category)
        try:
            cursor.execute(query, val)
            connection.commit()
            print("Wstawiono dane do tab")
        except mysql.Error as e:
            cursor.close()
            print(f"Nie udało się dodać rekordów: {e}")

if __name__ == '__main__':

    connection = connect_to_db("company")
    Gabi = EmployeeDB( 1,"Rozga Gabriela", "Menager", "Science")
    Mark = EmployeeDB(2, "Fischbach Mark", "Intern", "Movies")
    Cheese = Product(1, "Cheese", 10.00, "Dairy")
    Grapes = Product(2, "Grapes", 15.00, "Fruit")

    create_employees(connection)
    insert_employee(connection, Gabi)
    insert_employee(connection, Mark)

    create_products(connection)
    insert_product(connection, Cheese)
    insert_product(connection, Grapes)

    connection.close()
