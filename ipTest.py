import re
from os.path import split


class ValidareIP:
    def __init__(self, ip):
        self.ip = ip

    # A 0 ->127

    # B 128 -> 191

    # C 192 -> 223

    # D 224 -> 225

    # "10.1.1.7", "198.1.1.1"

    def validare(self):
        # pattern = r"^[0-9]{1,3},[.][0-9]{1,3},[.][0-9]{1,3}"
        # if re.match(pattern) == :
        #     return ip
        lista = list(self.ip)
        lista_noua = self.ip.split('.')
        validare = True
        # print(lista_noua)
        if len(lista_noua) == 4:
            for x in lista_noua:
                # print (x)
                if int(x) not in range(0, 256):
                    validare = False

            if int(lista_noua[0]) in range (0, 128):
                print ("Prima categorie: A")

            elif int(lista_noua[0]) in range (128, 192):
                print ("A doua categorie: B")

            elif int(lista_noua[0]) in range (129, 224):
                print ("A treia categorie: C")

            elif int(lista_noua[0]) in range (224, 225):
                print ("Ultima categorie: D")


        return validare


IP = ValidareIP('198.1.1.1')
print(IP.validare())
