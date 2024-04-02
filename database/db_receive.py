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

        names = ["ID", "quoting", "repayment", "nominal", "market", "frequency", "days", "qualification"]
        params = {name_table: value_table for name_table, value_table in zip(names, params)}
        sql_select_query = """SELECT * FROM All_Bonds WHERE 1=1 """
        if params["quoting"] != "—":
            sql_select_query += f"""AND Quoting >= {params["quoting"]} """
        if params["repayment"] != "—":
            sql_select_query += f"""AND Repayment >= {params["repayment"]} """
        if params["nominal"] != "—":
            sql_select_query += f"""AND Nominal >= {params["nominal"]} """
        if params["market"] != "—":
            sql_select_query += f"""AND Market >= {params["market"]} """
        if params["frequency"] != "—":
            sql_select_query += f"""AND Frequency = {params["frequency"]} """
        if params["days"] != "—":
            if params["days"] == 366:
                sql_select_query += f"""AND Days <= {params["days"]} """
            elif params["days"] == 365:
                sql_select_query += f"""AND Days >= {params["days"]} """
        if params["quoting"] != "—":
            sql_select_query += f"""AND Quoting >= {params["quoting"]} """
        if params["qualification"] != "—":
            sql_select_query += f"""AND Qualification LIKE '{params["qualification"]}' """

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

        sql_select_query = f"""SELECT * FROM User{user_id}_bonds WHERE ROWID = {pagen}"""
        cursor.execute(sql_select_query)
        bond = cursor.fetchone()
        cursor.close()
        sqlite_connection.close()
        return bond

    except sqlite3.Error as error:
        print("Ошибка при работе с RE_GetPapers", error)

