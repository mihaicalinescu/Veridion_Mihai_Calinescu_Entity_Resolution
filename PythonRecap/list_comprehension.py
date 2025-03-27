def patrate():
    numere = [1, 2, 3, 4, 5]
    patrate = [x ** 2 for x in numere]
    print(patrate)


def nr_pare():
    numere = [10, 15, 20, 25, 30, 35, 40]
    pare = [x for x in numere if x % 2 == 0]
    print(pare)


def len_cuvant():
    cuvinte = ['QA', 'Automation', "Python", 'Testare']
    lungimi = [len(cuvant) for cuvant in cuvinte]
    print (lungimi)

def impare_la_patrat():
    numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    impare_patrate = [x ** 2 for x in numere if x % 2 != 0]
    print(impare_patrate)

def dictionar_numere_la_patrat():
    numere = [1, 2, 3, 4, 5]
    patrate_dict = {x : x ** 2 for x in numere}
    print(patrate_dict)

def dictionar_numere_la_patrat2():
    numere = [1, 2, 3, 4, 5]
    patrate_dict = {}
    for x in numere:
        patrate_dict[x] = x ** 2
    print(patrate_dict)


def dictionar_filtrare():
    varste = {'Ana': 25, 'Bogdan': 17, 'Cristina': 30, 'David': 16}
    majore = {}
    for nume, varsta in varste.items():
        if varsta > 17:
            majore[nume] = varsta
    print(majore)

def dictionar_filtrare2():
    varste = {'Ana': 25, 'Bogdan': 17, 'Cristina': 30, 'David': 16}
    majore = {nume: varsta for nume, varsta in varste.items() if varsta > 17}
    print (majore)


def lista_tuple_dintr_o_lista():
    perechi = [(x, y) for x in [1, 2, 3] for y in ['a', 'b', 'c']]
    print(perechi)

def lista_tuple_dintr_o_lista2():
    perechi = []
    for x in [1, 2, 3]:
        for y in ['a', 'b', 'c']:
            perechi.append((x, y))

def elimina_duplicate_lista():
    numere = [1, 2, 2, 3, 4, 4, 5]
    fara_duplicate = list({x for x in numere})
    print(fara_duplicate)
# patrate()
# nr_pare()
# len_cuvant()
# impare_la_patrat()
# dictionar_numere_la_patrat2()
# dictionar_filtrare2()
# lista_tuple_dintr_o_lista()
elimina_duplicate_lista()