import json

try:
    with open ('pracownicy.json', 'r') as plik:
        pracownicy = json.load(plik)
except FileNotFoundError:
    pracownicy = []


akcja = input("Co chcesz zrobic? [d - dodaj, w - wypisz]: ")
if akcja == "d":
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    rok_ur = int(input("Rok urodzenia: "))
    pensja = float(input("Pensja: "))
    pracownicy.append({"imie": imie, "nazwisko": nazwisko,
                    "rok urodzenia": rok_ur, "pensja": pensja})
    with open("pracownicy.json", "w") as plik:
        json.dump(pracownicy, plik)
elif akcja == "w":
    for nr, p in enumerate(pracownicy, 1):
        print(f"- [{nr}] {p['imie']} {p['nazwisko']} - rok: {p['rok urodzenia']}, pensja: {p['pensja']} PLN")
