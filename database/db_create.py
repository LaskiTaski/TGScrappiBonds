import sqlite3
from bot_telegram import ABSOLUTE_PATH

# def CT_User_Information():
#     """
#     Ф-ия создающая таблицу внутри базы данных, подключение к которой происходит через абсолютный путь к файлу.
#     Создаёт колонки хранящие в себе:
#     ID - id пользователя написавшего команду /start
#     NAME - Имя указанное в профиле пользователя
#     USER_NAME - Ссылка на профиль пользователя
#     ACCESS - Имеет ли данный человек разрешение на пользование ботом -> True/False
#     :return:
#     """
#     try:
#         sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
#         sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS User_information (
#                                     ID TEXT UNIQUE,
#                                     NAME TEXT,
#                                     USER_NAME TEXT,
#                                     ACCESS TEXT
#                                     );'''
#         cursor = sqlite_connection.cursor()
#         cursor.execute(sqlite_create_table_query)
#         sqlite_connection.commit()
#         cursor.close()
#     except sqlite3.Error as error:
#         print("Ошибка в create_table_User_Information", error)
#     finally:
#         if (sqlite_connection):
#             sqlite_connection.close()
#
# def CT_User_settings():
#     """
#     :param ID: ID пользователя который зарегистрировался.
#     :param quoting: Параметры котировок облигаций.
#     :param repayment: Параметры Доходности к погашению.
#     :param nominal: Параметры Доходности купона к номиналу.
#     :param market: Параметры Доходности купона к рыночной цене.
#     :param frequency: Параметры Частоты купона.
#     :param days: Параметры Дней до погашения.
#     :param qualification: Статус квал. True / False
#     :return:
#     """
#     try:
#         sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
#         sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS User_settings (
#                                         ID TEXT UNIQUE,
#                                         quoting TEXT,
#                                         repayment TEXT,
#                                         nominal TEXT,
#                                         market TEXT,
#                                         frequency TEXT,
#                                         days TEXT,
#                                         qualification TEXT
#                                         );'''
#         cursor = sqlite_connection.cursor()
#         cursor.execute(sqlite_create_table_query)
#         sqlite_connection.commit()
#         cursor.close()
#     except sqlite3.Error as error:
#         print("Ошибка в create_client_settings", error)
#     finally:
#         if (sqlite_connection):
#             sqlite_connection.close()