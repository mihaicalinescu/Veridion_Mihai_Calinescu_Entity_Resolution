def intesectie_liste(lista1, lista2):
    return list(set(lista1) & set(lista2))

print (intesectie_liste([1, 2, 3, 4], [3, 4, 5, 6]))
print (intesectie_liste([10, 20, 30], [40, 50, 60]))