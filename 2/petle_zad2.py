dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}

# wysietli klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
# imie
# nazwisko

# wyswietlenie wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wyswietlenie par
for i in dictionary.items():
    print(i)

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski

pol_ang = {'kot': 'cat', 'pies': 'dog', 'jabłko': 'apple'}
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'cat': 'kot', 'dog': 'pies', 'apple': 'jabłko'}
print({value: key for key, value in pol_ang.items()})  # {'cat': 'kot', 'dog': 'pies', 'apple': 'jabłko'}
