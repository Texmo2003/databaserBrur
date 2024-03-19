DELETE FROM Ordre WHERE ordreID = 1 OR ordreID = 2;
DELETE FROM Billett WHERE ordreID = 1 OR ordreID = 2;
DELETE FROM Kunde WHERE kundeid = 69;

-- Dummy kunde
INSERT INTO Kunde (kundeID, tlfNr, navn, adresse) VALUES (69, 12345678, 'Ola Nordmann', 'Olasvei 1');

INSERT INTO Ordre (ordreID, kjøpsdato, kjøpstid, antallBilletter, kundeID, forestillingDato, stykkeID) VALUES (1, '2024-01-29', '02:37', 0, 69, '2024-02-03', 'Kongsemnene');
INSERT INTO Ordre (ordreID, kjøpsdato, kjøpstid, antallBilletter, kundeID, forestillingDato, stykkeID) VALUES (2, '2024-01-29', '02:38', 0, 69, '2024-02-03', 'Størst av alt er kjærligheten');