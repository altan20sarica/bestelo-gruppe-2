"""Prüft nur, ob Ihr Projekt richtig eingerichtet ist.

Wenn dieser Test grün ist, funktionieren Python, pytest und die Ordnerstruktur.
Sie dürfen die Datei behalten – sie zählt aber nicht zu den 18 Pflicht-Tests.
"""


def test_paket_ist_importierbar() -> None:
    import bestelo
    assert bestelo is not None


from pathlib import Path
from bestelo.__main__ import main, CSV_PFAD
from bestelo.bestellungen import Bestellung
from bestelo.kunden import Verein
from bestelo.produkte import Produkt


def test_ablauf_verein_bestellt_orangensaft():
    """
    Testet den Ablauf: Produkte laden, Verein anlegen, 24x Orangensaft bestellen
    und den Bruttobetrag (75.97 €) prüfen.
    """
    """ 1. Produkte aus CSV laden"""
    produkte = Produkt.aus_csv(CSV_PFAD)
    
    """2. Orangensaft (P-1003) heraussuchen"""
    # Wir suchen nach dem Namen oder der ID, je nachdem was dein Produkt-Objekt hat
    orangensaft = next(p for p in produkte if "Orangensaft" in p.name)
    
    """ 3. Verein anlegen (5% Rabatt)"""
    verein = Verein("SV Mustersstadt", rabatt=5)
    
    """4. Bestellung anlegen und 24 Stück hinzufügen"""
    bestellung = Bestellung("B-Test", verein)
    
    """Annahme: Die Methode heißt 'position_hinzufuegen' (wie in Aufgabe A)"""
    bestellung.position_hinzufuegen(24, orangensaft)
    
    """5. Brutto berechnen
     Netto = 24 * 2.80 = 67.20
     Rabatt 5% = 3.36
     Netto nach Rabatt = 63.84
     MwSt 19% = 12.13 (63.84 * 0.19 = 12.1296)
     Brutto = 63.84 + 12.13 = 75.97"""
    
    netto = sum(pos.menge * pos.produkt.preis for pos in bestellung.positionen)
    rabatt = netto * (verein.rabatt_prozent / 100)
    mwst = (netto - rabatt) * 0.19
    brutto = (netto - rabatt) + mwst
    
    # Prüfen, ob der Bruttobetrag auf 2 Nachkommastellen gerundet 75.97 ergibt
    assert round(brutto, 2) == 75.97


def test_demo_zeigt_bruttosumme(capsys):
    """
    Demo-Test: Führt main() aus und prüft mit capsys, ob die Ausgabe 
    den Bruttobetrag von 79.66 € enthält.
    """
    """main() ausführen (gibt alles auf der Konsole aus)"""
    main()
    
    """Alles abfangen, was print() ausgegeben hat"""
    ausgabe = capsys.readouterr().out
    
    """ Prüfen, ob der String "79.66" in der Ausgabe vorkommt"""
    assert "79.66" in ausgabe 