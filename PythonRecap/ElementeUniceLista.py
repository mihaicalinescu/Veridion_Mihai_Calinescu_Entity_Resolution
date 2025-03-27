def elemente_unice_lista(lista):
    set1 = set(lista)
    return len(set1) == len(lista)

print (elemente_unice_lista([1, 2, 3, 4, 5]))
print (elemente_unice_lista([1, 2, 3, 4, 5, 3]))
