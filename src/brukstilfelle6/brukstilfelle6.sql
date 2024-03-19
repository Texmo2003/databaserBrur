SELECT Forestilling.stykkeID, Forestilling.forestillingDato, COALESCE(SUM(Ordre.antallBilletter), 0) AS antallBilletter
FROM Forestilling LEFT JOIN Ordre ON Forestilling.forestillingDato = Ordre.forestillingDato AND Forestilling.stykkeID = Ordre.stykkeID
GROUP BY Forestilling.forestillingDato, Forestilling.stykkeID
ORDER BY antallBilletter DESC;