import sqlite3
conn = sqlite3.connect('teater.db')
c = conn.cursor()
with open("brukstilfelle5/brukstilfelle5.sql") as file:
    sql_script = file.read()
c.execute(sql_script)
queryResult = c.fetchall()
for i in queryResult:
    print(i)
conn.commit()
conn.close()