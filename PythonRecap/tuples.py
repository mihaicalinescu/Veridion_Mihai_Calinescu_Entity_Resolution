y = ('one', 2)
t = ('a', 'a', 'b')
# print (t.count('a'))

# tuple object does not support item assignment

def sum_tuple_elements(t):
    return sum(t)

def elemente_unice(tuplu):
    return tuple(set(tuplu))

tuplu_test = (1, 2, 2, 3, 4, 4, 5)
print(elemente_unice(tuplu_test))

t = (1, 2, 3, 4, 5)
