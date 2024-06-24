import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Base (
id INTEGER PRIMARY KEY,
userid INTEGER,
point INTEGER
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()