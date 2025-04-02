import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute(
"""
    SELECT u.f_name, u.l_name, b.name
    FROM borrowed_books bb
    JOIN books b ON bb.book_id = b.id
    JOIN users u ON bb.user_id = u.id
"""
)
borrow = cursor.fetchall()
for bor in borrow:
    print(bor)
conn.close()


