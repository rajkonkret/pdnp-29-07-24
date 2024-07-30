# słownik - para klucz-wartość
# {'user':"Radek"}
# {"klucz":"wartość"}
# słownik jest odpowiednikiem jsona w pythonie

# pusty słownik
dictionary = dict()
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = {}
print(type(dictionary_1))  # <class 'dict'>

# dodawanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 37
print(dictionary)  # {'imie': 'Radek', 'wiek': 37}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 37])
# dict_items([('imie', 'Radek'), ('wiek', 37)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 37}

# wypisanie elementu
print(dictionary['imie'])  # Tomek
# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary.get('Imie'))  # None
print(dictionary.get('Imie', 'default'))  # wartosc domyslna default

dictionary.update({'date': '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 37, 'date': '12-12-2024'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 4)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 4}

# # input() - pobiera dane od użytkownika
# tekst = input("Wpisz tekst")
# print(type(tekst))  # <class 'str'>
# print(tekst)
# <class 'str'>
# jakis tekst

# aplikacja kalkulator
# pobrac dwie liczby od uzytkownika
# wypisac wynik obliczenia (+)
# a = input("Podaj pierwszą liczbę")
# b = float(input("Podaj drugą liczbę"))
# print("Wynik dodawania", int(a) + b)  # Wynik dodawania 11.0
# # alt shift E - uruchomienie zaznaczonego fragmentu kodu

# napisac aplikację słownik
# powinna wyswietlic słowka, ktore umie przetłumaczyc
# pobrac słowko od uzytkownika
# wypisac tłumaczenie

pol_ang = {'kot': 'cat', 'pies': 'dog', 'jabłko': 'apple'}  # definowanie słownika
print("Słówka do przetłumaczenia", pol_ang.keys())  # wypisanie kluczy
odp = input("Podaj słówko")
# wypisanie tłumaczenia
print(pol_ang[odp.lower().strip()])
print(pol_ang[odp.lower().replace(" ", '')])
print(pol_ang.get(odp, 'Brak w słowniku'))
# cat
# cat
# Brak w słowniku
