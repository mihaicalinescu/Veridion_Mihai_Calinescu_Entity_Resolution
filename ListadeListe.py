def flatten_lista(liste):
    return [element for sublista in liste for element in sublista]

def flatten_lista_clasic(liste):
    lista_finala = []
    for sublista in liste:
        for element in sublista:
            lista_finala.append(element)
    return lista_finala
liste = [[1, 2, 3], [4, 5], [6, 7, 8]]

print (flatten_lista_clasic(liste))
print (flatten_lista(liste))