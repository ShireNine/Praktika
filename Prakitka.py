import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM Users WHERE age IS NULL')
unknow = cursor.fetchall()

for user in unknow:
    print(user)

connection.close()
