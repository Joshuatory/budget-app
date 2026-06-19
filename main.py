from storage import ExcelStorage
from budget import BudgetEngine
from recurring import RecurringEngine
from datetime import datetime


# ---------------- SETUP ----------------
storage = ExcelStorage()
budget = BudgetEngine(storage)
recurring = RecurringEngine(storage)

now = datetime.now()


# ---------------- MENU ----------------

while True:

    print("\n========================")
    print("     BUDGET SYSTEM")
    print("========================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Monthly Summary")
    print("4. Category Breakdown")
    print("5. Check Recurring")
    print("6. Add Savings")
    print("7. View Savings")
    print("8. Apply Recurring Expenses")
    print("9. Export Excel")
    print("10 . Exit")

    choice = input("> ")

    year = now.year
    month = now.month

    # ---------------- INCOME ----------------
    if choice == "1":
        cat = input("Category: ")
        amt = float(input("Amount: "))
        budget.add_income(cat, amt)

    # ---------------- EXPENSE ----------------
    elif choice == "2":
        cat = input("Category: ")
        amt = float(input("Amount: "))
        budget.add_expense(cat, amt)

    # ---------------- SUMMARY ----------------
    elif choice == "3":
        print(budget.monthly_summary(year, month))

    # ---------------- BREAKDOWN ----------------
    elif choice == "4":
        print(budget.category_breakdown(year, month))

    # ---------------- RECURRING ----------------
    elif choice == "5":
        due = recurring.get_due_today()

        for item in due:
            print("DUE:", item["category"], item["amount"])

    elif choice == "6":
        goal = input("Savings Goal: ")
        amt = float(input("Amount: "))
        budget.add_savings(goal, amt)

    elif choice == "7":
        print(budget.savings_summary())

    elif choice == "8":
        budget.apply_recurring()
        print("Recurring expenses applied.")

    elif choice == "9":
        storage.export_excel()

    # ---------------- EXIT ----------------
    elif choice == "10":
        break