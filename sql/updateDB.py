import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()
cursor.execute("""
    update books
    set year=1960
    where name="Nils Holgerson"
""")
conn.commit()
conn.close()