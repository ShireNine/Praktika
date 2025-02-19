import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM Users')
one = cursor.fetchone()
print(one)

first = cursor.fetchmany(5)
print(first)

alld = cursor.fetchall()
print(alld)
