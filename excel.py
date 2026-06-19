import pandas as pd


class ExcelManager:

    # EXPORT ALL DATA
    def export_transactions(self, db, user_id, month, filename="budget_export.xlsx"):
        data = db.get_transactions(user_id, month)

        df = pd.DataFrame(data, columns=["Type", "Category", "Amount"])
        df.to_excel(filename, index=False)

        print(f"Exported to {filename}")

    # IMPORT CSV BACK INTO SYSTEM
    def import_transactions(self, db, user_id, csv_file):
        df = pd.read_csv(csv_file)

        for _, row in df.iterrows():
            db.insert_transaction(
                user_id,
                row["date"] if "date" in df.columns else "2026-01-01",
                row.get("month", "2026-01"),
                row["type"],
                row["category"],
                float(row["amount"])
            )

        print("Import complete")