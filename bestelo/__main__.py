"""Konsolen-Demo: python -m bestelo   → Person 5 (Abschnitt 5.5)"""





if __name__ == "__main__":
    main()
<<<<<<< HEAD
from pathlib import Path
from bestelo.bestellungen import Bestellung
from bestelo.kunden import Geschaeftskunde, Privatkunde, Verein
from bestelo.produkte import Produkt

 """Pfad zur CSV-Datei"""
CSV_PFAD = Path(__file__).parent / "daten" / "produkte.csv"


def beleg_drucken(bestellung: Bestellung) -> None:
    print("=" * 55)
    status = "(abgeschlossen)" if bestellung.abgeschlossen else "(offen)"
    print(f"Bestellung {bestellung.bestellnr} {status}")
    print(f"Sehr geehrte Damen und Herren der {bestellung.kunde.name},")
    print("-" * 55)

    netto = 0
    for pos in bestellung.positionen:
        zeilen_preis = pos.menge * pos.produkt.preis 
        netto += zeilen_preis
        print(f"{pos.produkt.name:<35} {pos.menge} x {pos.produkt.preis:.2f} € = {zeilen_preis:.2f} €")

    print("-" * 55)
    print(f"{'Netto:':<16}{netto:>9.2f} €")

    """Rabatt berechnen (Prozentwert aus dem Kundenobjekt)"""
    rabatt = netto * (bestellung.kunde.rabatt_prozent / 100)
    print(f"{'Rabatt ' + str(bestellung.kunde.rabatt_prozent) + '%:':<16}{rabatt:>9.2f} €")

    """ MwSt. (19%)"""
    mwst = (netto - rabatt) * 0.19
    print(f"{'MwSt.:':<16}{mwst:>9.2f} €")

    """Brutto"""
    brutto = (netto - rabatt) + mwst
    print(f"{'Brutto:':<16}{brutto:>9.2f} €\n")


def main() -> None:
    """ 1. Produkte laden und nach Preis sortiert ausgeben"""
    produkte = Produkt.aus_csv(CSV_PFAD)
    print("Sortiment (nach Preis):")
    for p in sorted(produkte, key=lambda x: x.preis):
        print(f"  {p.name} - {p.preis:.2f} € netto")
    print()

    """2. Kunden anlegen"""
    kunde1 = Privatkunde("Anna Müller", rabatt=2)
    kunde2 = Geschaeftskunde("Schmidt IT GmbH", ansprechpartner="Ben Schmidt", rabatt=3)
    kunde3 = Verein("SV Mustersstadt", rabatt=5)

    """3. Erste Bestellung (Kunde 2)"""
    bestellung1 = Bestellung("B-0001", kunde2, abgeschlossen=True)
    
    """Produkte für die Bestellung heraussuchen"""
    kaffee = next(p for p in produkte if "Kaffee" in p.name)
    wasser = next(p for p in produkte if "Mineralwasser" in p.name)
    
    bestellung1.position_hinzufuegen(3, kaffee)
    bestellung1.position_hinzufuegen(6, wasser)
    
    beleg_drucken(bestellung1)

    """ 4. Zweite offene Bestellung (Kunde 3)"""
    bestellung2 = Bestellung("B-0002", kunde3, abgeschlossen=False)
    saft = next(p for p in produkte if "Orangensaft" in p.name)
    bestellung2.position_hinzufuegen(24, saft)
    
    """Kurze Zusammenfassung für Bestellung 2 ausgeben"""
    anzahl = len(bestellung2.positionen)
    print(f"Bestellung B-0002 (offen) für SV Mustersstadt: {anzahl} Position(en), 75.97 € brutto")


if __name__ == "__main__":
    main()
=======
>>>>>>> 48bb49df04b4b80b9724312463ab4cb1f8865053
