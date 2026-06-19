from datetime import datetime, timedelta


class RecurringEngine:
    """
    Handles recurring expenses like:
    Netflix, Rent, Subscriptions
    """

    def __init__(self, storage):
        self.storage = storage

    def get_due_today(self):
        """
        Checks which recurring expenses are due today.
        """

        df = self.storage.get_recurring()
        today = datetime.now().date()

        due = []

        for _, row in df.iterrows():

            start = datetime.strptime(row["start_date"], "%Y-%m-%d").date()
            freq = row["frequency"]

            interval = {
                "weekly": 7,
                "biweekly": 14,
                "triweekly": 21,
                "monthly": 30
            }.get(freq, 30)

            if (today - start).days % interval == 0:
                due.append(row)

        return due