import sqlite3
from bot_telegram import ABSOLUTE_PATH


def IC_UserInformation(information_user):
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
        else:
            sqlite_insert_change_with_param = """INSERT INTO User_information
                                  (ID, NAME, USER_NAME, ACCESS)
                                  VALUES (?, ?, ?, ?);"""
            data_tuple = tuple(information_user)

        cursor.execute(sqlite_insert_change_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка в IC_User_Information", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def IC_UserSetting(settings_user):
    """
    Ф-ия добавляющая / меняющая данные в таблице, подключение к которой происходит через абсолютный путь к файлу.
    Вставляет данные в колонки хранящие в себе:
    ID - ID пользователя
    quoting - Котировка облигаций
    repayment - Доходность к погашению
    nominal - Купонная доходность относительно номинальной цены
    market - Купонная доходность относительно рыночной цены
    frequency - Частота купонов
    days - Дней до погашения
    qualification - Имеется ли у пользователя статус квал.инвестора
    :param settings_user: Кортеж с данными которые нужно подставить в таблицу
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
        else:
            sqlite_insert_change_with_param = f"""INSERT INTO User_settings
                                  (ID, {param_setings})
                                  VALUES (?, ?);"""
            data_tuple = tuple(settings_user[:-1])

        cursor.execute(sqlite_insert_change_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка в IC_User_Setting", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def IC_UserClearSetting(ID):
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        user_id = ID
        param_settings = ['—', '—', '—', '—', '—', '—', '—']
        cursor.execute("SELECT * FROM User_settings WHERE ID=?", (user_id,))
        result = cursor.fetchone()
        if result:
            sqlite_insert_change_with_param = f"""UPDATE User_settings SET quoting=?,repayment=?, 
                                                nominal=?, market=?, frequency=?, days=?, qualification=? WHERE ID=?"""
            data_tuple = (*param_settings, user_id)
        else:
            sqlite_insert_change_with_param = f"""INSERT INTO User_settings
                                  (ID, quoting, repayment, nominal, market, frequency, days, qualification)
                                  VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
            data_tuple = (user_id,) + tuple(param_settings)

        cursor.execute(sqlite_insert_change_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка в IC_User_ClearSetting", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
