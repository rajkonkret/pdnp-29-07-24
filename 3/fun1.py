# funkcja - wydzielony fragment kodu, można go wywołać wielokrotnie w dowolnym momencie
# funkcja musi byc najpierw zadekalrowana
# w miejscu deklaracji funkcja się nie wykonuje
# żeby funkcja się wywokonała trzeba ją wywołać

a = 6
b = 8


# deklaracja funkcji
# sowko def, nazwa_funkcji, nawiasy()
# PEP8 wymaga by były dwie puste linie
# funkcja bez przekazywania argumentów
def dodaj():
    print(a + b)


def dodaj2(a, b):  # obowiązkowe do przekazania dwa argumenty a i b
    print(a + b)


def odejmij(a, b, c=0):
    print(a - b - c)


# wywołąnie funkcji
# nazwa_funkcji i nawiasy()
dodaj()  # 14
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
# przekazywanie argumentów po pozycji
dodaj2(6, 90)  # 96
odejmij(2, 3)
odejmij(2, 3, 4)

# przekazywanie argumentów po nazwie
odejmij(c=3, b=6, a=10)
odejmij(b=8, a=8)

# argumenty mieszane
odejmij(1, c=90, b=87)
# odejmij(a=1, c=90, 67)  # SyntaxError: positional argument follows keyword argumentSyntaxError: positional argument follows keyword argument
print(dodaj())  # None
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(dodaj() + dodaj2(6,90))
