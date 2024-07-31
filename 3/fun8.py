def allparams(a, b, /, c=42, d=256):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")


allparams(1, 2)
# a=1, b=2
# c=42, d=256
allparams(1, 2, 4, 5)


# a=1, b=2
# c=4, d=5
# Po dodaniu / w argumentach
# a i b nie mogą byc przekazanae jako pozycyjne
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-29-07-24\3\fun8.py", line 12, in <module>
#     allparams(a=6, b=7)
# TypeError: allparams() got some positional-only arguments passed as keyword arguments: 'a, b'
# allparams(a=6, b=7)
# a=6, b=7
# c=42, d=256

def allparams2(a, b, /, c=42, *args, d=256, **kwargs):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")
    print(f"{args=}, {kwargs=}")


allparams2(1, 2)
allparams2(1, 2, 3)
allparams2(1, 2, c=3)
allparams2(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
allparams2(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 23, 4, 5, 6, 7, d=9)
allparams2(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 23, 4, 5, 6, 7, d=9, e=900)
# args=(4, 5, 6, 7, 8, 9, 0, 11, 23, 4, 5, 6, 7), kwargs={'e': 900}
allparams2(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 23, 4, 5, 6, 7, d=9, e=900, a=1487)
