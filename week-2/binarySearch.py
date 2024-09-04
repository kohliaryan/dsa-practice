numbers = [7, 8, 9,10, 11]
target = 10


def binarySearch(L, v):
    low = 0
    high = len(L) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if L[mid] == v:
            return True
        elif L[mid] < v:
            low = mid + 1
        else:
            high = mid - 1
    return False

print(binarySearch(numbers, target))