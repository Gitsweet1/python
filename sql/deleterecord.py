import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()
cursor.execute("""
    delete from books
    where name="Nils Holgerson"
""")
conn.commit()
print(cursor.rowcount)
conn.close()