import xml.etree.ElementTree as ET
from random import randint


class BankAccount:
    def __init__(self, name, surname, account_number, account_type, balance):
        self.name = name
        self.surname = surname
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Wpłacono {amount}zl na konto")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Wypłacono {amount}zl z konta")
        else:
            print("Brak wystarczających środków na koncie")

    def check_balance(self):
        print(f"Środki na koncie {self.name} {self.surname}: {self.balance}")

def add_accounts_to_xml(path, accounts):
    root = ET.Element("Bank")
    for account in accounts:
        account_element = ET.SubElement(root, "Account")
        ET.SubElement(account_element, "Name").text = account.name
        ET.SubElement(account_element, "Surname").text = account.surname
        ET.SubElement(account_element, "AccountNumber").text = account.account_number
        ET.SubElement(account_element, "AccountType").text = account.account_type
        ET.SubElement(account_element, "Balance").text = str(account.balance)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    tree.write(path)

if __name__ == "__main__":
    range_start = 10 ** (25)
    range_end = (10 ** 26) - 1
    accounts = []
    accounts.append( BankAccount("Janina", "Borowik", str(randint(range_start,range_end)), "Personal", 10500))
    accounts.append(BankAccount("Marek", "Mickiewicz", str(randint(range_start,range_end)), "Savings", 50001))
    accounts.append(BankAccount("Boleslaw", "Prus", str(randint(range_start,range_end)), "Savings", 120003))
    add_accounts_to_xml("Bank.xml",accounts)