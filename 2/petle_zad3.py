# while - petla sterowana warunkiem

licznik = 0
while True:
    licznik += 1
    print("Komunikat 1 !")
    if licznik > 10:
        break  # przerywamy pętle

print(licznik)  # 11
licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 2 !!!")

# password = input("Podaj hasło")
# while password != "secret":
#     password = input("Błędne hasło. Podaj ponownie")
# print("Hasło prawidłowe")

# lista = []
# lista_int = []
# while True:
#     wej = input("podaj liczbę")
#     if not wej.isnumeric():
#         break
#     lista.append(wej)
#     lista_int.append(int(wej))
# print(lista)  # ['1', '2', '3', '8', '90']
# print(lista_int)  # [1, 2, 3, 8, 90]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # [1, 2, 3, 4, 6]
