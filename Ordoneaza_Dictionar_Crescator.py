def ordoneaza_dictionar_crescator(dictionar):
    return sorted(dictionar.items(), key=lambda x: x[1])

dictionar_test = {'a': 3, 'b':1, 'c':2}
print(ordoneaza_dictionar_crescator(dictionar_test))