def al_nlea_cel_mai_mare(lista, n):
    lista_fara_duplicate = sorted(set(lista), reverse=True)
    if n <= len(lista_fara_duplicate):
        return lista_fara_duplicate[n-1]
    else:
        return None
    
lista_test = [10, 5, 8, 20, 15, 20, 8]
n = 2
print(al_nlea_cel_mai_mare(lista_test, n))
