import sys

print()  # wypisz/wydrukuj
# ctr alt l - formatowanie kodu
print("Nazywam się Radek")
print('Nazywam się Radek')
# Nazywam się Radek
# Nazywam się Radek
# print('Nazywam się Radek")
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-29-07-24\1\pierwszy.py", line 7
#     print('Nazywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 7)
# ctrl / - zakomentowanie zaznaczonych linii
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
# ctrl d - powielanie lini z kursorem
# type() - sprawdzenie typów danych
print(type("Radek"))  # <class 'str'> dane typu tekstowego
print(type("39"))  # <class 'str'>
print("39")  # 39
print("39" + "39")  # 3939 - łaczenie stringów - konkatenacja
print(39)  # 39
print(type(39))  # <class 'int'> - liczby całkowite
print(sys.int_info)
# sys.int_info(
#     bits_per_digit=30,
#     sizeof_digit=4,
#     default_max_str_digits=4300,
#     str_digits_check_threshold=640)
# silne typowanie - nie zmienia sam typów podczas operacji
# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str
# musimy jawnie zamienic typy
print(int("39") + 39)  # int() - zamiana, rzutowanie na liczbę całkowitą 78
print("39" + str(39))  # str() - zamina, rzutowanie liczby na str(tekst), 3939
print("8" + "8" + "8")  # 888
print(8 + 8 + 8)  # 24

print(5 * "4")  # 44444
# zmienna  - pudełko, szufladka
liczba = 39
print(liczba)
print(type(liczba))  # <class 'int'>
print(5 * liczba)  # 195

liczba = "39"
print(liczba)
print(type(liczba))  # <class 'str'>
print(5 * liczba)  # 3939393939

name = "Radek"
# print(name + "Kowalski")  # RadekKowalski

name = 90
# print(name + "Kowalski")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# to jest tylko podpowiedź, hint
name: str = "Radek"
print(name)  # Radek

# nazwy zmiennych malymi literami
# snake_case
# nazwa zmiennej powinna podpowiadać co zmienna przechowuje
age = 56
print(age)
print(type(age))
