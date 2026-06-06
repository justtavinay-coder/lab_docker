import os
import time

import mysql.connector


class ItemModel:
    def __init__(self):
        self.config = {
            'host': os.getenv('DB_HOST', 'db'),
            'user': os.getenv('DB_USER', 'lab_user'),
            'password': os.getenv('DB_PASS'),
            'database': os.getenv('DB_NAME', 'lab_db'),
            'charset': 'utf8mb4',
            'collation': 'utf8mb4_unicode_ci'
        }

    def _connect(self):
        last_error = None
        for _ in range(10):
            try:
                return mysql.connector.connect(**self.config)
            except mysql.connector.Error as error:
                last_error = error
                time.sleep(1)
        raise last_error

    def get_all_items(self):
        try:
            conn = self._connect()
            cursor = conn.cursor(dictionary=True)
            cursor.execute('SELECT name FROM items ORDER BY id')
            items = cursor.fetchall()
            cursor.close()
            conn.close()
            return items
        except Exception as e:
            print(f"Error: {e}")
            return []

    def add_item(self, name):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO items (name) VALUES (%s)', (name,))
        conn.commit()
        cursor.close()
        conn.close()
