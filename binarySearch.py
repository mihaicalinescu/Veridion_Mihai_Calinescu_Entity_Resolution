def binary_search(lista, target):
    stanga = 0
    dreapta = len(lista) - 1
    print (stanga, dreapta)
    while stanga <= dreapta:
        mijloc = (stanga + dreapta) // 2
        if lista[mijloc] == target:
            return mijloc
        elif lista[mijloc] < target:
            stanga = mijloc + 1
        else:
            dreapta = mijloc - 1
    return -1



numere = [1, 3, 5, 7, 8, 11, 13]
print (binary_search(numere, 7))
