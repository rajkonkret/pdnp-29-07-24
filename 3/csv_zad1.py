# pliki csv
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
# plik tekstowy w którym wartości oddzielone są znakiem podziału np,: ,;tab

import csv

filename = 'records.csv'
row = ['Radek', 'Coe', 2, '9.1']
fileds = ['name', 'branch', 'year', 'cgpa']

dictionary = dict(zip(fileds, row))
print(dictionary)  # {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'}

with open(filename, 'w', newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fileds)
    csvwriter.writerow(row)

filename_2 = 'records_2.csv'
with open(filename_2, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fileds)
    csvwriter.writeheader()
    csvwriter.writerow(dictionary)

dict_list = [
    {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Tomek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Marek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Zenek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Krzysztof', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
    {'name': 'Ania', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'},
]

filename_3 = 'records_3.csv'
with open(filename_3, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fileds, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(dict_list)

# delimiter=";" - znak podziału
# newline='' - ominięcie problemu pustych linii
