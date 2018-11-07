def bold(func):
    def wrapper(arg):
        return'<b>' + func(arg) + '</b>'
    return wrapper

def italic(func):
    def wrapper(arg):
        return '<i>' + func(arg) + '</i>'
    return wrapper

@italic
@bold
def foo(arg):
    return f"Test {arg}"

print(foo(1))