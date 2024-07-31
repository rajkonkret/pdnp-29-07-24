# stworzyc funkcję obliczjącą średnią
def liczby(name=None, *cyfry):  # * przyjmuje dowolna ilosc danych przekazywanych po pozycji 1,2,3,4,5
    # print(cyfry)
    count = len(cyfry)  # dlugość kolekcji
    suma_p = sum(cyfry)  # suma  w pythonie
    suma = 0
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Uczeń {name}, Srednia wynosi", avg)
    finally:
        print("Następne obliczenie")


liczby(1, 2, 3, 4, 5, 6)
liczby(1)
liczby()
liczby("Tomek", 5, 4, 4, 5, 3)
# Uczeń Tomek, Srednia wynosi 4.2
# Następne obliczenie
