def lista_de_liste_fara_duplicate(lista):
    elemente_unice = set()
    for x in lista:
        elemente_unice.update(x)
    return list(elemente_unice)

def lista_de_liste_fara_duplicate_list_comprehension(lista):
    return list(set(element for x in lista for element in lista))

lista_de_liste = [[1, 2, 3], [2, 3, 4], [4, 5, 6], [6, 7, 8]]
print(lista_de_liste_fara_duplicate(lista_de_liste))
print(lista_de_liste_fara_duplicate_list_comprehension(lista_de_liste))