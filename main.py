from core import BudgetCore
from db import Database
from excel import ExcelManager
from datetime import datetime


def main():
    db = Database()
    core = BudgetCore(db)
    excel = ExcelManager()

    user_id = 1  # simple single-user system

    while True:
        print("\n========================")
        print("      BUDGET APP")
        print("========================")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Monthly Summary")
        print("4. Category Breakdown")
        print("5. Export Excel")
        print("6. Exit")

        choice = input("> ")

        month = datetime.now().strftime("%Y-%m")

        if choice == "1":
            amt = float(input("Amount: "))
            core.add_income(user_id, "Income", "Income", amt)

        elif choice == "2":
            cat = input("Category: ")
            amt = float(input("Amount: "))
            core.add_expense(user_id, "Expense", cat, amt)

        elif choice == "3":
            print(core.get_month_summary(user_id, month))

        elif choice == "4":
            print(core.category_breakdown(user_id, month))

        elif choice == "5":
            excel.export_transactions(db, user_id, month)

        elif choice == "6":
            break


if __name__ == "__main__":
    main()