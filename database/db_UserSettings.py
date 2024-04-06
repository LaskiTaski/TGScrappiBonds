import sqlite3
from bot_telegram import ABSOLUTE_PATH


def CREATE_UserSettings():
    """
    Таблица хранящая в себе настройки пользователя для отображения их в меню.
    Создаёт колонки хранящие в себе:
    :param ID: ID пользователя который зарегистрировался.
    :param quoting: Параметры котировок облигаций.
    :param repayment: Параметры Доходности к погашению.
    :param nominal: Параметры Доходности купона к номиналу.
    :param market: Параметры Доходности купона к рыночной цене.
    :param frequency: Параметры Частоты купона.
    :param days: Параметры Дней до погашения.
    :param qualification: Статус квал. True / False.
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS User_settings (
                                        ID TEXT UNIQUE,
                                        quoting INTEGER,
                                        repayment INTEGER,
                                        nominal INTEGER,
                                        market INTEGER,
                                        frequency INTEGER,
                                        days INTEGER,
                                        qualification TEXT
                                        );'''
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()

    except sqlite3.Error as error:
        print("Ошибка в CT_UserSettings", error)


def SET_UserStartSettings(user_id):
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        param_settings = ['—'] * 7
        cursor.execute("SELECT * FROM User_settings WHERE ID=?", (user_id,))
        result = cursor.fetchone()
        if result is None:
            sqlite_insert_change_with_param = f"""INSERT INTO User_settings
                                  (ID, quoting, repayment, nominal, market, frequency, days, qualification)
                                  VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
            data_tuple = (user_id,) + tuple(param_settings)
        else:
            sqlite_insert_change_with_param = f"""UPDATE User_settings SET quoting=?,repayment=?, nominal=?, 
                                                                           market=?, frequency=?, days=?, 
                                                                           qualification=? WHERE ID=?"""
            data_tuple = (*param_settings, user_id)

        cursor.execute(sqlite_insert_change_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()

    except sqlite3.Error as error:
        print("Ошибка в IC_UserStartSetting", error)


def SET_UserSettingParam(settings_user):
    """
    Вставляет данные в колонки хранящие в себе:
    ID - ID пользователя.
    quoting - Котировка облигаций.
    repayment - Доходность к погашению.
    nominal - Купонная доходность относительно номинальной цены.
    market - Купонная доходность относительно рыночной цены.
    frequency - Частота купонов.
    days - Дней до погашения.
    qualification - Имеется ли у пользователя статус квал.инвестора.
    :param settings_user: Кортеж хранящий в себе ID / значение / в какую-колку подставить.
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        user_id = settings_user["ID"]
        param_settings = settings_user["Column"]
        cursor.execute("SELECT * FROM User_settings WHERE ID=?", (user_id,))
        result = cursor.fetchone()

        try:
            if settings_user["Settings"] in ['Да', 'Нет']:
                pass
            else:
                settings_user["Settings"] = int(''.join(filter(str.isdigit, settings_user["Settings"])))
        except:
            settings_user["Settings"] = '—'

        if result is not None:
            sqlite_insert_change_with_param = f"""UPDATE User_settings SET {param_settings}=? WHERE ID=?"""
            data_tuple = (settings_user["Settings"], user_id)
        else:
            sqlite_insert_change_with_param = f"""INSERT INTO User_settings
                                  (ID, {param_settings})
                                  VALUES (?, ?);"""
            data_tuple = (user_id, settings_user["Settings"])

        cursor.execute(sqlite_insert_change_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()

    except sqlite3.Error as error:
        print("Ошибка в IC_UserSetting", error)


def GET_UserSettings(ID):
    """
    :param ID: ID пользователя.
    :return: Данные о параметрах настроенных пользователем.
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        sql_select_query = f"""SELECT * FROM User_settings WHERE ID = ?"""
        cursor.execute(sql_select_query, (ID,))

        result = cursor.fetchone()
        if result is not None:
            names = ["ID", "quoting", "repayment", "nominal", "market", "frequency", "days", "qualification"]
            information_params = {name_table: value_table for name_table, value_table in zip(names, result)}
            cursor.close()
            sqlite_connection.close()
            return information_params

    except sqlite3.Error as error:
        print("Ошибка при работе с RE_User_settings", error)
