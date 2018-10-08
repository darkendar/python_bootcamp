liczba = int(input("Podaj liczbe: "))

wieksza_od_10 = liczba > 10
mniejsza_rowna_15 = liczba <= 15
podzielna_przez_2 = liczba % 2 == 0

print(f"""Wieksza od 10: {wieksza_od_10}
Mniejsza rowna 15: {mniejsza_rowna_15}
Podzielna przez 2: {podzielna_przez_2}""")

print(f"Podzielna przez 3 i wieksza od 10: {liczba % 3 == 0 and liczba > 10}")
print(f"Wieksza od 10 lub podzielna przez 5: {liczba > 10 or liczba % 5 ==0}")