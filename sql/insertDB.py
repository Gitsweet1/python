import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()
# This is work!!!
#cursor.execute("INSERT INTO books (name, author, year) VALUES ('Pinokio', 'Saba Jepeto', 1976)")

cursor.executemany(
"""
    INSERT INTO books (name, author, year) VALUES (?, ?, ?)
""",
    [('Pinokio', 'Saba Jepeto', 1976),
     ('Marko', 'Father', 1981),
     ('Nils Holgerson', 'Comander Aka', 1989)]
)
conn.commit()
cursor.close()