## Heap-Sort
Heap-Sort ist ein vergleichsbasiertes Sortierverfahren, das auf einer speziellen Datenstruktur basiert: dem Heap (genauer: Max-Heap). Ein Max-Heap ist ein binärer Baum, bei dem der größte Wert immer an der Wurzel steht und jedes Eltern-Element größer oder gleich seinen Kindern ist.

### Grundidee
Heap-Sort ist ein Sortieralgorithmus, der einen Heap (meist einen Max-Heap) nutzt:
1. Heap aufbauen: Das Array wird so umgeordnet, dass das größte Element immer oben (an Position 0) steht und wie ein Baum aussieht.
2. Sortieren: Das größte Element wird mit dem letzten Element getauscht und ganz ans Ende gebracht und „entfernt“. Also in ein anderes Sortiertes Array gegeben.
3. Heap wiederherstellen: Der Heap wird neu angepasst (heapify).
4. Das wiederholt sich, bis alle Elemente sortiert sind.

### PAP des Heap-Sorts
```mermaid
graph TD
    A([Start]) --> B[Array initialisieren & sort_arr leer]
    B --> C{Solange arr nicht leer?}
    
    %% Innere Schleife: Heap bauen
    C -- Ja --> D[Schleife i von n//2 bis 0<br/>Heapify-Prozess]
    D --> E[Aufruf: kindtauschen_i]
    
    %% Die Hilfsfunktion kindtauschen
    subgraph "Funktion: kindtauschen(n)"
    E --> F{Kinder vorhanden?}
    F -- Nein --> G[Ende Rekursion]
    F -- Ja --> H{Kind-Wert > Eltern-Wert?}
    H -- Ja --> I[Größeres Kind mit Eltern tauschen]
    I --> J[[Rekursiver Aufruf: kindtauschen für neues Kind]]
    H -- Nein --> G
    end

    %% Nach dem Heap-Bau
    J -.-> K
    E --> K[Tausche arr_0 mit letztem Element arr_minus_1]
    K --> L[Letztes Element entfernen und in sort_arr speichern]
    L --> M[/Print Zwischenschritte/]
    M --> C
    
    %% Ende
    C -- Nein --> N[/Ausgabe: sort_arr/]
    N --> O([Ende])
```