import sqlite3

# Create the DB file
conn = sqlite3.connect("books.db")
# The cursor let us make sql commands on DB's
cursor = conn.cursor()
# Execute run the commands / query (one command).
# You also have the executemany to run multiple commands
#cursor.execute("CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY_KEY, name STRING, author STRING, year INTEGER)")
cursor.execute(
"""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    f_name TEXT,
    l_name TEXT)
""")
cursor.execute("INSERT INTO sqlite_sequence (name, seq) VALUES ('users', 99)")

cursor.execute(
"""
    CREATE TABLE IF NOT EXISTS borrowed_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    book_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (book_id) REFERENCES books (id))
""")
cursor.execute("INSERT INTO sqlite_sequence (name, seq) VALUES ('borrowed_books', 999)")

conn.commit()
# Close the connection to DB
cursor.close()