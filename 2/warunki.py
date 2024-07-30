# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# w zależnosci od warunku wykonuje jedna lub drugą operację
# warunek zwraca bool
# if
odp = True
print(bool(odp))  # True
odp = False
if odp:
    # blok wykonywany po if, gdy warunek True
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")

odp = "Radek"
if odp:
    print("Radek")  # Radek

if odp == "Radek":
    print("Nadal Radek")  # Nadal Radek

if odp == "Tomek":
    print("To jest Tomek")
else:  # w przeciwnym wypadku, działąnie domyślne
    print("To nie jest Tomek")  # To nie jest Tomek

# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki}")
# # dla przedziału 10000 do 29999 podatek wynosi 0.2
# # kolejnosc warunków ma znaczenie
# # pierwszy spełniony warunek, wychodzi z całości

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0
print(f"Rabat wynosi {rabacik}")  # Rabat wynosi 25
# ctrl / - komentowanie szybkie

rabat = 25 if suma_zam > 100 else 0  # ternary operator
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

# zasymulujemy system zbierania logów
# zmienne będą przechowywać dane, które przyszły z zewnętrznego systemu
# email, console, inny
# dla console: "Stało się coś strasznego"
# dla email: "System email"
# dla systemu email będa poziomy błedów
# error, medium, inny
# zapisac opis tych błedów w liscie

alert_system = 'email'
error = 'medium'
lista_b = []
if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == 'email':
    print("System email")  # # System email
    if error == 'medium':
        lista_b.append("Ostrzeżenie")
    elif error == 'error':
        lista_b.append("Krytyczny")
    else:
        lista_b.append('inny')
else:
    print("Nie znam takiego systemu")

print(lista_b)

# napisać test z.....
# pytanie
# pobrac od użytkownika odpowiedż
# wyświetlić wynik
punkty = 0
odp = input("Podaj datę Chrztu Polski")
if odp == '966':
    print("Odpowiedż prawidłowa")
    # punkty = punkty + 1
    punkty += 1
else:
    print("Bład")

print(punkty)
