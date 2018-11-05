# def foo(pierwszy, *reszta):
#     # print("pierwszy: ", pierwszy)
#     # print("reszta", reszta)
#     if reszta:
#         return pierwszy + reszta[-1]
#     return pierwszy
#
#
# print(foo(1))
# print(foo(1, 2, 5, 10))
# print(foo(1, 2))
#
# reszta = [2, 5, 10, 15]
# print(*reszta)
# print(reszta)
#
# def druga_funkcja(**slownik):
#     print(type(slownik))
#     if 'd' in slownik:
#         return slownik['a'] + slownik['d']
#     if slownik:
#         return slownik['a']
#     return "Żaden warunek nie był spełniony"
#
#
# print('a', druga_funkcja(a=2))
# print('a i d', druga_funkcja(a=2, b=2, c=3, d=4))
# print('a i d drugi raz', druga_funkcja(a=2, b=2, c=3, d=14, zosia=5, adas=15))
# print('a drugi raz ale bez d', druga_funkcja(a=2, b=2, c=3, d=14, zosia=5, adas=15))

# co_na_co = {
#     "Ala": "Kot",
#     "kota": "Alę"
# }


# def zamien(jakis_tekst, **co_na_co):
#     for klucz in co_na_co:
#         jakis_tekst = jakis_tekst.replace(klucz, co_na_co[klucz])
#
#     return jakis_tekst
#
# print(zamien("Ala ma kota", ma = "bije"))

napis = "Ten $produkt kosztuje $cena"
napis2 = "Zajęcia z $przedmiot zostały odwołane"

def formatuj(*napisy, **co_na_co):
    wynik = []
    for napis in napisy:
        for klucz in co_na_co:
            napis = napis.replace("$"+klucz, co_na_co[klucz])
        wynik.append(napis)
    if len(wynik) == 1:
        return wynik[0]
    return wynik

assert formatuj(napis, produkt="Samochód", cena="20000") == "Ten Samochód kosztuje 20000"
assert formatuj(napis2, przedmiot = "Fizyki") == "Zajęcia z Fizyki zostały odwołane"
