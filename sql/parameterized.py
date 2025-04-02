import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()
'''
def book_name():
    bn = input("What is the book name you want to search?\n")
    cursor.execute(
        """
        SELECT * FROM books WHERE name = ?
        """,
        (bn,)
    )
    return cursor.fetchall()

books = book_name()
for book in books:
    print(book)

conn.close()

'''
def book_name():
    bn = input("What is the book name you want to search?\n")
    cursor.execute(
    """
    SELECT * FROM books WHERE name = ?
    """
    ,(bn,))

book_name()
books = cursor.fetchall()
for book in books:
    print(book)
conn.close()
