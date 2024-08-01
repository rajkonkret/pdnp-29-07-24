# zrobic klasę Dom
# metraz, kolor, liczba_okien
# pola mają być prywatne
# wystawić metody do odczytu i zapisu tych pól
# dodać komentarze - dokumentacja
# użyć tej klasy do zbudowania obiektów i wywołać metody
class Dom:
    """
    klasa Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        """
        Metoda inicjalizująca
        :param metraz:
        :param kolor:
        :param liczba_okien:
        """
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def mam_metraz(self):
        print(f"Mam metraż {self.__metraz}")

    def mam_kolor(self):
        print(f"Mam kolor {self.__kolor}")

    def mam_okna(self):
        print(f"Liczba okien {self.__liczba_okien}")

    def zmien_metraz(self):
        odp = int(input("Podaj nowy metraż"))
        self.__metraz = odp
        self.mam_metraz()

    def zmien_okna(self):
        odp = int(input("Podaj nową liczbę okien"))
        self.__liczba_okien = odp
        self.zmien_okna()

    def zmien_kolor(self):
        odp = input("Podaj nowy kolor")
        self.__kolor = odp
        self.mam_kolor()


dom = Dom(300, "biały", 20)
dom.mam_metraz()
dom.mam_kolor()
dom.mam_okna()

dom.zmien_kolor()
# Mam metraż 300
# Mam kolor biały
# Liczba okien 20
# Podaj nowy kolorzielony
# Mam kolor zielony
