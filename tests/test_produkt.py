from bestelo.produkte import Produkt

import pytest

""" 01. Zeile einlesen und in ein Produkt-Objekt umwandeln """


def test_produkte_aus_csv_zeile():
    zeile = "P-1001;Kaffeebohnen 500 g;8.90;Lebensmittel"
    produkt = Produkt.aus_csv_zeile(zeile)
    assert produkt.artikelnummer == "P-1001"
    assert produkt.bezeichnung == "Kaffeebohnen 500 g"
    assert produkt.nettopreis == 8.90
    assert produkt.kategorie == "Lebensmittel"


""" assert kontrolliert das Ergebnis."""

"""02. Produkt Objekt aus CSV-Datei erstellen und überprüfen"""


def test_produkte_aus_csv_datei():
    pfad = "bestelo/daten/produkte.csv"
    produkte = Produkt.aus_csv_datei(pfad)
    assert len(produkte) == 6
    assert produkte[0].artikelnummer == "P-1001"
    assert produkte[0].bezeichnung == "Kaffeebohnen 500 g"
    assert produkte[0].nettopreis == 8.90
    assert produkte[0].kategorie == "Lebensmittel"
    assert min(produkte).artikelnummer == "P-1003"


""" [0] ist der Index des ersten Elements in der Liste. """

""" 03. __str__ und __repr__ Methoden testen """


def test_produkte_string_darstellung():
    produkt = Produkt("P-0001", "Kaffee 500 g", 8.90, "Lebensmittel")
    assert str(produkt) == "P-0001 Kaffee 500 g – 8.90 € netto"
    assert repr(produkt) == "Produkt('P-0001', 'Kaffee 500 g', 8.9, 'Lebensmittel')"


""" str(produkt) gibt eine menschenlesbare Darstellung des Objekts zurück, während repr(produkt) eine detailliertere Darstellung liefert, die für Entwickler nützlich ist. """

""" 04. Mehrwertsteuerberechnung testen """


def test_produkte_mehrwertsteuer_berechnung():
    produkt1 = Produkt("P-0001", "Kaffee 500 g", 8.90, "Lebensmittel")
    produkt2 = Produkt("P-0002", "Wasser", 10.00, "Getränke")

    assert produkt1.mwst_satz == 0.07
    assert produkt1.bruttopreis == 9.52

    assert produkt2.mwst_satz == 0.19
    assert produkt2.bruttopreis == 11.90


""" Die bruttopreis-Property berechnet den Bruttopreis eines Produkts. """
"""produkte1,2 sind Instanzen der Klasse Produkt, die jeweils unterschiedliche Kategorien und Preise haben """


""" 05. Vergleichmethoden testen """


def test_produkte_vergleichsmethoden():
    produkt1 = Produkt("P-0001", "Kaffee 500 g", 8.90, "Lebensmittel")
    produkt2 = Produkt("P-0002", "Wasser", 29.90, "Getränke")
    produkt3 = Produkt("P-0003", "Laptop", 999.00, "Elektronik")

    gleiches_produkt = Produkt("P-0001", "Another Kaffee", 1.00, "Lebensmittel")

    assert produkt1 == gleiches_produkt

    sortierte_produkte = sorted([produkt3, produkt1, produkt2])

    assert [p.artikelnummer for p in sortierte_produkte] == [
        "P-0001",
        "P-0002",
        "P-0003",
    ]


""" Die Vergleichsmethoden (__eq__ und __lt__) ermöglichen es, Produkte basierend auf ihrem Nettopreis zu vergleichen. """
""" p.artikelnummer for p in sortierte_produkte überprüft, ob die Artikelnummern der sortierten Produkte in der erwarteten Reihenfolge vorliegen. """


def test_produkte_unglueltige_werte():

    # Artikelnummer ohne P-
    with pytest.raises(ValueError):
        Produkt("Q-0001", "Kaffee 500 g", 8.90, "Lebensmittel")

    # Leere Bezeichnung
    with pytest.raises(ValueError):
        Produkt("P-0001", "", 8.90, "Lebensmittel")

    # Ungültige Kategorie
    with pytest.raises(ValueError):
        Produkt("P-0001", "Kaffee 500 g", 8.90, "Sportartikel")

    # Preis gleich 0
    with pytest.raises(ValueError):
        Produkt("P-0001", "Kaffee 500 g", 0, "Lebensmittel")


""" With pytest.raises(ValueError) wird überprüft, ob beim Erstellen eines Produkts mit ungültigen Werten eine ValueError-Ausnahme ausgelöst wird. """
