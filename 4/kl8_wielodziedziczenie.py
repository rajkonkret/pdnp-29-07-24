# wielodziedziczenie

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


a = A()
a.method()
b = B()
b.method()


# Metoda z klasy A
# Metoda z klasy B


class C(B, A):  # wielodziedziczenie, kolejność ma znaczenie
    """
    Klasa dziedziczy po klasie B i A
    """


c = C()
c.method()  # Metoda z klasy B
print(C.__mro__)


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

class D(A, B):
    def method(self):
        super().method()  # dziedziczy po klasie nadrzędnej


d = D()
d.method()  # Metoda z klasy A


class E(B, A):
    def method(self):
        print("Metoda z klasy E")


e = E()
e.method()  # Metoda z klasy E


class F(A, B):
    def method(self):
        B.method(self)  # wskazanie z której klasy ma dziedziczyć metodę tu: B


f = F()
f.method()  # Metoda z klasy B


class G(A, B):
    def method(self):
        super().method()  # Metoda z klasy A
        B.method(self)  # Metoda z klasy B
        print("Metoda z klasy G")  # Metoda z klasy G


g = G()
g.method()
# Metoda z klasy A
# Metoda z klasy B
# Metoda z klasy G
