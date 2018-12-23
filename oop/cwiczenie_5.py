import pytest


class NoEnoughMoney(ValueError):
    pass


class AmountNotDividableByTen(ValueError):
    pass


class TooManyBills(ValueError):
    pass


class CashMachine:

    def __init__(self):
        self._money = []

    @property
    def empty_slots(self):
        return 10 - len(self._money)

    def __str__(self):
        return f"Bankomat ma {empty_slots()} pustych miejsc"

    @property
    def is_available(self):
        if self._money:
            return True
        return False

    def put_money(self, money):
        if len(money) + len(self._money) > 10:
            raise TooManyBills("BŁĄD: Bankomat nie przyjmuje więcej niż 10 banknotów")
        self._money.extend(money)

    def withdraw_money(self, to_withdraw):

        if to_withdraw % 10 != 0:
            raise AmountNotDividableByTen("BŁĄD: Kwota powinna być wielokrotnością 10")

        bills_to_withdraw = []

        for bill in sorted(self._money, reverse=True):
            if sum(bills_to_withdraw) + bill <= to_withdraw:
                bills_to_withdraw.append(bill)

        if sum(bills_to_withdraw) != to_withdraw:
            raise NoEnoughMoney("BŁĄD: brak wystarczającej liczby banknotów")

        for bill in bills_to_withdraw:
            self._money.remove(bill)

        return bills_to_withdraw


def main():
    bankomat = CashMachine()
    while True:
        operacja = input("Podaj typ operacji w - wpłata, y - wypłata, k - zakończ, p - print: ")
        if operacja == "k":
            print("Dziękujemy za skorzystanie z naszych usług")
            return

        if operacja == "p":
            print(CashMachine)

        if operacja == "w":
            banknoty = input("Podaj jakie banknoty wpłacasz - wpisz je rozdzielając spacją (bankomat mieści maksymalnie 10 banknotów): ")
            banknoty = banknoty.split()
            banknoty = [int(x) for x in banknoty]
            try:
                bankomat.put_money(banknoty)
            except ValueError as e:
                print(e)
        elif operacja == "y":
            wyplata = int(input("Podaj kwotę do wypłacenia: "))
            try:
                wyplacone = bankomat.withdraw_money(wyplata)
            except ValueError as e:
                wyplacone = False
                print(e)
            if wyplacone:
                print(wyplacone)


main()


def test_cash_machine_not_available():
    cash_machine = CashMachine()
    assert not cash_machine.is_available


def test_cash_machine_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([50])
    cash_machine.put_money([50])
    assert cash_machine.is_available


def test_cash_machine_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    wallet = cash_machine.withdraw_money(150)
    assert wallet == [100, 50]


def test_cash_machine_withdraw_money_value_is_not_dividable_by_ten():
    cash_machine = CashMachine()
    with pytest.raises(ValueError):
        cash_machine.withdraw_money(123)


def test_cash_machine_input_too_many_bills():
    cash_machine = CashMachine()
    with pytest.raises(TooManyBills):
        cash_machine.put_money([10 for i in range(11)])
