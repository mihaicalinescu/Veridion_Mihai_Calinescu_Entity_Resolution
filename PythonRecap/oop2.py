from abc import ABC, abstractmethod

class Vehicul(ABC):
    def __init__(self, marca, model, an_fabricatie):
        self.marca = marca
        self.model = model
        self.an_fabricatie = an_fabricatie

    @abstractmethod
    def autonomie(self):
        pass

    def descriere(self):
        return f"{self.marca} {self.model}, fabricat in {self.an_fabricatie}"

class MasinaElectrica(Vehicul):
    def __init__(self, marca, model, an_fabricatie, capacitate_baterie):
        super().__init__(marca, model, an_fabricatie)
        self.capacitate_baterie = capacitate_baterie # Capacitate in kwh

    def autonomie(self):
        return self.capacitate_baterie * 5

    def descriere(self):
        return f"{super().descriere()} - Masina electrica cu {self.capacitate_baterie} kwh baterie"

class MasinaClasica(Vehicul):
    def __init__(self, marca, model, an_fabricatie, capacitate_rezervor, consum_combustibil):
        super().__init__(marca, model, an_fabricatie)
        self.capacitate_rezervor = capacitate_rezervor
        self.consum_combustibil = consum_combustibil

    def autonomie(self):
        return (self.capacitate_rezervor / self.consum_combustibil) * 100

    def descriere(self):
        return f"{super().descriere()} - Masina pe combustibil cu rezervor de {self.capacitate_rezervor}L"

# testare polimorfism
masina_electrica = MasinaElectrica('Tesla', 'Model3', 2022, 75)
masina_clasica = MasinaClasica('Vw', 'Passat', 2020, 50, 5.2)

print(masina_electrica.descriere())
print(f"Autonomie estimata: {masina_electrica.autonomie()}km")

print(masina_electrica.descriere())
print(f"Autonomie estimata: {masina_clasica.autonomie()}km")