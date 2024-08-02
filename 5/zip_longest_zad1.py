import numpy as np
from itertools import zip_longest

technologies = ['Spark', 'Pandas', 'Python', 'PHP']
fee = [25000, 20000, 15000, 18000, 22000]
duration = ['50 Days', '35 Days', np.nan, '15 Days', '10 Days']
# np.nan - odpowiednik None w bibliotecy NumPy
discount = [2000, 1000, 800, 500, 500]
columns = ['Courses', 'Fee', 'Duration', 'Discount']

lista = list(zip(technologies, fee, discount))
print(lista)
# [('Spark', 25000, 2000), ('Pandas', 20000, 1000), ('Python', 15000, 800), ('PHP', 18000, 500)]

lista_longest = list(zip_longest(technologies, fee))
print(lista_longest)
# [('Spark', 25000), ('Pandas', 20000), ('Python', 15000), ('PHP', 18000), (None, 22000)]

lista_longest_fv = list(zip_longest(technologies, fee, fillvalue="TEST"))
print(lista_longest_fv)
# [('Spark', 25000), ('Pandas', 20000), ('Python', 15000), ('PHP', 18000), ('TEST', 22000)]
