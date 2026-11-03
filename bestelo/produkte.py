"""Produkte von Bestelo.

Klasse Produkt inkl. CSV-Import → Person 3 (Abschnitt 5.3)
Die Produktdatei gehört nach bestelo/daten/produkte.csv.
"""

"""5.3 PERSON 3 """


class Produkt:

    KATEGORIEN = (
        "Lebensmittel",
        "Getränke",
        "Bücher",
        "Haushalt",
        "Elektronik",
        "Sonstiges",
    )

    ERMAESSIGTE_KATEGORIEN = ("Lebensmittel", "Bücher")
    MWST_ERMAESSIGT = 0.07
    MWST_REGULAER = 0.19

    """ 2. __init__-Methode, die die Attribute der Klasse initialisiert """

    def __init__(self, artikelnummer, bezeichnung, nettopreis, kategorie="Sonstiges"):
        """Hier ist die Prüfung in __init__ notwendig, da die Artikelnummer nur einmalig beim Erstellen des Objekts gesetzt werden kann."""
        """ Also kann es direkt zugewiesen werden, da kein Setter existiert."""
        if (
            not isinstance(artikelnummer, str)
            or not artikelnummer.startswith("P-")
            or len(artikelnummer) != 6
            or not artikelnummer[2:].isdigit()
        ):
            raise ValueError(
                "Artikelnummer muss mit 'P-' beginnen und danach nur Ziffern enthalten."
            )
        self.bezeichnung = bezeichnung
        self.nettopreis = nettopreis
        self.kategorie = kategorie
        self._artikelnummer = artikelnummer

    """ 3. Property-Methoden für die Attribute der Klasse, um die Validierung und Formatierung der Werte zu gewährleisten """

    @property
    def bezeichnung(self) -> str:
        return self._bezeichnung

    """ _bezeichnung ist ein privates Attribut, das nur innerhalb der Klasse verwendet werden sollte """

    @bezeichnung.setter
    def bezeichnung(self, wert) -> None:
        leerzeichen = wert.strip()  # Entfernt führende und nachgestellte Leerzeichen
        if leerzeichen == "":
            # Wenn die Bezeichnung nach dem Entfernen der Leerzeichen leer ist, wird eine ValueError ausgelöst
            raise ValueError("Bezeichnung darf nicht leer sein.")
        self._bezeichnung = leerzeichen

    @property
    def nettopreis(self) -> float:
        return self._nettopreis

    @nettopreis.setter
    def nettopreis(self, wert):

        if wert <= 0:
            raise ValueError("Nettopreis darf nicht null oder negativ sein.")
        self._nettopreis = round(wert, 2)

    @property
    def kategorie(self) -> str:
        return self._kategorie

    @kategorie.setter
    def kategorie(self, wert) -> None:
        if (
            wert not in self.KATEGORIEN
        ):  # hier wird überprüft, ob die Kategorie gültig ist
            raise ValueError(
                f"{wert} ist keine gültige Kategorie."
            )  # Wenn die Kategorie ungültig ist, wird eine ValueError ausgelöst
        self._kategorie = wert

    @property
    def artikelnummer(
        self,
    ) -> (
        int
    ):  # Getter-Methode für das Attribut artikelnummer das nur gelesen werden kann, da es keine Setter-Methode gibt
        return self._artikelnummer

    @property
    def mwst_satz(self) -> float:
        if self.kategorie in self.ERMAESSIGTE_KATEGORIEN:
            return self.MWST_ERMAESSIGT
        else:
            return self.MWST_REGULAER

    @property
    def bruttopreis(self) -> float:
        return round(self.nettopreis * (1 + self.mwst_satz), 2)

    def __str__(self) -> str:
        return (
            f"{self.artikelnummer} {self.bezeichnung} – {self.nettopreis:.2f} € netto"
        )

    def __repr__(self) -> str:
        return f"Produkt({self.artikelnummer!r}, {self.bezeichnung!r}, {self.nettopreis!r}, {self.kategorie!r})"

        # !r macht, dass die Werte in der Repräsentation in Anführungszeichen gesetzt werden, um anzuzeigen, dass es sich um Strings handelt.

    def __eq__(self, other) -> bool:
        if not isinstance(
            other, Produkt
        ):  # isinstance() ist eine Python-Funktion, mit der man überprüfen kann, ob eine Variable einen bestimmten Datentyp hat. (Bool: True/False)
            return NotImplemented

        return self.artikelnummer == other.artikelnummer

    def __lt__(
        self, other
    ):  # __lt__ bedeutet less than (kleiner als) nettopreis < other nettopreis
        if not isinstance(other, Produkt):
            return NotImplemented

        return self.nettopreis < other.nettopreis

    """ aus_csv_zeile(zeile) """

    @classmethod
    def aus_csv_zeile(cls, zeile):
        zeile = zeile.strip()

        artikelnummer, bezeichnung, preis, kategorie = zeile.split(";")
        return cls(artikelnummer, bezeichnung, float(preis), kategorie)

    """ cls(...) dagegen erstellt eine neue Instanz der Klasse """
    """ self ist die Referenz auf ein bereits vorhandenes Objekt """

    @classmethod
    def aus_csv(cls, pfad):
        return cls.aus_csv_datei(pfad)

    """ aus_csv_datei(pfad) """

    @classmethod
    def aus_csv_datei(cls, pfad):
        produkte = []

        with open(pfad, "r", encoding="utf-8") as datei:  # "r"

            zeilen = datei.readlines()
            """ readlines() → liest alle Zeilen in eine Liste """

            for zeile in zeilen[1:]:  # zeilen ab 0 1 bis Ende überspringt die Kopfzeile
                if zeile.strip():  # aktuelle Zeile überprüfen ob leer Zeile gibt
                    produkt = cls.aus_csv_zeile(zeile)
                    produkte.append(
                        produkt
                    )  # fügt das produkt der Liste hinzu produkte []

        return produkte
