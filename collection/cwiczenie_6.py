liczby = [5, 2, 1, 4, 3]
min_ = liczby[0]
max_ = liczby[0]
#assert False
#assert True
for liczba in liczby:
    if liczba > max_:
        max_ = liczba
    elif liczba < min_:
        min_ = liczba

print(min_, max_)
print(liczby.index(min_), liczby.index(max_))

#liczby[liczby.index(min_)] = max_
#liczby[liczby.index(max_)] = min_

liczby[liczby.index(min_)], liczby[liczby.index(max_)] = max_, min_


#assert liczby == [1, 2, 5, 4, 3]