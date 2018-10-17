liczba = 0
for x in range(101):
    if x % 3 == 0 or x % 5 == 0:
        print(x)
        liczba += 1

print(f"Podzielnych przez 3 i 5 jest {liczba} liczb")