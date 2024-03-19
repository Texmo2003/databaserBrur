# TDT4145 Datamodellering og Databasesystemer - DB2

All kode nødvendig for å kjøre databasen ligger i [src.zip](../src.zip). For å kjøre brukstilfellene, pakk ut [src.zip](../src.zip) og kjør [main.py](main.py) som ligger i `src/` mappen.

Det er viktig at [teater.db](../teater.db) ligger i samme rotmappe som `src/` mappen. [teater.db](../teater.db) skal altså **ikke** ligge i `src/` mappen, men 'ved siden av'.

De fleste brukstilfellene er avhengig av at brukstilfelle 1 blir kjørt først, da brukstilfelle 1 er ansvarlig for all innsetting av data. Alle brukstilfellene blir kjørt i rekkefølge i [main.py](main.py), så ved å kjøre [main.py](main.py), vil alle brukstilfellene bli kjørt i riktig rekkefølge.

Om man ønsker å tømme databasen, kan man kjøre [initalizeDB.py](initalizeDB.py).

For brukstilfellene som krever input, altså brukstilfelle 4 og 7, vil det komme en input prompt i terminalen. Her er inputten vi brukte for å generere våre resultat:

- **Brukstilfelle 4**: 2024-02-03
- **Brukstilfelle 7**: Emil Olafsson

For brukstilfellene som gjør en spørring, blir resultatet av spørringen satt i `resultat.txt` filen i mappen til brukstilfellet. I tillegg, så har vi satt inn resultatene i `output/` mappen, slik at man enkelt kan sjekke om alt kjører som det skal.

## Endringer fra DB1

- Endret stykkeID og salID sin type: int -> VARCHAR(250)
- Fjernet rolleID attributt i rolle, og gjorde om navn til unik identifikator
- Fjernet oppgaveID attributt i oppgave, og gjorde om oppgaveNavn til unik identifikator
- Gjorde Oppgave svak til Stykke, og fjernet OppgaverIStykke, fordi Oppgave uansett må ha (1,1) relasjon til stykke når den er svak.
  - Databasetabellene er fortsatt på fjerde normalform, siden ingen ikke-trivielle funksjonelle avhengigheter ble generert av dette.

## Antagelser

- Guttorm Ingesson er Baard Bratte
  - Dette antar vi fordi Guttorm Ingesson fra vedlegget 'Akter og roller i Kongsemnene', ikke ble funnet på [nettsiden til stykket](https://www.trondelag-teater.no/forestillinger/kongsemnene), og Baard Bratte fra nettsiden til stykket ikke ble funnet i vedlegget 'Akter og roller i Kongsemnene'.
- Trønder er med i akt 1
- I brukstilfelle 3 skal man legge inn en ordre på de 9 setene man har funnet, og at når det står "men du trenger ikke ta hensyn til selve betalingen, den antar vi skjer på et annet system som dere ikke trenger å lage", betyr det at vi ikke trenger å lage en betalingsmodul og bry oss om transaksjoner og lignende.
- I brukstilfelle 3 er det ubetydelig hvilken rad som blir valgt, så da velger vi den første raden som oppfyller kravene.
- I brukstilfelle 7 printer man ut når to skuespillere har spilt i samme stykke, og skiller ikke på om skuespillerene spilte sammen i kun én akt eller i flere akter i samme stykke.
