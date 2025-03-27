def suma_pare(lista):
    suma = 0
    for numar in lista:
        if numar % 2 == 0:
            suma += numar
    return suma

lista_test = [1, 2, 3, 4, 5, 6]
print(suma_pare(lista_test))