from datetime import datetime
from collections import defaultdict


class BudgetCore:
    def __init__(self, db):
        self.db = db

    # -------------------------
    # TRANSACTIONS
    # -------------------------
    def add_transaction(self, user_id, t_type, category, amount):
        now = datetime.now()

        self.db.insert_transaction(
            user_id=user_id,
            date=now.strftime("%Y-%m-%d"),
            month=now.strftime("%Y-%m"),
            t_type=t_type,
            category=category,
            amount=amount
        )

    def get_month_summary(self, user_id, month):
        data = self.db.get_transactions(user_id, month)

        income = 0
        expenses = 0
        categories = defaultdict(float)

        for t_type, cat, amt in data:
            if t_type == "Income":
                income += amt
            else:
                expenses += amt
                categories[cat] += amt

        return {
            "income": income,
            "expenses": expenses,
            "balance": income - expenses,
            "categories": dict(categories)
        }

    # -------------------------
    # SAVINGS GOALS
    # -------------------------
    def update_savings(self, goal_id, amount):
        self.db.add_to_savings(goal_id, amount)

    def get_savings_progress(self, goal_id):
        return self.db.get_savings(goal_id)