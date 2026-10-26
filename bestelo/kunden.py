"""Kunden von Bestelo.

Oben:  Kunde (Basisklasse) und Privatkunde       → Person 1 (Abschnitt 5.1)
Unten: Geschaeftskunde und Verein                → Person 2 (Abschnitt 5.2)

Bitte vor dem Arbeiten immer `git pull` – Person 1 und 2 teilen sich diese Datei.
"""
#5.1

class Kunde:
    def __init__(self, kundennummer: int, name: str, email: str):
        self.kundennummer = kundennummer
        self.name = name
        self.email = email

    def begruessung(self):
        return f"Hallo {self.name}!"

    def rabattsatz(self):
        return 0.0