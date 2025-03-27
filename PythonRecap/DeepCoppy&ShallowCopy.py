import copy

def testeaza_copiere(dictionar):
    shallow_copy = copy.copy(dictionar)

    deep_copy = copy.deepcopy(dictionar)

    dictionar['a'][0] = 100

    print("Dictionar original", dictionar)
    print("Shallow copy", shallow_copy)
    print("Deep copy", deep_copy)


dictionar = {
    'a': [1, 2, 3],
    'b': [4, 5],
}
testeaza_copiere(dictionar)