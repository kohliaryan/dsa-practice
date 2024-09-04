def insertionSort(L):
    length = len(L)
    if length < 1:
        return L
    for i in range(length):
        j = i
        while (j > 0 and L[j] < L[j - 1]):
            (L[j], L[j-1]) = (L[j-1],L[j])
            j = j-1
    return L
