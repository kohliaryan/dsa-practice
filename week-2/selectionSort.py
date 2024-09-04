def selectionSort(L):
    length = len(L)
    if length < 2:
        return L
    for i in range(length):
        minpos = i
        for j in range(i+1, length):
            if L[j] < L[minpos]:
                minpos = j
        (L[minpos], L[i]) = (L[i], L[minpos])
    return L