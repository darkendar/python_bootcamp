liczby = set()
sort = set()
min_ = None
max_ = None

while True:
    liczba = input("Wprowadz liczbe: ")
    if liczba == "k":
        break
    liczby.add(liczba)

for i in liczby:
    if min_ is None or min_ < i:
        min_ = i
    if max_ is None or max_ > i:
        max_ = i

print(liczby)
print(min_)
print(max_)