import sqlite3
import os

def __init__():
    if os.path.exists('output/brukstilfelle6.txt'):
        os.remove('output/brukstilfelle6.txt')

    conn = sqlite3.connect('teater.db')
    c = conn.cursor()
    with open("brukstilfelle6/brukstilfelle6.sql") as file:
        sql_script = file.read()
    c.execute(sql_script)
    with open("output/brukstilfelle6.txt", "w") as file:
        file.write("(StykkeID, Dato, AntallBilletterSolgt)\n")
        file.write("--------------------------------------------------\n")
        queryResult = c.fetchall()
        for i in queryResult:
            file.write(str(i) + '\n')

    conn.commit()
    conn.close()