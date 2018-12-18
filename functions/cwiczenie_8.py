def bold(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)
        return "<b>" + wynik + "<\\b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        wynik = func(*args, **kwargs)
        return "<i>" + wynik + "<\\i>"
    return wrapper

@bold # == nasza_funkcja = bold(nasza_funkcja)
@italic
def nasza_funkcja():
    return "jakis napis"

# nasza_funkcja = bold(nasza_funkcja)

print(nasza_funkcja())