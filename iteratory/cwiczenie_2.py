samogloski = "aeiouy"
class Vowels:

    def __init__(self, napis):
        self.napis = napis

    def __iter__(self):
        self.miejsce = 0
        return self

    def __next__(self):
        while self.miejsce < len(self.napis):
            litera = self.napis[self.miejsce]
            self.miejsce += 1
            if litera in samogloski:
                return litera
        raise StopIteration


for char in Vowels("ala ma kota"):
    print(char)
