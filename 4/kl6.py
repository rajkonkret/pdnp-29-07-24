# pracownik - imie, nazwisko, pensja
# manager - imie, nazwiska, pensje, premia

class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Mam na imię {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Manager(Pracownik):
    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 10000)
manager = Manager("Anna", "Nowak", 20000, 10000)

lista_pracownicy = [pracownik, manager]

for p in lista_pracownicy:
    p.przedstaw_sie()
    print("Pensja wynosi:", p.oblicz_pensje())

# Mam na imię Jan Kowalski
# Pensja wynosi: 10000
# Mam na imię Anna Nowak
# Pensja wynosi: 30000
