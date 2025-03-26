def elementeComuneListeSeturi(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    return set1 & set2

def elementeInPrimaListaNuSiInADoua(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    return set1 - set2

lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [5, 6, 7, 8, 9, 10]
print(elementeComuneListeSeturi(lista1, lista2))
print(elementeInPrimaListaNuSiInADoua(lista1, lista2))