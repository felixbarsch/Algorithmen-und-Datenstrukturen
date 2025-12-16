zahleingabe = int(input("Geben Sie die zu berechnende Fakultät ein: "))

def fakultaet(n):
    if n == 1:
        return 1
    else:
        return n * fakultaet(n - 1)
    
print("Die Fakultät von ", zahleingabe, " ist ", fakultaet(zahleingabe), ".")