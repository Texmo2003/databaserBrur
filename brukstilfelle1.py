import sqlite3
conn = sqlite3.connect('teater.db')

conn.execute("DELETE FROM Sete")
conn.execute("DELETE FROM Sal")
conn.execute("DELETE FROM Stykke")
conn.execute("DELETE FROM Forestilling")
conn.execute("DELETE FROM Billettgruppe")
conn.execute("DELETE FROM PrisForForestilling")
conn.execute("DELETE FROM Akt")
conn.execute("DELETE FROM Rolle")
conn.execute("DELETE FROM FinnesIAkt")
conn.execute("DELETE FROM Oppgave")
conn.execute("DELETE FROM TeaterAnsatt")
conn.execute("DELETE FROM HarRolle")
conn.execute("DELETE FROM HarOppgave")

# Setter inn sal 1 (Hovedscenen) og sal 2 (Gamle Scene) inn i Sal-tabellen
conn.execute("INSERT INTO Sal (salID, totaltAntallSeter) \
            VALUES ('Hovedscenen', 516)")
conn.execute("INSERT INTO Sal (salID, totaltAntallSeter) \
            VALUES ('Gamle Scene', 332)")

# Setter inn seter i sal 1 (Hovedscenen) i Sete-tabellen
with open("filesNeeded/hovedscenen.txt") as file:
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
        for stol in range(1, len(line)):
            stolnr += 1
            if line[stol] == "x":
                continue
            else:
                conn.execute("INSERT INTO Sete (stolNr, radNr, område, salID) VALUES (?, ?, ?, 'Hovedscenen')", (stolnr, radnr, omraade))
        radnr += 1

# Setter inn seter i sal 2 (Gamle Scene) i Sete-tabellen
with open("filesNeeded/gamle-scene.txt") as file:
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
        for stol in range(1, len(line)):
            stolnr += 1
            conn.execute("INSERT INTO Sete (stolNr, radNr, område, salID) VALUES (?, ?, ?, 'Gamle Scene')", (stolnr, radnr, omraade))
        radnr += 1
        stolnr = 1

# kanskje lage en sjekk som sjekker count(*) fra Sete og sammenligner med summen av seter i Sal? (for å sjekke at alle setene er lagt inn i Sete-tabellen)

# Setter inn stykker i Stykke-tabellen
conn.execute("INSERT INTO Stykke (stykkeID, forBarn, klokkeslett, salID) VALUES ('Kongsemnene', false, '19:00', 'Hovedscenen')")
conn.execute("INSERT INTO Stykke (stykkeID, forBarn, klokkeslett, salID) VALUES ('Størst av alt er kjærligheten', true, '18:30', 'Gamle Scene')")

# Setter inn forestillinger i Forestilling-tabellen
conn.execute("INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-01', 'Kongsemnene')")
conn.execute("INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-02', 'Kongsemnene')")
conn.execute("INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-03', 'Kongsemnene')")
conn.execute("INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-05', 'Kongsemnene')")
conn.execute("INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-06', 'Kongsemnene')")

conn.execute("INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-03', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-06', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-07', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-12', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-13', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-14', 'Størst av alt er kjærligheten')")

# Setter inn billettgrupper i Billettgruppe-tabellen
conn.execute("INSERT INTO Billettgruppe (gruppeNavn) VALUES ('Ordinær')")
conn.execute("INSERT INTO Billettgruppe (gruppeNavn) VALUES ('Honnør')")
conn.execute("INSERT INTO Billettgruppe (gruppeNavn) VALUES ('Student')")
conn.execute("INSERT INTO Billettgruppe (gruppeNavn) VALUES ('Barn')")
conn.execute("INSERT INTO Billettgruppe (gruppeNavn) VALUES ('Gruppe 10')")
conn.execute("INSERT INTO Billettgruppe (gruppeNavn) VALUES ('Gruppe honnør 10')")

# Setter inn priser for forestillinger i PrisForForestilling-tabellen
conn.execute("INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Kongsemnene', 'Ordinær', 450)")
conn.execute("INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Kongsemnene', 'Honnør', 380)")
conn.execute("INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Kongsemnene', 'Student', 280)")
conn.execute("INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Kongsemnene', 'Gruppe 10', 420)")
conn.execute("INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Kongsemnene', 'Gruppe honnør 10', 360)")

conn.execute("INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Størst av alt er kjærligheten', 'Ordinær', 350)")
conn.execute("INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Størst av alt er kjærligheten', 'Honnør', 300)")
conn.execute("INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Størst av alt er kjærligheten', 'Student', 220)")
conn.execute("INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Størst av alt er kjærligheten', 'Barn', 220)")
conn.execute("INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Størst av alt er kjærligheten', 'Gruppe 10', 320)")
conn.execute("INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Størst av alt er kjærligheten', 'Gruppe honnør 10', 270)")

# Setter inn akter i Akt-tabellen
conn.execute("INSERT INTO Akt (aktNr, stykkeID, navn) VALUES (1, 'Kongsemnene', null)")
conn.execute("INSERT INTO Akt (aktNr, stykkeID, navn) VALUES (2, 'Kongsemnene', null)")
conn.execute("INSERT INTO Akt (aktNr, stykkeID, navn) VALUES (3, 'Kongsemnene', null)")
conn.execute("INSERT INTO Akt (aktNr, stykkeID, navn) VALUES (4, 'Kongsemnene', null)")
conn.execute("INSERT INTO Akt (aktNr, stykkeID, navn) VALUES (5, 'Kongsemnene', null)")

conn.execute("INSERT INTO Akt (aktNr, stykkeID, navn) VALUES (1, 'Størst av alt er kjærligheten', null)")

# Setter inn roller i Rolle-tabellen
conn.execute("INSERT INTO Rolle (navn) VALUES ('Haakon Haakonssønn')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Inga fra Vartejg (Haakons mor)')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Skule jarl')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Fru Ragnhild (Skules hustru)')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Margrete (Skules datter)')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Sigrid (Skules søster)')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Ingebjørg')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Biskop Nikolas')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Gregorius Jonssønn')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Pål Flida')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Trønder')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Baard Bratte')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Jatgeir Skald')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Dagfinn Bonde')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Peter (prest og Ingebjørgs sønn)')")

conn.execute("INSERT INTO Rolle (navn) VALUES ('Sunniva Du Mond Nordal')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Jo Saberniak')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Marte M. Steinholt')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Tor Ivar Hagen')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Trond-Ove Skrødal')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Natalie Grøndahl Tangen')")
conn.execute("INSERT INTO Rolle (navn) VALUES ('Åsmund Flaten')")

# Setter inn roller i FinnesIAkt-tabellen
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Haakon Haakonssønn')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Haakon Haakonssønn')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Haakon Haakonssønn')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Haakon Haakonssønn')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Haakon Haakonssønn')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Dagfinn Bonde')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Dagfinn Bonde')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Dagfinn Bonde')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Dagfinn Bonde')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Dagfinn Bonde')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Jatgeir Skald')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Sigrid (Skules søster)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Sigrid (Skules søster)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Sigrid (Skules søster)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Ingebjørg')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Baard Bratte')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Skule jarl')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Skule jarl')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Skule jarl')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Skule jarl')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Skule jarl')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Inga fra Vartejg (Haakons mor)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Inga fra Vartejg (Haakons mor)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Pål Flida')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Pål Flida')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Pål Flida')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Pål Flida')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Pål Flida')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Fru Ragnhild (Skules hustru)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Fru Ragnhild (Skules hustru)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Gregorius Jonssønn')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Gregorius Jonssønn')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Gregorius Jonssønn')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Gregorius Jonssønn')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Margrete (Skules datter)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Margrete (Skules datter)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Margrete (Skules datter)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Margrete (Skules datter)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Biskop Nikolas')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Biskop Nikolas')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Biskop Nikolas')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Peter (prest og Ingebjørgs sønn)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Peter (prest og Ingebjørgs sønn)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Peter (prest og Ingebjørgs sønn)')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Trønder')")

conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Sunniva Du Mond Nordal')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Jo Saberniak')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Marte M. Steinholt')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Tor Ivar Hagen')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Trond-Ove Skrødal')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Natalie Grøndahl Tangen')")
conn.execute("INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Åsmund Flaten')")

# Setter inn oppgaver i Oppgaver-tabellen
conn.execute("INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Regi', 'Kongsemnene')")
conn.execute("INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Musikkutvelgelse', 'Kongsemnene')")
conn.execute("INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Scenografi', 'Kongsemnene')")
conn.execute("INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Kostymer', 'Kongsemnene')")
conn.execute("INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Lysdesign', 'Kongsemnene')")
conn.execute("INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Dramaturg', 'Kongsemnene')")

conn.execute("INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Regi', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Scenografi', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Kostymer', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Lysdesign', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Dramaturg', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Musikalsk ansvarlig', 'Størst av alt er kjærligheten')")

# Setter inn teateransatte i TeaterAnsatt-tabellen
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (1, 'Arturo Scotti', 'acotti@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (2, 'Ingunn Beate Strige Øyen', 'ibsoyen@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (3, 'Hans Petter Nilsen', 'hpnilsen@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (4, 'Madeleine Brandtzæg Nilsen', 'mbnilsen@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (5, 'Synnøve Fossum Eriksen', 'sferiksen@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (6, 'Emma Caroline Deichmann', 'ecdeichmann@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (7, 'Thomas Jensen Takyi', 'tjtakyi@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (8, 'Per Bogstad Gulliksen', 'pbgulliksen@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (9, 'Isak Holmen Sørensen', 'ihsorensen@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (10, 'Fabian Heidelberg Lunde', 'fhlunde@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (11, 'Emil Olafsson', 'eolafsson@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (12, 'Snorre Ryen Tøndel', 'srtondel@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (13, 'Yury Butusov', 'ybutusov@gmail.com', 'fast', 'Resterende Roller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (14, 'Aleksandr Shishkin-Hokusai', 'ashokusai@gmail.com', 'fast', 'Resterende Roller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (15, 'Eivind Myren', 'emyren@gmail.com', 'fast', 'Resterende Roller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (16, 'Mina Rype Stokke', 'mrstokke@gmail.com', 'fast', 'Resterende Roller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (17, 'Sunniva Du Mond Nordal', 'sdmnordal@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (18, 'Jo Saberniak', 'jsaberniak@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (19, 'Marte M. Steinholt', 'mmsteinholt@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (20, 'Tor Ivar Hagen', 'tihagen@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (21, 'Trond-Ove Skrødal', 'toskrødal@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (22, 'Natalie Grøndahl Tangen', 'ngtangen@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (23, 'Åsmund Flaten', 'aaflaten@gmail.com', 'fast', 'Skuespiller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (24, 'Jonas Corell Petersen', 'jcpetersen@gmail.com', 'fast', 'resterende roller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (25, 'David Ghert', 'dghert@gmail.com', 'fast', 'resterende roller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (26, 'Gaute Tønder', 'gtonder@gmail.com', 'fast', 'resterende roller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (27, 'Magnus Mikaelsen', 'mmikaelsen@gmail.com', 'fast', 'resterende roller')")
conn.execute("INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (28, 'Kristoffer Spender', 'kspender@gmail.com', 'fast', 'resterende roller')")

# Setter inn teateransatte i HarRolle-tabellen
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (1, 'Haakon Haakonssønn')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (2, 'Inga fra Vartejg (Haakons mor)')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (3, 'Skule jarl')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (4, 'Fru Ragnhild (Skules hustru)')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (5, 'Margrete (Skules datter)')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (6, 'Sigrid (Skules søster)')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (6, 'Ingebjørg')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (7, 'Biskop Nikolas')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (8, 'Gregorius Jonssønn')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (9, 'Pål Flida')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (9, 'Trønder')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (10, 'Baard Bratte')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (10, 'Trønder')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (11, 'Jatgeir Skald')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (11, 'Dagfinn Bonde')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (12, 'Peter (prest og Ingebjørgs sønn)')")

conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (17, 'Sunniva Du Mond Nordal')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (18, 'Jo Saberniak')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (19, 'Marte M. Steinholt')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (20, 'Tor Ivar Hagen')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (21, 'Trond-Ove Skrødal')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (22, 'Natalie Grøndahl Tangen')")
conn.execute("INSERT INTO HarRolle (ansattID, navn) VALUES (23, 'Åsmund Flaten')")

# Setter inn teateransatte i HarOppgave-tabellen
conn.execute("INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (13, 'Regi', 'Kongsemnene')")
conn.execute("INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (13, 'Musikkutvelgelse', 'Kongsemnene')")
conn.execute("INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (14, 'Scenografi', 'Kongsemnene')")
conn.execute("INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (14, 'Kostymer', 'Kongsemnene')")
conn.execute("INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (15, 'Lysdesign', 'Kongsemnene')")
conn.execute("INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (16, 'Dramaturg', 'Kongsemnene')")

conn.execute("INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (24, 'Regi', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (25, 'Scenografi', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (25, 'Kostymer', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (26, 'Musikalsk ansvarlig', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (27, 'Lysdesign', 'Størst av alt er kjærligheten')")
conn.execute("INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (28, 'Dramaturg', 'Størst av alt er kjærligheten')")

conn.commit()