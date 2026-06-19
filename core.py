from datetime import datetime


class BudgetCore:

    def __init__(self, db):
        self.db = db

    def add_income(self, user_id, category, amount):
        self.db.insert_transaction(
            user_id,
            datetime.now().strftime("%Y-%m-%d"),
            datetime.now().strftime("%Y-%m"),
            "Income",
            category,
            amount
        )

    def add_expense(self, user_id, category, amount):
        self.db.insert_transaction(
            user_id,
            datetime.now().strftime("%Y-%m-%d"),
            datetime.now().strftime("%Y-%m"),
            "Expense",
            category,
            amount
        )

    def summary(self, user_id, month):
        data = self.db.get_transactions(user_id, month)

        income = 0
        expenses = 0

        for t_type, cat, amt in data:
            if t_type == "Income":
                income += amt
            else:
                expenses += amt

        return income, expenses, income - expenses