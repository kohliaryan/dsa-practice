def insertionSort(L):
    length = len(L)
    if length < 2:
        return L
    for i in range(length):
        j = i
        while j > 0 and L[j-1] > L[j]:
            (L[j-1], L[j]) = (L[j], L[j-1])
            j -=1
    return L
