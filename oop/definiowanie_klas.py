

class Animal:
    krolestwo = "Fauna"

    def _init_(self, nazwa):
        self.nazwa = nazwa

a1 = Animal("Żyrafa") #instancja klasy
a2 = Animal("Mysz") #instancja klasy

print(a1.nazwa)
print(a2.nazwa)

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