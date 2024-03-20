import sqlite3
conn = sqlite3.connect('teater.db')
c = conn.cursor()
with open("createDB.sql") as file:
    sql_script = file.read()
c.executescript(sql_script)
conn.commit()
conn.close()