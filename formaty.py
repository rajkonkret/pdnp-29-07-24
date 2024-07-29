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

