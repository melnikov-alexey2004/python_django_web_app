import sqlite3

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect(r'D:\kursach_full\DATASETS\chinook.db')

connection.close()