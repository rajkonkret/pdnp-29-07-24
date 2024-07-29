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
