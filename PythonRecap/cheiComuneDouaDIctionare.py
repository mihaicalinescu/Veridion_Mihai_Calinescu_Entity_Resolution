def combina_dcitionare(dict1, dict2):
    return {cheie: dict1[cheie] + dict2[cheie] for cheie in dict1 if cheie in dict2}


dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}
print (combina_dcitionare(dict1, dict2))