"""Kunden von Bestelo.

Oben:  Kunde (Basisklasse) und Privatkunde       → Person 1 (Abschnitt 5.1)
Unten: Geschaeftskunde und Verein                → Person 2 (Abschnitt 5.2)

Bitte vor dem Arbeiten immer `git pull` – Person 1 und 2 teilen sich diese Datei.
"""

### 5.1 PERSON 1 ###
from datetime import date


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



class Privatkunde(Kunde):
    """ erweitert Kunde um Geburtsjahr und Stammkundenrabatt"""
    
    def __init__(self, kundennummer: int, name: str, email: str, geburtsjahr: int, stammkunde: bool = False) -> None:
        """ erstellt Priv.Kunde mit Geburtsjahr und Stammkundenstatus"""
        super().__init__(kundennummer, name, email)
        self.geburtsjahr = geburtsjahr
        self.stammkunde = stammkunde

    @property
    def geburtsjahr(self) -> int:
        """ gibt Geb.Jahr des Priv.Kunden zurück"""
        return self._geburtsjahr

    @geburtsjahr.setter
    def geburtsjahr(self, wert: int) -> None:
        """setzt Geb.Jahr zwischen 1900 und dem aktuellen Jahr"""
        if type(wert) is not int or wert < 1900 or wert > date.today().year:
            raise ValueError("Geburtsjahr muss zwischen 1900 und dem aktuellen Jahr liegen")
        self._geburtsjahr = wert

    @property 
    def stammkunde(self) -> bool:
        """Gibt an ob Privatkunde ein Stammkunde ist"""
        return self._stammkunde

    @stammkunde.setter
    def stammkunde(self, wert: bool) -> None:
        """Setzt Stammkundenstatus auf True oder False"""
        if not isinstance(wert, bool):
            raise ValueError("Stammkunde muss entweder True oder False sein")
        self._stammkunde = wert
        
    def alter(self, stichjahr: int | None = None) -> int:
        """Berechnet Alter im Stichjahr oder im aktuekken Jahr"""
        if stichjahr is None: 
            stichjahr = date.today().year
        return stichjahr - self.geburtsjahr

    def rabattsatz(self) -> float:
        """Gibt für Stammkunden 2 Prozent Rabatt zurück, für keine Stammklunden 0 Prozent"""
        if self.stammkunde:
            return 0.02
        return 0.0