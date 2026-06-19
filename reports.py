import pandas as pd


class Reports:

    def __init__(self, store):
        self.store = store

    def export_excel(self, filename="export.xlsx"):
        df = self.store.get_transactions()
        df.to_excel(filename, index=False)
        print("Exported:", filename)

    def monthly_trend(self):
        df = self.store.get_transactions()

        df["amount"] = df.apply(
            lambda x: x["amount"] if x["type"] == "Income" else -x["amount"],
            axis=1
        )

        return df.groupby("month")["amount"].sum()