def chei_cu_valori_pare(dictionar):
    return [cheie for cheie, valoare in dictionar.items() if valoare % 2 == 0]

dictionar = {'a':1, 'b': 2, 'c': 3, 'd': 4}
print(chei_cu_valori_pare(dictionar))