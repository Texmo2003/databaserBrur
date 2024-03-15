import sqlite3
conn = sqlite3.connect('teater.db')
c = conn.cursor()

c.execute("DELETE FROM Ordre")
c.execute("DELETE FROM Billett")
c.execute("DELETE FROM Kunde WHERE kundeid = 69")
c.execute("DELETE FROM Sete")

# Dummy kunde
c.execute("INSERT INTO Kunde (kundeID, tlfNr, navn, adresse) VALUES (69, 12345678, 'Ola Nordmann', 'Olasvei 1')")

# Setter inn seter i sal 1 (Hovedscenen) i Sete-tabellen
with open("filesNeeded/hovedscenen.txt") as file:
    omraade = "Parkett"
    radnr = 1
    stolnr = 0
    amtTickets = 0

    c.execute("INSERT INTO Ordre (ordreID, kjøpsdato, kjøpstid, antallBilletter, kundeID, forestillingDato, stykkeID) VALUES (1, '2024-01-29', '02:37', 0, 69, '2024-02-03', 'Kongsemnene')")
    for line in reversed(list(file)):
        if line == "Parkett\n":
            omraade = "Galleri"
            radnr = 1
            continue
        if line[0] != "1" and line[0] != "0":
            continue
        for stol in range(0, len(line)-1):
            stolnr += 1
            if line[stol] != "1" and line[stol] != "0":
                continue
            if line[stol] == "1":
                amtTickets += 1
                c.execute("INSERT INTO Billett (billettNr, ordreID, gruppeNavn, stolNr, radNr, område, salID) VALUES (?, 1, 'Ordinær', ?, ?, ?, 'Hovedscenen')", (amtTickets, stolnr, radnr, omraade))
        radnr += 1
    c.execute("UPDATE Ordre SET antallBilletter = ? WHERE ordreID = 1", (amtTickets,))

# c.execute("INSERT INTO Billett (billettNr, ordreID, gruppeNavn, stolNr, radNr, område, salID) VALUES (?, 1, 'Ordinær', ?, ?, ?, 'Hovedscenen')", (amtTickets, stolnr, radnr, omraade))
# Setter inn seter i sal 2 (Gamle Scene) i Sete-tabellen
# with open("filesNeeded/gamle-scene.txt") as file:
#     omraade = "Parkett"
#     radnr = 1
#     stolnr = 1

#     for line in reversed(list(file)):
#         if line == "Parkett\n":
#             omraade = "Balkong"
#             radnr = 1
#             continue
#         if line == "Balkong\n":
#             omraade = "Galleri"
#             radnr = 1
#             continue
#         if line[0] != "1" and line[0] != "0":
#             continue
#         for stol in range(1, len(line)):
#             stolnr += 1
#             c.execute("INSERT INTO Sete (stolNr, radNr, område, salID) VALUES (?, ?, ?, 'Gamle Scene')", (stolnr, radnr, omraade))
#         radnr += 1
#         stolnr = 1










































conn.commit()