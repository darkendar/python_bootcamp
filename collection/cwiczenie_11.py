liczby = set()
parzyste = set(range(2, 101, 2))

while True:
    liczba = input("Podaj liczbe: ")
    if liczba == "k":
        break
    liczby.add(liczba)

wspolne = parzyste & liczby
print(wspolne)
print(f"Wprowadzono {len(liczby)} liczb, z których {len(wspolne)} jest parzystych")

#napisz program ktory posortuje liczby w tablicy przy wykorzystaniu algorytmu "sortowanie przez wybranie"
