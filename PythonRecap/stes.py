# myset = set()
# myset.add(1)
# print (myset)
# myset.add(2)
# print (myset)
# myset.add(2)
# print (myset)

def common_elements(list1, list2):
    return set(list1) & set(list2)

def elemente_comune(set1, set2):
    return set1 & set2

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# print(common_elements(list1, list2))
print (elemente_comune(set1, set2))
