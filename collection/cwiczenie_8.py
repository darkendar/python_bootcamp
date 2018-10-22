napis = input("Podaj napis: ")

# for i in napis:
#     if i == "<":
#         x = napis.index(i)
#     elif i == ">":
#         y = napis.index(i)
#
# znaki = y - x - 1
#
# print(znaki)

licznik = 0
czy_zliczac = False

for i in napis:
    if i == "<":
        czy_zliczac = True
    elif i == ">":
        czy_zliczac = False
    elif czy_zliczac:
        licznik += 1

print(licznik)