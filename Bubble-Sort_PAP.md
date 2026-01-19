## Bubble-Sort
Bubble-Sort ist ein sehr einfacher Sortieralgorithmus. Er ordnet eine Liste, indem er benachbarte Elemente immer wieder vergleicht und vertauscht, wenn sie in der falschen Reihenfolge stehen.
Der Name kommt daher, dass große Werte wie Luftblasen nach oben „aufsteigen“.

### Grundidee
1. Gehe die Liste von links nach rechts durch.
2. Vergleiche jeweils zwei Nachbarn.
3. Sind sie falsch sortiert → tausche sie.
4. Wiederhole das Ganze mehrmals, bis keine Vertauschung mehr nötig ist. Und dies passiert in zwei Schleifen.

### PAP des Bubble-Sorts
```mermaid
graph TD
    A([Start]) --> B[Array erstellen & n = Länge]
    B --> C[/Ausgabe: Unsortiertes Array/]
    C --> D{i < n ?<br/>Äußere Schleife}
    
    D -- Ja --> E{j < n-i-1 ?<br/>Innere Schleife}
    D -- Nein --> K[/Ausgabe: Ergebnis/]
    
    E -- Ja --> F{arr_j > arr_j+1 ?<br/>Vergleich}
    E -- Nein --> J[i erhöhen]
    
    F -- Ja --> G[Tauschen: arr_j <-> arr_j+1]
    G --> H[/Ausgabe: Schritt/]
    H --> I[j erhöhen]
    
    F -- Nein --> I
    
    I --> E
    J --> D
    
    K --> L([Ende])
```