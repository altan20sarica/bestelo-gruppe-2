"""Bestellpositionen und Bestellungen.

Klassen Bestellposition und Bestellung → Person 4 (Abschnitt 5.4)
"""
class Bestellposition:
    def __init_ (self , produkt, menge = 1): 
        if menge < 1 :
            raise ValueError("Menge muss mindestens 1 sein!")        
        self.produkt = produkt
        self.menge = menge
        

        self.netto = round(self.produkt.nettopreis * self.menge, 2) # nette etc berechnen
        self.mwst  = round(self.netto * self.produkt.mwst_satz, 2)
        self.brutto = round(self.netto + self.mwst, 2 ) 

    def __str__ (self):
        return f"{self.menge} * {self.product.name} a {self.brutto} * {self.brutto*self.menge} € " #gibt als text an

class Bestellung
    def __init__ (self , kunde):
        self.kunde = kunde
        self.positionen = []

    def hinzufügen (self, produkt, menge = 1): #fügt erzeugtes objekt an ender der leeren liste dazu
       self.positionen.append(Bestellposition(produkt, menge))

    def abschließen (self, status): #zeigt den status an ob es noch offen oder abgeschlossen ist
        self.status = status 
        
    def __len__(self): #mit len kann die länge der bestellungen angezeigt werden
        return len(self.positionen)

    def __str__(self):
        bruttosumme = sum(pos.brutto for pos in self.positionen) #Brutto entpreis berechnen
        mwstsumme = sum(pos.mwst for pos in self.positionen)
        nettosumme = sum(pos.netto for pos in self.positionen)

        

        return f"{self.kunde} * {len(self.positionen)} Positionen  * {bruttosumme} € * {mwstsumme} € * {nettosumme}€." #die bestellung vom kunden ausgeben
    
    
    

        