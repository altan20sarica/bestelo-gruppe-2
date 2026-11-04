import pytest
from bestelo import Bestellung, Bestellposition, Produkt, Kunde  # Import anpassen


@pytest.fixture
def kaffee():
    # Konstruktor anpassen: Bezeichnung, Nettopreis, MwSt-Satz
    return Produkt("Kaffeebohnen", 10.00, 0.07)


@pytest.fixture
def kunde():
    return Kunde("Test Kunde")  # ggf. anpassen


# 1. Bestellposition: Menge 0 -> ValueError
def test_position_menge_null_wirft_fehler(kaffee):
    with pytest.raises(ValueError):
        Bestellposition(kaffee, 0)


def test_position_werte(kaffee):
    pos = Bestellposition(kaffee, 3)
    assert pos.netto == round(kaffee.nettopreis * 3, 2)
    assert pos.mwst == round(pos.netto * kaffee.mwst_satz, 2)
    assert pos.brutto == round(pos.netto + pos.mwst, 2)
    assert "3" in str(pos) and kaffee.bezeichnung in str(pos)


# 2. Summen aus dem Rechenbeispiel
def test_summen_rechenbeispiel(kunde):
    best = Bestellung(kunde)
    # Produkte aus dem Rechenbeispiel der Aufgabe hinzufügen:
    # best.hinzufuegen(produkt_a, menge)
    # ...
    assert best.netto_summe == 71.7
    assert best.rabatt_betrag == 2.15
    assert best.netto_nach_rabatt == 69.55
    assert best.mwst_betrag == 10.11
    assert best.brutto_summe == 79.66


# 3. Gleiches Produkt zweimal -> eine Position
def test_gleiches_produkt_addiert_menge(kunde, kaffee):
    best = Bestellung(kunde)
    best.hinzufuegen(kaffee, 2)
    best.hinzufuegen(kaffee, 3)
    assert len(best) == 1
    assert best.positionen[0].menge == 5


# 4. Fortlaufende Bestellnummern (reihenfolgeunabhängig)
def test_bestellnummern_fortlaufend(kunde):
    erste = Bestellung(kunde)
    zweite = Bestellung(kunde)
    nr1 = int(erste.bestellnummer.split("-")[1])
    nr2 = int(zweite.bestellnummer.split("-")[1])
    assert nr2 == nr1 + 1


# 5. Abschließen
def test_leere_bestellung_abschliessen(kunde):
    with pytest.raises(ValueError):
        Bestellung(kunde).abschliessen()


def test_hinzufuegen_nach_abschliessen(kunde, kaffee):
    best = Bestellung(kunde)
    best.hinzufuegen(kaffee, 1)
    best.abschliessen()
    with pytest.raises(ValueError):
        best.hinzufuegen(kaffee, 1)


# 6. Kapselung
def test_positionen_ist_kopie(kunde, kaffee):
    best = Bestellung(kunde)
    best.hinzufuegen(kaffee, 1)
    best.positionen.clear()
    assert len(best) == 1