import pytest
from bestelo.kunden import Kunde, Privatkunde
from bestelo.kunden import Kunde, Privatkunde

anna = Kunde(1001, "  Anna Müller  ", "anna@example.com")

print(anna)
print(repr(anna))
print(anna.begruessung(), anna.rabattsatz())
print(anna == Kunde(1001, "A. Müller", "a.mueller@example.com"))
print(Kunde.ist_gueltige_email("anna-at-example.com"))