miastoa = input("Podaaj miasto z którego jedziesz: ")
miastob = input("Podaj miasto docelowe: ")
dystans = int(input("Podaj dystans miedzy miastami : "))
paliwo_cena = float(input("Podaj cene paliwa: "))
spalanie = float(input("Podaj spalanie na 100 km: "))

koszt = round(spalanie * paliwo_cena * (dystans/100), 2)

print(f"Cena przejazdu z {miastoa} do {miastob} wynosi: {koszt} zł")

