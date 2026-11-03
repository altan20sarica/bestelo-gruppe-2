from bestelo.produkte import Produkt

# Einzelnes Produkt aus einer CSV-Zeile erstellen
zeile = "P-1001;Kaffeebohnen 500 g;8.90;Lebensmittel"
kaffee = Produkt.aus_csv_zeile(zeile)

# Produkt direkt erstellen
wasser = Produkt("P-1002", "Mineralwasser 12 × 1 l", 7.50, "Getränke")

# __str__ und __repr__ testen
print(kaffee)
print(repr(kaffee))


# Mehrwertsteuer und Bruttopreis testen
print(kaffee.mwst_satz, kaffee.bruttopreis)

# Vergleichsmethoden testen
print(wasser < kaffee, kaffee == Produkt("P-1001", "Anderer Name", 1.00))
# Die 1.00 ist hier der Nettopreis eines zweiten, nur zum Test erstellten Produkts.
# Es könnte auch anderes sein solange aber der Preis positiv ist

# Ganze CSV-Datei einlesen
produkte = Produkt.aus_csv_datei("bestelo/daten/produkte.csv")

# Anzahl und günstigstes Produkt ausgeben
print(len(produkte), "Produkte, das günstigste: ", min(produkte))
