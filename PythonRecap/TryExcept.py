class Calculator:
    @staticmethod
    def imparte(numar1, numar2):
        try:
            rezultat = numar1 / numar2
            return rezultat
        except ZeroDivisionError:
            return "Eroare: Impartirea la 0 nu este permisa"
        except TypeError:
            return "Eroare: Trebuie sa introduceti doar numere!"

print(Calculator.imparte(10, 2))
print(Calculator.imparte(10, 0))
print(Calculator.imparte('10', 0))
