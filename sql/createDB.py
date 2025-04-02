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
    CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    author TEXT,
    year INTEGER)
""")
conn.commit()
# Close the connection to DB
cursor.close()