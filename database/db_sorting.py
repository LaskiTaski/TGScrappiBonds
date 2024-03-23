def get_the_nominal_info(from_quoting=0, before_quoting=100,
                         from_repayment=0, before_repayment=10_000,
                         from_coupon_to_the_market=0, before_coupon_to_the_market=10_000,
                         from_coupon_frequency=0, before_coupon_frequency=12,
                         from_cancellation_days=0, before_cancellation_days=99_000,
                         only_for_quarters='Нет'):
    try:
        sqlite_connection = sqlite3.connect('ABSOLUTE_PATH')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_select_query = """SELECT * FROM All_Bonds WHERE Котировка_облигации > ? AND Котировка_облигации < ? AND
        Доходность_к_погашению > ? AND Доходность_к_погашению < ? AND
        Доходность_купона_к_номиналу > ? AND Доходность_купона_к_номиналу < ?
        Доходность_купона_к_рынку > ? AND Доходность_купона_к_рынку < ?
        Частота_купона > ? AND Частота_купона < ?
        Дней_до_погашения > ? AND Дней_до_погашения < ?
        Только_для_квалов = ?"""
        cursor.execute(sql_select_query, (from_quoting, before_quoting, from_repayment, before_repayment,
                                          from_coupon_to_the_market, before_coupon_to_the_market,
                                          from_coupon_frequency, before_coupon_frequency,
                                          from_cancellation_days, before_cancellation_days, only_for_quarters))
        records = cursor.fetchall()
        for row in records:
            print(row)
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с get_the_nominal_info", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()