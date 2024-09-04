names = [1, 2, 3, 4, 5, 6, 70, 8, 9, 10];
target = 70

def naiveSearch(L, v):
    for i in L:
        if (i == v):
            return True
    return False 
print(naiveSearch(names, target))