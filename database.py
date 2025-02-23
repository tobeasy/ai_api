import sqlite3

class Database:
    conn = None
    c = None

    def __init__(self):
        # create a database connection (file is created if it doesn't exist)
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        # Create table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS api_keys (
            Name TEXT NOT NULL,
            Api_key TEXT NOT NULL
        )
        ''')
        self.conn.commit()
        self.conn.close()

    def add_entry(self, name, api_key):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO api_keys (Name, Api_key) VALUES (?, ?)", (name, api_key))
        self.conn.commit()
        self.conn.close()