def formatuj(*args, **kwargs):
    tekst = "\n".join(args)
    for k in kwargs:
        tekst = tekst.replace("$" + k, str(kwargs[k]))
    return tekst

def test_formatuj():
    assert formatuj(
        'koszt $cena PLN',
        'kwota $cena brutto',
        cena=10,
    ) == 'koszt 10 PLN\nkwota 10 brutto'
