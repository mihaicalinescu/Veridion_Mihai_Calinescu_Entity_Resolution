def sorteaza_dupa_chei(dictionar):
    return dict(sorted(dictionar.items()))

def sorteaza_dupa_valori(dictionar):
    return dict(sorted(dictionar.items(), key=lambda item: item[1]))

def sorteaza_descrescator_dupa_valori(dictionar):
    return dict(sorted(dictionar.items(), key=lambda item: item[1], reverse=True))

dictionar_test = {'c': 3, 'a': 5, 'b': 1, 'e': 4, 'd': 2}
print(sorteaza_dupa_chei(dictionar_test))
print(sorteaza_dupa_valori(dictionar_test))
print(sorteaza_descrescator_dupa_valori(dictionar_test))