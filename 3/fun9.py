# funkcja lambda
# skrócony zapis funkcji
# zwraca wynik
# funkcja anonimowa, możliowśc deklaracji w miejscu wykonania
from functools import reduce


def odejmij(a, b):
    return a - b


print(odejmij(7, 2))  # 5

odejmij2 = lambda a, b: a - b
print(odejmij2(123, 89))  # 34

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))
print(wiek(10))
print(wiek(17))
print(wiek(18))
print(wiek(25))
# dziecko
# nastolatek
# nastolatek
# dorosły
# dorosły

lista = [1, 2, 5, 10, 25, 50, 69, 70, 500]

l = []
for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 10, 20, 50, 100, 138, 140, 1000]

print([i * 2 for i in lista])  # [2, 4, 10, 20, 50, 100, 138, 140, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 10, 20, 50, 100, 138, 140, 1000]

# funkcje wyzszego rzędu
# map() - pobiera elemnty i wykonuje na nich funkcję
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 10, 20, 50, 100, 138, 140, 1000]
# Lambda jako funkcja anonimowa
# deklaracja w  miejscu wykonania
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 10, 20, 50, 100, 138, 140, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 7, lista))}")

# filtrowanie danych
l3 = []
for i in lista:
    if i < 10:
        l3.append(i)
print(l3)  # [1, 2, 5]
# filter()
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 10, lista))}")
# Zastosowanie filter(): [1, 2, 5]
# dla x > 40
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 40, lista))}")
# dal x > 5 i x < 100
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 5 and x < 100, lista))}")
# Zastosowanie filter(): [10, 25, 50, 69, 70]
print(f"Zastosowanie filter(): {list(filter(lambda x: 5 < x < 100, lista))}")
# Zastosowanie filter(): [10, 25, 50, 69, 70]


# reduce()
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#     ((((1+2)+3)+4)+5).
lista_reduce = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, lista_reduce))  # 15
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
print(reduce(lambda a, b: a * b, lista_reduce))  # 120
# 1 * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120
