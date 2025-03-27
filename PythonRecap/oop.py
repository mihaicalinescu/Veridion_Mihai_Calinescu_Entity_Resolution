class Masina:
    def __init__(self, marca, model, an_fabricatie):
        self.marca = marca
        self.model = model
        self.an_fabricatie = an_fabricatie

    def descriere(self):
        return (f"Masina este un {self.marca} {self.model}, fabricata in {self.an_fabricatie}.")

    def vechime(self):
        an_curent = 2025
        return an_curent - self.an_fabricatie

# masina_mea = Masina('Vokswagen', 'Arteon', 2022)
# print (masina_mea.descriere())
# print (masina_mea.vechime())

class Vehicul:
    def __init__(self, marca, model, viteza_maxima):
        self.marca = marca
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descriere(self):
        return f"{self.marca} {self.model} - Viteza maxima: {self.viteza_maxima} km/h"

class Masina(Vehicul):
    def __init__(self, marca, model, viteza_maxima, numar_usi):
        super().__init__(marca, model, viteza_maxima)
        self.numar_usi = numar_usi

    def descriere(self):
        return f"{super().descriere()}, Numar usi: {self.numar_usi}"

class Motocicleta(Vehicul):
    def __init__(self, marca, model, viteza_maxima, tip_motocileta):
        super().__init__(marca, model, viteza_maxima)
        self.tip_motocicleta = tip_motocileta

    def descriere(self):
        return f"{super().descriere()}, Tip motocicleta : {self.tip_motocicleta}"


masina1 = Masina("BMW", "Seria 3", 240, 4)
motocicleta1 = Motocicleta("Yamaha", "R1", 300, 'sport')
print(masina1.descriere())
print(motocicleta1.descriere())