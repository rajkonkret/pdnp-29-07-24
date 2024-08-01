class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    # print(5 / 0)
    raise ZeroDivisionError("Dzielenie przez zero!!!")
except ZeroDivisionError as e:
    print("Nie dziel przez zero", e)

# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-29-07-24\4\kl9_exception.py", line 15, in <module>
#     raise MyException('X nie może być 0')
# MyException: X nie może być 0
x = 0

try:
    if x == 0:
        raise MyException('X nie może być 0')
except MyException as e:
    print("Bład wartości", e)
# Bład wartości X nie może być 0
