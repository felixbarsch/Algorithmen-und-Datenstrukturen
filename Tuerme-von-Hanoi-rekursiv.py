ScheibenAnzahl = int(input("Geben Sie eine Anzahl von Scheiben an: "))
StangenStackKupfer = []
StangenStackSilber = []
StangenStackGold = []
zaehler = 0


class Scheibe:
    groesse = 0

for i in range(0, ScheibenAnzahl, 1):
    scheibe = Scheibe()
    scheibe.groesse = ScheibenAnzahl - i
    StangenStackKupfer.append(scheibe)

def bewegeScheibe(vonStange, zuStange):
    if len(zuStange) == 0 or zuStange[-1].groesse > vonStange[-1].groesse:
        zuStange.append(vonStange.pop())
        return True
    else:
        print("Ungültiger Zug")
        return False


def hanoi_rekursiv(n, von_stange, zu_stange, hilfs_stange):
    global zaehler
    zaehler+=1
    
    if n == 1:
        bewegeScheibe(von_stange, zu_stange)
        return

    hanoi_rekursiv(n - 1, von_stange, hilfs_stange, zu_stange)
    bewegeScheibe(von_stange, zu_stange)
    hanoi_rekursiv(n - 1, hilfs_stange, zu_stange, von_stange)


hanoi_rekursiv(ScheibenAnzahl, StangenStackKupfer, StangenStackGold, StangenStackSilber)
print("Das Programm konnte die Türme von Hanoi in", zaehler,"Zügen lösen.")