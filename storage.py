import pandas as pd
import os

FILE = "data.xlsx"


class ExcelStorage:
    """
    This class is responsible for ALL Excel file operations.
    Think of it as your database layer.
    """

    def __init__(self):
        self._init_file()

    def _init_file(self):
        """
        Creates Excel file with required sheets if it doesn't exist.
        """

        if not os.path.exists(FILE):
            with pd.ExcelWriter(FILE, engine="openpyxl") as writer:

                # Transactions sheet (income + expenses)
                pd.DataFrame(columns=[
                    "datetime", "year", "month", "type",
                    "category", "amount"
                ]).to_excel(writer, sheet_name="transactions", index=False)

                # Savings goals
                pd.DataFrame(columns=[
                    "goal", "target", "current"
                ]).to_excel(writer, sheet_name="savings", index=False)

                # Recurring expenses
                pd.DataFrame(columns=[
                    "category", "amount", "frequency", "start_date"
                ]).to_excel(writer, sheet_name="recurring", index=False)

    # ---------------- TRANSACTIONS ----------------

    def add_transaction(self, row):
        """
        Adds a single transaction to Excel.
        """

        df = pd.read_excel(FILE, sheet_name="transactions")
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

        with pd.ExcelWriter(FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheet_name="transactions", index=False)

    def get_transactions(self):
        """Returns all transactions"""
        return pd.read_excel(FILE, sheet_name="transactions")

    # ---------------- SAVINGS ----------------

    def get_savings(self):
        return pd.read_excel(FILE, sheet_name="savings")

    def save_savings(self, df):
        with pd.ExcelWriter(FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheet_name="savings", index=False)

    # ---------------- RECURRING ----------------

    def get_recurring(self):
        return pd.read_excel(FILE, sheet_name="recurring")