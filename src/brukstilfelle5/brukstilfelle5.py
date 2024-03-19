import os
import sqlite3

def __init__():
    conn = sqlite3.connect('teater.db')
    c = conn.cursor()
    with open("src/brukstilfelle5/brukstilfelle5.sql") as file:
        sql_script = file.read()
    c.execute(sql_script)
    if os.path.exists('src/brukstilfelle5/resultat.txt'):
        os.remove('src/brukstilfelle5/resultat.txt')
    with open("src/brukstilfelle5/resultat.txt", "w") as file:
        for i in c.fetchall():
            file.write(str(i) + '\n')
    conn.commit()
    conn.close()