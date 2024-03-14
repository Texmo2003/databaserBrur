import sqlite3
conn = sqlite3.connect('teater.db')

conn.execute("DELETE FROM Sal")

# Setter inn sal 1 (Hovedscenen) og sal 2 (Gamle scene) inn i Sal-tabellen
conn.execute("INSERT INTO Sal (salID, totaltAntallSeter) \
            VALUES (1, 516)")
conn.execute("INSERT INTO Sal (salID, totaltAntallSeter) \
            VALUES (2, 332)")

# Setter inn seter i sal 1 (Hovedscenen) i Sete-tabellen
for stolnr in range(0, 524):
    område = "parkett"
    if (stolnr > 467 and stolnr < 472) or (stolnr > 495 and stolnr < 500):
        continue
    if stolnr < 505:
        område = "galleri"
    conn.execute("INSERT INTO Sete (stolNr, radNr, område, salID) \
                    VALUES (?, ?, ?, 2)", (stolnr+1, (stolnr//28) + 1, område))

# Setter inn seter i sal 2 (Lille Scene) i Sete-tabellen

# ka den her gamle scenen variabelen e? e d liste over antall seter per rad per område liksom? føle d hadde vore nice me en kommentar ovenfor
gamlescene = [[18,16,17,18,18,17,18,17,17,14], [28,27,22,17], [33,18,17]]
omraader = ["parkett", "balkong", "galleri"]
for omraade in range(len(gamlescene)):
    for rad in range(len(gamlescene[omraade])):
        for stolnr in range(0, int(gamlescene[omraade][rad])):
            conn.execute("INSERT INTO Sete (stolNr, radNr, område, salID) \
                #VALUES (?, ?, ?, 2)", (stolnr+1, rad+1, omraader[omraade]))
            print(rad, omraader[omraade], stolnr+1)

conn.commit()

# kanskje lage en sjekk som sjekker count(*) fra Sete og sammenligner med summen av seter i Sal? (for å sjekke at alle setene er lagt inn i Sete-tabellen)
