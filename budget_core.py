from datetime import datetime
import pandas as pd


class BudgetCore:

    def __init__(self, store):
        self.store = store

    def add_income(self, amount, category="Income", note=""):
        self._add("Income", category, amount, note)

    def add_expense(self, amount, category, note=""):
        self._add("Expense", category, amount, note)

    def _add(self, t_type, category, amount, note):
        now = datetime.now()

        row = {
            "date": now.strftime("%Y-%m-%d"),
            "month": now.strftime("%Y-%m"),
            "type": t_type,
            "category": category,
            "amount": amount,
            "note": note
        }

        self.store.add_transaction(row)

    # ---------------- SUMMARY ----------------
    def get_month_summary(self, month):
        df = self.store.get_transactions()
        df = df[df["month"] == month]

        income = df[df["type"] == "Income"]["amount"].sum()
        expenses = df[df["type"] == "Expense"]["amount"].sum()

        return {
            "income": income,
            "expenses": expenses,
            "balance": income - expenses
        }

    # ---------------- CATEGORY BREAKDOWN ----------------
    def category_breakdown(self, month):
        df = self.store.get_transactions()
        df = df[(df["month"] == month) & (df["type"] == "Expense")]

        return df.groupby("category")["amount"].sum().to_dict()

    # ---------------- BUDGET CHECK ----------------
    def budget_status(self, month):
        budgets = self.store.get_budgets()
        expenses = self.category_breakdown(month)

        results = []

        for _, row in budgets.iterrows():
            cat = row["category"]
            limit = row["budget"]
            spent = expenses.get(cat, 0)

            results.append({
                "category": cat,
                "spent": spent,
                "budget": limit,
                "remaining": limit - spent
            })

        return results