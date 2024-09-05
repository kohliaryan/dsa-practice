def merge(A, B):
    (m, n) = (len(A), len(B))
    (C, i, j) = ([], 0, 0)

    while i < m and j < n:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    
    # Yeh loops if-else ke baahar hone chahiye
    while i < m:
        C.append(A[i])
        i += 1

    while j < n:
        C.append(B[j])
        j += 1
    
    return C

def mergesort(L):
    length = len(L)
    if length <= 1:
        return L
    Left_Half = mergesort(L[:length//2])
    Right_Half = mergesort(L[length//2:])
    Sorted_Merged_List = merge(Left_Half, Right_Half)
    return (Sorted_Merged_List)

L = [4, 2, 7, 6, 8, 3, 5, 1]
print(mergesort(L))
