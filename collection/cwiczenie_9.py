# produkty = {
#     "ziemniaki": {"cena": 3, "ilosc": 47},
#     "cebula": {"cena": 2, "ilosc": 23},
#     "woda": {"cena": 1.5, "ilosc": 15},
#     "piwo": {"cena": 2.5, "ilosc": 10}
# }
#
# ziemniaki = produkty["ziemniaki"]
# cebula = produkty["cebula"]
# woda = produkty["woda"]
# piwo = produkty["piwo"]

produkty = {
    "ziemniaki": 3,
    "cebula": 2,
    "woda": 1.5,
    "piwo": 2.5
}

magazyn = {
    "ziemniaki": 10,
    "cebula": 10,
    "woda": 10,
    "piwo": 10
}
koszyk = {}



while True:

    komenda = input("""Wybierz opcje:
     [d] - dodaj do magazynu
     [k] - kup
     [z] - zakocz
    """)
    print("W naszym sklepie oferujemy: ")
    for produkt in produkty:
        print(f" - {produkt} - w cenie: {produkty[produkt]} PLN")

    print()

    if komenda == "k":
        wybor_produktu = input("Który produkt chcesz kupić? (wpisz koniec by zakonczyc)")
        if wybor_produktu == "zakoncz":
            break

        if wybor_produktu in produkty:
            ile = int(input(f"Ile chcesz kupic [{wybor_produktu}]"))
            # cena = float(ile) * produkty[wybor_produktu]
            if ile <= magazyn[wybor_produktu]:
                koszyk[wybor_produktu] = ile
                magazyn[wybor_produktu] -= ile
            else:
                print(f"Przykro mi. Nie mam tego produktu! Pozostało [{magazyn[wybor_produktu]}]")
        else:
            print("Sorry nie mam tego produktu")
    elif komenda == "d":
        co = input("Jaki produkt chcesz dodać?")
        ile = input(f"Ile {co} chcesz dodać?")
        magazyn[co] = magazyn.get(co, 0) + ile
        if co not in produkty:
            cena = float(input("Jaka cena za {co}"))
            produkty[co] = cena
    elif komenda == "z":
        break



print()
print()
print("Twój rachunek: ")
sumarycznie = 0
for produkt in koszyk:
    cena = koszyk[produkt] * produkty[produkt]
    print(f" - {produkt}: [{koszyk[produkt]}]: {cena} PLN")
    sumarycznie += cena

print("="*30)
print(f"Suma: {sumarycznie} PLN")
print("Dziękujemy! Zapraszamy ponownie!")


