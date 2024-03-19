import sqlite3

def __init__ ():
    conn = sqlite3.connect('teater.db')
    c = conn.cursor()
    with open("src/brukstilfelle1/brukstilfelle1.sql") as file:
        sql_script = file.read()
    c.executescript(sql_script)

    # Setter inn seter i Hovedscenen i Sete-tabellen og billetter for opptatte seter i Billett-tabellen
    with open("src/filesNeeded/hovedscenen.txt") as file:
        omraade = "Parkett"
        radnr = 1
        stolnr = 0

        for line in reversed(list(file)):
            if line == "Parkett\n":
                omraade = "Galleri"
                radnr = 1
                continue
            if line[0] != "1" and line[0] != "0":
                continue
            for stol in range(0, len(line)-1):
                stolnr += 1
                if line[stol] == "x":
                    continue
                c.execute("INSERT INTO Sete (stolNr, radNr, område, salID) VALUES (?, ?, ?, 'Hovedscenen')", (stolnr, radnr, omraade))
            radnr += 1
    c.execute("UPDATE Sal SET totaltAntallSeter = (SELECT COUNT(*) FROM SETE WHERE salID = 'Hovedscenen') WHERE salID = 'Hovedscenen'")


    # Setter inn seter i Gamle Scene i Sete-tabellen og billetter for opptatte seter i Billett-tabellen
    with open("src/filesNeeded/gamle-scene.txt") as file:
        omraade = "Parkett"
        radnr = 1
        stolnr = 1

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
                c.execute("INSERT INTO Sete (stolNr, radNr, område, salID) VALUES (?, ?, ?, 'Gamle Scene')", (stolnr, radnr, omraade))
                stolnr += 1
            radnr += 1
            stolnr = 1
    c.execute("UPDATE Sal SET totaltAntallSeter = (SELECT COUNT(*) FROM SETE WHERE salID = 'Gamle Scene') WHERE salID = 'Gamle Scene'")

    conn.commit()
    conn.close()