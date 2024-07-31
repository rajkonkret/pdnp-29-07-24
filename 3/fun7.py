def connect(**opcje):  # ** argumnty słownikowe, nazwane
    print(opcje)
    print(type(opcje))


connect(a=9)  # {'a': 9}, <class 'dict'>
connect(a=9, b=9, c=7, name="Radek")  # <class 'dict'>, {'a': 9, 'b': 9, 'c': 7, 'name': 'Radek'}


def all_params(*args, **kwargs):
    print(args, kwargs)


all_params(1, 2, 3, 4, 5, 6)
all_params(1, 2, 3, 4, 5, 6, a=9, b=90)
all_params(a=9)
# (1, 2, 3, 4, 5, 6) {}
# (1, 2, 3, 4, 5, 6) {'a': 9, 'b': 90}
# () {'a': 9}
all_params()  # () {}
