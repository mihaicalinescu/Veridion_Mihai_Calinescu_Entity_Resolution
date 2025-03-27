def cheia_cea_mai_mare_val_tuplu(dictionar):
    return max(dictionar.items(), key=lambda x: x[1])

def cheia_cea_mai_mare_val(dictionar):
    return max(dictionar, key=dictionar.get)

dictionar = {'a': 10, 'b': 25, 'c':7, 'd': 30}
print(cheia_cea_mai_mare_val(dictionar))