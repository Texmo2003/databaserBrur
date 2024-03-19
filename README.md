# TDT4145 Datamodellering og Databasesystemer - DB2

All kode nødvendig for å kjøre databasen ligger i src.zip. For å kjøre databasen, pakk ut src.zip. Brukstilfeller 2 og 3 er implementert på en måte som forventer at Brukstilfelle 1, altså innsetting av data, er kjørt først. Dette er fordi brukstilfelle 2 og 3 forventer at det finnes data i databasen.

For hvert brukstilfelle, kjører du `.py` filen i den tilhørende mappen.

- For brukstilfellene som krever input, følg instruksjonene i terminalen.
- For brukstilfellene som gjør en spørring, så ligger resultatet av spørringen i en `resultat.txt` fil i mappen til brukstilfellet, og resultatet blir også printet i terminalen.

## Endringer

- Endret stykkeID og salID sin type: int -> VARCHAR(250)
- Fjernet rolleID attributt i rolle, og gjorde om navn til unik identifikator
- Fjernet oppgaveID attributt i oppgave, og gjorde om oppgaveNavn til unik identifikator
- Gjorde oppgave svak til stykke, og fjernet OppgaverIStykke, siden Oppgave må ha (1,1) relasjon til stykke når den er svak.
  - Databasetabellene er fortsatt på fjerde normalform, siden ingen ikke-trivielle funksjonelle avhengigheter ble generert av dette.

## Antagelser

- Antar at Guttorm Ingesson er Baard Bratte.
- Antar at Trønder er med i akt 1
- Antar at i brukstilfelle 3 så skal man legge inn en ordre på de 9 setene man har funnet, og at når det står "men du trenger ikke ta hensyn til selve betalingen, den antar vi skjer på et annet system som dere ikke trenger å lage", så betyr det at vi ikke trenger å lage en betalingsmodul og bry oss om transaksjoner og lignende.
- Antar at i brukstilfelle 7 så printer man ut når to skuespillere har spilt i samme stykke, og skiller ikke på om skuespillerene spilte sammen i kun én akt eller i flere akter i samme stykke.
