from django.http import HttpResponse
from django.shortcuts import render

from maths.models import Math


def obliczenia(request, dzialanie, a, b):

    if dzialanie == 'add':
        a = int(a)
        b = int(b)
        wynik = a+b
    elif dzialanie == "div":
        a, b = float(a), float(b)
        if b == 0:
            wynik = "Dzie dziele przez zero!"
        else:
            wynik = a/b

    m = Math(operacja=dzialanie, a=a, b=b, wynik=wynik)
    m.save()

    print(m.a, m.b, m.operacja)

    return HttpResponse(wynik)
# Create your views here.
