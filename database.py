import sqlite3
import os

# Create database folder if it doesn't exist
if not os.path.exists("database"):
    os.makedirs("database")

# Connect to SQLite database
conn = sqlite3.connect("database/library.db")
cursor = conn.cursor()

# Create books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    category TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
""")

conn.commit()
conn.close()

print("Database and books table created successfully!")