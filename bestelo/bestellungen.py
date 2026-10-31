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
        return f"{self.menge} * {self.product.name} a {self.produkt.brutto} = {self.brutto} € " #gibt als text an

class Bestellung:
    naechstenummer = 1
    def __init__ (self , kunde):
        self.kunde = kunde
        self.positionen = []
        self.status = "offen"
        self.bestellnummer = f"B-{Bestellung.naechstenummer:04d}"
        Bestellung.naechstenummer +=1

    def hinzufügen (self, produkt, menge = 1): #fügt erzeugtes objekt an ender der leeren liste dazu
       if self.status != "offen":
           raise ValueError("keine Bestellung vorhanden")
    
       for pos in self.positionen:
           if pos.produkt == produkt:
               pos.menge += menge
               return 

       self.positionen.append(Bestellposition(produkt, menge))

    def abschließen (self): #zeigt den status an ob es noch offen oder abgeschlossen ist
        if len(self.positionen) == 0:
            raise ValueError("Bestellung hat keine position")
        self.status ="abgeschlossen"   
             
    def __len__(self): #mit len kann die länge der bestellungen angezeigt werden
        return len(self.positionen)

    def netto_summe(self):
        return round(sum(pos.netto for pos in self.positionen) , 2)

    def rabatt_betrag(self):
        return round(self.netto_summe * self.kunde.rabattsatz(), 2)

    def netto_nach_rabatt(self):
        return round(self.netto_summe - self.rabatt_betrag , 2)

    def mwst_betrag(self):
        # Summe der MwSt aller Positionen multipliziert mit (1 - Rabattsatz)
        mwst_roh = sum(pos.mwst for pos in self.positionen)
        return round(mwst_roh * (1 - self.kunde.rabattsatz()), 2)

    def brutto_summe(self):
        return round(self.netto_nach_rabatt + self.mwst_betrag, 2)       

    def __str__(self):
        #bruttosumme = sum(pos.brutto for pos in self.positionen) #Brutto entpreis berechnen
        #mwstsumme = sum(pos.mwst for pos in self.positionen)
        #nettosumme = sum(pos.netto for pos in self.positionen)

        #return f"{self.kunde} * {len(self.positionen)} Positionen  * {bruttosumme} € * {mwstsumme} € * {nettosumme}€." #die bestellung vom kunden ausgeben
        return f"Bestellung {self.bestellnummer} ({self.status}) für {self.kunde}: {len(self.positionen)} Position(en), {self.brutto_summe} € brutto"    
    
    

        