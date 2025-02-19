##import sqlite3
##
##connection = sqlite3.connect('my_database.db')
##cursor = connection.cursor()
##
##cursor.execute ('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'nesfgefe@mail.ru', 28))
##connection.commit()
##connection.close()

##import sqlite3
##connection = sqlite3.connect('my_database.db')
##cursor = connection.cursor()
##cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser'))
##
##connection.commit()
##connection.close()


import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser'))


connection.commit()
connection.close()
