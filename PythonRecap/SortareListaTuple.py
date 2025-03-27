def sortare_lista_tuple(lista):
    return sorted(lista, key=lambda x: x[1])

def sortare_lista_tuple_descrescator(lista):
    return sorted(lista, key=lambda x: x[1], reverse=True)

lista_tuple = [(1, 5), (2, 3), (3, 8), (4, 1)]
print (sortare_lista_tuple(lista_tuple))
print (sortare_lista_tuple_descrescator(lista_tuple))