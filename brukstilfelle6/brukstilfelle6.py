import sqlite3
import os

def __init__():
    if os.path.exists('brukstilfelle6/resultat.txt'):
        os.remove('brukstilfelle6/resultat.txt')

    conn = sqlite3.connect('teater.db')
    c = conn.cursor()
    with open("brukstilfelle6/brukstilfelle6.sql") as file:
        sql_script = file.read()
    c.execute(sql_script)
    with open("brukstilfelle6/resultat.txt", "w") as file:
        queryResult = c.fetchall()
        for i in queryResult:
            file.write(str(i) + '\n')

    conn.commit()
    conn.close()