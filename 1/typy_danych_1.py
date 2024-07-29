import sys

wiek = 47
rok = 2024
temp = 36.6  # float

print(temp)
print(type(temp))  # <class 'float'>
print(5 * wiek)  # 235
print(5 * "wiek")  # wiekwiekwiekwiekwiek

print(wiek + rok)  # 2071
print(wiek - rok)  # -1977
print(wiek * rok)  # 95128
print(wiek / rok)  # 0.023221343873517788

print(rok // wiek)  # część całkowita dzielenia 43
print(rok % wiek)  # modulo -> 3, reszta z dzielenia
print(5 % 2)  # 1

print(wiek ** rok)  # potęgowanie
# len() - zwraca długośc elementu
print(len(str(wiek ** rok)))  # 3385 znaków
# print(len(str(wiek ** rok ** 2)))  # ValueError: Exceeds the limit (4300 digits)
# for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# przy liczbach float mamy bład zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# 1.3 x 10 ^ 3
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024, max_10_exp=308,
#                min=2.2250738585072014e-308,
#                min_exp=-1021,
#                min_10_exp=-307,
#                dig=15,
#                mant_dig=53,
#                epsilon=2.220446049250313e-16,
#                radix=2,
#                rounds=1)


print(f"Sprawdzenie zmiennej {temp} {wiek}")  # Sprawdzenie zmiennej 36.6 47
print(f"""
{wiek}
    {temp}""")
# "47
#     36.6"

# typ logiczny
# prawda fałsz
# True False
czy_znasz_python = True
print(czy_znasz_python)  # True
print(type(czy_znasz_python))  # <class 'bool'>

# 1 - prawda, 0 - fałsz
print(int(False))  # 0
print(int(czy_znasz_python))  # 1
x = 100
print(bool(x))  # True
print(bool(-10))  # True
print(bool("radek"))  # True

print(bool(""))  # False
print(bool(0))  # False
print(bool("0"))  # True
x = None  # stan nieokreslony, nic, nie wiem -> null
print(bool(x))  # False

# dzialania logiczne
# and  - i
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or - lub
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

x = 0
print(not x == 1)  # == porównanie

# not - negacja
print(not True)  # False
print(not False)  # True

a = 8
b = 6

print(f"Porówanie {a} > {b}= {a > b}")  # Porówanie 8 > 6= True
print(f"Porówanie {a} < {b}= {a < b}")  # Porówanie 8 < 6= False
print(f"Porówanie {a <= b = }")  # Porówanie a <= b = False
print(f"Porówanie {a >= b = }")  # Porówanie a >= b = True
print(f"Porównanie {a} == {b} = {a == b}")  # Porównanie 8 == 6 = False, == porównanie
print(f"Porównanie {a} != {b} = {a != b}")  # Porównanie 8 != 6 = True, != różne
