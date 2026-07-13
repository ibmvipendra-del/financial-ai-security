import sqlite3
from src import config


class ConversationMemory:

    def __init__(self):

        self.conn = sqlite3.connect(config.DATABASE_PATH)

        self.create_table()

    def create_table(self):

        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversation_memory(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            role TEXT,

            message TEXT
        )
        """)

        self.conn.commit()

    def add_message(self, role, message):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT INTO conversation_memory(role,message)
            VALUES(?,?)
            """,
            (role, message),
        )

        self.conn.commit()

    def get_history(self):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT role,message
            FROM conversation_memory
            ORDER BY id
            """
        )

        return cursor.fetchall()

    def clear(self):

        cursor = self.conn.cursor()

        cursor.execute(
            "DELETE FROM conversation_memory"
        )

        self.conn.commit()