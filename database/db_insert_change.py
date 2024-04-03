import sqlite3
from bot_telegram import ABSOLUTE_PATH


def IC_UserInformation(information_user: dict):
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
            sqlite_insert_change_with_param = f"""UPDATE User_information SET NAME=?, USER_NAME=?, ACCESS=?
                                                  WHERE ID=?"""
            data_tuple = (information_user["Name"], information_user["User_name"], information_user["Access"], user_id,)
        else:
            sqlite_insert_change_with_param = """INSERT INTO User_information (ID, NAME, USER_NAME, ACCESS)
                                                                               VALUES (?, ?, ?, ?);"""
            data_tuple = tuple(information_user.values())

        cursor.execute(sqlite_insert_change_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()

    except sqlite3.Error as error:
        print("Ошибка в IC_UserInformation", error)



def IC_UserStartSetting(user_id):
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        param_settings = ['—'] * 7
        cursor.execute("SELECT * FROM User_settings WHERE ID=?", (user_id,))
        result = cursor.fetchone()
        if not result:
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

def IC_UserSetting(settings_user):
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

        if result:
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


def IC_UserBonds(bonds):
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        user_id = bonds[0]
        sqlite_insert_change_with_param = f"""DELETE FROM User{user_id}_bonds"""
        cursor.execute(sqlite_insert_change_with_param)
        for bond in bonds[1]:
            sqlite_insert_change_with_param = f"""INSERT INTO User{user_id}_bonds
                                      (URL, NAME, Quoting, Repayment, Market, Nominal, 
                                      Frequency, Date, Days, ISIN, Code, Qualification, TIME_DATE)
                                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            cursor.execute(sqlite_insert_change_with_param, bond)
            sqlite_connection.commit()

        cursor.close()
        sqlite_connection.close()


    except sqlite3.Error as error:
        print(f"Ошибка в IC_UserBonds", error)
