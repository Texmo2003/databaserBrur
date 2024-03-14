import sqlite3
conn = sqlite3.connect('teater.db')

conn.execute("DELETE FROM Sal")
conn.execute("DELETE FROM Sete")

# Setter inn sal 1 (Hovedscenen) og sal 2 (Gamle scene) inn i Sal-tabellen
conn.execute("INSERT INTO Sal (salID, totaltAntallSeter) \
            VALUES (1, 516)")
conn.execute("INSERT INTO Sal (salID, totaltAntallSeter) \
            VALUES (2, 332)")

# Setter inn seter i sal 1 (Hovedscenen) i Sete-tabellen
for stolnr in range(1, 525):
    område = "parkett"
    radnr = ((stolnr-1)//28) + 1
    if (stolnr > 466 and stolnr < 471) or (stolnr > 494 and stolnr < 499):
        continue
    if stolnr > 504:
        område = "galleri"
        radnr = ((504//28) + 1) + ((stolnr-505)//5)

    print(stolnr, radnr, område)
    conn.execute("INSERT INTO Sete (stolNr, radNr, område, salID) VALUES (?, ?, ?, 1)", (stolnr, radnr, område))

# Setter inn seter i sal 2 (Lille Scene) i Sete-tabellen

# ka den her gamle scenen variabelen e? e d liste over antall seter per rad per område liksom? føle d hadde vore nice me en kommentar ovenfor
gamlescene = [[18,16,17,18,18,17,18,17,17,14], [28,27,22,17], [33,18,17]]
omraader = ["parkett", "balkong", "galleri"]
for omraade in range(len(gamlescene)):
    for rad in range(len(gamlescene[omraade])):
        for stolnr in range(0, int(gamlescene[omraade][rad])):
            conn.execute("INSERT INTO Sete (stolNr, radNr, område, salID) VALUES (?, ?, ?, 2)", (stolnr+1, rad+1, omraader[omraade]))
            print(rad, omraader[omraade], stolnr+1)

conn.commit()

# kanskje lage en sjekk som sjekker count(*) fra Sete og sammenligner med summen av seter i Sal? (for å sjekke at alle setene er lagt inn i Sete-tabellen)
