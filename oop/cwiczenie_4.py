class Product:
    ID = 1

    def __init__(self, cena, nazwa, ID):
        self.cena = cena
        self.nazwa = nazwa
        self.ID = ID

    def print_info(self):
        print(f"Produkt '{self.nazwa}'\nID: {self.ID}\nCena: {self.cena} PLN")

    def dej_cene(self):
        return self.cena


class BasketEntry:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.cena * self.quantity

    def __str__(self):
        return f"{self.product.nazwa} | {self.product.cena} | {self.quantity}"

    def generate_report(self):
        return f"- {self.product.nazwa} ({self.product.id}), cena: {self.product.cena} x {self.quantity}\n"

class Basket:

    def __init__(self):
        self.entries = []

    def add_product(self, product, qty):
        self.entries.append(BasketEntry(product, qty))

    def count_total_price(self):
        total_price = 0
        for entry in self.entries:
            total_price += entry.count_price()
        return total_price

    def generate_report(self):
        pass