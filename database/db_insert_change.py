import sqlite3
from bot_telegram import ABSOLUTE_PATH


def IC_User_Information(information_user):
    """
    Ф-ия добавляющая / меняющая данные в таблице, подключение к которой происходит через абсолютный путь к файлу.
    Вставляет данные в колонки хранящие в себе:
    ID - id пользователя написавшего команду /start
    NAME - Имя указанное в профиле пользователя
    USER_NAME - Ссылка на профиль пользователя
    ACCESS - Имеет ли данный человек разрешение на пользование ботом -> True/False
    :return:
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()

        user_id = information_user[0]
        cursor.execute("SELECT * FROM User_information WHERE ID=?", (user_id,))
        result = cursor.fetchone()

        if result:
            sqlite_insert_change_with_param = f"""UPDATE User_information SET NAME=?, USER_NAME=?, ACCESS=? WHERE ID=?"""
            data_tuple = tuple(information_user[1::]) + (user_id,)
            print(f'UPDATE User_Information {data_tuple}')
        else:
            sqlite_insert_change_with_param = """INSERT INTO User_information
                                  (ID, NAME, USER_NAME, ACCESS)
                                  VALUES (?, ?, ?, ?);"""
            data_tuple = tuple(information_user)
            print(f'INSERT User_Information {data_tuple}')

        cursor.execute(sqlite_insert_change_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка в IC_User_Information", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def IC_User_Setting(settings_user):
    """
    Ф-ия добавляющая / меняющая данные в таблице, подключение к которой происходит через абсолютный путь к файлу.
    ?!?!?!?!
    :param settings_user: кортеж с данными которые нужно подставить в таблицу
    :return:
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        user_id = settings_user[0]
        param_setings = settings_user[-1]
        cursor.execute("SELECT * FROM User_settings WHERE ID=?", (user_id,))
        result = cursor.fetchone()

        if result:
            sqlite_insert_change_with_param = f"""UPDATE User_settings SET {param_setings}=? WHERE ID=?"""
            data_tuple = (settings_user[1], user_id)
            print(f'UPDATE IC_User_Setting {data_tuple} {param_setings}')
        else:
            sqlite_insert_change_with_param = f"""INSERT INTO User_settings
                                  (ID, {param_setings})
                                  VALUES (?, ?);"""
            data_tuple = tuple(settings_user[:-1])
            print(f'INSERT IC_User_Setting {data_tuple} {param_setings}')

        cursor.execute(sqlite_insert_change_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка в IC_User_Setting", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
