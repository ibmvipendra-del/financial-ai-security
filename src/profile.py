import sqlite3
from pathlib import Path
from src import config


class UserProfile:

    def __init__(self):

        Path(config.DATABASE_PATH).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.conn = sqlite3.connect(config.DATABASE_PATH)

        self.create_table()

    def create_table(self):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_profile (

                id INTEGER PRIMARY KEY,

                name TEXT,

                age INTEGER,

                monthly_income REAL,

                monthly_expense REAL,

                savings REAL,

                goal TEXT
            )
            """
        )

        self.conn.commit()

    def save_profile(
        self,
        name,
        age,
        income,
        expense,
        savings,
        goal,
    ):

        cursor = self.conn.cursor()

        cursor.execute("DELETE FROM user_profile")

        cursor.execute(
            """
            INSERT INTO user_profile
            (
                name,
                age,
                monthly_income,
                monthly_expense,
                savings,
                goal
            )

            VALUES
            (?, ?, ?, ?, ?, ?)
            """,
            (
                name,
                age,
                income,
                expense,
                savings,
                goal,
            ),
        )

        self.conn.commit()

    def get_profile(self):

        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT * FROM user_profile LIMIT 1"
        )

        return cursor.fetchone()