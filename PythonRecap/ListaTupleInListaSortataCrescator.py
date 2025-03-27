def lista_tuple_in_lista_sortata_crescator(lista_tuple):
    return sorted(lista_tuple, key=lambda x: x[1])


persoane = [('Andrei', 25), ('Maria', 22), ('Ion', 30), ('Elena', 27)]
print (lista_tuple_in_lista_sortata_crescator(persoane))
