"""Bestellpositionen und Bestellungen.

Klassen Bestellposition und Bestellung → Person 4 (Abschnitt 5.4)
"""
class Bestellposition:
    def __init_ (self , produkt, menge = 1):
        self.produkt = produkt
        self.menge = menge
        

        self.netto = round(self.product.nettopreis * self.menge, 2)
        self.mwst  = round(self.netto * self.produkt.mwst_satz, 2)
        self.brutto = round(self.netto + self.mwst, 2 ) 

    def __str__ (self):
        return f"{self.menge} * {self.product.name} - Brutto: {self.brutto} € "