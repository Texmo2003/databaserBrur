# databaserBrur

Trenger en forklaring på hvordan man kjører databasen i python

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