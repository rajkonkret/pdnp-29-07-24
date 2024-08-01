class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # __ - pole prywatne, hermetyzacja

    # wystawienie metod do odczytu i zapisu wartośći pól - enkapsulacja
    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamulec(self):
        self.__predkosc -= 10


car1 = Car("Fiat 126p", 2024)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# pooznaczeniu jako prywatne pole nie jest widoczne poza klasą
# print(car1.__predkosc)  # 50
car1.licznik()  # Prędkość wynosi 50 km/h
car1.__predkosc = 0  # doda pole o tej nazwie o zasiegu globalnym
car1.hamulec()
car1.hamulec()
car1.hamulec()
car1.hamulec()
car1.hamulec()
car1.licznik()  # Prędkość wynosi 0 km/h
