def decorator_exemplu(func):
    def wrapper():
        print("Se executa cea inaintea functiei")
        func()
        print("Se executa ceva dupa functie")
    return wrapper()

@decorator_exemplu
def salut():
    print("Salut!")

salut()