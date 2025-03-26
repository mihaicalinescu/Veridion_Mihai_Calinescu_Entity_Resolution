def lista_palindrom(lista):
    return lista == lista[::-1]

print (lista_palindrom([1, 2, 3, 2, 1]))
print (lista_palindrom([1, 2, 3, 4, 5]))