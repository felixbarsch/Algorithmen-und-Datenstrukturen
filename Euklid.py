x = int(input("Geben Sie die Ganze Zahl für x ein: "))
y = int(input("Geben Sie die Ganze Zahl für y ein: "))

while x != y:
    if x > y:
        x = x-y
    else:
        y = y-x
print("ggT: " , x)