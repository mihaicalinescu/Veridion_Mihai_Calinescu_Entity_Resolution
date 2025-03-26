def ordine_descrescatoare(lista):
    lungime = len(lista)
    for x in range(lungime - 1):
        for y in range(lungime - x - 1):
            if lista[y] < lista[y + 1]:
                z = lista[y]
                lista[y] = lista[y + 1]
                lista[y + 1] = z
    #           lista[y], lista[y + 1] = lista[y + 1], lista[y]
    return lista

lista = [10, 5, 8, 20, 15]
print (ordine_descrescatoare(lista))