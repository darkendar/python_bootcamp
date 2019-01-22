def generator(napis):
    for i in napis:
        if i in "aeiouy":
            yield i


for x in generator("ala ma kota a kot ma ale"):
    print(x)
