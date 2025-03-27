def dictionar_la_patrat(dictionar):
    return {cheie: valoare ** 2 for cheie, valoare in dictionar.items()}

dictionar = {'a': 2, 'b': 3, 'c': 4}
print(dictionar_la_patrat(dictionar))