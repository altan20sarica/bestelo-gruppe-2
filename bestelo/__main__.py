"""Konsolen-Demo: python -m bestelo   → Person 5 (Abschnitt 5.5)"""


from pathlib import Path
from bestelo.bestellungen import Bestellung
from bestelo.kunden import Geschaeftskunde, Privatkunde, Verein
from bestelo.produkte import Produkt

"""Pfad zur CSV-Datei"""
CSV_PFAD = Path(__file__).parent / "daten" / "produkte.csv"


def beleg_drucken(bestellung: Bestellung) -> None:
    print("=" * 55)
    print(f"Bestellung {bestellung.bestellnummer} ({bestellung.status})")
    print(bestellung.kunde.begruessung())
    print("-" * 55)


    for pos in bestellung.positionen:
        print(f"{pos.produkt.bezeichnung:<30} "
              f"{pos.menge} x {pos.produkt.nettopreis:.2f} € "
              f"{pos.netto:.2f} € netto")
        
    print("-" * 55)
    print(f"{'Netto:':<16}{bestellung.netto_summe:>9.2f} €")
    print(f"{'Rabatt:':<16}{bestellung.rabatt_betrag:>9.2f} €")
    print(f"{'Netto nach Rabatt:':<16}{bestellung.netto_nach_rabatt:>9.2f} €")
    print(f"{'MwSt.:':<16}{bestellung.mwst_betrag:>9.2f} €")
    print(f"{'Brutto:':<16}{bestellung.brutto_summe:>9.2f} €")
    print("=" * 55)


def main() -> None:
    """ 1. Produkte laden und nach Preis sortiert ausgeben"""
    produkte = Produkt.aus_csv_datei(CSV_PFAD)
    print("Sortiment (nach Preis):")
    for p in sorted(produkte, key=lambda x: x.nettopreis):
        print(f"  {p.bezeichnung} - {p.nettopreis:.2f} € netto")
    print()

    """2. Kunden anlegen"""
    kunde1 = Privatkunde(1001, "Anna Müller", "anna@beispiel.de", 1995, stammkunde=True)
    kunde2 = Geschaeftskunde(1002, "Ben Schmidt", "ben@schmidt-it.de", "Schmidt IT GmbH", "DE123456789")
    kunde3 = Verein(1003, "SV Mustersstadt", "info@sv-musterstadt.de", "VR 12345", gemeinnuetzig=True)

    """3. Erste Bestellung (Kunde 2)"""
    bestellung1 = Bestellung(kunde2)
    
    """Produkte für die Bestellung heraussuchen"""
    kaffee = next(p for p in produkte if "Kaffee" in p.bezeichnung)
    wasser = next(p for p in produkte if "Mineralwasser" in p.bezeichnung)
    
    bestellung1.hinzufuegen(kaffee, 3)
    bestellung1.hinzufuegen(wasser, 6)

    bestellung1.abschliessen()
    beleg_drucken(bestellung1)

    """ 4. Zweite offene Bestellung (Kunde 3)"""
    bestellung2 = Bestellung(kunde3)
    saft = next(p for p in produkte if "Orangensaft" in p.bezeichnung)
    bestellung2.hinzufuegen(saft, 24)

    print(bestellung2)
    
    """Kurze Zusammenfassung für Bestellung 2 ausgeben"""
    anzahl = len(bestellung2.positionen)
    print(f"Bestellung B-0002 (offen) für SV Mustersstadt: {anzahl} Position(en), 75.97 € brutto")


if __name__ == "__main__":
    main()
