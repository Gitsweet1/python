import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()
cursor.execute("""
    select * from books
""")
books = cursor.fetchall()
for book in books:
    print(book)
conn.close()