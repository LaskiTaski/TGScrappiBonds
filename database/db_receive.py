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
        params = cursor.fetchone()
        if params:
            names = ["ID", "quoting", "repayment", "nominal", "market", "frequency", "days", "qualification"]
            information_params = {name_table: value_table for name_table, value_table in zip(names, params)}
            cursor.close()
            sqlite_connection.close()
            return information_params
    except sqlite3.Error as error:
        print("Ошибка при работе с RE_User_settings", error)

def RE_SuitablePapers(ID):
    """
    Собирает динамический запрос опираясь на предпочтения пользователя и возвращает все подошедшие бумаги.
    :param ID: ID - пользователя
    :return:
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        user_id = ID

        sql_select_query = f"""SELECT * FROM User_settings WHERE ID = ?"""
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
        print("Ошибка при работе с RE_SuitablePapers", error)


def RE_GetPaper(ID: str, pagen: int) -> [list]:
    """
    Выдаёт каждую бумагу по отдельности в зависимости от нумерации в таблице и кэш значения.
    :param ID: ID пользователя для подключения к нужной таблице
    :param pagen: Номер бумаги в таблице
    :return:
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        user_id = ID

        sql_select_query = f"""SELECT * FROM User{user_id}_bonds WHERE ROWID = {pagen}"""
        cursor.execute(sql_select_query)
        result = cursor.fetchone()

        name = ["URL", "Название", "Котировка", "К погашению", "К рынку",
                "К номиналу", "Частота", "Дата", "Дней", "ISIN", "Код", "Статус", "Обновление"]
        bond = {param: info if info is not None else "—" for param, info in zip(name, result)}

        cursor.close()
        sqlite_connection.close()
        return bond

    except sqlite3.Error as error:
        print("Ошибка при работе с RE_GetPapers", error)


def RE_GetPages(ID: str) -> [int]:
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()
        user_id = ID

        sql_select_query = f"""SELECT COUNT(*) FROM User{user_id}_bonds"""
        cursor.execute(sql_select_query)
        total_pages = cursor.fetchone()[0]
        cursor.close()
        sqlite_connection.close()
        return total_pages

    except sqlite3.Error as error:
        print("Ошибка при работе с RE_GetPages", error)

