from random import randint
from przedmiot import Przedmiot
#randint(1,10) - liczba całkowita z przedziału 1-10

class Postac:

    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self.atak = atak
        self.zdrowie = zdrowie
        self.zdrowie_max = zdrowie
        self.ekwipunek = []

    def przedstaw_sie(self):
        print(self)

    def __str__(self):
        if self.czy_zyje():
            napis = "EKWIPUNEK:\n"
            for x in self.ekwipunek:
                napis += str(x) + "\n"
            return f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.zdrowie_max} życia. " + napis
        else:
            return f"Jestem {self.imie}, miałem {self.atak} i nie żyję."

    def wylecz(self, ile):
        if self.czy_zyje():
            self.zdrowie += ile
            if self.zdrowie > self.zdrowie_max:
                self.zdrowie = self.zdrowie_max
            print(f"{self.imie} ma teraz {self.zdrowie} zdrowia.")
        else:
            print("Nie możesz uleczyć trupa")

    def otrzymaj_obrazenia(self, ile):
        self.zdrowie -= ile
        if self.zdrowie < 0:
            self.zdrowie = 0

    def czy_zyje(self):
        return self.zdrowie > 0

    def daj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def atak_plus(self):
        self.atak += ekwipunek[1]

    def moc_ataku(self):
        return self.atak//2 + randint(0, self.atak//2)

    @staticmethod
    def walka(atakujacy, broniacy):
        print(f"Walka: {atakujacy.imie} vs {broniacy.imie}")
        while atakujacy.czy_zyje() and broniacy.czy_zyje():
            print(atakujacy)
            print(broniacy)
            print(f"{atakujacy.imie} uderza {broniacy.imie} za {atakujacy.moc_ataku()} obrażeń.")
            broniacy.otrzymaj_obrazenia(atakujacy.moc_ataku())
            print(f"{broniacy.imie} uderza {atakujacy.imie} za {broniacy.moc_ataku()} obrażeń.")
            atakujacy.otrzymaj_obrazenia(broniacy.moc_ataku())
        print("KONIEC WALKI")


rufus = Postac("Rufus", 30, 300)
janusz = Postac("Janusz", 40, 300)

tulipan = Przedmiot("Zielony tulipan znieszczenia", 5)
rufus.daj_przedmiot(tulipan)

Postac.walka(rufus, janusz)
print(rufus)
print(janusz)


# rufus.przedstaw_sie()
# print(rufus)
# rufus.otrzymaj_obrazenia(10)
# rufus.wylecz(10)
# rufus.otrzymaj_obrazenia(20)
# rufus.wylecz(30)
# rufus.otrzymaj_obrazenia(110)
# print(rufus)
# rufus.wylecz(10)


def test_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(50)
    assert postac.zdrowie == 170

def test_leczenie_nieboszczyka():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(800)
    assert postac.zdrowie == 0
    postac.wylecz(50)
    assert postac.zdrowie == 0


def test_za_duze_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(505)
    assert postac.zdrowie == 200
