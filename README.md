# Bestelo – Gruppe N

> Allgemeines Shopsystem in Python · Programmieren 2 (BW220) · HWG Ludwigshafen
> Die Aufgabenbeschreibung finden Sie auf OLAT.

Ein Satz zu Ihrem Projekt: …

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
    class Kunde {
        +kundennummer: int
        +name: str
    }
    class Privatkunde
    Kunde <|-- Privatkunde
```

*(Person 5: vollständig ausbauen – alle 7 Klassen mit Eigenschaften, Methoden und Beziehungen.)*

## Ideen für Phase 2

- Branche: …
- Features: …
