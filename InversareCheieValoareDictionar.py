def inversare_cheie_valoare(dictionar):
    return {valoare: cheie for cheie, valoare in dictionar.items()}


dictionar = {'a': 1, 'b': 2, 'c':3}
print(inversare_cheie_valoare(dictionar))