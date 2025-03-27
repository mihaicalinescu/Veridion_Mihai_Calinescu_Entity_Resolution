def frecventa_caractere(text):
    frecventa = {}

    for caracter in text:
        if caracter in frecventa:
            frecventa[caracter] += 1
        else:
            frecventa[caracter] = 1
    return frecventa

print(frecventa_caractere('hello world'))