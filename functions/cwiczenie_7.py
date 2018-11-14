def przytnij(lista, w_start, w_stop):
    out = []
    for element in lista:
        if w_start(element):
            out.append(element)
        if w_stop(element):
            return out

def przytnij1(data, start, stop):
    result = []
    dodawac_do_listy = False
    for el in data:
        if start(el):
            dodawac_do_listy = True
        if dodawac_do_listy:
            result.append(el)
            if stop(el):
                break
    return result


def test_przytnij_liste():
    data = [1, 2, 3, 4, 5, 6, 7]
    start = lambda x: x > 3
    stop = lambda x: x == 6
    assert przytnij(data, start, stop) == [4, 5, 6]

def test_przytnij_liste1():
    data = [1, 2, 3, 4, 5, 6, 7]
    start = lambda x: x > 3
    stop = lambda x: x == 6
    assert przytnij1(data, start, stop) == [4, 5, 6]