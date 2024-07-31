import pandas

# pip install pandas

data = pandas.read_csv('records_3.csv', delimiter=";")
print(data)
#         name branch  year  cgpa
# 0      Radek    Coe     2   9.1
# 1      Tomek    Coe     2   9.1
# 2      Marek    Coe     2   9.1
# 3      Zenek    Coe     2   9.1
# 4  Krzysztof    Coe     2   9.1
# 5       Ania    Coe     2   9.1

print(data.columns)
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['Radek' 'Coe' 2 9.1]
#  ['Tomek' 'Coe' 2 9.1]
#  ['Marek' 'Coe' 2 9.1]
#  ['Zenek' 'Coe' 2 9.1]
#  ['Krzysztof' 'Coe' 2 9.1]
#  ['Ania' 'Coe' 2 9.1]]
print(data.items)
# <bound method DataFrame.items of         name branch  year  cgpa
# 0      Radek    Coe     2   9.1
# 1      Tomek    Coe     2   9.1
# 2      Marek    Coe     2   9.1
# 3      Zenek    Coe     2   9.1
# 4  Krzysztof    Coe     2   9.1
# 5       Ania    Coe     2   9.1>
