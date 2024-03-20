# TDT4145 Datamodellering og Databasesystemer - DB2

For å initialisere databasen, kjør [initalizeDB.py](initalizeDB.py). For å kjøre brukstilfellene, kjør [main.py](main.py). For brukstilfellene som krever input, altså brukstilfelle 4 og 7, vil det komme en input prompt i terminalen. Her er inputten vi brukte for å generere våre resultat:

- **Brukstilfelle 4**: 2024-02-03
- **Brukstilfelle 7**: Emil Olafsson

De fleste brukstilfellene er avhengig av at brukstilfelle 1 blir kjørt først, da brukstilfelle 1 er ansvarlig for all innsetting av data. Alle brukstilfellene blir kjørt i rekkefølge i [main.py](main.py), så om man bare forholder seg til [main.py](main.py) burde alt fungere som forventet.

Om det er ønskelig å tømme innholdet i databasen, men fortsatt beholde skjemaene/tabellene, kan man kjøre [initalizeDB.py](initalizeDB.py) på nytt.

For hvert brukstilfelle som gjør en spørring, blir resultatet av spørringen lagret i `output/` mappen i en `.txt` fil med navn som tilsvarer brukstilfellet.

## Forventet resultat fra hver spørring

### Brukstilfelle 3

```
(TotalPris)
--------------------------------------------------
3150
```

### Brukstilfelle 4

Sett inn dato for brukstilfelle 4 (Format: ÅÅÅÅ-MM-DD): `2024-02-03`

```
(StykkeID, AntallBilletter)
--------------------------------------------------
('Kongsemnene', 65)
('Størst av alt er kjærligheten', 36)
```

### Brukstilfelle 5

```
(StykkeID, Skuespillers navn, Rolle)
--------------------------------------------------
('Kongsemnene', 'Arturo Scotti', 'Haakon Haakonssønn')
('Kongsemnene', 'Ingunn Beate Strige Øyen', 'Inga fra Vartejg (Haakons mor)')
('Kongsemnene', 'Hans Petter Nilsen', 'Skule jarl')
('Kongsemnene', 'Madeleine Brandtzæg Nilsen', 'Fru Ragnhild (Skules hustru)')
('Kongsemnene', 'Synnøve Fossum Eriksen', 'Margrete (Skules datter)')
('Kongsemnene', 'Emma Caroline Deichmann', 'Sigrid (Skules søster)')
('Kongsemnene', 'Emma Caroline Deichmann', 'Ingebjørg')
('Kongsemnene', 'Thomas Jensen Takyi', 'Biskop Nikolas')
('Kongsemnene', 'Per Bogstad Gulliksen', 'Gregorius Jonssønn')
('Kongsemnene', 'Isak Holmen Sørensen', 'Pål Flida')
('Kongsemnene', 'Isak Holmen Sørensen', 'Trønder')
('Kongsemnene', 'Fabian Heidelberg Lunde', 'Baard Bratte')
('Kongsemnene', 'Fabian Heidelberg Lunde', 'Trønder')
('Kongsemnene', 'Emil Olafsson', 'Jatgeir Skald')
('Kongsemnene', 'Emil Olafsson', 'Dagfinn Bonde')
('Kongsemnene', 'Snorre Ryen Tøndel', 'Peter (prest og Ingebjørgs sønn)')
('Størst av alt er kjærligheten', 'Sunniva Du Mond Nordal', 'Sunniva Du Mond Nordal')
('Størst av alt er kjærligheten', 'Jo Saberniak', 'Jo Saberniak')
('Størst av alt er kjærligheten', 'Marte M. Steinholt', 'Marte M. Steinholt')
('Størst av alt er kjærligheten', 'Tor Ivar Hagen', 'Tor Ivar Hagen')
('Størst av alt er kjærligheten', 'Trond-Ove Skrødal', 'Trond-Ove Skrødal')
('Størst av alt er kjærligheten', 'Natalie Grøndahl Tangen', 'Natalie Grøndahl Tangen')
('Størst av alt er kjærligheten', 'Åsmund Flaten', 'Åsmund Flaten')
```

### Brukstilfelle 6

```
(StykkeID, Dato, AntallBilletterSolgt)
--------------------------------------------------
('Kongsemnene', '2024-02-03', 65)
('Størst av alt er kjærligheten', '2024-02-03', 36)
('Kongsemnene', '2024-02-01', 0)
('Kongsemnene', '2024-02-02', 0)
('Kongsemnene', '2024-02-05', 0)
('Kongsemnene', '2024-02-06', 0)
('Størst av alt er kjærligheten', '2024-02-06', 0)
('Størst av alt er kjærligheten', '2024-02-07', 0)
('Størst av alt er kjærligheten', '2024-02-12', 0)
('Størst av alt er kjærligheten', '2024-02-13', 0)
('Størst av alt er kjærligheten', '2024-02-14', 0)
```

### Brukstilfelle 7

Sett inn navn på skuespiller for brukstilfelle 7: `Emil Olafsson`

```
(Skuespillers navn, Kollegas navn, StykkeID)
--------------------------------------------------
('Emil Olafsson', 'Arturo Scotti', 'Kongsemnene')
('Emil Olafsson', 'Ingunn Beate Strige Øyen', 'Kongsemnene')
('Emil Olafsson', 'Hans Petter Nilsen', 'Kongsemnene')
('Emil Olafsson', 'Madeleine Brandtzæg Nilsen', 'Kongsemnene')
('Emil Olafsson', 'Synnøve Fossum Eriksen', 'Kongsemnene')
('Emil Olafsson', 'Emma Caroline Deichmann', 'Kongsemnene')
('Emil Olafsson', 'Thomas Jensen Takyi', 'Kongsemnene')
('Emil Olafsson', 'Per Bogstad Gulliksen', 'Kongsemnene')
('Emil Olafsson', 'Isak Holmen Sørensen', 'Kongsemnene')
('Emil Olafsson', 'Fabian Heidelberg Lunde', 'Kongsemnene')
('Emil Olafsson', 'Snorre Ryen Tøndel', 'Kongsemnene')
```

## Endringer fra DB1

- Endret stykkeID og salID sin type: int -> VARCHAR(250)
- Fjernet rolleID attributt i rolle, og gjorde om navn til unik identifikator
- Fjernet oppgaveID attributt i oppgave, og gjorde om oppgaveNavn til unik identifikator
- Gjorde Oppgave svak til Stykke, og fjernet OppgaverIStykke, fordi Oppgave uansett må ha (1,1) relasjon til stykke når den er svak.
  - Databasetabellene er fortsatt på fjerde normalform, siden ingen ikke-trivielle funksjonelle avhengigheter ble generert av dette.

## Antagelser

- Med 'skal være tom' tolker vi det til å mene at det ikke skal være noen kolonner, tabeller, eller noe som helst i `.db` filen.
- Guttorm Ingesson er Baard Bratte
  - Dette antar vi fordi Guttorm Ingesson fra vedlegget 'Akter og roller i Kongsemnene', ikke ble funnet på [nettsiden til stykket](https://www.trondelag-teater.no/forestillinger/kongsemnene), og Baard Bratte fra nettsiden til stykket ikke ble funnet i vedlegget 'Akter og roller i Kongsemnene'.
- Trønder er med i akt 1
- I brukstilfelle 3 skal man legge inn en ordre på de 9 setene man har funnet, og at når det står "men du trenger ikke ta hensyn til selve betalingen, den antar vi skjer på et annet system som dere ikke trenger å lage", betyr det at vi ikke trenger å lage en betalingsmodul og bry oss om transaksjoner og lignende.
- I brukstilfelle 3 er det ubetydelig hvilken rad som blir valgt, så da velger vi den første raden som oppfyller kravene.
- I brukstilfelle 7 printer man ut når to skuespillere har spilt i samme stykke, og skiller ikke på om skuespillerene spilte sammen i kun én akt eller i flere akter i samme stykke.
