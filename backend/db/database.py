import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None

    def _connect(self):
        """Establishes a connection to the database."""
        try:
            self.conn = sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def initialize_tables(self):
        """Creates the necessary tables if they do not exist."""
        self._connect()
        if self.conn:
            try:
                cursor = self.conn.cursor()
                
                # Create merchants table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS merchants (
                        merchant_mapping_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        merchant_name TEXT,
                        merchant_name_statement TEXT,
                        category TEXT
                    )
                """)

                # Create transactions table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT,
                        original_desc TEXT,
                        amount REAL,
                        category TEXT,
                        account_source TEXT,
                        merchant_mapping_id INTEGER,
                        is_recurring BOOLEAN,
                        FOREIGN KEY(merchant_mapping_id) REFERENCES merchants(merchant_mapping_id)
                    )
                """)

                self.conn.commit()
                print("Tables initialized successfully.")
            except sqlite3.Error as e:
                print(f"Error creating tables: {e}")
            finally:
                self.conn.close()

if __name__ == "__main__":
    # Ensure data directory exists
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    db_path = os.path.join(data_dir, "expenses.db")
    db_manager = DatabaseManager(db_path)
    db_manager.initialize_tables()
