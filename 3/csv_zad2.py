import csv

fileds = []
rows = []

filename = 'records_2.csv'

with open(filename, 'r') as f:
    csvreader = csv.reader(f)
    print(csvreader)  # <_csv.reader object at 0x0000019D711E1AE0>
