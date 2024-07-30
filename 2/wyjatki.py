# wyjątki
# błędy podczas wykonywania programu
# print(5 / 0)

# print("Dalsza częśc programu")
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-29-07-24\2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

number = 90
try:
    # print(number / 0)
    # print("A" + 9)
    # print(int("A"))
    # raise KeyError - rzucenie błedu
    wynik = number / 3
except ZeroDivisionError:
    print("Nie można dzielić przez 0")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
else:  # tylko gdy nie bedzie błedu
    print(f"Wynik działania {wynik}")
finally:  # wykona się zawsze
    print("Działam dalej")
print("Dalsza część programu")
# Nie można dzielić przez 0
# Dalsza część programu

# try except [else - finally]
