def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                # x = lista[j]
                # lista[j] = lista[j+1]
                # lista[j+1] = x
    return lista

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
