def suma_numerelor_pare(lista):
    return sum(x for x in lista if x % 2 == 0)

print (suma_numerelor_pare([1, 2, 3, 4, 5, 6]))
print (suma_numerelor_pare([10, 15, 20, 25]))