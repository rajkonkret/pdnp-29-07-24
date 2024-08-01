# dziedziczenie
# przejęcie cech innej kalsy, nadpisanie, modyfikacja, rozszerzenie

class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print("Kolor", self.kolor)


class Samochod(Pojazd):  # dziedziczenie po klasie Pojazd
    """
    Klasa Samochód
    """

    def __init__(self, kolor, marka="Skoda"):
        super().__init__(kolor)  # musimy!!! obowiązkowo użyc konstruktora z klasy nadrzędnej
        self.marka = marka

    def info(self):
        super().info()  # mozemy (nie musimy) wywołąc taką metode z klasy nadrzędnej
        print(f"Marka: {self.marka}")


poj = Pojazd("niebieski")
poj.info()  # Kolor niebieski

car = Samochod("Czerwony")
car.info()  # Kolor Czerwony

car_2 = Samochod("Biały", "Porsche")
car_2.info()

# polimorfizm możliwość wykorzystania cech wspólnych dla obiektów różnych klas dziedziczących po wspólnej klasie
lista = [poj, car_2, car]
for i in lista:
    i.info()
# Marka: Porsche
# Kolor niebieski
# Kolor Biały
# Marka: Porsche
# Kolor Czerwony
# Marka: Skoda
