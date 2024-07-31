# funkcje zwracające wynik
# kończą słówkiem return
# gdy napotka return wychodzi z funkcji

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(8, 67))  # 75
print(odejmij(1, 23))
print(odejmij())
print(odejmij(c=1234))

print(oblicz_vat(1000))
print(oblicz_vat(1000, 15))
print(oblicz_vat(cena=6000))
print(oblicz_vat(1000) + dodaj(7, 89))  # 1326.0

zm = oblicz_vat(5000, 8)
print(zm)  # 5400.0
print(type(zm))  # <class 'float'>
if zm == 5400:
    print("Ok")  # Ok
