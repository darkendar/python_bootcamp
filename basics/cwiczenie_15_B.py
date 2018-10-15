from random import randint
graczx = randint(1, 10)
graczy = randint(1, 10)
skarbx = randint(1, 10)
skarby = randint(1, 10)

while True:

    print(f"Położenie gracza to {graczx}, {graczy}")

    kierunek = intput("Podaj kierunek ruchu: ")

    minkrokowprzed = abs(skarbx - graczx) + abs(skarby - graczy)

    if kierunek == "w":
        graczy += 1
    elif kierunek == "s":
        graczy -= 1
    elif kierunek == "a":
        graczx -= 1
    elif kierunek == "d":
        graczx += 1

    minkrokowpo = abs(skarbx - graczx) + abs(skarby - graczy)

    if minkrokowpo == 0:
        print("Znalazles skarb!")
        break
    if randint(1, 5) < 5:
        if minkrokowprzed < minkrokowpo:
            print("Oddalasz sie")
        else:
            print("Zbliżasz się")

    if graczx > 10 or graczx < 1 or graczy > 10 or graczy < 1:
        print("Spadłeś z planszy!")
        break
