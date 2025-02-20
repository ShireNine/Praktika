import sqlite3

connection = sqlite3.connect('Stima.db')
cursor = connection.cursor()
cursor.execute('''SELECT 
    c.id, 
    c.Фамилия, 
    c.Имя, 
    c.Отчество, 
    s.Модель, 
    s.Количество, 
    s.Цена, 
    p.Скидка
FROM 
    Clients c
JOIN 
    Payments p ON c.id = p.id_Client
JOIN 
    Stima s ON p.id_Zakaza = s.id_Zakaza
WHERE 
    c.Фамилия LIKE 'В%' OR c.Фамилия LIKE 'Л%';''')

users = cursor.fetchall()
print(users)

print('===============================================')

cursor.execute('''
SELECT 
    c.id, 
    c.Фамилия, 
    c.Имя, 
    c.Отчество, 
    c.адрес, 
    s.Модель, 
    s.Количество
FROM 
    Clients c
JOIN 
    Payments p ON c.id = p.id_Client
JOIN 
    Stima s ON p.id_Zakaza = s.id_Zakaza
WHERE 
    s.Модель LIKE '%Модель 1%'
    AND c.адрес IN ('Гагариена')
    AND s.Количество >= 5;
    ''')

users1 = cursor.fetchall()
print(users1)


connection.close()

