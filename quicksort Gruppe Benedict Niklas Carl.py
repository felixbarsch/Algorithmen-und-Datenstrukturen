import random

list=[]
for i in range (0,13):
    list.append(random.randint(1,100))
print("Unsortiert", list)


def quicksort(arr,start,ende):
    if start >= ende:
        return
    pivot =arr[start]
    i= start+1
    j= ende
    while i <= j:     
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            print(arr)
            #print("Werte tauschen",arr) 
    
    arr[start], arr[j] = arr[j], arr[start]
    #print("Pivot verschieben", arr)
    print(arr)
    quicksort(arr, start, j - 1)
    quicksort(arr, j + 1, ende)



quicksort(list,0,len(list)-1)

