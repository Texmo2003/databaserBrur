import sqlite3
conn = sqlite3.connect('teater.db')
c = conn.cursor()

def get_colleagues(who):
    c.execute('''
        SELECT DISTINCT AkterMedI.navn, Kollega.navn, FinnesIAkt.stykkeID
        FROM ((TeaterAnsatt INNER JOIN HarRolle ON TeaterAnsatt.ansattID = HarRolle.ansattID) INNER JOIN FinnesIAkt ON HarRolle.navn = FinnesIAkt.navn) AS Kollega INNER JOIN (
        SELECT DISTINCT FinnesIAkt.stykkeID, FinnesIAkt.aktNr, TeaterAnsatt.navn AS navn
        FROM (TeaterAnsatt INNER JOIN HarRolle ON TeaterAnsatt.ansattID = HarRolle.ansattID) INNER JOIN FinnesIAkt ON HarRolle.navn = FinnesIAkt.navn
        WHERE TeaterAnsatt.navn = ?
        ) AS AkterMedI ON Kollega.stykkeID = AkterMedI.stykkeID AND Kollega.aktNr = AkterMedI.aktNr
        WHERE Kollega.navn <> AkterMedI.navn
    ''', (who,))
    return c.fetchall()

ting = get_colleagues('Emil Olafsson')
for i in ting:
    print(i)

conn.commit()
conn.close()