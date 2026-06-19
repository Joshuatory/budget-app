from db import Database
from core import BudgetCore
from datetime import datetime


db = Database()
core = BudgetCore(db)

user_id = 1


while True:
    print("\n--- BUDGET APP ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Exit")

    choice = input("> ")
    month = datetime.now().strftime("%Y-%m")

    if choice == "1":
        cat = input("Category: ")
        amt = float(input("Amount: "))
        core.add_income(user_id, cat, amt)

    elif choice == "2":
        cat = input("Category: ")
        amt = float(input("Amount: "))
        core.add_expense(user_id, cat, amt)

    elif choice == "3":
        income, expenses, balance = core.summary(user_id, month)
        print("\nIncome:", income)
        print("Expenses:", expenses)
        print("Balance:", balance)

    elif choice == "4":
        break