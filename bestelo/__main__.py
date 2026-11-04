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
<<<<<<< HEAD
        zeilen_preis = pos.menge * pos.produkt.nettopreis
        netto += zeilen_preis
        print(
            f"{pos.produkt.bezeichnung:<35} {pos.menge} x {pos.produkt.nettopreis:.2f} € = {zeilen_preis:.2f} €"
        )

    print("-" * 55)
    print(f"{'Netto:':<16}{netto:>9.2f} €")

    """Rabatt berechnen (Prozentwert aus dem Kundenobjekt)"""
    rabatt = netto * bestellung.kunde.rabattsatz()
    print(
        f"{'Rabatt ' + str(bestellung.kunde.rabattsatz() * 100) + '%:':<16}{rabatt:>9.2f} €"
    )

    """ MwSt. (19%)"""
    mwst = (netto - rabatt) * 0.19
    print(f"{'MwSt.:':<16}{mwst:>9.2f} €")

    """Brutto"""
    brutto = (netto - rabatt) + mwst
    print(f"{'Brutto:':<16}{brutto:>9.2f} €\n")
=======
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
>>>>>>> 8f6a87de0996bc93caa254a518b8052342d8c146


def main() -> None:
    """1. Produkte laden und nach Preis sortiert ausgeben"""
    produkte = Produkt.aus_csv_datei(CSV_PFAD)
    print("Sortiment (nach Preis):")
    for p in sorted(produkte, key=lambda x: x.nettopreis):
        print(f"  {p.bezeichnung} - {p.nettopreis:.2f} € netto")
    print()

    """2. Kunden anlegen"""
    kunde1 = Privatkunde(1001, "Anna Müller", "anna@beispiel.de", 1995, stammkunde=True)
    kunde2 = Geschaeftskunde(
        1002, "Schmidt IT GmbH", "kontakt@schmidt.de", "DE123456789"
    )
    kunde3 = Verein(
        "SV Mustersstadt", "kontakt@verein.de", "VR 12345", gemeinnuetzig=True
    )

    """3. Erste Bestellung (Kunde 2)"""
    bestellung1 = Bestellung("B-0001", kunde2, abgeschlossen=True)

    """Produkte für die Bestellung heraussuchen"""
    kaffee = next(p for p in produkte if "Kaffee" in p.bezeichung)
    wasser = next(p for p in produkte if "Mineralwasser" in p.bezeichung)

    bestellung1.position_hinzufuegen(3, kaffee)
    bestellung1.position_hinzufuegen(6, wasser)

    beleg_drucken(bestellung1)

    """ 4. Zweite offene Bestellung (Kunde 3)"""
    bestellung2 = Bestellung(kunde3)
    saft = next(p for p in produkte if "Orangensaft" in p.bezeichnung)
    bestellung2.position_hinzufuegen(24, saft)

    """Kurze Zusammenfassung für Bestellung 2 ausgeben"""
    anzahl = len(bestellung2.positionen)
    print(
        f"Bestellung B-0002 (offen) für SV Mustersstadt: {anzahl} Position(en), 75.97 € brutto"
    )


if __name__ == "__main__":
    main()
