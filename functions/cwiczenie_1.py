def czy_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


x = czy_pierwsza(3)
y = czy_pierwsza(9)

print(x)
print(y)

def test_czy_pierwsza_dla_liczby_pierwszej():
    assert czy_pierwsza(11)
    assert czy_pierwsza(83)
    assert czy_pierwsza(101)

def test_czy_pierwsza_dla_liczby_nie_pierwszej():
    assert not czy_pierwsza(10)
    assert not czy_pierwsza(27)
    assert not czy_pierwsza(100)

