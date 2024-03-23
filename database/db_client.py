import sqlite3
from bot_telegram import ABSOLUTE_PATH

def create_table_User_Information():
    """
    Ф-ия создающая таблицу внутри базы данных, подключение к которой происходит через абсолютный путь к файлу.
    Создаёт колонки хранящие в себе:
    ID - id пользователя написавшего команду /start
    NAME - Имя указанное в профиле пользователя
    USER_NAME - Ссылка на профиль пользователя
    ACCESS - Имеет ли данный человек разрешение на пользование ботом -> True/False
    :return:
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS User_information (
                                    ID TEXT UNIQUE,
                                    NAME TEXT,
                                    USER_NAME TEXT,
                                    ACCESS TEXT
                                    );'''
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка в create_table_User_Information", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def insert_change_into_User_Information(information_user):
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()

        user_id = information_user[0]
        cursor.execute("SELECT * FROM User_information WHERE ID=?", (user_id,))
        result = cursor.fetchone()

        if result:
            sqlite_insert_change_with_param = """UPDATE User_information SET ID=?, NAME=?, USER_NAME=?, ACCESS=?"""
            data_tuple = tuple(information_user[1::]) + (user_id,)
            print(f'UPDATE User_Information {data_tuple}')
        else:
            sqlite_insert_change_with_param = """INSERT INTO All_Bonds
                                  (ID, NAME, USER_NAME, ACCESS)
                                  VALUES (?, ?, ?, ?);"""
            data_tuple = tuple(information_user)
            print(f'INSERT User_Information {data_tuple}')

        cursor.execute(sqlite_insert_change_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка в insert_change_into_User_Information", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


