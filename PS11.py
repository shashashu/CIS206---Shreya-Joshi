import sqlite3

def create_table(cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS Fruits '
                   '(Name TEXT, '
                   'Weight REAL, '
                   'Cost REAL, '
                   'Quantity INTEGER, '
                   'Description TEXT)')  

def put_data(cursor):
    data = [
        ('Apples', 0.83, 0.5, 6, 'crunchy and good for pies'),
        ('Bananas', 0.75, 0.4, 8, 'delicious in protein smoothies'),
        ('Cuties', 0.95, 0.6, 4, 'cute baby oranges'),
        ('Cantalopes', 0.32, 0.8, 12, 'textured outside but very sweet'),
        ('Pineapples', 1.58, 2.5, 1, 'difficult to cut but delicious')
    ]
    cursor.executemany('INSERT INTO Fruits VALUES (?, ?, ?, ?, ?)', data)

def modify_column(cursor):
    cursor.execute("UPDATE Fruits SET Description='ABCD'")  

def update_rows(cursor):
    cursor.execute("UPDATE Fruits SET Description='XYZ' WHERE Name='Apples'") 
    cursor.execute("UPDATE Fruits SET Quantity=10 WHERE Name='Bananas'")

def delete_row(cursor):
    cursor.execute("DELETE FROM Fruits WHERE Name='Pineapples'")  

def questions(cursor):
    cursor.execute('SELECT * FROM Fruits')
    print("a. List all columns and rows:")
    print(cursor.fetchall())

    cursor.execute("SELECT * FROM Fruits WHERE Name='Bananas'")
    print("b. List all columns but using the where clause select only certain rows using a text column:")
    print(cursor.fetchall())

    cursor.execute('SELECT Description FROM Fruits') 
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

create_table(cursor)
print("table 'Fruits' created.")

input("type to add your own data: ")
put_data(cursor)
print("data added.")

modify_column(cursor)
print("column are now ABCD.")

update_rows(cursor)
print("apples and bananas updated.")

delete_row(cursor)
print("pineapple removed :( ")

questions(cursor)

conn.commit()
conn.close()
