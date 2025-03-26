def dictionar_la_patrat(dictionar):
    return {cheie: valoare ** 2 for cheie, valoare in dictionar.items()}

def dictionar_la_patrat_clasic(dictionar):
    noul_dictionar = {}
    for cheie, valoare in dictionar.items():
        noul_dictionar[cheie] = valoare ** 2
    return noul_dictionar

dictionar = {'a': 2, 'b': 3, 'c': 4}
print (dictionar_la_patrat_clasic(dictionar))