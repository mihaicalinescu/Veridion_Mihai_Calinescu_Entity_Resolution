def separate_pare_impare(numere):
    pare, impare = [], []
    for x in numere:
        if x % 2 == 0:
            pare.append(x)
        else:
            impare.append(x)
    return pare, impare

def separate_pare_impare_comprehension(numere):
    pare = [x for x in numere if x % 2 == 0]
    impare = [x for x in numere if x % 2 == 1]
    return pare, impare
    
numere = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print (separate_pare_impare_comprehension(numere))