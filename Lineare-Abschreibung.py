print("Berechnung einer linearen Abschreibung")
anschaffungskosten = int(input("Geben Sie die Anschaffungskosten in EUR ein: "))
restwert = int(input("Geben Sie den Restwert EUR ein: "))
nutzungsdauer = int(input("Geben Sie die Nutzungsdauer in Jahren für die Abschreibung an: "))

zaehler = anschaffungskosten - restwert
nenner = nutzungsdauer

abschreibung = zaehler / nenner

print("Die jährliche Abschreibung beträgt", abschreibung, "EUR.")