import pytest
from bestelo.kunden import Kunde, Privatkunde


def test_beispiel_kunde():
    """Testet das vorgegebene Beispiel der Klasse Kunde."""
    anna = Kunde(1001, "  Anna Müller  ", "anna@example.com")

    assert str(anna) == "Kunde 1001: Anna Müller"
    assert repr(anna) == "Kunde(1001, 'Anna Müller')"
    assert anna.begruessung() == "Hallo Anna Müller!"
    assert anna.rabattsatz() == 0.0
    assert anna == Kunde(1001, "A. Müller", "a.mueller@example.com")
    assert Kunde.ist_gueltige_email("anna-at-example.com") is False

    with pytest.raises(ValueError, match="Name darf nicht leer sein"):
        anna.name = "  "


def test_beispiel_privatkunde():
    """Testet das vorgegebene Beispiel für Privatkunde."""
    anna = Privatkunde(
        1001, "Anna Müller", "anna@example.com", 1995,
        stammkunde=True
    )

    assert str(anna) == "Kunde 1001: Anna Müller"
    assert repr(anna) == "Privatkunde(1001, 'Anna Müller')"
    assert anna.alter(2026) == 31
    assert anna.rabattsatz() == 0.02
    assert isinstance(anna, Kunde) is True


def test_leerer_name():
    """Prüft, ob ein leerer Name abgelehnt wird."""
    anna = Kunde(1001, "Anna", "anna@example.com")

    with pytest.raises(ValueError):
        anna.name = "  "


def test_ungueltige_email():
    """Prüft, ob eine ungültige E-Mail abgelehnt wird."""
    with pytest.raises(ValueError):
        Kunde(1001, "Anna", "ungueltige-email")


def test_kundennummer_nur_lesbar():
    """Prüft, ob die Kundennummer unveränderbar ist."""
    anna = Kunde(1001, "Anna", "anna@example.com")

    with pytest.raises(AttributeError):
        anna.kundennummer = 5


def test_ungueltiges_geburtsjahr():
    """Prüft, ob ein ungültiges Geburtsjahr abgelehnt wird."""
    with pytest.raises(ValueError):
        Privatkunde(1001, "Anna", "anna@example.com", 1800)


def test_rabatt_ohne_stammkunde():
    """Prüft den Rabatt ohne Stammkundenstatus."""
    anna = Privatkunde(1001, "Anna", "anna@example.com", 1995)

    assert anna.stammkunde is False
    assert anna.rabattsatz() == 0.0