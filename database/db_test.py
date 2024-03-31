import sqlite3
from bot_telegram import ABSOLUTE_PATH

def connect_db():
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        print('Подключение установленно...')
        sqlite_connection.close()

    except sqlite3.Error as error:
        print("Ошибка в CREATE_DB", error)
