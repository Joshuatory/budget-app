from db import Database
from core import BudgetCore
from excel import ExcelManager
from datetime import datetime


db = Database()
core = BudgetCore(db)
excel = ExcelManager()

user_id = 1  # temporary (no login yet)


while True:
    print("\n--- BUDGET APP ---")
    print("1. Add Expense")
    print("2. Add Income")
    print("3. Monthly Summary")
    print("4. Export Excel")
    print("5. Exit")

    choice = input("> ")

    month = datetime.now().strftime("%Y-%m")

    if choice == "1":
        cat = input("Category: ")
        amt = float(input("Amount: "))
        core.add_transaction(user_id, "Expense", cat, amt)

    elif choice == "2":
        cat = input("Category: ")
        amt = float(input("Amount: "))
        core.add_transaction(user_id, "Income", cat, amt)

    elif choice == "3":
        summary = core.get_month_summary(user_id, month)
        print(summary)

    elif choice == "4":
        excel.export_transactions(db, user_id, month)

    elif choice == "5":
        break