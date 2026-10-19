"""Prüft nur, ob Ihr Projekt richtig eingerichtet ist.

Wenn dieser Test grün ist, funktionieren Python, pytest und die Ordnerstruktur.
Sie dürfen die Datei behalten – sie zählt aber nicht zu den 18 Pflicht-Tests.
"""


def test_paket_ist_importierbar() -> None:
    import bestelo
    assert bestelo is not None
