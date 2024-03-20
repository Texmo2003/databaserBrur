DROP TABLE IF EXISTS HarOppgave;
DROP TABLE IF EXISTS HarRolle;
DROP TABLE IF EXISTS FinnesIAkt;
DROP TABLE IF EXISTS PrisForForestilling;
DROP TABLE IF EXISTS TeaterAnsatt;
DROP TABLE IF EXISTS Rolle;
DROP TABLE IF EXISTS Akt;
DROP TABLE IF EXISTS Oppgave;
DROP TABLE IF EXISTS Forestilling;
DROP TABLE IF EXISTS Stykke;
DROP TABLE IF EXISTS Billettgruppe;
DROP TABLE IF EXISTS Sete;
DROP TABLE IF EXISTS Sal;
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
    stykkeID VARCHAR(250),
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
    salID VARCHAR(250),
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
    salID VARCHAR(250),
    PRIMARY KEY (stolNr, radNr, område, salID),
    FOREIGN KEY (salID) REFERENCES Sal(salID)
);

CREATE TABLE Sal (
    salID VARCHAR(250) PRIMARY KEY,
    totaltAntallSeter INT
);

CREATE TABLE Billettgruppe (
    gruppeNavn VARCHAR(100) PRIMARY KEY
);

CREATE TABLE Stykke (
    stykkeID VARCHAR(250) PRIMARY KEY,
    forBarn BOOLEAN,
    klokkeslett TIME,
    salID VARCHAR(250),
    FOREIGN KEY (salID) REFERENCES Sal(salID)
);

CREATE TABLE Forestilling (
    forestillingDato DATE,
    stykkeID VARCHAR(250),
	PRIMARY KEY (forestillingDato, stykkeID),
    FOREIGN KEY (stykkeID) REFERENCES Stykke(stykkeID)
);

CREATE TABLE Oppgave (
    oppgaveNavn VARCHAR(100),
    stykkeID VARCHAR(250),
    PRIMARY KEY (oppgaveNavn, stykkeID),
    FOREIGN KEY (stykkeID) REFERENCES Stykke(stykkeID)
);

CREATE TABLE Akt (
    aktNr INT,
    stykkeID VARCHAR(250),
    navn VARCHAR(100) NULL,
	PRIMARY KEY (aktNr, stykkeID),
    FOREIGN KEY (stykkeID) REFERENCES Stykke(stykkeID)
);

CREATE TABLE Rolle (
    navn VARCHAR(100) PRIMARY KEY
);

CREATE TABLE TeaterAnsatt (
    ansattID INT PRIMARY KEY,
    navn VARCHAR(100),
    epost VARCHAR(255),
    ansattstatus VARCHAR(50),
    typeAnsatt VARCHAR(50)
);

CREATE TABLE PrisForForestilling (
    stykkeID VARCHAR(250),
    gruppeNavn VARCHAR(100),
    pris DECIMAL(10,2),
    PRIMARY KEY (stykkeID, gruppeNavn),
    FOREIGN KEY (stykkeID) REFERENCES Stykke(stykkeID),
    FOREIGN KEY (gruppeNavn) REFERENCES Billettgruppe(gruppeNavn)
);

CREATE TABLE FinnesIAkt (
    stykkeID VARCHAR(250),
    aktNr INT,
    navn VARCHAR(100),
    PRIMARY KEY (stykkeID, aktNr, navn),
    FOREIGN KEY (aktNr) REFERENCES Akt(aktNr),
    FOREIGN KEY (stykkeID) REFERENCES Akt(stykkeID),
    FOREIGN KEY (navn) REFERENCES Rolle(navn)
);

CREATE TABLE HarRolle (
    ansattID INT,
    navn VARCHAR(100),
    PRIMARY KEY (ansattID, navn),
    FOREIGN KEY (ansattID) REFERENCES TeaterAnsatt(ansattID),
    FOREIGN KEY (navn) REFERENCES Rolle(navn)
);

CREATE TABLE HarOppgave (
    ansattID INT,
    oppgaveNavn VARCHAR(100),
    stykkeID VARCHAR(250),
    PRIMARY KEY (ansattID, oppgaveNavn, stykkeID),
    FOREIGN KEY (ansattID) REFERENCES TeaterAnsatt(ansattID),
    FOREIGN KEY (oppgaveNavn) REFERENCES Oppgave(oppgaveNavn)
    FOREIGN KEY (stykkeID) REFERENCES Oppgave(stykkeID)
);