

def splaszcz(lista):
    out = []
    for element in lista:
        if isinstance(element, list):
            wynik = splaszcz(element)
            for el in wynik:
                out.append(el)
        else:
            out.append(element)
    return out


# def splaszcz(lista):
#     out = []
#     for element in lista:
#         if isinstance(element, list):
#             out.extend(splaszcz(element))
#         else:
#             out.append(element)
#     return out


def test_splaszcz_niezagniiezdzona_lista():
    lista = [1, 2, 3, 4, 5, 6, 7]
    assert splaszcz(lista) == [1, 2, 3, 4, 5, 6, 7]

def test_splaszcz_jedno_zagniezdzenie():
    lista = [1, [2, 3]]
    assert splaszcz(lista) == [1, 2, 3]

def test_splaszcz_wiele_zagniezdzen():
    lista = [1, 2, 3, [4, 5, [6, 7]], 7]
    assert splaszcz(lista) == [1, 2, 3, 4, 5, 6, 7, 7]

#int, float, list, tuple, str, dict, set, complex
# assert isinstance(lista[0], int)
# assert isinstance(lista[3], int])
#
# assert splaszcz(lista) == [1, 2, 3, 4, 5, 6, 7, 7]

