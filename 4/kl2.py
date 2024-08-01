class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    # stworzyc metode wypisz_wiek()
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def wypisz_wrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Magda", '37', 170)
print(cz1.wiek)
print(cz1.plec)
print(cz1.wzrost)
print(cz1.imie)
# 37
# k
# 170
# Magda
cz2 = Human("Radek", 50, 190, "m")
print(cz2.wiek)
print(cz2.plec)
print(cz2.wzrost)
print(cz2.imie)
# 50
# m
# 190
# Radek

cz1.powitanie()
cz2.powitanie()
# Nazywam się Magda
# Nazywam się Radek
cz2.wypisz_wiek()
cz1.wypisz_wiek()
# Mam 50 lat.
# Mam 37 lat.
cz1.ruszaj()
cz2.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę
