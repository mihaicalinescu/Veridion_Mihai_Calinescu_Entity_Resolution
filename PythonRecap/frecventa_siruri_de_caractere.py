def frecventa_caractere(sir_de_caractere):
    frecventa = {}
    for caracter in sir_de_caractere:
        if caracter in frecventa:
            frecventa[caracter] += 1
        else:
            frecventa[caracter] = 1
    return frecventa

def frecventa_caractere_dictionary_comprehension (sir_de_caractere):
    return {caracter: sir_de_caractere.count(caracter) for caracter in set(sir_de_caractere)}

sir_de_caractere = 'hello world'
print(frecventa_caractere(sir_de_caractere))
print(frecventa_caractere_dictionary_comprehension(sir_de_caractere))