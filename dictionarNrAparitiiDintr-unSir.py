from collections import Counter
def numara_aparitii(text):
    frecventa = {}
    for caracter in text:
        if caracter in frecventa:
            frecventa[caracter] += 1
        else:
            frecventa[caracter] = 1
    return frecventa

def numara_aparitii2(text):
    return dict(Counter(text))

text = "python rocks"
print (numara_aparitii(text))
