
def hello():
    print("Hello World")
    return 10

def hello2(name):
    print(f"Hello {name}")

def hello3(name = 'World'):
    print(f"Hello {name}")

def dodaj(a, b):
    return a + b

def test_dodaj_dwie_liczby():
    assert dodaj(1, 2) == 3

def test_dodaj_dwa_napisy():
    assert dodaj("1", "2") == "12"

hello()
hello2("Mikołaj")
hello3()

x = print("testuje co zwraca print")
print("x:", x)

y = dir()
print("y:", y)

z = hello()
print("z:", z)

wynik = dodaj(10, 11)
wynik2 = dodaj(1.1, 20.2)
wynik3 = dodaj("a", "b")

print(wynik)
print(wynik2)
print(wynik3)

def klon(imie, wiek = 18, wzrost = 181):
    print(f"Witaj {imie}")
    if wiek == 18 and wzrost == 181:
        print("Masz standardowe parametry")
    else:
        print("Różnisz sie od pozostałych!")