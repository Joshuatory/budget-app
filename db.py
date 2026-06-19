import sqlite3


class Database:
    def __init__(self, db_name="budget.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cur = self.conn.cursor()

        # Transactions
        cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TEXT,
            month TEXT,
            type TEXT,
            category TEXT,
            amount REAL
        )
        """)

        # Budgets (monthly limits)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            month TEXT,
            category TEXT,
            limit_amount REAL
        )
        """)

        # Savings goals
        cur.execute("""
        CREATE TABLE IF NOT EXISTS savings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            target REAL,
            current REAL DEFAULT 0
        )
        """)

        self.conn.commit()

    # ---------------- TRANSACTIONS ----------------
    def insert_transaction(self, user_id, date, month, t_type, category, amount):
        cur = self.conn.cursor()
        cur.execute("""
        INSERT INTO transactions (user_id, date, month, type, category, amount)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, date, month, t_type, category, amount))
        self.conn.commit()

    def get_transactions(self, user_id, month):
        cur = self.conn.cursor()
        cur.execute("""
        SELECT type, category, amount
        FROM transactions
        WHERE user_id=? AND month=?
        """, (user_id, month))
        return cur.fetchall()

    # ---------------- SAVINGS ----------------
    def create_savings_goal(self, name, target):
        cur = self.conn.cursor()
        cur.execute("""
        INSERT INTO savings (name, target, current)
        VALUES (?, ?, 0)
        """, (name, target))
        self.conn.commit()

    def add_to_savings(self, goal_id, amount):
        cur = self.conn.cursor()
        cur.execute("""
        UPDATE savings
        SET current = current + ?
        WHERE id=?
        """, (amount, goal_id))
        self.conn.commit()

    def get_savings(self, goal_id):
        cur = self.conn.cursor()
        cur.execute("""
        SELECT name, target, current
        FROM savings
        WHERE id=?
        """, (goal_id,))
        return cur.fetchone()