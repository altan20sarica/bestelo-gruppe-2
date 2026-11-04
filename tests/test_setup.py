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
    produkte = Produkt.aus_csv_datei(CSV_PFAD)
    
    """2. Orangensaft (P-1003) heraussuchen
     suchen nach dem Namen oder der ID, je nachdem was dein Produkt-Objekt hat"""
    orangensaft = next(p for p in produkte if "Orangensaft" in p.bezeichnung)
    
    """ 3. Verein anlegen (5% Rabatt)"""
    verein = Verein(1003, "SV Mustersstadt", "info@sv-musterstadt.de", "VR 12345", gemeinnuetzig=True)
    
    """4. Bestellung anlegen und 24 Stück hinzufügen"""
    bestellung = Bestellung(verein)
    
    """Annahme: Die Methode heißt 'hinzufuegen' (wie in Aufgabe A)"""
    bestellung.hinzufuegen(orangensaft, 24)
    
    assert bestellung.brutto_summe == 75.97


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
