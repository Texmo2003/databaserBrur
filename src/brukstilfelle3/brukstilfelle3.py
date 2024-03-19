import sqlite3
import os

conn = sqlite3.connect('teater.db')
c = conn.cursor()

def __init__ ():
    if os.path.exists('src/brukstilfelle3/resultat.txt'):
        os.remove('src/brukstilfelle3/resultat.txt')
    with open("src/brukstilfelle3/brukstilfelle3.sql") as file:
        sql_script = file.read()
    c.executescript(sql_script)
    with open("src/brukstilfelle3/resultat.txt", "w") as file:
        file.write("Totalpris: " + str(get_total_price_when_ordering_amt_tickets_in_same_row("Størst av alt er kjærligheten", '2024-02-03', 9, "Ordinær")))
    conn.commit()
    conn.close()

def get_available_rows_having_amt_seats (what_show, when, min_available_seats):
    c.execute('''
        SELECT Sete.radNr, Sete.område, Sete.salID
        FROM Sete LEFT JOIN (
            SELECT stolNr, radNr, område, salID
            FROM Billett INNER JOIN Ordre ON Billett.ordreID = Ordre.ordreID
            WHERE Ordre.stykkeID = ? AND Ordre.forestillingDato = ?
        ) AS ReserverteSeter ON ReserverteSeter.stolNr = Sete.stolNr AND ReserverteSeter.radNr = Sete.radNr AND ReserverteSeter.område = Sete.område AND ReserverteSeter.salID = Sete.salID
        WHERE ReserverteSeter.stolNr IS NULL AND Sete.salID = (SELECT salID FROM Stykke WHERE stykkeID = ?)
        GROUP BY Sete.radNr, Sete.område
        HAVING COUNT(*) >= ?
        ORDER BY Sete.område, Sete.radNr
    ''', (what_show, when, what_show, min_available_seats))
    return c.fetchall()

def get_available_seats_in_row (row_number, area, salID):
    c.execute('''
        SELECT Sete.stolNr, Sete.radNr, Sete.område, Sete.salID
        FROM Sete LEFT JOIN (
            SELECT stolNr, radNr, område, salID
            FROM Billett INNER JOIN Ordre ON Billett.ordreID = Ordre.ordreID
            WHERE Ordre.stykkeID = "Størst av alt er kjærligheten" AND Ordre.forestillingDato = '2024-02-03'
        ) AS ReserverteSeter ON ReserverteSeter.stolNr = Sete.stolNr AND ReserverteSeter.radNr = Sete.radNr AND ReserverteSeter.område = Sete.område AND ReserverteSeter.salID = Sete.salID
        WHERE ReserverteSeter.stolNr IS NULL AND Sete.radNr = ? AND Sete.område = ? AND Sete.salID = ?
    ''', (row_number, area, salID))
    return c.fetchall()

def get_total_price_for_all_tickets_of_same_type (show, orderID, groupName):
    c.execute('''
        SELECT SUM(PrisForForestilling.pris)
        FROM (Billett INNER JOIN Ordre ON Billett.ordreID = Ordre.ordreID) INNER JOIN PrisForForestilling ON Ordre.stykkeID = PrisForForestilling.stykkeID
        WHERE PrisForForestilling.gruppeNavn = ? AND Ordre.stykkeID = ? AND Ordre.ordreID = ? AND Billett.gruppeNavn = ?
    ''', (groupName, show, orderID, groupName))
    return c.fetchone()[0]

def order_tickets_for_forestilling (orderID, groupName, available_seats, amtTicketsToOrder, forestillingDato, stykkeID, kundeID):
    c.execute("DELETE FROM Billett WHERE ordreID = ?", (orderID, ))
    c.execute("DELETE FROM Ordre WHERE ordreID = ?", (orderID, ))
    c.execute("INSERT INTO Ordre (ordreID, kjøpsdato, kjøpstid, antallBilletter, kundeID, forestillingDato, stykkeID) VALUES (?, '2024-02-02', '12:00', 0, ?, ?, ?)", (orderID, kundeID, forestillingDato, stykkeID))
    for i in range(amtTicketsToOrder):
        c.execute("INSERT INTO Billett (billettNr, ordreID, gruppeNavn, stolNr, radNr, område, salID) VALUES (?, ?, ?, ?, ?, ?, ?)", (i+1, orderID, groupName, available_seats[i][0], available_seats[i][1], available_seats[i][2], available_seats[i][3]))
    c.execute("UPDATE Ordre SET antallBilletter = (SELECT COUNT(*) FROM Billett WHERE ordreID = ?) WHERE ordreID = ?", (orderID, orderID))

def get_total_price_when_ordering_amt_tickets_in_same_row (stykkeID, forestillingDato, amtTicketsToOrder, groupName):
    available_rows = get_available_rows_having_amt_seats("Størst av alt er kjærligheten", '2024-02-03', 9)

    selected_row = available_rows[0]
    selected_row_number = selected_row[0]
    selected_area = selected_row[1]
    selected_salID = selected_row[2]

    available_seats = get_available_seats_in_row(selected_row_number, selected_area, selected_salID)

    order_tickets_for_forestilling(3, "Ordinær", available_seats, 9, '2024-02-03', "Størst av alt er kjærligheten", 69)

    total_price = get_total_price_for_all_tickets_of_same_type("Størst av alt er kjærligheten", 3, "Ordinær")

    return total_price