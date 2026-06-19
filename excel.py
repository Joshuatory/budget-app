import pandas as pd
import os

FILE = "data/budget.xlsx"


class ExcelStore:

    def __init__(self):
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(FILE):
            with pd.ExcelWriter(FILE, engine="openpyxl") as writer:
                pd.DataFrame(columns=[
                    "date", "month", "type", "category", "amount", "note"
                ]).to_excel(writer, sheet_name="transactions", index=False)

                pd.DataFrame(columns=[
                    "month", "category", "budget"
                ]).to_excel(writer, sheet_name="budgets", index=False)

                pd.DataFrame(columns=[
                    "goal", "target", "current"
                ]).to_excel(writer, sheet_name="savings", index=False)

                pd.DataFrame(columns=[
                    "category", "amount", "frequency", "start_date"
                ]).to_excel(writer, sheet_name="recurring", index=False)

    # ---------------- TRANSACTIONS ----------------
    def add_transaction(self, row):
        df = pd.read_excel(FILE, sheet_name="transactions")

        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

        with pd.ExcelWriter(FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheet_name="transactions", index=False)

    def get_transactions(self):
        return pd.read_excel(FILE, sheet_name="transactions")

    # ---------------- BUDGETS ----------------
    def get_budgets(self):
        return pd.read_excel(FILE, sheet_name="budgets")

    def save_budgets(self, df):
        with pd.ExcelWriter(FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheet_name="budgets", index=False)

    # ---------------- SAVINGS ----------------
    def get_savings(self):
        return pd.read_excel(FILE, sheet_name="savings")

    def save_savings(self, df):
        with pd.ExcelWriter(FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheet_name="savings", index=False)

    # ---------------- RECURRING ----------------
    def get_recurring(self):
        return pd.read_excel(FILE, sheet_name="recurring")