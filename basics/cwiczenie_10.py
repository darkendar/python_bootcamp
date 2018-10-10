liczba1 = int(input("Podaj liczbe: "))
liczba2 = int(input("Podaj liczbe: "))
operacja = input("Podaj znak operacji: ")

dodawanie = liczba1 + liczba2
odejmowanie = liczba1 - liczba2
mnozenie = liczba1 * liczba2


if operacja == "+":
    print(dodawanie)
elif operacja == "-":
    print(odejmowanie)
elif operacja == "*":
    print(mnozenie)
elif operacja == "/":
    if liczba2 == 0:
        dzielenie = "Dzielenie przez 0"
    else:
        dzielenie = liczba1 / liczba2
    print(dzielenie)