a = 10
b = 15


def dodaj():
    a = 7  # zasięg lokalny, nie wpływa na globalne wartości zmiennych o tej samej nazwie
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # Uzyj a globalne
    a = 9  # nadpisujemy a globalne
    b = 87
    print(a + b)


print(f"Wartość a z góry {a}")  # Wartość a z góry 10
dodaj()  # 15
print(f"Wartość a z góry {a}")  # Wartość a z góry 10
dodaj2()  # 25
print(f"Wartość a z góry {a}")  # Wartość a z góry 10
dodaj3()  # 96
print(f"Wartość a z góry {a}")  # Wartość a z góry 9
dodaj2()  # 24
