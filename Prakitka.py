##import sqlite3
##connection = sqlite3.connect('my_database.db')
##cursor = connection.cursor()
##
##try:
##    cursor.execute('BEGIN')
##    cursor.execute('INSERT INTO Users(username, email) VALUES (?, ?)', ('user2', 'ewrwrew@fdfd'))
##
##    cursor.execute('COMMIT')
##
##except:
##    cursor.execute('ROLLBACK')
##
##connection.close()


import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

try:
    with connection:
        cursor.execute('INSERT INTO Users(username, email) VALUES (?, ?)', ('users3', 'fsdsf@mail0110'))
        cursor.execute('INSERT INTO Users(username, email) VALUES (?, ?)', ('users4', 'fsdsf@mail00'))
except:
    pass
        
