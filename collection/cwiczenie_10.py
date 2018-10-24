napis = input("Podaj napis: ")
znaki = {}


for i in napis.lower():
    if i != " ":
        if i in znaki:
            znaki[i] += 1
        else:
            znaki[i] = znaki.get(i, 1)

print(znaki)


for k in znaki:
    print(f"Litera [{k}] wystąpiła: {znaki[k]} razy")

# for litera in napis:
#     if litera != " ":
#         znaki[litera] = liczniki.get(litera, 0) + 1