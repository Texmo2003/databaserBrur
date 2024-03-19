import sqlite3
conn = sqlite3.connect('teater.db')
c = conn.cursor()

def __init__():
    ting = get_all_forestillinger_on_date('2024-02-03')
    for i in ting:
        print(i)
    conn.commit()
    conn.close()

def get_all_forestillinger_on_date(date):
    c.execute('''
        SELECT Forestilling.stykkeID, COALESCE(SUM(Ordre.antallBilletter), 0) AS antallBilletter
        FROM Forestilling LEFT JOIN Ordre ON Forestilling.forestillingDato = Ordre.forestillingDato AND Forestilling.stykkeID = Ordre.stykkeID
        WHERE Forestilling.forestillingDato = ?
        GROUP BY Forestilling.stykkeID
    ''', (date, ))
    return c.fetchall()