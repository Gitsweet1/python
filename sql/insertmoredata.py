import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()
# This is work!!!
#cursor.execute("INSERT INTO books (name, author, year) VALUES ('Pinokio', 'Saba Jepeto', 1976)")

cursor.executemany(
"""
    INSERT INTO users (f_name, l_name) VALUES (?, ?)
""",
    [('Hertzi', 'Halevi'),
     ('Moni', 'Moshonov'),
     ('Obi', 'One Conobi')]
)

cursor.executemany(
"""
    INSERT INTO borrowed_books (user_id, book_id) VALUES (?, ?)
""",
    [(10, 1),
     (11, 5),
     (12, 9)]
)

conn.commit()
cursor.close()