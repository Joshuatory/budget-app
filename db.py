class Database:
    def __init__(self):
        self.transactions = []

    def insert_transaction(self, user_id, date, month, t_type, category, amount):
        self.transactions.append({
            "user_id": user_id,
            "date": date,
            "month": month,
            "type": t_type,
            "category": category,
            "amount": amount
        })

    def get_transactions(self, user_id, month):
        return [
            (t["type"], t["category"], t["amount"])
            for t in self.transactions
            if t["user_id"] == user_id and t["month"] == month
        ]