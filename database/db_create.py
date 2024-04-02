import sqlite3
from bot_telegram import ABSOLUTE_PATH

def CT_UserInformation():
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
                                    ACCESS TEXT
                                    );'''
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()

    except sqlite3.Error as error:
        print("Ошибка в CT_UserInformation", error)


def CT_UserSettings():
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
                                        quoting TEXT,
                                        repayment TEXT,
                                        nominal TEXT,
                                        market TEXT,
                                        frequency TEXT,
                                        days TEXT,
                                        qualification TEXT
                                        );'''
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()

    except sqlite3.Error as error:
        print("Ошибка в CT_UserSettings", error)


def CT_UserClearSettings():
    """
    Таблица хранящая в себе очищенные от лишних символов параметры пользователя.
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
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS User_clear_settings (
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
        print("Ошибка в CT_UserClearSettings", error)


def CT_UserBonds(user_id):
    """
    Таблица хранящая в себе бумаги подготовленные для конкретного пользователя.
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
        sqlite_create_table_query = f'''CREATE TABLE IF NOT EXISTS User{user_id}_bonds (
                                    URL TEXT UNIQUE,
                                    NAME TEXT,
                                    Quoting REAL,
                                    Repayment REAL,
                                    Market REAL,
                                    Nominal REAL,
                                    Frequency INTEGER,
                                    Date DATETIME,
                                    Days INTEGER,
                                    ISIN TEXT,
                                    Code TEXT,
                                    Qualification TEXT,
                                    TIME_DATE TEXT
                                    );'''
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()

    except sqlite3.Error as error:
        print("Ошибка в CT_UserSettings", error)
