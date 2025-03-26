def inversare_cheie_cu_valoare_dictionar(dictionar):
    return {valoare: cheie for cheie, valoare in dictionar.items()}

def inversare_cheie_cu_valoare_dictionar_in_lista(dictionar):
    dict_nou = {}
    for cheie, valoare in dictionar.items():
        if valoare not in dict_nou:
            dict_nou[valoare] = cheie
        else:
            dict_nou[valoare].append(cheie)
    return dict_nou

dictionar_test = {'a': 1, 'b': 2, 'c': 3}
print(inversare_cheie_cu_valoare_dictionar(dictionar_test))
print(inversare_cheie_cu_valoare_dictionar_in_lista(dictionar_test))
