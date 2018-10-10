x = int(input("Podaj pozycję gracza X: "))
y = int(input("Podaj pozycję gracza Y: "))

if x > 100 or x < 0 or y > 100 or y < 0:
    print("Jestes poza plansza")
else:
    cntr = x > 10 and x < 90 and y > 10 and y < 90
    pdr = x >= 90 and y <= 10
    ldr = x <= 10 and y <= 10
    pgr = x >= 90 and y >= 90
    lgr = x <= 10 and y >= 90
    dk = x > 10 and x < 90 and y < 10
    gk = x > 10 and x < 90 and y > 90
    pk = x > 90 and y > 10 and y < 90
    lk = x < 10 and y > 10 and y < 90

    if cntr:
        print("Jestes w centrum")
    elif pdr:
        print("Jestes w prawym dolnym rogu")
    elif ldr:
        print("Jestes w lewym dolnym rogu")
    elif pgr:
        print("Jestes w prawym gornym rogu")
    elif lgr:
        print("Jestes w lewym gornym rogu")
    elif dk:
        print("Jestes na dolnej krawedzi")
    elif gk:
        print("Jestes na gornej krawedzi")
    elif lk:
        print("Jestes na lewej krawedzi")
    elif pk:
        print("Jetses na prawej krawedzi")