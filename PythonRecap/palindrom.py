def este_palindrom(text):
    text = str(text).lower()
    return text == text[::-1]


def este_palindrom2(numar):
    copie_nr = numar
    palin = 0
    while copie_nr != 0:
        palin = palin * 10
        palin += copie_nr % 10
        copie_nr //= 10
    if numar == palin:
        return True
    return False
# print(este_palindrom('Ana'))
# print(este_palindrom('02320'))

print(este_palindrom2(12210))