"""Kunden von Bestelo.

Oben:  Kunde (Basisklasse) und Privatkunde       → Person 1 (Abschnitt 5.1)
Unten: Geschaeftskunde und Verein                → Person 2 (Abschnitt 5.2)

Bitte vor dem Arbeiten immer `git pull` – Person 1 und 2 teilen sich diese Datei.
"""

### 5.1 PERSON 1 (Altan Sarica) ###
from datetime import date


class Kunde:
    """Speichert Grunddaten von Kunden"""

    def __init__(self, kundennummer: int, name: str, email: str) -> None:
        """Erstellt Kunde und prüft Angabe"""
        if type(kundennummer) is not int or kundennummer< 1000: 
            raise ValueError("Kundennummer muss eine ganze Zahl und mind. 1000 sein")

        self._kundennummer = kundennummer
        self.name = name
        self.email = email

    @property
    def kundennummer(self) -> int:
        """Gibt unveränderbare/nur lesbare Kundennummer zurück"""
        return self._kundennummer

    @property
    def name(self) -> str:
        """Gibt Namen des Kunden zurück"""
        return self._name

    @name.setter
    def name(self, wert: str) -> None:
        """Setzt Name der nicht leer sein darf"""
        if not isinstance(wert, str) or not wert.strip():
            raise ValueError("Name darf nicht leer sein")
        self._name= wert.strip()

    @property               
    def email(self) ->str:
        """Gibt email adresse zurück"""
        return self._email

    @email.setter
    def email(self, wert: str) -> None:
        """Prüft und setzt Email adresse"""
        if not self.ist_gueltige_email(wert):
            raise ValueError("Ungültige EMail Adresse")   
        self._email = wert

    @staticmethod
    def ist_gueltige_email(email: str) -> bool:
        """Prüft ob E-mail genau ein @ Zeichen und ein Punkt hat"""
        if not isinstance(email, str):
            return False
        return email.count("@") == 1 and "." in email.split("@")[1]
    

    def begruessung(self) -> str:
        """Begrüßt die Person mit eigenen Namen"""
        return f"Hallo {self.name}!"

    def rabattsatz(self) -> float:
        """Gibt Rabatsatz für normale Kunden zurück"""
        return 0.0

    def __str__(self) -> str:
        """Gibt lesbare Darstellung des Kunden zurück,
          mit Kundennummer und Name"""
        return f"Kunde {self.kundennummer}: {self.name}"

    def __repr__(self) -> str:
        """Gibt technische Darstellung des Kunden zurück,
                  mit Kundenklasse, Kundennummer und Name"""
        return f"{type(self).__name__}({self.kundennummer}, {self.name!r})"    #!r setzt Name bei Ausgabe in 'Anführungszeichen'     

    def __eq__(self, other: object) -> bool:
        """Vergleicht zwei Kunden anhand der Kundennummer, bzw das __eq__ definiert das Verhalten des Vergleichsoperators =="""
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
        """Berechnet Alter im Stichjahr oder im aktuellen Jahr"""
        if stichjahr is None: 
            stichjahr = date.today().year
        return stichjahr - self.geburtsjahr

    def rabattsatz(self) -> float:
        """Gibt für Stammkunden 2 Prozent Rabatt zurück,
          für keine Stammkunden 0 Prozent"""
        if self.stammkunde:
            return 0.02
        return 0.0


### 5.2 PERSON 2 ###

class Geschaeftskunde(Kunde):
    def __init__(self, kundennummer: int, name: str, email: str, firmenname: str, ust_id: str, zahlungsziehl_tage: int = 14) -> None:
        """Erstellt Geschäftskunde mit Firmenname, Umsatzsteuer-ID und Zahlungszieltagen"""
        super().__init__(kundennummer, name, email)
        self.firmenname = firmenname
        self.ust_id = ust_id
        self.zahlungsziehl_tage = zahlungsziehl_tage

    @property
    def firmenname(self) -> str:
        """Gibt den Firmennamen zurück"""
        return self.name

    @firmenname.setter
    def firmenname(self, wert: str) -> None:
        """Setzt den Firmennamen, der nicht leer sein darf"""
        if not isinstance(wert, str) or not wert.strip():
            raise ValueError("Firmenname darf nicht leer sein")
        self.name = wert.strip()
    
    @property
    def ust_id(self) -> str:
        """Gibt die Umsatzsteuer-ID zurück"""
        return self._ust_id

    @ust_id.setter
    def ust_id(self, wert: str) -> None:
        """Setzt die Umsatzsteuer-ID, der nicht leer sein darf"""
        if not isinstance(wert, str) or not wert.strip():
            raise ValueError("USt-ID darf nicht leer sein")
        self._ust_id = wert.strip()

    @property
    def zahlungsziehl_tage(self) -> int:
        """Gibt das Zahlungsziel in Tagen zurück"""
        return self._zahlungsziehl_tage

    @zahlungsziehl_tage.setter
    def zahlungsziehl_tage(self, wert: int) -> None:
        """Prüft und setzt Zahlungsziel"""
        if not self.ist_gueltiges_zahlungsziel(wert):
            raise ValueError("Zahlungsziel muss zwischen 0 und 60 Tagen liegen")
        self._zahlungsziehl_tage = wert

    @staticmethod
    def ist_gueltiges_zahlungsziel(zahlungsziel: int) -> bool:
        """Prüft ob das Zahlungsziel zwischen 0 und 60 Tagen liegt"""
        return 0 <= zahlungsziel <= 60

    def begruessung(self) -> str:
        """Begrüßt Geschäftskunden mit Firmenname"""
        return f"Sehr geehrte Damen und Herren der {self.name},"

    def rabattsatz(self) -> float:
        """Gibt für Geschäftskunden 3 Prozent Rabatt zurück,
          für keine Geschäftskunden 0 Prozent"""
        if self.stammkunde:
            return 0.03
        return 0.0
    
    def __str__(self) -> str:
        """Gibt lesbare Darstellung des Kunden zurück,
          mit Kundennummer und Name"""
        return f"Kunde {self.kundennummer}: {self.firmenname}\n (Ansprechpartner: {self.name})"

class Verein(Kunde):
    """Erweitert Kunde um Registernummer und gemeinnützigen Status"""
    
    def __init__(self, kundennummer: int, name: str, email: str, registernummer: str, gemeinnuetzig: bool = True) -> None:
        super().__init__(kundennummer, name, email)
        self.registernummer = registernummer
        self.gemeinnuetzig = gemeinnuetzig

    @property
    def registernummer(self) -> str:
        """Gibt die Registernummer zurück"""
        return self._registernummer

    @registernummer.setter
    def registernummer(self, wert: str) -> None:
        """Setzt die Registernummer, die nicht leer sein darf"""
        if not isinstance(wert, str) or not wert.strip():
            raise ValueError("Registernummer darf nicht leer sein")
        self._registernummer = wert.strip()

    @staticmethod
    def ist_gueltige_registernummer(registernummer: str) -> bool:
        """Prüft ob die Registernummer mit VR leerzeichen beginnt und danach nur Ziffern enthält"""
        return isinstance(registernummer, str) and registernummer.startswith("VR ") and registernummer[3:].isdigit()

    @property
    def gemeinnuetzig(self) -> bool:
        """Gibt den gemeinnützigen Status zurück"""
        return self._gemeinnuetzig

    @gemeinnuetzig.setter
    def gemeinnuetzig(self, wert: bool) -> None:
        """Setzt den gemeinnützigen Status auf True oder False"""
        if not isinstance(wert, bool):
            raise ValueError("Gemeinnütziger Status muss entweder True oder False sein")
        self._gemeinnuetzig = wert

    def rabattsatz(self) -> float:
        """Gibt für gemeinnützige Vereine 5 Prozent Rabatt zurück,
          für keine gemeinnützigen Vereine 0 Prozent"""
        if self.gemeinnuetzig:
            return 0.05
        return 0.0

    def begruessung(self) -> str:
        """Begrüßt den Vereinsvorstand mit Vereinsnamen"""
        return f"An den Vorstand des Vereins {self.name},"