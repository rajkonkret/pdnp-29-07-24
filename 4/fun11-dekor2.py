# zamienia wynik działania funkcji na duże litery upper()
print("Radek".upper())  # RADEK


def upper_case(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


def bold_decorator(func):
    def wrapper():
        result = func()
        return "\033[1m" + result + "\033[0m"

    return wrapper


@bold_decorator
@upper_case
def greeting():
    return "Hello World!"


print(greeting())  # HELLO WORLD!
