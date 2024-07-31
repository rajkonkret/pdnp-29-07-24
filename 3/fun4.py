# funkcja wewnętrzna, zagnieżdżona
# dekorator - używa mechanizmu funkcji wewnętrznej
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwróćenie adresu fun2 (referencji)


fun1()  # To jest fun1
print()
xFun = fun1()
print(type(xFun))  # <class 'function'>
print(xFun)  # <function fun1.<locals>.fun2 at 0x00000228AEAD98A0>
xFun()  # To jest fun2
