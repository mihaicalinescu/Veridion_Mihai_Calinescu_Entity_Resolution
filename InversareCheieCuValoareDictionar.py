def inversare_dictionar(dictionar):
    dictionar_nou = {}
    for cheie, valoare in dictionar.items():
        if valoare in dictionar_nou:
            dictionar_nou[valoare].append(cheie)
        else:
            dictionar_nou[valoare] = [cheie]

    return dictionar_nou

dictionar = {'a': 1, 'b': 2, 'c':1, 'd': 3, 'e': 2}
print (inversare_dictionar(dictionar))