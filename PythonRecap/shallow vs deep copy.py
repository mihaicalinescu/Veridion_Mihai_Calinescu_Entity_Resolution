import copy

# lista_originala = [[1, 2], [3, 4]]
# lista_copie = lista_originala
# lista_copie[0][0] = 99
#
# print(lista_originala)
# print(lista_copie)
#
# dict_original = {'a': [1, 2], 'b': [3, 4]}
# dict_copie = dict_original.copy()
# dict_copie['a'][0] = 99
#
# print(dict_original)
# print(dict_copie)
#
# lista_originala = [[1, 2], [3, 4]]
# deep_copy = copy.deepcopy(lista_originala)
# deep_copy[0][0] = 99
#
# print(lista_originala)
# print(lista_copie)

lista_originala = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(lista_originala)
deep_copy = copy.deepcopy(lista_originala)

shallow_copy[0][0] = 99
deep_copy[1][1] = 88

print("Lista originală:   ", lista_originala)
print("Shallow copy:      ", shallow_copy)
print("Deep copy:         ", deep_copy)