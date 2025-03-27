d = {'key1':['a','b','c']}
mylist = d['key1']
# print (mylist)

def keys_with_large_values(d):
    return [key for key, value in d.items() if value > 10]

def chei_valori_mari(dictionar):
    return [cheie for cheie, valoare in dictionar.items() if valoare > 10]

dictionar_test = {'a': 5, 'b': 12, 'c': 8, 'd': 15}
print(chei_valori_mari(dictionar_test))

d = {"a": 5, "b":15, "c":20}
# print(keys_with_large_values(d))
