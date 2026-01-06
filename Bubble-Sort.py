import numpy as np

random_array = np.random.randint(0, 100, size=10)

print(random_array)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("Schritt: " , arr)
    return arr

bubble_sort(random_array)
print("Ergebnis:", random_array)