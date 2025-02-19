import sqlite3

connection = sqlite3.connect('tasks.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Task')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Task(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    status TEXT DEFAULT 'Not Started'
)
''')


def add_task(title):
    cursor.execute('INSERT INTO Task(title) VALUES (?)', (title,))
    connection.commit()


def update_list(task_id, status):
    cursor.execute('UPDATE Task SET status = ? WHERE id = ?', (status, task_id))
    connection.commit()


def list_task():
    cursor.execute('SELECT * FROM Task')
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)


add_task('Подготовить презентацию')
add_task('Закончить отчёт')
add_task('Приготовить ужин')


update_list(2, 'In Progress')


list_task()


connection.close()
