import sqlite3
from bot_telegram import ABSOLUTE_PATH

# Переписать всю ф-ию, для получения данных о настройках пользователя, прежде чем сортировать, что-то
def get_User_settings(from_quoting=0, before_quoting=100,
                         from_repayment=0, before_repayment=10_000,
                         from_coupon_to_the_nominal=0, before_coupon_to_the_nominal=10_000,
                         from_coupon_to_the_market=0, before_coupon_to_the_market=10_000,
                         from_coupon_frequency=0, before_coupon_frequency=12,
                         from_cancellation_days=0, before_cancellation_days=99_000,
                         only_for_quarters='Нет'):
    """
    Ф-ия позволяющая пользователю выбрать параметры для сортировки ценных бумаг.
    ________________________________________________________________________________________
                                ПАРАМЕТРЫ КОТИРОВКИ ОБЛИГАЦИЙ
    :param from_quoting: ПО УМОЛЧАНИЮ ИМЕЕТ ЗНАЧЕНИЕ = 0
    :param before_quoting: ПО УМОЛЧАНИЮ ИМЕЕТ ЗНАЧЕНИЕ = 100
    ________________________________________________________________________________________
                                ПАРАМЕТРЫ ДОХОДНОСТИ К ПОГАШЕНИЮ
    :param from_repayment: ПО УМОЛЧАНИЮ ИМЕЕТ ЗНАЧЕНИЕ = 0
    :param before_repayment: ПО УМОЛЧАНИЮ ИМЕЕТ ЗНАЧЕНИЕ = 10_000
    ________________________________________________________________________________________
                    ПАРАМЕТРЫ ДОХОДНОСТИ КУПОНА ОТНОСИТЕЛЬНО НОМИНАЛЬНОЙ ЦЕНЫ
    :param from_coupon_to_the_nominal: ПО УМОЛЧАНИЮ ИМЕЕТ ЗНАЧЕНИЕ = 0
    :param before_coupon_to_the_nominal: ПО УМОЛЧАНИЮ ИМЕЕТ ЗНАЧЕНИЕ = 10_000
    ________________________________________________________________________________________
                    ПАРАМЕТРЫ ДОХОДНОСТИ КУПОНА ОТНОСИТЕЛЬНО РЫНОЧНОЙ ЦЕНЫ
    :param from_coupon_to_the_market: ПО УМОЛЧАНИЮ ИМЕЕТ ЗНАЧЕНИЕ = 0
    :param before_coupon_to_the_market: ПО УМОЛЧАНИЮ ИМЕЕТ ЗНАЧЕНИЕ = 10_000
    ________________________________________________________________________________________
                                    ПАРАМЕТРЫ ЧАСТОТЫ КУПОНА
    :param from_coupon_frequency:
    :param before_coupon_frequency:
    ________________________________________________________________________________________
                                    ПАРАМЕТРЫ ДНЕЙ ДО ПОГАШЕНИЯ
    :param from_cancellation_days:
    :param before_cancellation_days:
    ________________________________________________________________________________________
                                ПАРАМЕТРЫ СТАТУСА КВАЛ. ИНВЕСТОРА
    :param only_for_quarters:
    ________________________________________________________________________________________
    :return:
    """
    try:
        sqlite_connection = sqlite3.connect(ABSOLUTE_PATH)
        cursor = sqlite_connection.cursor()

        sql_select_query = """SELECT * FROM All_Bonds WHERE Котировка_облигации > ? AND Котировка_облигации < ? AND
        Доходность_к_погашению > ? AND Доходность_к_погашению < ? AND
        Доходность_купона_к_номиналу > ? AND Доходность_купона_к_номиналу < ?
        Доходность_купона_к_рынку > ? AND Доходность_купона_к_рынку < ?
        Частота_купона > ? AND Частота_купона < ?
        Дней_до_погашения > ? AND Дней_до_погашения < ?
        Только_для_квалов = ?"""
        cursor.execute(sql_select_query, (from_quoting, before_quoting,
                                          from_repayment, before_repayment,
                                          from_coupon_to_the_nominal, before_coupon_to_the_nominal,
                                          from_coupon_to_the_market, before_coupon_to_the_market,
                                          from_coupon_frequency, before_coupon_frequency,
                                          from_cancellation_days, before_cancellation_days,
                                          only_for_quarters))
        records = cursor.fetchall()
        for row in records:
            print(row)
        cursor.close()
        sqlite_connection.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с get_the_nominal_info", error)