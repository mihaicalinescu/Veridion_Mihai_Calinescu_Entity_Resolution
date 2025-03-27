def sorteaza_valori_dictionar(dictionar):
    return {cheie: sorted(valoare) for cheie, valoare in dictionar.items()}

dictionar = {
    'a': [3, 1, 2],
    'b': [9, 7, 8],
    'c': [6, 5, 4]
}

print (sorteaza_valori_dictionar(dictionar))