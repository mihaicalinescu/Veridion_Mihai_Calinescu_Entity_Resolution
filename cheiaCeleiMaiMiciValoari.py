def cheia_celei_mai_mici_valori(dictionar):
    return min(dictionar, key=dictionar.get)

dictionar = {'a': 10, 'b': 25, 'c': 7, 'd': 30}
print (cheia_celei_mai_mici_valori(dictionar))