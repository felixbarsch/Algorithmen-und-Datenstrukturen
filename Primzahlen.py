x = int(input("Geben Sie einen Startwert ein: "))

def ist_primzahl(zahl):
    if zahl < 2:
        return False

    for i in range(2, zahl):
        if zahl % i == 0:
            return False
    return True

def primzahlen_bis(n):
    primzahlen = []

    for zahl in range(2, n):
        if ist_primzahl(zahl):
            primzahlen.append(zahl)

    return primzahlen

def summe_primzahlen(prim_arr):
    return sum(prim_arr)

print(primzahlen_bis(x), summe_primzahlen(primzahlen_bis(x)))