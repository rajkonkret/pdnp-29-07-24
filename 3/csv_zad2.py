import csv

fileds = []
rows = []

# filename = 'records_2.csv'
filename = 'records_3.csv'

with open(filename, 'r') as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter)  # ;
    f.seek(0)  # ustawienie odczytu na początek pliku
    # csvreader = csv.reader(f, delimiter=";")
    csvreader = csv.reader(f, delimiter=dialect.delimiter)
    print(csvreader)  # <_csv.reader object at 0x0000019D711E1AE0>

    fileds = next(csvreader)  # odczyt bieżacego elemntu z iteratora, ustawienie na następny
    for row in csvreader:  # pętla wystartuje od drugiego elemntu
        # print(row)
        rows.append(row)

print(rows)
print(fileds)
# [['Radek;Coe;2;9.1'], ['Tomek;Coe;2;9.1'],
# ['Marek;Coe;2;9.1'], ['Zenek;Coe;2;9.1'], ['Krzysztof;Coe;2;9.1'], ['Ania;Coe;2;9.1']]
# ['name;branch;year;cgpa']
# # delimiter ;
# [['Radek', 'Coe', '2', '9.1'], ['Tomek', 'Coe', '2', '9.1'],
# ['Marek', 'Coe', '2', '9.1'], ['Zenek', 'Coe', '2', '9.1'],
# ['Krzysztof', 'Coe', '2', '9.1'], ['Ania', 'Coe', '2', '9.1']]
# ['name', 'branch', 'year', 'cgpa']
