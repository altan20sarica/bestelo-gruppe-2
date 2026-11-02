"""Bestellpositionen und Bestellungen.

Klassen Bestellposition und Bestellung → Person 4 (Abschnitt 5.4)
"""
class Bestellposition:
    def __init__ (self , produkt, menge = 1):        
        self._produkt = produkt
        self.menge = menge 
    
    @property
    def produkt(self):
        return self._produkt
    
    @property
    def menge(self):
        return self._menge
    
    @menge.setter
    def menge(self, value):
        if value < 1:
            raise ValueError("Menge muss mindestens 1 sein") 
        self._menge = value

    @property
    def netto(self):
        return round(self.produkt.nettopreis * self.menge, 2) 
       
    @property         
    def mwst(self):
        return round(self.netto * self.produkt.mwst_satz, 2)
    
    @property
    def brutto(self):
        return round(self.netto + self.mwst, 2)
    
    def __str__ (self):
        einzelpreis = self.produkt.brutto
        return (f"{self.menge} × {self.produkt.name} à "
                f"{einzelpreis:.2f} € = {self.brutto:.2f} €")

class Bestellung:
    _naechste_nummer = 1
    def __init__ (self , kunde):
        self._kunde = kunde
        self._positionen = []
        self._status = "offen"
        self._bestellnummer = f"B-{Bestellung._naechste_nummer:04d}"
        Bestellung._naechste_nummer +=1

    @property
    def bestellnummer(self):
        return self._bestellnummer

    @property
    def kunde(self):
        return self._kunde

    @property
    def status(self):
        return self._status

    @property
    def positionen(self):
        return list(self._positionen)  # Kopie        

    def hinzufuegen (self, produkt, menge = 1): #fügt erzeugtes objekt an ender der leeren liste dazu
       if self._status != "offen":
           raise ValueError("Bestellung ist nicht mehr offen")
    
       for pos in self._positionen:
           if pos.produkt == produkt:
               pos.menge += menge
               return 

       self._positionen.append(Bestellposition(produkt, menge))

    def abschliessen (self): #zeigt den status an ob es noch offen oder abgeschlossen ist
        if len(self.positionen) == 0:
            raise ValueError("Bestellung hat keine position")
        self._status ="abgeschlossen"   
             
    def __len__(self): #mit len kann die länge der bestellungen angezeigt werden
        return len(self._positionen)
    
    @property
    def netto_summe(self):
        return round(sum(pos.netto for pos in self._positionen) , 2)
    
    @property
    def rabatt_betrag(self):
        return round(self.netto_summe * self.kunde.rabattsatz(), 2)
    
    @property
    def netto_nach_rabatt(self):
        return round(self.netto_summe - self.rabatt_betrag , 2)
    
    @property
    def mwst_betrag(self):
        # Summe der MwSt aller Positionen multipliziert mit (1 - Rabattsatz)
        mwst_roh = sum(pos.mwst for pos in self.positionen)
        return round(mwst_roh * (1 - self.kunde.rabattsatz()), 2)
    
    @property
    def brutto_summe(self):
        return round(self.netto_nach_rabatt + self.mwst_betrag, 2)       

    def __str__(self):
        return (f"Bestellung {self.bestellnummer} ({self.status}) für "
                f"{self.kunde}: {len(self)} Position(en), "
                f"{self.brutto_summe:.2f} € brutto")
    
    

        