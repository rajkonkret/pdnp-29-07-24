# match case
# od pythona 3.10

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.lower().strip():
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("Znam Javę")
    case _:  # wartość domyślna, odpowiednik else
        print("Nie znam takiego języka")

print(lista)
