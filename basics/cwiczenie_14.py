znalezione_max = None
znalezione_min = None

while True:

    dane = input("Wprowadz liczbe: ")

    if dane == "koniec":
        break

    x = int(dane)
    if znalezione_max is None or x > znalezione_max:
        znalezione_max = x
    if znalezione_min is None or x < znalezione_min:
        znalezione_min = x


if znalezione_max is None:
    print("Nie wprowadzono danych")
else:
    print(f"Najwieksza wprowadzona liczba to: {znalezione_max}, a najmniejsza to: {znalezione_min}")