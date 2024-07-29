tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))  # <class 'str'>

# wszystko jest obiektem
# teksty są niemutowalne
#     """ Return a copy of the string converted to uppercase. """
tekst.upper()
print(tekst)  # Witaj Świecie
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie - orginał nie jest zmieniany

# zmienic na małe litery i wypisać
tekst_lower = tekst.lower()
print(tekst_lower)
print(tekst.lower())  # witaj świecie

print(tekst.count("i"))  # 3
print(tekst.count("j", 0, 4))  # 0123 -> 0, bo z prawej strony zbiór otwarty, indeks 4 nie jest brany pod uwage
# indeksowanie od 0
# Witaj Świecie
# 0123456789
# z prawej strony zbiór otwarty

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

tekst_zamiana = "Witaj dobry Świecie"
print(tekst_zamiana.replace("dobry", ""))  # "Witaj  Świecie"

print(tekst.removesuffix("Świecie").strip())  # "Witaj" strip() - usunie białe znaki np.: spacje końcowe, początkowe itd

print(tekst[4])  # wypisanie znaku o indeksie 4 -> "j"

# kodowanie znaków
encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9awiecie'  b - typ bajtowy
# \x - liczba zapisana w systemie szesnastkowym
print(type(encoded_s))  # <class 'bytes'> - typ bajtowy
print(encoded_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
# f - fstring, string sforamtowany
tekst_format = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format)
# 	Mam na imię Radek
#  i lubię pythona
# \t tabulator
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s!"  # %s - oczekuje str
print(starszy % imie)  # Witaj Radek! - w miejsce %s podstawiło wartość zmiennej imie

print("Witaj {}!".format(imie))  # Witaj Radek!

print("Wiatj", imie)  # Wiatj Radek

# tekst wielolinijkowy
print("""Tekst
wielolinijkowy
    tabulator""")
# "Tekst
# wielolinijkowy
#     tabulator"
