class Counter:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.licznik=0
        return self

    def __next__(self):
        if self.licznik > self.limit:
            raise StopIteration
        liczba = self.licznik
        self.licznik += 1
        return liczba


for i in Counter(10):
    print(i)



