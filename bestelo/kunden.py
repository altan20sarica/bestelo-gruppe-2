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

        if kundennummer< 1000: 
            raise ValueError("Kundennummer muss mind. 1000 sein")

    @property
    def kundennummer(self) -> int:
        return self._kundennummer

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, wert: str) -> None:
        wert = wert.strip()
        if not wert:
            raise ValueError("Name darf nicht leer sein")
        self._name= wert

    @property
    def email(self, wert: str) -> None:
        if not self.ist_gueltige_email(wert):
            raise ValueError("Ungültige EMail Adresse")   
        self._email = wert

    @staticmethod
    def ist_gueltige_email(email: str) -> bool:
        return email.count("@") == 1 and "." in email.split("@")[1]
    

    def begruessung(self) -> str:
        return f"Hallo {self.name}!"

    def rabattsatz(self) -> float:
        return 0.0

    def __str__(self) -> str:
        return f"Kunde {self.kundennummer}: {self.name}"

    def __repr__(self) -> str:
        return f"{type(self).__name__} ({self.kundennummer}, {self.name!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Kunde):
            return NotImplemented
        return self.kundennummer == other.kundennummer