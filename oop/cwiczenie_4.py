import sys
import numpy as np
print(sys.path)
from cwiczenie_1 import Product


# class Product():
#     ID = 1
#
#     def __init__(self, nazwa, cena):
#         self.id = Product.ID
#         self.nazwa = nazwa
#         self.cena = cena
#         Product.ID += 1
#
#     def print_info(self):
#         print(f"Produkt {self.nazwa}, id: {self.id}, cena: {self.cena} PLN")
#
#     def dej_cene(self):
#         return self.cena


class BasketEntry:
    def __init__(self, product, quantity):
        """
        :param product: instance of Product class
        :param quantity: quantity of product - int
        """

        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.cena * self.quantity

    def __str__(self):
        return f'{self.product.nazwa} x {self.quantity}'

    def generate_report(self):
        return f'- {self.product.nazwa} ({self.product.id}), cena: {self.product.cena} x {self.quantity}\n'


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
        out = "Produkty w koszyku:\n"
        for entry in self.entries:
            out += entry.generate_report()
        out += f"W sumie: {self.count_total_price()}"
        return out


pr1 = Product("Woda", 2)
pr2 = Product("Piwo", 3)
pr3 = Product("Salceson", 5)
basket = Basket()
basket.add_product(pr1, 4)
basket.add_product(pr2, 2)
basket.add_product(pr3, 1)
basket.add_product(pr1, 3)

print(basket.count_total_price())
print(basket.generate_report())
# assert basket.count_total_price() == 8