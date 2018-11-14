def silnia(liczba):
    if liczba == 0:
        return 1
    else:
        return liczba * silnia(liczba-1)



def test_silnia_dla_0():
    assert silnia(0) == 1

def test_silnia_dla_wieksze_od_0():
    assert silnia(2) == 2
    assert silnia(5) == 120
    assert silnia(6) == 720