lista = [10, 20, 30, 40, 50]
lista2 = [x for x in range(1000)]

def reku_print(lista):
    if len(lista) == 1:
        print(lista[0])
    else:
        print(lista[0])
        reku_print(lista[1:])


reku_print(lista2)
