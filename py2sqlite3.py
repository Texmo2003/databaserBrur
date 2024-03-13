import sqlite3
conn = sqlite3.connect('prosjekt.db')

conn.execute("INSERT INTO Sal (salID, totaltAntallSeter) \
            VALUES (1, 516 )");

conn.execute("INSERT INTO Sal (salID, totaltAntallSeter) \
            VALUES (2, 332 )");

conn.commit()
