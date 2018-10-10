i = 1
suma = 0

while True:

    dane = input("Podaj temperature lub wpisz k by zakonczyc: ")

    if dane == "k":
        break

    suma += float(dane)
    i = i + 1

 print("Srednia temperatura to: ", suma/i)