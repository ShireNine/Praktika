##import sqlite3
##connection = sqlite3.connect('my_database.db')
##cursor = connection.cursor()
##cursor.execute('SELECT SUM (age) FROM Users')
##total_users = cursor.fetchone()[0]
##
##print('Общее количество пользоватлей', total_users)
##connection.close()


##import sqlite3
##connection = sqlite3.connect('my_database.db')
##cursor = connection.cursor()
##cursor.execute('SELECT SUM(age) FROM Users')
##total_age = cursor.fetchone()[0]
##
##print('Общая сумму возраство пользователей', total_age)
##connection.close()


##import sqlite3
##connection = sqlite3.connect('my_database.db')
##cursor = connection.cursor()
##cursor.execute('SELECT MIN(age) FROM Users')
##min_age = cursor.fetchone()[0]
##
##print('Минимальныи возраст среди пользователе', min_age)
##connection.close()


import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('SELECT MAX(age) FROM Users')
max_age = cursor.fetchone()[0]

print('Max возраст среди пользователе', max_age)
connection.close()
