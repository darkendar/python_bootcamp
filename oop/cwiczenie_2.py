class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Employee(Osoba):

    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko)
        self.stawka = stawka
        self.czas_pracy = 0

    # def register_time(self, czas_pracy):
    #     if czas_pracy > 8:
    #         self.czas_pracy = 8 + 2 * (czas_pracy-8)
    #     else:
    #         self.czas_pracy = czas_pracy

    def register_time(self, czas_pracy):
        self.czas_pracy += czas_pracy
        if czas_pracy > 8:
            self.czas_pracy += czas_pracy - 8

    def pay_salary(self):
        wyplata = self.stawka * self.czas_pracy
        self.czas_pracy = 0
        return wyplata


class PremiumEmployee(Employee):

    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, kwota):
        self.bonus += kwota

    def pay_salary(self):
        to_pay = super().pay_salary()
        self.bonus = 0
        return to_pay + self.bonus


kopacz = PremiumEmployee("Maciej", "Kowalski", 100)
print(kopacz.pay_salary())
kopacz.register_time(10)
kopacz.give_bonus(1000)
print(kopacz.pay_salary())
print(kopacz.pay_salary())
