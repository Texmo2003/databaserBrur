# TDT4145 Datamodellering og Databasesystemer - DB2

All kode nødvendig for å kjøre databasen ligger i `src.zip`. For å kjøre brukstilfellene, pakk ut `src.zip` og kjør `main.py` som ligger i `src/` mappen.

Det er viktig at `teater.db` ligger i samme rotmappe som `src/` mappen. `teater.db` skal altså **ikke** ligge i `src/` mappen.

De fleste brukstilfellene er avhengig av at brukstilfelle 1 blir kjørt først, siden brukstilfelle 1 er ansvarlig for all innsetting av data. Alle brukstilfellene blir kjørt i rekkefølge i `main.py`.

Om man ønsker å tømme databasen, kan man kjøre `initalizeDB.py`.

- For brukstilfellene som krever input, altså brukstilfelle 4 og 7, så har vi allerede satt inn et eksempel på input i `main.py` filen, og kommentert linjene man kan endre om inputten ønskes å endres.
- For brukstilfellene som gjør en spørring, så blir resultatet av spørringen satt i `resultat.txt` filen i mappen til brukstilfellet.

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
- Antar at i brukstilfelle 3 så er det ubetydelig hvilken rad som blir valgt, så da velger vi den første raden som oppfyller kravene.
- Antar at i brukstilfelle 7 så printer man ut når to skuespillere har spilt i samme stykke, og skiller ikke på om skuespillerene spilte sammen i kun én akt eller i flere akter i samme stykke.
