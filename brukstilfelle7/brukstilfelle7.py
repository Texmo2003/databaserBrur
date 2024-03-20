import os
import sqlite3
conn = sqlite3.connect('teater.db')
c = conn.cursor()

def __init__(navn):
    if os.path.exists('output/brukstilfelle7.txt'):
        os.remove('output/brukstilfelle7.txt')
    with open("output/brukstilfelle7.txt", "w") as file:
        file.write("(Skuespillers navn, Kollegas navn, StykkeID)\n")
        file.write("--------------------------------------------------\n")
        for i in get_colleagues(navn):
            file.write(str(i) + '\n')
    conn.commit()
    conn.close()

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