DELETE FROM Sal;
DELETE FROM Sete;
DELETE FROM Stykke;
DELETE FROM Forestilling;
DELETE FROM Billettgruppe;
DELETE FROM PrisForForestilling;
DELETE FROM Akt;
DELETE FROM Rolle;
DELETE FROM FinnesIAkt;
DELETE FROM Oppgave;
DELETE FROM TeaterAnsatt;
DELETE FROM HarRolle;
DELETE FROM HarOppgave;

INSERT INTO Sal (salID, totaltAntallSeter) VALUES ('Hovedscenen', 0);
INSERT INTO Sal (salID, totaltAntallSeter) VALUES ('Gamle Scene', 0);

INSERT INTO Stykke (stykkeID, forBarn, klokkeslett, salID) VALUES ('Kongsemnene', false, '19:00', 'Hovedscenen');
INSERT INTO Stykke (stykkeID, forBarn, klokkeslett, salID) VALUES ('Størst av alt er kjærligheten', true, '18:30', 'Gamle Scene');


INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-01', 'Kongsemnene');
INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-02', 'Kongsemnene');
INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-03', 'Kongsemnene');
INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-05', 'Kongsemnene');
INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-06', 'Kongsemnene');

INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-03', 'Størst av alt er kjærligheten');
INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-06', 'Størst av alt er kjærligheten');
INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-07', 'Størst av alt er kjærligheten');
INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-12', 'Størst av alt er kjærligheten');
INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-13', 'Størst av alt er kjærligheten');
INSERT INTO Forestilling (forestillingDato, stykkeID) VALUES ('2024-02-14', 'Størst av alt er kjærligheten');


INSERT INTO Billettgruppe (gruppeNavn) VALUES ('Ordinær');
INSERT INTO Billettgruppe (gruppeNavn) VALUES ('Honnør');
INSERT INTO Billettgruppe (gruppeNavn) VALUES ('Student');
INSERT INTO Billettgruppe (gruppeNavn) VALUES ('Barn');
INSERT INTO Billettgruppe (gruppeNavn) VALUES ('Gruppe 10');
INSERT INTO Billettgruppe (gruppeNavn) VALUES ('Gruppe honnør 10');


INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Kongsemnene', 'Ordinær', 450);
INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Kongsemnene', 'Honnør', 380);
INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Kongsemnene', 'Student', 280);
INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Kongsemnene', 'Gruppe 10', 420);
INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Kongsemnene', 'Gruppe honnør 10', 360);

INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Størst av alt er kjærligheten', 'Ordinær', 350);
INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Størst av alt er kjærligheten', 'Honnør', 300);
INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Størst av alt er kjærligheten', 'Student', 220);
INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Størst av alt er kjærligheten', 'Barn', 220);
INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Størst av alt er kjærligheten', 'Gruppe 10', 320);
INSERT INTO PrisForForestilling (stykkeID, gruppeNavn, pris) VALUES ('Størst av alt er kjærligheten', 'Gruppe honnør 10', 270);


INSERT INTO Akt (aktNr, stykkeID, navn) VALUES (1, 'Kongsemnene', null);
INSERT INTO Akt (aktNr, stykkeID, navn) VALUES (2, 'Kongsemnene', null);
INSERT INTO Akt (aktNr, stykkeID, navn) VALUES (3, 'Kongsemnene', null);
INSERT INTO Akt (aktNr, stykkeID, navn) VALUES (4, 'Kongsemnene', null);
INSERT INTO Akt (aktNr, stykkeID, navn) VALUES (5, 'Kongsemnene', null);

INSERT INTO Akt (aktNr, stykkeID, navn) VALUES (1, 'Størst av alt er kjærligheten', null);


INSERT INTO Rolle (navn) VALUES ('Haakon Haakonssønn');
INSERT INTO Rolle (navn) VALUES ('Inga fra Vartejg (Haakons mor)');
INSERT INTO Rolle (navn) VALUES ('Skule jarl');
INSERT INTO Rolle (navn) VALUES ('Fru Ragnhild (Skules hustru)');
INSERT INTO Rolle (navn) VALUES ('Margrete (Skules datter)');
INSERT INTO Rolle (navn) VALUES ('Sigrid (Skules søster)');
INSERT INTO Rolle (navn) VALUES ('Ingebjørg');
INSERT INTO Rolle (navn) VALUES ('Biskop Nikolas');
INSERT INTO Rolle (navn) VALUES ('Gregorius Jonssønn');
INSERT INTO Rolle (navn) VALUES ('Pål Flida');
INSERT INTO Rolle (navn) VALUES ('Trønder');
INSERT INTO Rolle (navn) VALUES ('Baard Bratte');
INSERT INTO Rolle (navn) VALUES ('Jatgeir Skald');
INSERT INTO Rolle (navn) VALUES ('Dagfinn Bonde');
INSERT INTO Rolle (navn) VALUES ('Peter (prest og Ingebjørgs sønn)');

INSERT INTO Rolle (navn) VALUES ('Sunniva Du Mond Nordal');
INSERT INTO Rolle (navn) VALUES ('Jo Saberniak');
INSERT INTO Rolle (navn) VALUES ('Marte M. Steinholt');
INSERT INTO Rolle (navn) VALUES ('Tor Ivar Hagen');
INSERT INTO Rolle (navn) VALUES ('Trond-Ove Skrødal');
INSERT INTO Rolle (navn) VALUES ('Natalie Grøndahl Tangen');
INSERT INTO Rolle (navn) VALUES ('Åsmund Flaten');


INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Haakon Haakonssønn');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Haakon Haakonssønn');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Haakon Haakonssønn');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Haakon Haakonssønn');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Haakon Haakonssønn');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Dagfinn Bonde');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Dagfinn Bonde');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Dagfinn Bonde');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Dagfinn Bonde');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Dagfinn Bonde');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Jatgeir Skald');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Sigrid (Skules søster)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Sigrid (Skules søster)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Sigrid (Skules søster)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Ingebjørg');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Baard Bratte');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Skule jarl');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Skule jarl');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Skule jarl');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Skule jarl');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Skule jarl');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Inga fra Vartejg (Haakons mor)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Inga fra Vartejg (Haakons mor)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Pål Flida');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Pål Flida');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Pål Flida');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Pål Flida');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Pål Flida');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Fru Ragnhild (Skules hustru)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Fru Ragnhild (Skules hustru)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Gregorius Jonssønn');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Gregorius Jonssønn');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Gregorius Jonssønn');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Gregorius Jonssønn');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Margrete (Skules datter)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Margrete (Skules datter)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Margrete (Skules datter)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Margrete (Skules datter)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Biskop Nikolas');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 2, 'Biskop Nikolas');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Biskop Nikolas');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 3, 'Peter (prest og Ingebjørgs sønn)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 4, 'Peter (prest og Ingebjørgs sønn)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 5, 'Peter (prest og Ingebjørgs sønn)');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Kongsemnene', 1, 'Trønder');

INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Sunniva Du Mond Nordal');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Jo Saberniak');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Marte M. Steinholt');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Tor Ivar Hagen');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Trond-Ove Skrødal');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Natalie Grøndahl Tangen');
INSERT INTO FinnesIAkt (stykkeID, aktNr, navn) VALUES ('Størst av alt er kjærligheten', 1, 'Åsmund Flaten');


INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Regi', 'Kongsemnene');
INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Musikkutvelgelse', 'Kongsemnene');
INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Scenografi', 'Kongsemnene');
INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Kostymer', 'Kongsemnene');
INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Lysdesign', 'Kongsemnene');
INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Dramaturg', 'Kongsemnene');

INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Regi', 'Størst av alt er kjærligheten');
INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Scenografi', 'Størst av alt er kjærligheten');
INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Kostymer', 'Størst av alt er kjærligheten');
INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Lysdesign', 'Størst av alt er kjærligheten');
INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Dramaturg', 'Størst av alt er kjærligheten');
INSERT INTO Oppgave (oppgaveNavn, stykkeID) VALUES ('Musikalsk ansvarlig', 'Størst av alt er kjærligheten');


INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (1, 'Arturo Scotti', 'acotti@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (2, 'Ingunn Beate Strige Øyen', 'ibsoyen@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (3, 'Hans Petter Nilsen', 'hpnilsen@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (4, 'Madeleine Brandtzæg Nilsen', 'mbnilsen@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (5, 'Synnøve Fossum Eriksen', 'sferiksen@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (6, 'Emma Caroline Deichmann', 'ecdeichmann@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (7, 'Thomas Jensen Takyi', 'tjtakyi@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (8, 'Per Bogstad Gulliksen', 'pbgulliksen@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (9, 'Isak Holmen Sørensen', 'ihsorensen@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (10, 'Fabian Heidelberg Lunde', 'fhlunde@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (11, 'Emil Olafsson', 'eolafsson@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (12, 'Snorre Ryen Tøndel', 'srtondel@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (13, 'Yury Butusov', 'ybutusov@gmail.com', 'fast', 'ResterendRoller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (14, 'Aleksandr Shishkin-Hokusai', 'ashokusai@gmail.com', 'fast', 'Resterende Roller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (15, 'Eivind Myren', 'emyren@gmail.com', 'fast', 'ResterendRoller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (16, 'Mina Rype Stokke', 'mrstokke@gmail.com', 'fast', 'ResterendRoller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (17, 'Sunniva Du Mond Nordal', 'sdmnordal@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (18, 'Jo Saberniak', 'jsaberniak@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (19, 'Marte M. Steinholt', 'mmsteinholt@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (20, 'Tor Ivar Hagen', 'tihagen@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (21, 'Trond-Ove Skrødal', 'toskrødal@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (22, 'Natalie Grøndahl Tangen', 'ngtangen@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (23, 'Åsmund Flaten', 'aaflaten@gmail.com', 'fast', 'Skuespiller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (24, 'Jonas Corell Petersen', 'jcpetersen@gmail.com', 'fast', 'Resterende Roller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (25, 'David Ghert', 'dghert@gmail.com', 'fast', 'Resterende Roller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (26, 'Gaute Tønder', 'gtonder@gmail.com', 'fast', 'resterendroller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (27, 'Magnus Mikaelsen', 'mmikaelsen@gmail.com', 'fast', 'Resterende Roller');
INSERT INTO TeaterAnsatt (ansattID, navn, epost, ansattstatus, typeAnsatt) VALUES (28, 'Kristoffer Spender', 'kspender@gmail.com', 'fast', 'Resterende Roller');


INSERT INTO HarRolle (ansattID, navn) VALUES (1, 'Haakon Haakonssønn');
INSERT INTO HarRolle (ansattID, navn) VALUES (2, 'Inga fra Vartejg (Haakons mor)');
INSERT INTO HarRolle (ansattID, navn) VALUES (3, 'Skule jarl');
INSERT INTO HarRolle (ansattID, navn) VALUES (4, 'Fru Ragnhild (Skules hustru)');
INSERT INTO HarRolle (ansattID, navn) VALUES (5, 'Margrete (Skules datter)');
INSERT INTO HarRolle (ansattID, navn) VALUES (6, 'Sigrid (Skules søster)');
INSERT INTO HarRolle (ansattID, navn) VALUES (6, 'Ingebjørg');
INSERT INTO HarRolle (ansattID, navn) VALUES (7, 'Biskop Nikolas');
INSERT INTO HarRolle (ansattID, navn) VALUES (8, 'Gregorius Jonssønn');
INSERT INTO HarRolle (ansattID, navn) VALUES (9, 'Pål Flida');
INSERT INTO HarRolle (ansattID, navn) VALUES (9, 'Trønder');
INSERT INTO HarRolle (ansattID, navn) VALUES (10, 'Baard Bratte');
INSERT INTO HarRolle (ansattID, navn) VALUES (10, 'Trønder');
INSERT INTO HarRolle (ansattID, navn) VALUES (11, 'Jatgeir Skald');
INSERT INTO HarRolle (ansattID, navn) VALUES (11, 'Dagfinn Bonde');
INSERT INTO HarRolle (ansattID, navn) VALUES (12, 'Peter (prest og Ingebjørgs sønn)');

INSERT INTO HarRolle (ansattID, navn) VALUES (17, 'Sunniva Du Mond Nordal');
INSERT INTO HarRolle (ansattID, navn) VALUES (18, 'Jo Saberniak');
INSERT INTO HarRolle (ansattID, navn) VALUES (19, 'Marte M. Steinholt');
INSERT INTO HarRolle (ansattID, navn) VALUES (20, 'Tor Ivar Hagen');
INSERT INTO HarRolle (ansattID, navn) VALUES (21, 'Trond-Ove Skrødal');
INSERT INTO HarRolle (ansattID, navn) VALUES (22, 'Natalie Grøndahl Tangen');
INSERT INTO HarRolle (ansattID, navn) VALUES (23, 'Åsmund Flaten');


INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (13, 'Regi', 'Kongsemnene');
INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (13, 'Musikkutvelgelse', 'Kongsemnene');
INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (14, 'Scenografi', 'Kongsemnene');
INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (14, 'Kostymer', 'Kongsemnene');
INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (15, 'Lysdesign', 'Kongsemnene');
INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (16, 'Dramaturg', 'Kongsemnene');

INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (24, 'Regi', 'Størst av alt er kjærligheten');
INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (25, 'Scenografi', 'Størst av alt er kjærligheten');
INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (25, 'Kostymer', 'Størst av alt er kjærligheten');
INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (26, 'Musikalsk ansvarlig', 'Størst av alt er kjærligheten');
INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (27, 'Lysdesign', 'Størst av alt er kjærligheten');
INSERT INTO HarOppgave (ansattID, oppgaveNavn, stykkeID) VALUES (28, 'Dramaturg', 'Størst av alt er kjærligheten');