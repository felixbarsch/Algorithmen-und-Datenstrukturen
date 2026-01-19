## Quick-Sort
Quicksort ist ein sehr schneller Sortieralgorithmus, der nach dem Prinzip „Teile und herrsche“ (Divide and Conquer) arbeitet.

### Grundidee
1. Wähle ein Pivot-Element
2. Teile die Liste so auf, dass
    - links vom Pivot: kleinere oder gleiche Werte
    - rechts vom Pivot: größere Werte
3. Das Pivot ist danach an der richtigen Position
4. Wende dasselbe Verfahren rekursiv auf die linke und rechte Teilliste an

### PAP des Bubble-Sorts
```mermaid
graph TD
    A([Start]) --> B[Array initialisieren]
    B --> C{Bereich gültig?<br/>low < high}
    
    C -- Nein --> Z([Zweig fertig / Return])
    C -- Ja --> D[Wähle letztes Element als Pivot]
    
    D --> E{Alle Elemente im Bereich<br/>mit Pivot verglichen?}
    
    E -- Nein --> F{Aktuelles Element<br/> kleiner als Pivot?}
    F -- Ja --> G[Element nach links schieben]
    F -- Nein --> H[Nächstes Element prüfen]
    G --> H
    H --> E
    
    E -- Ja --> I[Pivot in die Mitte setzen]
    
    I --> J[[Sortiere linke Hälfte<br/>rekursiv]]
    I --> K[[Sortiere rechte Hälfte<br/>rekursiv]]
    
    J -.-> C
    K -.-> C
    
    Z --> L[/Ergebnis ausgeben/]
    L --> M([Ende])
```