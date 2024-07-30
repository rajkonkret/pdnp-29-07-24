# krotka - kolekcja niemutowalna
# pozwala efektywniej zarzadzac pamięcią
# krotka jedoelementowa - stała - zmienna

tupla = "Radek"
print(type(tupla))  # <class 'str'>

tupla_2 = ("Radek")
print(type(tupla))  # <class 'str'>

tupla_3 = ("Radek",)
print(type(tupla_3))  # <class 'tuple'>
tupla_4 = "Radek",
print(type(tupla_4))  # <class 'tuple'>
# PEP8 zaleca by tuple jednoelementowa umiesczać w nawiasach
print((4,))  # (4,)

# tupla wieloelementowa moze miec nawiasy ale nie musi
# tupla_liczby = 43, 55, 22.34, 11, 200
tupla_liczby = (43, 55, 22.34, 11, 200)
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>

# tupla_liczby[2] = 123  # TypeError: 'tuple' object does not support item assignment

# del tupla_liczby  # usunięcie całej tupli
# print(tupla_liczby)  # NameError: name 'tupla_liczby' is not defined

tupla_imona = "Radek", "Tomek", "Zenek", "Olek", 'Robert', "Michał"
print(tupla_imona)  # ('Radek', 'Tomek', 'Zenek', 'Olek', 'Robert', 'Michał')
print(type(tupla_imona))  # <class 'tuple'>

print(tupla_imona.index("Radek"))  # indeks 0
print(tupla_imona.count("Olek"))  # wystepuje 1 raz w kolekcji

# rozpakowanie tupli
tup = 1, 2
a, b = tup
print(a, b)  # 1 2

tup_1 = 1, 2, 3
# a, b = tup_1  # ValueError: too many values to unpack (expected 2)

a, *b = tup_1  # * worek na pozostałe dane
print(a, b)  # 1 [2, 3]

print(tupla_imona)  # ('Radek', 'Tomek', 'Zenek', 'Olek', 'Robert', 'Michał')
name1, name2, *name3 = tupla_imona  # Radek Tomek ['Zenek', 'Olek', 'Robert', 'Michał']
print(name1, name2, name3)

name1, *name2, name3 = tupla_imona  # Radek ['Tomek', 'Zenek', 'Olek', 'Robert'] Michał
print(name1, name2, name3)

*name1, name2, name3 = tupla_imona  # ['Radek', 'Tomek', 'Zenek', 'Olek'] Robert Michał
print(name1, name2, name3)

# sortowanie krotki zwraca listę
print(sorted(tupla_imona))  # ['Michał', 'Olek', 'Radek', 'Robert', 'Tomek', 'Zenek']
print(tupla_imona)  # ('Radek', 'Tomek', 'Zenek', 'Olek', 'Robert', 'Michał')

lista = list(tupla_imona)
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Olek', 'Robert', 'Michał']
print(type(lista))  # <class 'list'>
