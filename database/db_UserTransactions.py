import sqlite3
from bot_telegram import ABSOLUTE_PATH
from datetime import datetime


def CREATE_UserTransactions():
    """
    Таблица хранящая в себе данные о транзакциях.
    Создаёт колонки хранящие в себе:
    ID - id пользователя написавшего команду /start.
    NAME - Имя указанное в профиле пользователя.
    USER_NAME - Ссылка на профиль пользователя.
    ACCESS - Имеет ли данный человек разрешение на пользование ботом -> True/False.
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS User_transactions (
                                    ID TEXT UNIQUE,
                                    DateRegistration TEXT,
                                    DatePayment TEXT,
                                    EndSubscription  TEXT,
                                    DaysLeft INTEGER 
                                    );'''
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()

    except sqlite3.Error as error:
        print("Ошибка в CT_UserInformation", error)


def SET_UserInformTransactions(information_user):
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()

        user_id = information_user["ID"]
        cursor.execute("SELECT * FROM User_transactions WHERE ID=?", (user_id,))
        result = cursor.fetchone()
        if result is not None:
            sqlite_insert_change_with_param = f"""UPDATE User_transactions SET DateRegistration=?, 
            DatePayment=?, EndSubscription=?, DaysLeft=? WHERE ID=?"""
            data_tuple = (user_id,)
        else:
            sqlite_insert_change_with_param = """INSERT INTO User_transactions (ID, DateRegistration, DatePayment,
                                                                                EndSubscription, DaysLeft)
                                                                                VALUES (?, ?, ?, ?, ?);"""
            data_tuple = tuple(information_user.values())

        cursor.execute(sqlite_insert_change_with_param, data_tuple)
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()

    except sqlite3.Error as error:
        print("Ошибка в IC_UserTransactions", error)


def UPDATE_UserDaysLeft(information_user):
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()

        user_id = information_user["ID"]
        cursor.execute("SELECT DatePayment, EndSubscription FROM User_transactions WHERE ID=?", (user_id,))
        result = cursor.fetchone()

        if result is not None:
            DatePayment = datetime.strptime(result[0], "%d.%m.%Y")
            EndSubscription = datetime.strptime(result[1], "%d.%m.%Y")
            DaysLeft = int((EndSubscription - DatePayment).days)

            sqlite_insert_change_with_param = f"""UPDATE User_transactions SET DaysLeft=? WHERE ID=?"""
            data_tuple = (DaysLeft,) + (user_id,)

            cursor.execute(sqlite_insert_change_with_param, data_tuple)

        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
    except sqlite3.Error as error:
        print("Ошибка в Update_UserDaysLeft", error)


def CHECK_UserDaysLeft(information_user):
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()

        user_id = information_user["ID"]
        cursor.execute("SELECT DaysLeft FROM User_transactions WHERE ID=?", (user_id,))
        try:
            result = cursor.fetchone()[0]
        except:
            result = cursor.fetchone()

        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
        return result
    except sqlite3.Error as error:
        print("Ошибка в Check_UserDaysLeft", error)
