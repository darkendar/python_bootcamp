class Employee():

    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
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


kopacz = Employee("Maciej", "Kowalski", 100)
print(kopacz.pay_salary())
kopacz.register_time(5)
kopacz.register_time(10)
print(kopacz.pay_salary())
print(kopacz.pay_salary())
