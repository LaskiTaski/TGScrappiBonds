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
            cursor.close()
            sqlite_connection.close()
            return information_params
    except sqlite3.Error as error:
        print("Ошибка при работе с RE_User_settings", error)

def RE_GetPapers(ID):
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        user_id = ID

        sql_select_query = f"""SELECT * FROM User_clear_settings WHERE ID = ?"""
        cursor.execute(sql_select_query, (user_id,))
        params = cursor.fetchone()
        params = {name_table: value_table for name_table, value_table in zip(["ID", "quoting", "repayment",
                                                                              "nominal", "market",
                                                                              "frequency", "days",
                                                                              "qualification"],
                                                                             params)}
        sql_select_query = f"""SELECT * FROM All_Bonds WHERE 
        Quoting >= {int(params["quoting"])} AND Repayment >= {int(params["repayment"])} AND
        Nominal >= {int(params["nominal"])} AND Market >= {int(params["market"])} AND 
        Frequency >= {int(params["frequency"])} AND Days <= {30000 if int(params["days"] == -100) else int(params["days"])} AND
        Qualification LIKE '{'Нет' if params["qualification"] == '—' else params["qualification"]}' """
        cursor.execute(sql_select_query)
        bonds = cursor.fetchall()
        cursor.close()
        sqlite_connection.close()
        return bonds

    except sqlite3.Error as error:
        print("Ошибка при работе с RE_GetPapers", error)


def RE_UserPappers(ID, pagen):
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        user_id = ID

        sql_select_query = f"""SELECT * FROM User{user_id}_bonds WHERE ROWID = {pagen+1}"""
        cursor.execute(sql_select_query)
        bond = cursor.fetchone()
        cursor.close()
        sqlite_connection.close()
        print(bond)
        return bond

    except sqlite3.Error as error:
        print("Ошибка при работе с RE_GetPapers", error)

