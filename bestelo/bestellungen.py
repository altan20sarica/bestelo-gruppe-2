"""Bestellpositionen und Bestellungen.

Klassen Bestellposition und Bestellung → Person 4 (Abschnitt 5.4)
"""
class Bestellposition:
    def __init_ (self , produkt, menge = 1):
        self.produkt = produkt
        self.menge = menge
        self.preise_berechnen()

    def preise_berechnen (self):
        self.netto = round(self.product.nettopreis * self.menge, 2)
        self.mwst  = round(self.netto * self.produkt.mwst_satz, 2)
        self.brutto = round(self.netto + self.mwst, 2 ) 
print(f"Der netto preis liegt bei {self.netto}€")
print(f"Die Mwst liegt bei {self.mwst}€")
print(f"Der Bruttopreis liegt bei {self.brutto}€")      