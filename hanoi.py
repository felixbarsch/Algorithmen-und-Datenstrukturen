t1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
t2 = []
t3 = []
Versuche = 0

def move(n, tower1, tower2, tower3):
    global Versuche
    Versuche += 1

    if n > 0:
            move(n-1, tower1, tower3, tower2)
            if tower1:
                tower3.append(tower1[len(tower1)-1])
                tower1.pop
            move(n-1,tower2, tower1, tower3)
    return Versuche

      

print("Es wurden:",move(len(t1)-1,t1,t2,t3), "Versuche benötigt")