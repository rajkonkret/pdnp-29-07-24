import random

# generowania liczb pseudolosowych

print(random.randint(1, 100))  # int 1..100
print(random.randrange(1, 100))  # int 1..99
print(random.randrange(5))  # int 0 .. 4
print(random.random())  # float 0.015928431561942014 od 0 do 0.999999
print(random.random() * 10)  # float 2.145128647344362 od 0 do 9.999999

lista = [67, 45, 23, 45, 67, 89, 90]
print(random.choice(lista))  # 67

lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)
# print(random.choice(lista_kule))
# print(random.choice(lista_kule))
# print(random.choice(lista_kule))
# print(random.choice(lista_kule))
# print(random.choice(lista_kule))
# print(random.choice(lista_kule))

# wyn = random.choice(lista_kule)
# lista_kule.remove(wyn)
# print(wyn)

print(random.choices(lista_kule, k=6))  # losuje z powtórzeniami
# losowanie bez powtórzeń
print(random.sample(lista_kule, 6))  # [18, 21, 3, 29, 19, 8]
print(random.sample(lista_kule, k=6))  # [27, 14, 1, 25, 43, 29]
