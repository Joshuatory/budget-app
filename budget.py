from datetime import datetime
import pandas as pd


class BudgetEngine:
    """
    This class handles all calculations:
    - monthly summaries
    - filtering by year/month
    - savings logic
    """

    def __init__(self, storage):
        self.storage = storage

    # ---------------- ADD INCOME ----------------

    def add_income(self, category, amount):
        self._add_transaction("Income", category, amount)

    # ---------------- ADD EXPENSE ----------------

    def add_expense(self, category, amount):
        self._add_transaction("Expense", category, amount)

    def _add_transaction(self, t_type, category, amount):
        """
        Creates a properly formatted transaction row.
        """

        now = datetime.now()

        row = {
            "datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
            "year": now.year,
            "month": now.month,
            "type": t_type,
            "category": category,
            "amount": amount
        }

        self.storage.add_transaction(row)

    # ---------------- MONTH FILTERING ----------------

    def _get_month_data(self, year, month):
        """
        Filters transactions for a specific month + year.
        """

        df = self.storage.get_transactions()

        return df[
            (df["year"] == year) &
            (df["month"] == month)
        ]

    # ---------------- MONTHLY SUMMARY ----------------

    def monthly_summary(self, year, month):
        """
        Returns income, expenses, and balance for a month.
        """

        df = self._get_month_data(year, month)

        income = df[df["type"] == "Income"]["amount"].sum()
        expenses = df[df["type"] == "Expense"]["amount"].sum()

        return {
            "income": float(income),
            "expenses": float(expenses),
            "balance": float(income - expenses)
        }

    # ---------------- CATEGORY BREAKDOWN ----------------

    def category_breakdown(self, year, month):
        """
        Shows spending per category for a month.
        """

        df = self._get_month_data(year, month)
        df = df[df["type"] == "Expense"]

        return df.groupby("category")["amount"].sum().to_dict()