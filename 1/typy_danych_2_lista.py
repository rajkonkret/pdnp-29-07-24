# Kolekcje
# lista - przechowuje wiele danych, różnego typu na raz
# zachowuje kolejnosc przy dodawaniu do listy

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodanie elemntu (na końcu) do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Olek")
lista.append("Michał")
lista.append("Robert")
lista.append("Zenek")
print(lista)
# ['Radek', 'Tomek', 'Olek', 'Michał', 'Robert', 'Zenek']
#     0        1        2        3         4         5
#    -6      -5      -4       -3         -2         -1
print(lista[0])  # Radek
print(lista[2])  # Olek
print(lista[4])  # Robert
print(lista[5])  # Zenek
print(len(lista))  # 6 - długosc listy, mniejsza o jeden niz ostatni nr indeksu
# print(lista[6])  # IndexError: list index out of range
print(lista[-1])  # Zenek
print(lista[-4])  # Olek

# wyswietlenie fragmentu listy (slicowanie)
print(lista[0:3])  # start:stop 012  ['Radek', 'Tomek', 'Olek']  nie uwzględnia indeksu 3
print(lista[:3])  # ['Radek', 'Tomek', 'Olek']
print(lista[2:])  # ['Olek', 'Michał', 'Robert', 'Zenek']  indeksy 2345
print(lista[2:5])  # ['Olek', 'Michał', 'Robert']
print(lista[:])  # ['Radek', 'Tomek', 'Olek', 'Michał', 'Robert', 'Zenek']
print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # [0:4], ['Radek', 'Tomek', 'Olek', 'Michał']
print(lista[2:3])  # ['Olek']
print(lista[2:10])  # ['Olek', 'Michał', 'Robert', 'Zenek']
print(lista[10:29])  # []
print(lista[0:5:2])  # [start:stop:krok]  ['Radek', 'Olek', 'Robert'] indeksy 024

lista_15 = list(range(15))  # 0..14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[0:14:3])  # [0, 3, 6, 9, 12]
print(lista_15[-10])  # 5

# nadpisanie elemntu listy
lista[3] = "Mikołaj"
print(lista)  # ['Radek', 'Tomek', 'Olek', 'Mikołaj', 'Robert', 'Zenek']

# rozszerzenie listy we wskazanym indeksie
lista.insert(1, "Joanna")
print(lista)  # ['Radek', 'Joanna', 'Tomek', 'Olek', 'Mikołaj', 'Robert', 'Zenek']
print(len(lista))  # 7

lista.insert(15, 'Patryk')
print(lista)  # ['Radek', 'Joanna', 'Tomek', 'Olek', 'Mikołaj', 'Robert', 'Zenek', 'Patryk']

# sprawdzenie indeksu dla elemntu
print(lista.index("Patryk"))  # indeks numer 7

# usunięcie elementu z listy
lista.remove("Patryk")
print(lista)  # ['Radek', 'Joanna', 'Tomek', 'Olek', 'Mikołaj', 'Robert', 'Zenek']

# usunięcie elemnentu z listy po indeksie
# zwraca usunięty element
print(lista.pop(5))  # Robert
print(lista)
print(lista.pop(-2))  # Mikołaj
print(lista.pop())  # Zenek - usunie ostatni element z listy

a = 1
b = 3
a = b
print(a, b)  # 3 3
b = 7
print(a, b)  # 3 7

lista_2 = lista  # a = b ? kopiowanie referencji (adresu pamięci)
lista_copy = lista.copy()  # kopia elementów listy
print(lista_2, lista)  # ['Radek', 'Joanna', 'Tomek', 'Olek'] ['Radek', 'Joanna', 'Tomek', 'Olek']
lista.clear()  # odpowiednik b=7
print(lista_2, lista)  # [] []
print(id(lista))  # 2120898171264
print(id(lista_2))  # 2120898171264
print(lista_copy)  # ['Radek', 'Joanna', 'Tomek', 'Olek']
print(id(lista_copy))  # 2120898491776

liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)
print(type(liczby))  # <class 'list'>

liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]

liczby = [54, 999, 34, 22, 12.34, 687, "A"]
# liczby.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

lista_osob = ['radek', 'ola', 'agata', 'lena']
lista_osob.sort()
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']
lista_osob.sort(reverse=True)
print(lista_osob)  # ['radek', 'ola', 'lena', 'agata']
lista_osob.reverse()  # odwrócenie bez sortowania
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek']

liczby[3] = 666
print(liczby[0:3])  # [54, 999, 34]
print(liczby[-2])  # 687
print(liczby)  # [54, 999, 34, 666, 12.34, 687, 'A']

print(liczby.pop(2))  # 34, usunie element o indeksie 2
liczby.remove(54)  # usunie element 54
print(liczby)  # [999, 666, 12.34, 687, 'A']

tekst = "Pyt hon."
lista1 = list(tekst)
print(lista1)  # ['P', 'y', 't', ' ', 'h', 'o', 'n', '.'] rozpakowanie sekwencji

lista2 = [tekst]
print(lista2)  # ['Pyt hon.']

krotka = tuple(liczby)  # tuple() - rzutowanie na krotkę (tuplę)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (999, 666, 12.34, 687, 'A')
