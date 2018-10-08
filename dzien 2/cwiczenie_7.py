liczba = int(input("Podaj liczbe: "))

wynik = liczba == 7 or (liczba % 2 == 0 and liczba % 3 == 0 and liczba > 10)

print(f"Podzielna przez 2 i 3 i wieksza od 10 lub jest to 7: {wynik}")