import sqlite3
from bot_telegram import ABSOLUTE_PATH


def CREATE_UserInformation():
    """
    Таблица хранящая в себе данные о пользователе и уровне доступа.
    Создаёт колонки хранящие в себе:
    ID - id пользователя написавшего команду /start.
    NAME - Имя указанное в профиле пользователя.
    USER_NAME - Ссылка на профиль пользователя.
    ACCESS - Имеет ли данный человек разрешение на пользование ботом -> True/False.
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS User_information (
                                    ID TEXT UNIQUE,
                                    NAME TEXT,
                                    USER_NAME TEXT,
                                    DateRegistration TEXT,
                                    ACCESS TEXT
                                    );'''
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()

    except sqlite3.Error as error:
        print("Ошибка в CT_UserInformation", error)


def SET_UserInformation(information_user: dict):
    """
    Вставляет данные в колонки хранящие в себе:
    ID - id пользователя написавшего команду /start.
    NAME - Имя указанное в профиле пользователя.
    USER_NAME - Ссылка на профиль пользователя.
    ACCESS - Имеет ли данный человек разрешение на пользование ботом -> True/False.
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()

        user_id = information_user["ID"]
        cursor.execute("SELECT * FROM User_information WHERE ID=?", (user_id,))
        result = cursor.fetchone()
        if result:
            sqlite_insert_change_with_param = f"""UPDATE User_information SET NAME=?, USER_NAME=?, DateRegistration=?,
             ACCESS=? WHERE ID=?"""
            data_tuple = (tuple(information_user.values())[1::]) + (user_id,)

        else:
            sqlite_insert_change_with_param = """INSERT INTO User_information (ID, NAME, USER_NAME,
                                                                               DateRegistration, ACCESS)
                                                                               VALUES (?, ?, ?, ?, ?);"""
            data_tuple = tuple(information_user.values())

        cursor.execute(sqlite_insert_change_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()

    except sqlite3.Error as error:
        print("Ошибка в IC_UserInformation", error)


def GET_UserDateRegistration(information_user):
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()

        user_id = information_user["ID"]
        cursor.execute("SELECT DateRegistration FROM User_information WHERE ID=?", (user_id,))
        result = cursor.fetchone()

        cursor.close()
        sqlite_connection.close()

        return result
    except sqlite3.Error as error:
        print("Ошибка в IC_UserTransactions", error)
