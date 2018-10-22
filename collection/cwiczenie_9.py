# cennik = {"ziemniaki": 5, "pomidory": 7, "marchewki": 3}
# print(cennik)
# naleznosc = []
#
# while True:
#     towar = input("Podaj nazwe towaru: ")
#     waga = input("Podaj wage [kg]: ")
#
#     if towar == "k" or waga == "k":
#         break
#
#     for i in cennik:
#         if i == towar:
#             naleznosc = cennik.value(i) * waga
#
# cena = sum(naleznosc)


produkty = {
    "ziemniaki": 3,
    "cebula": 2,
    "woda": 1.5,
    "piwo": 2.5
}

print("W naszym sklepie oferujemy: ")

for produkt in produkty:
    print(f" - {produkt} - w cenie: {produkty[produkt]} PLN")

print()
wybor_produktu = input("Który produkt chcesz kupić?")
ile = input(f"Ile chcesz kupic [{wybor_produktu}]")

cena = float(ile) * produkty[wybor_produktu]
print(f"Zapłacisz: {cena}")