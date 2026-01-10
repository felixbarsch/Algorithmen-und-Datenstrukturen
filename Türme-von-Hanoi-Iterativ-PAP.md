1. Start

2. Eingabe
   Lies ScheibenAnzahl ein

3. Initialisierung
   Erzeuge leere Listen (Stacks): Kupfer, Silber, Gold
   Setze zaehler = 0

4. Scheiben erstellen und auf Kupfer stapeln
   Für i = 0 bis ScheibenAnzahl-1
     Erzeuge Scheibe
     Setze groesse = ScheibenAnzahl - i
     Lege Scheibe auf Stack Kupfer

5. Stabrollen abhängig von gerader/ungerader Scheibenanzahl festlegen
   Setze von = Kupfer, hilf = Silber, zu = Gold
   Entscheidung: ScheibenAnzahl % 2 == 0?
     Ja (gerade)
       Tausche hilf und zu
     Nein (ungerade)
       Keine Änderung

6. Gesamtzahl der notwendigen Züge bestimmen
   Setze maxZuege = 2^ScheibenAnzahl - 1

7. Hauptschleife (iterativer Lösungsablauf)
   Für zug = 1 bis maxZuege
     Entscheidung: zug % 3 == 1?
       Ja
         legalerZug(von, zu)
     Sonst Entscheidung: zug % 3 == 2?
       Ja
         legalerZug(von, hilf)
     Sonst (zug % 3 == 0)
         legalerZug(hilf, zu)
     Erhöhe zaehler um 1

8. Ablauf in legalerZug(stab1, stab2)
   Fall 1: stab1 ist leer
     Bewege oberste Scheibe von stab2 nach stab1
   Fall 2: stab2 ist leer
     Bewege oberste Scheibe von stab1 nach stab2
   Fall 3: beide Stäbe nicht leer
     Entscheidung: oberste Scheibe von stab1 < oberste Scheibe von stab2?
       Ja
         Bewege Scheibe von stab1 nach stab2
       Nein
         Bewege Scheibe von stab2 nach stab1

9. Ausgabe
   Gib aus: „Problem in zaehler Zügen gelöst.“

10. Ende
