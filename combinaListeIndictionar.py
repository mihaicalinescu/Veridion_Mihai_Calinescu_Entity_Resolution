def combina_liste_in_dictionar(lista_chei, lista_valori):
    return dict(zip(lista_chei, lista_valori))

lista_chei = ['a', 'b', 'c']
lista_valori = [1, 2, 3]
print(combina_liste_in_dictionar(lista_chei, lista_valori))