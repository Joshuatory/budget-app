from datetime import datetime, timedelta


class RecurringEngine:

    def __init__(self, store):
        self.store = store

    def due_today(self):
        df = self.store.get_recurring()
        today = datetime.now().date()

        due = []

        for _, row in df.iterrows():
            start = datetime.strptime(row["start_date"], "%Y-%m-%d").date()
            freq = row["frequency"]

            days = {
                "weekly": 7,
                "biweekly": 14,
                "triweekly": 21,
                "monthly": 30
            }.get(freq, 30)

            if (today - start).days % days == 0:
                due.append(row)

        return due