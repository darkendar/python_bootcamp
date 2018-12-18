# def fun():
#     print("Cześć")
#
# fun()
#
# def prosty_prawie_dekorator(func):
#     def wrapper():
#         print("Przed wywołaniem")
#         func()
#         print("Po wywołaniu")
#     return wrapper
#
#
# nowa_fun = prosty_prawie_dekorator(fun)
#
# print("Akuku")
# nowa_fun()

def prosty_dekorator(func):
    def wrapper(*args, **kwargs):
        print("Przed wywołaniem")
        result = func(*args, **kwargs)
        print("Po wywołaniu")
        return result
    return wrapper

# fun = dwa_wywolania(fun)
def dwa_wywolania(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper()

@dwa_wywolania
@prosty_dekorator
def fun():
    print("Cześć")

@prosty_dekorator
@dwa_wywolania
def fun():
    print("Cześć")

@prosty_dekorator
def silnia(x):
    wynik = 1
    for i in range(1, x+1):
        wynik *= i
    return wynik

fun = prosty_prawie_dekorator(fun)

print("Akuku")
fun()