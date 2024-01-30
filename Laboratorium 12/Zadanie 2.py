import sqlalchemy
from sqlalchemy import MetaData, Table, select, func
from sqlalchemy.engine import URL
import json

if __name__ == "__main__":
    url_object = URL.create(
        "mariadb+pymysql",
        username="root",
        password="",  # plain (unescaped) text
        host="localhost",
        database="company",
    )
    engine = sqlalchemy.create_engine(url_object)
    connection = engine.connect()


    metadata = MetaData(bind=None)
    employee = Table(
        'employees',
        metadata,
        autoload=True,
        autoload_with=engine
    )
    products = Table(
        'products',
        metadata,
        autoload=True,
        autoload_with=engine
    )
    query = select(employee)
    exe = connection.execute(query)
    employees_table = exe.fetchall()
    for st in employees_table:
        print(st)
    query = select(products)
    exe = connection.execute(query)
    products_table = exe.fetchall()
    for st in products_table:
        print(st)
    query = select(employee).order_by('name')
    exe = connection.execute(query)
    sorted_employees = exe.fetchall()
    print("Sorted employees:")
    for st in sorted_employees:
        print(st)



    json_employees = [{"id": employee[0], "name": employee[1], "position": employee[2], "department": employee[3]}
                      for employee in sorted_employees]

    with open("employees.txt", 'w') as file:
        json.dump(json_employees, file, indent=2)

    average_price= select(func.avg(products.c.price))
    print(f"Average price:{connection.execute(average_price).scalar()}")
