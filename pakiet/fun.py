def powitanie():
    print("Cześć")


def info():
    print("Jestem pakietem")


# jak uruchamiam bezpośrednio ma wartość __main__
# jak uruchmaiam z importu ma wartość pakiet.fun
print(__name__)
if __name__ == '__main__':
    info()
