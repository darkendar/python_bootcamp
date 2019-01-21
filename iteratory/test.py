class Iterator:
    def __iter__(self):
        self.licznik=0
        return self

    def __next__(self):
        if self.licznik > 10:
            raise StopIteration
        liczba = self.licznik += 1
        return liczba

for i in Iterator():
    print(i)