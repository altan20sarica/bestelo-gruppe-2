"""Produkte von Bestelo.

Klasse Produkt inkl. CSV-Import → Person 3 (Abschnitt 5.3)
Die Produktdatei gehört nach bestelo/daten/produkte.csv.
"""


class Produkt:

    # 1. Konstanten für die Kategorien und Steuersätze
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

    # 2. __init__-Methode, die die Attribute der Klasse initialisiert
    def __init__(self, artikelnummer, bezeichnung, nettopreis, kategorie="Sonstiges"):
        # Hier ist die Prüfung in __init__ notwendig, da die Artikelnummer nur einmalig beim Erstellen des Objekts gesetzt werden kann.
        # Also kann es direkt zugewiesen werden, da kein Setter existiert.
        if (
            not artikelnummer.startswith(
                "P-"
            )  # überprüft, ob die Artikelnummer mit "P-" beginnt
            or len(artikelnummer)
            != 6  # überprüft, ob die Länge der Artikelnummer genau 6 Zeichen beträgt
            or not artikelnummer[
                2:
            ].isdigit()  # überprüft, ob die restlichen Zeichen der Artikelnummer (ab dem 3. Zeichen) nur aus Ziffern bestehen
        ):
            raise ValueError(
                "Artikelnummer muss mit 'P-' beginnen und danach nur Ziffern enthalten."
            )
        self.bezeichnung = bezeichnung
        self.nettopreis = nettopreis
        self.kategorie = kategorie
        self._artikelnummer = artikelnummer

    # 3. Property-Methoden für die Attribute der Klasse, um die Validierung und Formatierung der Werte zu gewährleisten
    @property
    def bezeichnung(self):
        return (
            self._bezeichnung
        )  # _bezeichnung ist ein privates Attribut, das nur innerhalb der Klasse verwendet werden sollte

    @bezeichnung.setter
    def bezeichnung(self, wert):
        leerzeichen = wert.strip()  # Entfernt führende und nachgestellte Leerzeichen
        if (
            leerzeichen == ""
        ):  # Wenn die Bezeichnung nach dem Entfernen der Leerzeichen leer ist, wird eine ValueError ausgelöst
            raise ValueError("Bezeichnung darf nicht leer sein.")
        self._bezeichnung = leerzeichen

    @property
    def nettopreis(self):
        return self._nettopreis

    @nettopreis.setter
    def nettopreis(self, wert):

        if wert <= 0:
            raise ValueError("Nettopreis darf nicht null oder negativ sein.")
        self._nettopreis = round(wert, 2)

    @property
    def kategorie(self):
        return self._kategorie

    @kategorie.setter
    def kategorie(self, wert):
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
    ):  # Getter-Methode für das Attribut artikelnummer das nur gelesen werden kann, da es keine Setter-Methode gibt
        return self._artikelnummer

    @property
    def mwst_satz(self):
        if (
            self.kategorie in self.ERMAESSIGTE_KATEGORIEN
        ):  # hier wird überprüft, ob die Kategorie des Produkts in der Liste der ermäßigten Kategorien enthalten ist
            return (
                self.MWST_ERMAESSIGT
            )  # Wenn ja, wird der ermäßigte Steuersatz zurückgegeben
        else:
            return (
                self.MWST_REGULAER
            )  # Wenn nein, wird der reguläre Steuersatz zurückgegeben

    @property
    def bruttopreis(self):
        return round(self.nettopreis * (1 + self.mwst_satz), 2)

    def __str__(self):
        return (
            f"{self.artikelnummer} {self.bezeichnung} – {self.nettopreis:.2f} € netto"
        )

    def __repr__(self):
        return f"Produkt({self.artikelnummer!r}, {self.bezeichnung!r}, {self.nettopreis!r}, {self.kategorie!r})"

    # !r macht, dass die Werte in der Repräsentation in Anführungszeichen gesetzt werden, um anzuzeigen, dass es sich um Strings handelt.

    # return f"{self.artikelnummer}: {self.bezeichnung} ({self.kategorie}) - Nettopreis: {self.nettopreis} €, Brutto: {self.bruttopreis} €"
    # hier wird die Artikelnummer, Bezeichnung, Kategorie, Nettopreis und Brutto-Preis des Produkts in einem lesbaren Format zurückgegeben.


# Beispiel die als Ausgabe zählen
# P = Produkt("P-1001", "Kaffeebohnen 500 g", 8.9, "Lebensmittel")
# print(str(P) == "P-1001 Kaffeebohnen 500 g – 8.90 € netto")
# print(repr(P) == "Produkt('P-1001', 'Kaffeebohnen 500 g', 8.9, 'Lebensmittel')")

# P2 = Produkt("P-1006", "USB-C-Ladekabel 2 m", 9.9, "Elektronik")
# print(P2)
