from excel_store import ExcelStore
from budget_core import BudgetCore
from reports import Reports
from recurring import RecurringEngine
from datetime import datetime


store = ExcelStore()
core = BudgetCore(store)
reports = Reports(store)
recurring = RecurringEngine(store)


def menu():
    print("\n--- BUDGET APP ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Monthly Summary")
    print("4. Category Breakdown")
    print("5. Export Excel")
    print("6. Check Recurring")
    print("7. Exit")


while True:
    menu()
    choice = input("> ")

    month = datetime.now().strftime("%Y-%m")

    if choice == "1":
        amt = float(input("Amount: "))
        core.add_income(amt)

    elif choice == "2":
        cat = input("Category: ")
        amt = float(input("Amount: "))
        core.add_expense(amt, cat)

    elif choice == "3":
        print(core.get_month_summary(month))

    elif choice == "4":
        print(core.category_breakdown(month))

    elif choice == "5":
        reports.export_excel()

    elif choice == "6":
        due = recurring.due_today()
        for d in due:
            print("DUE:", d["category"], d["amount"])

    elif choice == "7":
        break