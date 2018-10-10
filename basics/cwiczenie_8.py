wys = int(input("Wprowadz wysokosc opakowania [cm]: "))
szer = int(input("Wprowadz szerokosc opakowania [cm]: "))
dl = int(input("Wprowadz długość opakowania [cm]: "))

obj = wys * szer * dl

spr = obj > 1000

if obj > 1000:
    print("Objetosc wieksza niz 1 litr")
else:
    print("Objetosc mniejsza badz rowna litrowi")

