

ScheibenAnzahl = int(input("Geben Sie eine Anzahl von Scheiben an: "))
StangenStackKupfer = []
StangenStackSilber = []
StangenStackGold = []
zaehler = 0

def turmausgabe():
    print("-" *20)
    print("Kupfer:")
    for element in reversed(StangenStackKupfer):
        print(element.groesse)
    print("Silber:")
    for element in reversed(StangenStackSilber):
        print(element.groesse)
    print("Gold:")
    for element in reversed(StangenStackGold):
        print(element.groesse)
    print("-" *20)

class Scheibe:
    groesse = 0

for i in range(0, ScheibenAnzahl, 1):
    scheibe = Scheibe()
    scheibe.groesse = ScheibenAnzahl - i
    StangenStackKupfer.append(scheibe)

def bewegeScheibe(vonStange, zuStange):
    if len(zuStange) == 0 or zuStange[-1].groesse > vonStange[-1].groesse:
        zuStange.append(vonStange.pop())
        print("Bewege Scheibe von", vonStange, "zu", zuStange)
        turmausgabe()
        return True
    else:
        print("Ungültiger Zug")
        return False


def hanoi_rekursiv(n, von_stange, zu_stange, hilfs_stange):
    # Basisfall: Wenn nur eine Scheibe zu bewegen ist
    global zaehler
    zaehler+=1
    
    if n == 1:
        bewegeScheibe(von_stange, zu_stange)
        return

    # 1. Bewege n-1 Scheiben vom Start- zum Hilfs-Stab
    hanoi_rekursiv(n - 1, von_stange, hilfs_stange, zu_stange)

    # 2. Bewege die unterste, größte Scheibe vom Start- zum Ziel-Stab
    bewegeScheibe(von_stange, zu_stange)

    # 3. Bewege die n-1 Scheiben vom Hilfs- zum Ziel-Stab
    hanoi_rekursiv(n - 1, hilfs_stange, zu_stange, von_stange)
    

hanoi_rekursiv(ScheibenAnzahl, StangenStackKupfer, StangenStackGold, StangenStackSilber)
print("Das Programm konnte die Türme von Hanoi in", zaehler,"Zügen lösen.")