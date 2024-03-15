import sqlite3
conn = sqlite3.connect('teater.db')
c = conn.cursor()
with open("brukstilfelle3/brukstilfelle3.sql") as file:
    sql_script = file.read()
c.executescript(sql_script)

c.execute('''
    SELECT Sete.radNr, Sete.område, Sete.salID
    FROM Sete LEFT JOIN (
        SELECT stolNr, radNr, område, salID
        FROM Billett INNER JOIN Ordre ON Billett.ordreID = Ordre.ordreID
        WHERE Ordre.stykkeID = "Størst av alt er kjærligheten" AND Ordre.forestillingDato = '2024-02-03'
    ) AS ReserverteSeter ON ReserverteSeter.stolNr = Sete.stolNr AND ReserverteSeter.radNr = Sete.radNr AND ReserverteSeter.område = Sete.område AND ReserverteSeter.salID = Sete.salID
    WHERE ReserverteSeter.stolNr IS NULL AND Sete.salID = (SELECT salID FROM Sal WHERE stykkeID = "Størst av alt er kjærligheten")
    GROUP BY Sete.radNr, Sete.område
    HAVING COUNT(*) >= 9
    ORDER BY Sete.område, Sete.radNr
''')
available_row = c.fetchone()

c.execute('''
    SELECT Sete.stolNr, Sete.radNr, Sete.område, Sete.salID
    FROM Sete LEFT JOIN (
        SELECT stolNr, radNr, område, salID
        FROM Billett INNER JOIN Ordre ON Billett.ordreID = Ordre.ordreID
        WHERE Ordre.stykkeID = "Størst av alt er kjærligheten" AND Ordre.forestillingDato = '2024-02-03'
    ) AS ReserverteSeter ON ReserverteSeter.stolNr = Sete.stolNr AND ReserverteSeter.radNr = Sete.radNr AND ReserverteSeter.område = Sete.område AND ReserverteSeter.salID = Sete.salID
    WHERE ReserverteSeter.stolNr IS NULL AND Sete.radNr = ? AND Sete.område = ? AND Sete.salID = ?
''', (available_row[0], available_row[1], available_row[2]))

available_seats = c.fetchall()

for i in range(9):
    c.execute("INSERT INTO Billett (billettNr, ordreID, gruppeNavn, stolNr, radNr, område, salID) VALUES (?, 3, 'Ordinær', ?, ?, ?, ?)", (i+1, available_seats[i][0], available_seats[i][1], available_seats[i][2], available_seats[i][3]))
c.execute("UPDATE Ordre SET antallBilletter = (SELECT COUNT(*) FROM Billett WHERE ordreID = 3) WHERE ordreID = 3")

c.execute('''
    SELECT SUM(PrisForForestilling.pris)
    FROM (Billett INNER JOIN Ordre ON Billett.ordreID = Ordre.ordreID) INNER JOIN PrisForForestilling ON Ordre.stykkeID = PrisForForestilling.stykkeID
    WHERE PrisForForestilling.gruppeNavn = 'Ordinær' AND Ordre.stykkeID = "Størst av alt er kjærligheten" AND Ordre.ordreID = 3
''')

total_price = c.fetchone()[0]
print("Totalpris:", total_price, "NOK")

conn.commit()
conn.close()