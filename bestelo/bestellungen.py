"""Bestellpositionen und Bestellungen.

Klassen Bestellposition und Bestellung → Person 4 (Abschnitt 5.4)
"""
class Bestellposition:
    def __init__ (self , produkt, menge = 1) -> None:
        """Erstellt eine Position mit Produkt und Menge"""        
        self._produkt = produkt
        self.menge = menge 
    
    @property
    def produkt(self):
        """gibt das produkt der Position zurück"""
        return self._produkt
    
    @property
    def menge(self) -> int:
        """gibt die bestellte Menge zurück"""
        return self._menge
    
    @menge.setter
    def menge(self, value) -> None:
        """setzt die Menge, wirft ValueError, wenn sie kleiner als 1 ist"""    
        if value < 1:
            raise ValueError("Menge muss mindestens 1 sein") 
        self._menge = value

    @property
    def netto(self) -> float:
        """Berechnet den Nettopreis der Position"""
        return round(self.produkt.nettopreis * self.menge, 2) 
       
    @property         
    def mwst(self) -> float:
        """"Berechnet den MehrwersteuerBetrag der Position"""
        return round(self.netto * self.produkt.mwst_satz, 2)
    
    @property
    def brutto(self) -> float:
        """Berechnet den Brutto preis der Position"""
        return round(self.netto + self.mwst, 2)
    
    def __str__ (self) -> str:
        """Gibt die Position als Text zurück"""
        einzelpreis = self.produkt.brutto
        return (f"{self.menge} × {self.produkt.name} à "
                f"{einzelpreis:.2f} € = {self.brutto:.2f} €")

class Bestellung:
    """eine Bestellung eines Kunden mit mehreren Positionen"""  
    _naechste_nummer = 1
    def __init__ (self , kunde) -> None:
        """Erstellt eine offene Bestellung für einen Kunden mit neuer Bestellnummer"""
        self._kunde = kunde
        self._positionen = []
        self._status = "offen"
        self._bestellnummer = f"B-{Bestellung._naechste_nummer:04d}"
        Bestellung._naechste_nummer +=1

    @property
    def bestellnummer(self) -> str:
        """gibt die Bestellnummer zurück"""
        return self._bestellnummer

    @property
    def kunde(self):
        """Gibt den Kunden der Bestellung zurück"""
        return self._kunde

    @property
    def status(self) -> str:
        """Gibt den Status zurück"""
        return self._status

    @property
    def positionen(self) -> list:
        """Gibt eine Kopie der Positionsliste zurück"""
        return list(self._positionen)  # Kopie        

    def hinzufuegen (self, produkt, menge = 1) -> None: 
       """Fügt ein Produkt hinzu oder erhöht die meng. Wirft Valueerror, wenn die Bestellung nicht mehr offen ist"""
       if self._status != "offen":
           raise ValueError("Bestellung ist nicht mehr offen")
    
       for pos in self._positionen:
           if pos.produkt == produkt:
               pos.menge += menge
               return 

       self._positionen.append(Bestellposition(produkt, menge))

    def abschliessen (self) -> None: 
        """Schließt die Bestellung ab. Wirft ValueError aus wenn keine Poitionen vorhanden sind"""
        if len(self.positionen) == 0:
            raise ValueError("Bestellung hat keine position")
        self._status ="abgeschlossen"   
             
    def __len__(self) -> int: 
        """Gibt die Anzahl an Positionen zurück"""
        return len(self._positionen)
    
    @property
    def netto_summe(self) -> float:
        """Summe der Nettopreise aller Positionen"""
        return round(sum(pos.netto for pos in self._positionen) , 2)
    
    @property
    def rabatt_betrag(self) -> float:
        """Rabatt in Euro"""
        return round(self.netto_summe * self.kunde.rabattsatz(), 2)
    
    @property
    def netto_nach_rabatt(self) -> float:
        """Netto summe abzüglich Rabatt"""
        return round(self.netto_summe - self.rabatt_betrag , 2)
    
    @property
    def mwst_betrag(self) -> float:
        """Mehrwersteuer aller Positionen, reduziert um den Rabattsatz"""
        # Summe der MwSt aller Positionen multipliziert mit (1 - Rabattsatz)
        mwst_roh = sum(pos.mwst for pos in self.positionen)
        return round(mwst_roh * (1 - self.kunde.rabattsatz()), 2)
    
    @property
    def brutto_summe(self) -> float:
        """Endbetrag der Bestellung"""
        return round(self.netto_nach_rabatt + self.mwst_betrag, 2)       

    def __str__(self) -> str:
        """Gibt die Bestellung als Text zurück"""
        return (f"Bestellung {self.bestellnummer} ({self.status}) für "
                f"{self.kunde}: {len(self)} Position(en), "
                f"{self.brutto_summe:.2f} € brutto")
    
    

        