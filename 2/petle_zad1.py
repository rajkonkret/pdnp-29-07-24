# petle - dają nam możliwość wykonania wielokrotnie tego samego kodu
# for petla iteraacyjna
import random

for i in range(5):  # 0..4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(5):  # _ niema zmienna
    print("Test podłoga")
    # print(_)
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga

for i in range(20):
    print(i * 2)

# na podstawie lotto
# przerobić na petle
lista_kule = list(range(1, 50))
lista_wylosowane = []
for i in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    # print(wyn)
    lista_wylosowane.append(wyn)

print(lista_wylosowane)  # [2, 9, 34, 14, 39, 37]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehension
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista_wylosowane:
    if c > 10:
        print("Większe od 10", c)
# Większe od 10 30
# Większe od 10 39
# Większe od 10 42
# Większe od 10 40
# Większe od 10 43

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(10, 0, -2):  # krok ujemny, odliczamy w tył
    print(i)

for i in range(-10, 0):
    print(i)

for c in lista3:
    if c == 2:
        c += 1
    print(c)  # 3
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

imiona = ['Radek', 'Tomek', 'Zenek', 'Ania']
print(imiona)
print(type(imiona))
# ['Radek', 'Tomek', 'Zenek', 'Ania']
# <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# wypisac elementy tej listy z indeksem 0 Radek
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i in range(len(imiona)):  # range(4) 0..3
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - zwraca element kolekcji i jego pozycję
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')
i, o = (0, 'Radek')
print(i, o)
for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

ludzie = ['Radek', 'Ania', 'Tomek', 'Zenek']
wiek = [44, 55, 44, 22]
# Radek 44
for i in ludzie:
    print(i, wiek[ludzie.index(i)])
# Radek 44
# Ania 55
# Tomek 44
# Zenek 22

ludzie = ['Radek', 'Ania', 'Tomek', 'Zenek', "Magda"]
wiek = [44, 55, 44, 22]
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])  # IndexError: list index out of range

# zip() - łaczy kolekcje
for i in zip(ludzie, wiek):
    print(i)
# ('Radek', 44)
# ('Ania', 55)
# ('Tomek', 44)
# ('Zenek', 22)
for o, w in zip(ludzie, wiek):
    print(o, w)
# Radek 44
# Ania 55
# Tomek 44
# Zenek 22

# 0 Radek 44
for i in enumerate(zip(ludzie, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Ania', 55))
# (2, ('Tomek', 44))
# (3, ('Zenek', 22))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(c, d)  # Radek 44
(a, (c, d)) = (0, ('Radek', 44))
print(a, c, d)  # 0 Radek 44
a, (c, d) = (0, ('Radek', 44))
for a, (c, d) in enumerate(zip(ludzie, wiek)):
    print(a, c, d)
# 0 Radek 44
# 1 Ania 55
# 2 Tomek 44
# 3 Zenek 22
