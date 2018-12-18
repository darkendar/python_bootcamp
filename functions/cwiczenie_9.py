from time import time

def czas(func):
    def wrapper(*args, **kwargs):
        przed_wywolaniem = time()
        wynik = func(*args, *kwargs)
        po_wywolaniu = time()
        print(f"Czas wywołania funkcji {func.__name__}: {po_wywolaniu - przed_wywolaniem}s")
        return wynik
    return wrapper

# @czas - w tym miejscu wywolywaloby w nieskonczonosc
def fib(x):
    if x <= 1:
        return x
    return fib(x - 1) + fib(x - 2)

@czas
def funkcyja(x):
    return fib(x)


print(funkcyja(30))