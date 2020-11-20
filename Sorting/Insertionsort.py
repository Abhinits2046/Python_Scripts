l = list(map(int,input("Enter Elements for insertion Sort: ").split()))
print(l)
def InsertionSort(l):
    for sliceEnd in range(len(l)):
        pos = sliceEnd

        while pos > 0 and l[pos] < l[pos-1]:
            (l[pos],l[pos-1]) = (l[pos-1],l[pos])
            pos = pos-1



InsertionSort(l)
print("Sorted list", l)