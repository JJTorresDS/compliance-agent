import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Transactions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    user_id TEXT,
    amount REAL,
    country TEXT,
    date TEXT
)
""")

# Insert dummy data
data = [
    ("user_123", 100, "AR", "2024-01-01"),
    ("user_123", 5000, "US", "2024-01-05"),
    ("user_123", 7000, "MX", "2024-01-10"),
]

cursor.executemany("INSERT INTO transactions VALUES (?, ?, ?, ?)", data)

conn.commit()
conn.close()

print("DB ready ✅")