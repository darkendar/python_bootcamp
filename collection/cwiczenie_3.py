x=[1, -2, 0, -3, -4, 5, -6, 7, 8]
ujemne = 0
dodatnie = 0
zera = 0

for i in x:

    if i < 0:
        ujemne += 1
    elif i > 0:
        dodatnie += 1
    elif i == 0:
        zera += 1

print(f"Dodatnie: {dodatnie}, ujemne: {ujemne}, zera = {zera}")

