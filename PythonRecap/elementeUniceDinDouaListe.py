def elemente_unice_din_doua_liste(lista1, lista2):
    print (list((set(lista1) ^ set(lista2))))


lista1 = [10, 20, 30]
lista2 = [20, 30, 40]
print(elemente_unice_din_doua_liste(lista1, lista2))