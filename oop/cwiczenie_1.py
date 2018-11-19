class Product():

    def __init__(self, cena, nazwa, ID):
        self.cena = cena
        self.nazwa = nazwa
        self.ID = ID

    def print_info(self):
        print(f"Produkt '{self.nazwa}'\nID: {self.ID}\nCena: {self.cena} PLN")


woda = Product(10.99, "Woda", 1)
chleb = Product(7.99, "Chleb", 2)
woda.print_info()
chleb.print_info()

# print(woda.cena)
