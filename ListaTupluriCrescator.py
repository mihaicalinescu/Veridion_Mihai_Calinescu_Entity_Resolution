def lista_tupluri_crescatoare(lista):
    return sorted(lista, key=lambda x: x[1])


persoane = [('Andrei', 25), ('Maria', 30), ('Ion', 22)]
print(lista_tupluri_crescatoare(persoane))