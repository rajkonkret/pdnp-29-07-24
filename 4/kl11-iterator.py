# iterator - zwraca kolejne elementy
class Count:
    def __init__(self, low, high):
        """
        Klasa inicjalizująca
        :param low: wartość minimalna
        :param high: wartość maksymalna
        """
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


counter = Count(low=1, high=9)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# licznik wyjdzie poza zakres
# print(next(counter))  # StopIteration - zakończyło działanie iteratora
