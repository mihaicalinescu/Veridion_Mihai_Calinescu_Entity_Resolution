def aduna_valori_chei_comune(lista_dict):
    dictionar_nou = {}
    for dictionar in lista_dict:
        for cheie, valoare in dictionar.items():
            if cheie in dictionar_nou:
                dictionar_nou[cheie] += valoare
            else:
                dictionar_nou[cheie] = valoare
    return dictionar_nou

def aduna_valori_chei_comune_comprehension(lista_dict):
    return {cheie: sum(d.get(cheie, 0) for d in lista_dict) for dictionar in lista_dict for cheie, valoare in dictionar.items()}

lista_dict = [{'a': 1, 'b': 2}, {'a': 2, 'b': 3, 'c': 4}, {'a': 3, 'b': 4, 'c': 5}]
print(aduna_valori_chei_comune(lista_dict))
print(aduna_valori_chei_comune_comprehension(lista_dict))