from random import randint

graczX = randint(1, 10)
graczY = randint(1, 10)
skarbX = randint(1, 10)
skarbY = randint(1, 10)
odlX = abs(skarbX - graczX)
odlY = abs(skarbY - graczY)

print(f"Twoje położenie to X: {graczX}, Y = {graczY}")
print(f"Położenie skarbu X: {skarbX}, Y = {skarbY}")

while True:

    ruch = input("Podaj kierunek w który chcesz sie udać (w s a d): ")

    if ruch == "w":
        graczY = graczY + 1
        if graczY > 10:
            print("Wyszedles poza plansze!")
        print(f"Twoje położenie to X: {graczX}, Y = {graczY}")
        if abs(skarbY - graczY) < odlY:
            print("Idziesz w dobrym kierunku")
            odlY = odlY - 1
            if graczY == skarbY:
                print("Współrzędna Y sie zgadza!")
        elif skarbY == graczY:
            print("Współrzędna Y sie zgadza!")
        else:
            print("Idziesz w złym kierunku")
            odlY = odlY + 1
    elif ruch == "s":
        graczY = graczY - 1
        if graczY < 0:
            print("Wyszedles poza plansze!")
        print(f"Twoje położenie to X: {graczX}, Y = {graczY}")
        if abs(skarbY - graczY) < odlY:
            print("Idziesz w dobrym kierunku")
            odlY = odlY - 1
            if graczY == skarbY:
                print("Współrzędna Y sie zgadza!")
        elif skarbY == graczY:
            print("Współrzędna Y sie zgadza!")
        else:
            print("Idziesz w złym kierunku")
            odlY = odlY + 1
    elif ruch == "a":
        graczX = graczX - 1
        if graczX < 0:
            print("Wyszedles poza plansze!")
        print(f"Twoje położenie to X: {graczX}, Y = {graczY}")
        if abs(skarbX - graczX) < odlX:
            print("Idziesz w dobrym kierunku")
            odlX = odlX - 1
            if graczX == skarbX:
                print("Współrzędna X sie zgadza!")
        elif graczX == skarbX:
            print("Współrzędna X sie zgadza!")
        else:
            print("Idziesz w złym kierunku")
            odlX = odlX + 1
    elif ruch == "d":
        graczX = graczX + 1
        if graczX > 10:
            print("Wyszedles poza plansze!")
        print(f"Twoje położenie to X: {graczX}, Y = {graczY}")
        if abs(skarbX - graczX) < odlX:
            print("Idziesz w dobrym kierunku")
            odlY = odlY - 1
            if graczX == skarbX:
                print("Współrzędna X sie zgadza!")
        elif skarbX == graczX:
            print("Współrzędna X sie zgadza!")
        else:
            print("Idziesz w złym kierunku")
            odlX = odlX + 1

    if graczX == skarbX and graczY == skarbY:
        break


print("Odnalazles skarb!")


