#!/usr/bin/python3

# Quelle: https://www.geeksforgeeks.org/dsa/iterative-tower-of-hanoi/
# Wikipedia: https://en.wikipedia.org/wiki/Tower_of_Hanoi#Iterative_solution

# Algorithmus
# - Calculate the total number of moves required i.e., "pow(2, n) - 1"  with n is number of disks.
# - If number of disks (i.e., n) is even then interchange destination pole and auxiliary pole.
# - Loop for i = 1 to total number of moves 
#     if i%3 == 1: legal movement of top disk between source pole and destination pole
#     if i%3 == 2: legal movement of top disk between source pole and auxiliary pole    
#     if i%3 == 0: legal movement of top disk between auxiliary pole and destination pole 

rod = ['S', 'A', 'D']
stacks = [[], [], []]


def moveDisk(a, b):
    if not stacks[b] or (stacks[a] and stacks[a][-1] < stacks[b][-1]):
        print(f"Move disk {stacks[a][-1]} from rod {rod[a]} to rod {rod[b]}")
        stacks[b].append(stacks[a].pop())
    else:
        moveDisk(b, a)


def towerOfHanoi(n):
    print(f"Tower of Hanoi for {n} disks:")

    src, aux, dest = 0, 1, 2
    stacks[src] = list(range(n, 0, -1))

    totalMoves = (1 << n) - 1
    if n % 2 == 0:
        aux, dest = dest, aux

    for i in range(1, totalMoves + 1):
        if i % 3 == 0:
            moveDisk(aux, dest)
        elif i % 3 == 1:
            moveDisk(src, dest)
        else:
            moveDisk(src, aux)


if __name__ == "__main__":
    n = 5  # number of disks
    towerOfHanoi(n)


