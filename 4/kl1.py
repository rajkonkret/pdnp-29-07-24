# klasa - element programowania obiektowego
# klasa - szablon, przepis
# wskazuje minimum tego co obiekt musi posiadac
# obiekt (instancja) zbudowany według przepisu (klasy)
# definicja kalsy - nic się nie wykona
# dopiero budowanie obiektu uruchmi elelmenty klasy
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja
# pola (stan obiektu)
# metody (funkcje)
class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"


"""komentarz"""
print(Human.__doc__)  # Klasa Humn opisująca człowieka w pythonie
print(print.__doc__)
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.
# cd 4 - wejscie do katalogu 4
# pydoc -b - generowanie serwera dokumentacji
# pydoc -w kl1

cz1 = Human()
print(cz1)  # <__main__.Human object at 0x0000019B88E61D90>
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
#
# None
# k
cz1.imie = "Ania"
cz1.wiek = 29
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Ania
# 29
# k

# stworzyc obiekt klasy Human, odmiennej płci
cz2 = Human()
cz2.imie = "Tomek"
cz2.wiek = 45
cz2.plec = "m"
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
