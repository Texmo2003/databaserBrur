DROP TABLE IF EXISTS HarOppgave;
DROP TABLE IF EXISTS HarRolle;
DROP TABLE IF EXISTS FinnesIAkt;
DROP TABLE IF EXISTS OppgaverIStykke;
DROP TABLE IF EXISTS PrisForForestilling;
DROP TABLE IF EXISTS TeaterAnsatt;
DROP TABLE IF EXISTS Rolle;
DROP TABLE IF EXISTS Akt;
DROP TABLE IF EXISTS Oppgave;
DROP TABLE IF EXISTS Forestilling;
DROP TABLE IF EXISTS Stykke;
DROP TABLE IF EXISTS Billettgruppe;
DROP TABLE IF EXISTS Sal;
DROP TABLE IF EXISTS Sete;
DROP TABLE IF EXISTS Billett;
DROP TABLE IF EXISTS Ordre;
DROP TABLE IF EXISTS Kunde;

CREATE TABLE Kunde (
    kundeID INT PRIMARY KEY,
    tlfNr VARCHAR(20),
    navn VARCHAR(100),
    adresse VARCHAR(255)
);

CREATE TABLE Ordre (
    ordreID INT PRIMARY KEY,
    kjøpsdato DATE,
    kjøpstid TIME,
    antallBilletter INT,
    kundeID INT,
    forestillingDato DATE,
    stykkeID INT,
    FOREIGN KEY (kundeID) REFERENCES Kunde(kundeID),
	FOREIGN KEY (forestillingDato) REFERENCES Forestilling(forestillingDato),
	FOREIGN KEY (stykkeID) REFERENCES Forestilling(stykkeID)
);

CREATE TABLE Billett (
    billettNr INT,
    ordreID INT,
    gruppeNavn VARCHAR(100),
    stolNr INT,
    radNr INT,
    område VARCHAR(50),
    salID INT,
	PRIMARY KEY (billettNr, ordreID),
    FOREIGN KEY (ordreID) REFERENCES Ordre(ordreID),
    FOREIGN KEY (gruppeNavn) REFERENCES Billettgruppe(gruppeNavn),
	FOREIGN KEY (stolNr) REFERENCES Sete(stolNr),
	FOREIGN KEY (radNr) REFERENCES Sete(radNr),
	FOREIGN KEY (område) REFERENCES Sete(område),
	FOREIGN KEY (salID) REFERENCES Sete(salID)
);

CREATE TABLE Sete (
    stolNr INT,
    radNr INT,
    område VARCHAR(50),
    salID INT,
    PRIMARY KEY (stolNr, radNr, område, salID),
    FOREIGN KEY (salID) REFERENCES Sal(salID)
);

CREATE TABLE Sal (
    salID INT PRIMARY KEY,
    totaltAntallSeter INT
);

CREATE TABLE Billettgruppe (
    gruppeNavn VARCHAR(100) PRIMARY KEY
);

CREATE TABLE Stykke (
    stykkeID INT PRIMARY KEY,
    forBarn BOOLEAN,
    klokkeslett TIME,
    salID INT,
    FOREIGN KEY (salID) REFERENCES Sal(salID)
);

CREATE TABLE Forestilling (
    forestillingDato DATE,
    stykkeID INT,
	PRIMARY KEY (forestillingDato, stykkeID),
    FOREIGN KEY (stykkeID) REFERENCES Stykke(stykkeID)
);

CREATE TABLE Oppgave (
    oppgaveID INT PRIMARY KEY,
    oppgaveNavn VARCHAR(100)
);

CREATE TABLE Akt (
    aktNr INT,
    stykkeID INT,
    navn VARCHAR(100) NULL,
	PRIMARY KEY (aktNr, stykkeID),
    FOREIGN KEY (stykkeID) REFERENCES Stykke(stykkeID)
);

CREATE TABLE Rolle (
    rolleID INT PRIMARY KEY,
    navn VARCHAR(100)
);

CREATE TABLE TeaterAnsatt (
    ansattID INT PRIMARY KEY,
    navn VARCHAR(100),
    epost VARCHAR(255),
    ansattstatus VARCHAR(50),
    typeAnsatt VARCHAR(50)
);

CREATE TABLE PrisForForestilling (
    stykkeID INT,
    gruppeNavn VARCHAR(100),
    pris DECIMAL(10,2),
    PRIMARY KEY (stykkeID, gruppeNavn),
    FOREIGN KEY (stykkeID) REFERENCES Stykke(stykkeID),
    FOREIGN KEY (gruppeNavn) REFERENCES Billettgruppe(gruppeNavn)
);

CREATE TABLE OppgaverIStykke (
    oppgaveID INT,
    stykkeID INT,
    PRIMARY KEY (oppgaveID, stykkeID),
    FOREIGN KEY (oppgaveID) REFERENCES Oppgave(oppgaveID),
    FOREIGN KEY (stykkeID) REFERENCES Stykke(stykkeID)
);

CREATE TABLE FinnesIAkt (
    stykkeID INT,
    aktNr INT,
    rolleID INT,
    PRIMARY KEY (stykkeID, aktNr, rolleID),
    FOREIGN KEY (aktNr) REFERENCES Akt(aktNr),
    FOREIGN KEY (stykkeID) REFERENCES Akt(stykkeID),
    FOREIGN KEY (rolleID) REFERENCES Rolle(rolleID)
);

CREATE TABLE HarRolle (
    ansattID INT,
    rolleID INT,
    PRIMARY KEY (ansattID, rolleID),
    FOREIGN KEY (ansattID) REFERENCES TeaterAnsatt(ansattID),
    FOREIGN KEY (rolleID) REFERENCES Rolle(rolleID)
);

CREATE TABLE HarOppgave (
    ansattID INT,
    oppgaveID INT,
    PRIMARY KEY (ansattID, oppgaveID),
    FOREIGN KEY (ansattID) REFERENCES TeaterAnsatt(ansattID),
    FOREIGN KEY (oppgaveID) REFERENCES Oppgave(oppgaveID)
);