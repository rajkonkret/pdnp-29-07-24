from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """

        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # dekorator oznaczający metode jako abstrakcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać.")


class Orzel(Ptak):
    """
    Klasa orzeł
    """

    def wydaj_odglos(self):
        print("kieer kier kir")

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# klas Sowa nie nadpisuje metody wydaj_odglos() - nie można stworzyc obiektu takiej klasy
class Sowa(Ptak):
    """
    Klasa Sowa
    """


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# pozonaczeniu metody jako abstrakcyjna, klasa staje się abstrakcyjna
# nie można utworzyć obiektu tej klasy
# or1 = Ptak("Orzeł Bielik", 45)
# or1.latam()  # Tu Orzeł Bielik Lecę z szybkością 45
# kur1 = Ptak("Kura Domowa", 0)
# kur1.latam()  # Tu Kura Domowa Lecę z szybkością 0
# kur1.wydaj_odglos()
# or1.wydaj_odglos()

kur2 = Kura("Kura Domowa")
kur2.latam()  # Tu Kura Domowa Lecę z szybkością 0
kur2.wydaj_odglos()  # Ko ko ko ko

or2 = Orzel("Orzeł Bielik", 50)
or2.latam()
or2.wydaj_odglos()
# Tu Orzeł Bielik Lecę z szybkością 50
# kieer kier kir
kur2.dziobanie()
or2.poluj()
# Tu Kura Domowa Idę sobie podziobać.
# Tu Orzeł Bielik Rozpoczynam polowanie

# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# klas Sowa nie nadpisuje metody wydaj_odglos() - nie można stworzyc obiektu takiej klasy
# sowa = Sowa("Sowa", 15)
