DELETE FROM Billett WHERE ordreID = 3;
DELETE FROM Ordre WHERE ordreID = 3;
DELETE FROM Kunde WHERE kundeid = 69;

-- Dummy kunde
INSERT INTO Kunde (kundeID, tlfNr, navn, adresse) VALUES (69, 12345678, 'Ola Nordmann', 'Olasvei 1');

INSERT INTO Ordre (ordreID, kjøpsdato, kjøpstid, antallBilletter, kundeID, forestillingDato, stykkeID) VALUES (3, '2024-02-02', '12:00', 0, 69, '2024-02-03', 'Størst av alt er kjærligheten');