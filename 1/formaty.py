user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # liczby zmiennoprzecinkowe -> float
print(type(wersja))  # <class 'float'>
liczba = 123456789123
print(type(liczba))  # <class 'int'>

print("Witaj %s masz teraz %d lat." % (user, wiek))  # Witaj Tomek masz teraz 39 lat.
# przy takim formatowaniu tekstów python sprawdza typy
# print("Witaj %d masz teraz %s lat." % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit - liczba
print("Witaj %(user)s masz teraz %(wiek)d lat" % {'user': user, 'wiek': wiek})  # Witaj Tomek masz teraz 39 lat

print("Witaj {}, masz teraz {} lat.".format(user, wiek))  # Witaj Tomek, masz teraz 39 lat.
print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
# f - fstring - sformatowany tekst

# zaokrągla przy wyświetlaniu
print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3.9)  # Używamy wersji pythona 3.900000
print("Używamy wersji pythona %.1f" % 3.9)  # Używamy wersji pythona 3.9
print("Używamy wersji pythona %.2f" % 3.9)  # Używamy wersji pythona 3.90
print("Używamy wersji pythona %.0f" % 3.9)  # Używamy wersji pythona 4
print("Używamy wersji pythona %.f" % 3.9)  # Używamy wersji pythona 4
print("Wynik = %.2f" % 3.876)  # Wynik = 3.88
x = 3.14
print("Zero miejsc po przecinku %.f" % x)  # Zero miejsc po przecinku 3
print("X nadal się nie zmmieniło", x)  # X nadal się nie zmmieniło 3.14
y = round(x)
print("y=", y)
print("x=", x)
# y= 3
# x= 3.14

x = 3.1415
print(round(x, 2))  # 3.14

print(f"Używamy wersji pythona {wersja}")  # Używamy wersji pythona 3.900001
print(f"Używamy wersji pythona {wersja:.1f}")  # Używamy wersji pythona 3.9
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.90
print(f"Używamy wersji pythona {wersja:.0f}")  # Używamy wersji pythona 4

print(f'{user:>10}')  # "     Tomek"
print(f'{user:<20}')  # "Tomek               "
print(f"{user:^25}")  # "          Tomek          "

print(liczba)  # 123456789123
print(f"NAsza duża liczba {liczba:,}")  # NAsza duża liczba 123,456,789,123
print(f"NAsza duża liczba {liczba:,}".replace(",", "."))
print(f"NAsza duża liczba {liczba:,}".replace(",", " "))
# NAsza duża liczba 123.456.789.123
# NAsza duża liczba 123 456 789 123

liczba_2 = 123_456_789_123
print(liczba_2)
print(type(liczba_2))  # <class 'int'>

# 15_000_000
# 15000000
