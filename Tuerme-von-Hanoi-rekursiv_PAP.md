# Türme von Hanoi, rekursiv

1. **Start**

2. **Eingabe**

   * Lies `ScheibenAnzahl` ein

3. **Initialisierung**

   * Erzeuge leere Listen: `Kupfer`, `Silber`, `Gold`
   * Setze `zaehler = 0`

4. **Scheiben erstellen und auf Kupfer stapeln**

   * Für `i = 0` bis `ScheibenAnzahl-1`:

     * Erzeuge `Scheibe`
     * Setze `groesse = ScheibenAnzahl - i`
     * Lege Scheibe auf Stack `Kupfer`

5. **Funktion `hanoi_rekursiv(n, von, zu, hilf)` aufrufen**

   * Aufruf: `hanoi_rekursiv(ScheibenAnzahl, Kupfer, Gold, Silber)`

6. **Ablauf in `hanoi_rekursiv`**

   * Erhöhe `zaehler` um 1
   * **Entscheidung:** `n == 1`?

     * **Ja:**

       * `bewegeScheibe(von, zu)`
       * **Return**
     * **Nein:**

       1. `hanoi_rekursiv(n-1, von, hilf, zu)`
       2. `bewegeScheibe(von, zu)`
       3. `hanoi_rekursiv(n-1, hilf, zu, von)`

7. **Ablauf in `bewegeScheibe(vonStange, zuStange)`**

   * **Entscheidung:** `zuStange leer` ODER `oberste Scheibe von zuStange größer als oberste von vonStange`?

     * **Ja:** Scheibe von `vonStange` nach `zuStange` bewegen → `True`
     * **Nein:** Ausgabe „Ungültiger Zug“ → `False`

8. **Ausgabe**

   * Gib aus: „… in `zaehler` Zügen lösen.“

9. **Ende**
