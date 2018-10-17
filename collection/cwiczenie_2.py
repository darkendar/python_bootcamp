x=[]

while len(x) < 10:
    y = input("Podaj liczbe: ")
    if y == "k":
        break
    liczba = int(y)
    x.append(liczba)

if len(x) == 0:
    print("Nie podano danych")
else:
    srednia = sum(x) / len(x)
    print(srednia)