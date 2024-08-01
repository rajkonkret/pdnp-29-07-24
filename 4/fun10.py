# dekoratory
# dekoratory wykorzystują mechanizm funkcji wewnętrznej
# dekorator przyjmuje funkcję jako argument, dodaje nową funkcjonalność, zwraca wynik

def dekor(funk):
    def wew():
        print("Dekoruje")
        return funk()

    return wew


@dekor
def hej():
    print("Hej")


@dekor
def odejmij():
    print(7 - 9)


hej()  # Hej
# Po dodaniu dekoratora wynik funkcji:
# Dekoruje
# Hej

odejmij()
# Dekoruje
# -2
