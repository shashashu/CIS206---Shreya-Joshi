import sqlite3

def createtable(cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS Fruits '
                   '(Name TEXT, '
                   'Weight REAL, '
                   'Cost REAL, '
                   'Quantity INTEGER)')

def putdata(cursor):
    data = [
        ('Apples', 0.83, 0.5, 6),
        ('Bananas', 0.75, 0.4, 8),
        ('Cuties', 0.95, 0.6, 4),
        ('Cantalopes', 0.32, 0.8, 12),
        ('Pineapples', 1.58, 2.5, 1)
    ]
    cursor.executemany('INSERT INTO Fruits VALUES (?, ?, ?, ?)', data)

def questions(cursor):
    cursor.execute('SELECT * FROM Fruits')
    print("a. List all columns and rows:")
    print(cursor.fetchall())

    cursor.execute("SELECT * FROM Fruits WHERE Name='Banana'")
    print("b. List all columns but using the where clause select only certain rows using a text column:")
    print(cursor.fetchall())

    cursor.execute('SELECT Name FROM Fruits')
    print("c. List only the text columns but all the rows:")
    print(cursor.fetchall())

    cursor.execute('SELECT SUM(Weight) FROM Fruits')
    print("d. Sum of the Weight column:")
    print(cursor.fetchone()[0])

    cursor.execute('SELECT COUNT(*) FROM Fruits')
    print("e. Count of the rows in the table:")
    print(cursor.fetchone()[0])

    cursor.execute('SELECT * FROM Fruits')
    print("f. Cursor showing all rows and columns:")
    for row in cursor.fetchall():
        print(row)

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

createtable(cursor)
putdata(cursor)
questions(cursor)
conn.commit()
conn.close()
