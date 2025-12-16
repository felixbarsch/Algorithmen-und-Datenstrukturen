zahleingabe = int(input("Geben Sie die zu berechnende Fakultät ein: "))

def fakultaet(n):
    zaehler = 1
    for i in range(2, n + 1):
        zaehler *= i
    return zaehler

print("Die Fakultät von ", zahleingabe, " ist ", fakultaet(zahleingabe), ".")