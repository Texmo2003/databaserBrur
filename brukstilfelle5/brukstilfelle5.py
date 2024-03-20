import os
import sqlite3

def __init__():
    conn = sqlite3.connect('teater.db')
    c = conn.cursor()
    with open("brukstilfelle5/brukstilfelle5.sql") as file:
        sql_script = file.read()
    c.execute(sql_script)
    if os.path.exists('output/brukstilfelle5.txt'):
        os.remove('output/brukstilfelle5.txt')
    with open("output/brukstilfelle5.txt", "w") as file:
        file.write("(StykkeID, Skuespillers navn, Rolle)\n")
        file.write("--------------------------------------------------\n")
        for i in c.fetchall():
            file.write(str(i) + '\n')
    conn.commit()
    conn.close()