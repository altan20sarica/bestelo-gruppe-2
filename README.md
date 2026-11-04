# Bestelo – Gruppe N

> Allgemeines Shopsystem in Python · Programmieren 2 (BW220) · HWG Ludwigshafen
> Die Aufgabenbeschreibung finden Sie auf OLAT.

Ein Satz zu Ihrem Projekt: Bestelo ist ein Konsolen-basiertes Bestellsystem, das es ermöglicht, Produkte aus einer CSV-Datei zu laden, verschiedene Kundentypen (Privatkunden, Geschäftskunden, Vereine) mit individuellen Rabatten zu verwalten und Bestellungen inklusive vollständigem Rechnungsdruck (Netto, Rabatt, MwSt., Brutto) abzuwickeln.



## Team

| Name | GitHub-Name | Rolle | Eigene Klassen / Dateien |
|------|-------------|-------|--------------------------|
| Altan Sarica      | @altan20sarica    | 1 · Teamleitung | `Kunde`, `Privatkunde` |
| Yakub Karakaya    | @yakubtaha-ai     | 2      | `Geschaeftskunde`, `Verein` |
| Mohammadmahdi Zandian | @Mehdixx007   | 3      | `Produkt`, `daten/produkte.csv` |
| Umutcan Yesil     | @Umutcanyesil     | 4      | `Bestellposition`, `Bestellung` |
| Yunus Apaydin     | @yunus0280        | 5      | Demo, README, UML, Integrationstest |

(Teamleitung bitte markieren.)

## So starten Sie

Im obersten Projektordner:

```bash
python -m pip install pytest   # einmalig
python -m pytest               # alle Tests ausführen
python -m bestelo              # Konsolen-Demo starten
```

## UML-Klassendiagramm

```mermaid
classDiagram
    direction TB

    class Kunde {
        +int kundennummer
        +str name
        +str email
        +__init__(kundennummer, name, email)
        +ist_gueltige_email(email) bool$
        +begruessung() str
        +rabattsatz() float
        +__str__() str
        +__repr__() str
        +__eq__(other) bool
    }

    class Privatkunde {
        +int geburtsjahr
        +bool stammkunde
        +__init__(kundennummer, name, email, geburtsjahr, stammkunde)
        +alter(stichjahr) int
        +rabattsatz() float
    }

    class Geschaeftskunde {
        +str firmenname
        +str ust_id
        +int zahlungsziel_tage
        +__init__(kundennummer, name, email, firmenname, ust_id, zahlungsziel_tage)
        +begruessung() str
        +rabattsatz() float
        +__str__() str
    }

    class Verein {
        +str registernummer
        +bool gemeinnuetzig
        +__init__(kundennummer, name, email, registernummer, gemeinnuetzig)
        +begruessung() str
        +rabattsatz() float
    }

    class Produkt {
        +tuple KATEGORIEN$
        +tuple ERMAESSIGTE_KATEGORIEN$
        +float MWST_ERMAESSIGT$
        +float MWST_REGULAER$
        +str artikelnummer
        +str bezeichnung
        +float nettopreis
        +str kategorie
        +float mwst_satz
        +float bruttopreis
        +__init__(artikelnummer, bezeichnung, nettopreis, kategorie)
        +aus_csv_zeile(zeile) Produkt$
        +aus_csv_datei(pfad) list$
        +__str__() str
        +__repr__() str
        +__eq__(other) bool
        +__lt__(other) bool
    }

    class Bestellposition {
        +Produkt produkt
        +int menge
        +float netto
        +float mwst
        +float brutto
        +__init__(produkt, menge)
        +__str__() str
    }

    class Bestellung {
        -int _naechste_nummer$
        +str bestellnummer
        +Kunde kunde
        +str status
        +list positionen
        +float netto_summe
        +float rabatt_betrag
        +float netto_nach_rabatt
        +float mwst_betrag
        +float brutto_summe
        +__init__(kunde)
        +hinzufuegen(produkt, menge)
        +abschliessen()
        +__len__() int
        +__str__() str
    }

    Kunde <|-- Privatkunde
    Kunde <|-- Geschaeftskunde
    Kunde <|-- Verein

    Kunde "1" <-- "0..*" Bestellung : kunde
    Produkt "1" <-- "0..*" Bestellposition : produkt
    Bestellung "1" *-- "0..*" Bestellposition : positionen
```




## Ideen für Phase 2

- Branche: Bürobedarf und Büroausstattung
- Features: - Filter nach Kategorie und Preis 
            - Lagerbestand anzeigen und bei einer Bestellung aktualisieren 
            - Bestellbestätigung ausgeben
