#otworzenie pliku do odczyti
# with open("dane/input.txt") as f:
#     for linia in f:
#         print(linia)

# with open("dane/input.txt") as f:
#     for linia in f:
#         if len(linia) > 600:
#             print(len(linia))

#tryb do odczytu

with open("info.txt", "w", encoding="utf8") as f:
    for i in range(10):
        f.write("Jakiś tekst\n")

with open("info.txt", "a", encoding="utf8") as f:
    f.write("inny tekst")