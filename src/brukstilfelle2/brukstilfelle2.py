import sqlite3

def __init__ ():
    conn = sqlite3.connect('teater.db')
    c = conn.cursor()
    with open("src/brukstilfelle2/brukstilfelle2.sql") as file:
        sql_script = file.read()
    c.executescript(sql_script)

    # Setter inn seter i Hovedscenen i Sete-tabellen og billetter for opptatte seter i Billett-tabellen
    with open("filesNeeded/hovedscenen.txt") as file:
        omraade = "Parkett"
        radnr = 1
        stolnr = 0
        amtTickets = 0

        for line in reversed(list(file)):
            if line == "Parkett\n":
                omraade = "Galleri"
                radnr = 1
                continue
            if line[0] != "1" and line[0] != "0":
                continue
            for stol in range(0, len(line)-1):
                stolnr += 1
                if line[stol] == "1":
                    amtTickets += 1
                    c.execute("INSERT INTO Billett (billettNr, ordreID, gruppeNavn, stolNr, radNr, område, salID) VALUES (?, 1, 'Ordinær', ?, ?, ?, 'Hovedscenen')", (amtTickets, stolnr, radnr, omraade))
            radnr += 1
        c.execute("UPDATE Ordre SET antallBilletter = ? WHERE ordreID = 1", (amtTickets,))

    # Setter inn seter i Gamle Scene i Sete-tabellen og billetter for opptatte seter i Billett-tabellen
    with open("filesNeeded/gamle-scene.txt") as file:
        omraade = "Parkett"
        radnr = 1
        stolnr = 1
        amtTickets = 0

        for line in reversed(list(file)):
            if line == "Parkett\n":
                omraade = "Balkong"
                radnr = 1
                continue
            if line == "Balkong\n":
                omraade = "Galleri"
                radnr = 1
                continue
            if line[0] != "1" and line[0] != "0":
                continue
            for stol in range(0, len(line)-1):
                if line[stol] == "1":
                    amtTickets += 1
                    c.execute("INSERT INTO Billett (billettNr, ordreID, gruppeNavn, stolNr, radNr, område, salID) VALUES (?, 2, 'Ordinær', ?, ?, ?, 'Gamle Scene')", (amtTickets, stolnr, radnr, omraade))
                stolnr += 1
            radnr += 1
            stolnr = 1
        c.execute("UPDATE Ordre SET antallBilletter = ? WHERE ordreID = 2", (amtTickets,))

    conn.commit()
    conn.close()