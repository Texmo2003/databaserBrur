# databaserBrur

Trenger en forklaring på hvordan man kjører databasen i python

## Endringer

- Endret stykkeID og salID sin type: int -> VARCHAR(250)
- Fjernet rolleID attributt i rolle, og gjorde om navn til unik identifikator
- Fjernet oppgaveID attributt i oppgave, og gjorde om oppgaveNavn til unik identifikator
- Gjorde oppgave svak til stykke, og fjernet OppgaverIStykke, siden Oppgave må ha (1,1) relasjon til stykke når den er svak.
  - Databasetabellene er fortsatt på fjerde normalform, siden ingen ikke-trivielle funksjonelle avhengigheter ble generert av dette.
- Oppdaterte Sal-tabellen til

## Antagelser

- Antar at Guttorm Ingesson er Baard Bratte.
- Antar at Trønder er med i akt 1
