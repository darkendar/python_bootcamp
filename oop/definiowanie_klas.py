
# class Animal:
#     krolestwo = "Fauna"
#
#     def _init_(self, nazwa):
#         self.nazwa = nazwa
#
# a1 = Animal("Żyrafa") #instancja klasy
# a2 = Animal("Mysz") #instancja klasy
#
# print(a1.nazwa)
# print(a2.nazwa)

# print(type(zyrafa))
#
#
# print(zyrafa.krolestwo)
# print(mysz.krolestwo)
#
# #atrybut klasowy moge zmodyfikowac
#
# Animal.krolestwo = "Flora"
#
# print(zyrafa.krolestwo)
# print(mysz.krolestwo)
#
# zyrafa.krolestwo = "Fauna"
#
# print(zyrafa.krolestwo)
class Osoba():

    def __init__(self, imie, nazwisko):
        print("No siema")
        self.imie = imie
        self.nazwisko = nazwisko


    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}")

    @staticmethod
    def metoda_statyczna():
        print("Metoda statyczna")

obiekt = Osoba("Adam", "Małysz")
obiekt2 = Osoba("Adam", "Mickiewicz")

obiekt.przedstaw_sie()
obiekt2.przedstaw_sie()
Osoba.metoda_statyczna()