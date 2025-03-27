def suma_fiecarei_subliste(lista_de_liste):
    return [sum(subliste) for subliste in lista_de_liste]

lista_de_liste = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print (suma_fiecarei_subliste(lista_de_liste))