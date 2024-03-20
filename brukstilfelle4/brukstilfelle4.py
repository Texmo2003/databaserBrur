import os
import sqlite3
conn = sqlite3.connect('teater.db')
c = conn.cursor()

def __init__(dato):
    if os.path.exists('output/brukstilfelle4.txt'):
        os.remove('output/brukstilfelle4.txt')
    with open("output/brukstilfelle4.txt", "w") as file:
        file.write("(StykkeID, AntallBilletter)\n")
        file.write("--------------------------------------------------\n")
        for i in get_all_forestillinger_on_date(dato):
            file.write(str(i) + '\n')
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