import sqlite3
from bot_telegram import ABSOLUTE_PATH


def RE_UserSettings(ID):
    """
    :param ID: ID пользователя.
    :return: Данные о параметрах настроенных пользователем.
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        sql_select_query = f"""SELECT * FROM User_settings WHERE ID = ?"""
        cursor.execute(sql_select_query, (ID,))
        params = cursor.fetchall()
        if params:
            information_params = {name_table: value_table for name_table, value_table in zip(["ID", "quoting", "repayment",
                                                                                              "nominal", "market",
                                                                                              "frequency", "days",
                                                                                              "qualification"],
                                                                                             params[0])}
        else:
            information_params = {name_table: value_table for name_table, value_table in
                                  zip(["ID", "quoting", "repayment",
                                       "nominal", "market",
                                       "frequency", "days",
                                       "qualification"],
                                      ['—', '—', '—', '—', '—', '—', '—', '—'])}
        cursor.close()
        return information_params

    except sqlite3.Error as error:
        print("Ошибка при работе с RE_User_settings", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

def RE_GetPapers(ID):
    """
    :param ID: ID пользователя.
    :return: Рекомендуемые бумаги.
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        sql_select_query = f"""SELECT * FROM User_clear_settings WHERE ID = ?"""
        cursor.execute(sql_select_query, (ID,))
        params = cursor.fetchall()
        sql_select_query = f"""SELECT * FROM All_Bonds WHERE ID = ?"""


        cursor.close()
        return information_params

    except sqlite3.Error as error:
        print("Ошибка при работе с RE_GetPapers", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
