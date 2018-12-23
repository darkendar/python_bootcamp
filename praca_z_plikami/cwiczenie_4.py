import sys
import os


def drzewko(katalog, ile_wciec=0):
    zawartosc = list(os.scandir(katalog))
    for elem in zawartosc:
        if elem == zawartosc[-1]:
            sepa = "/   "
        else:
            sepa = "|   "
        print(ile_wciec*sepa, elem.name, sep="")
        if elem.is_dir():
            drzewko(elem, ile_wciec + 1)


directory = sys.argv[1]
drzewko(directory)
