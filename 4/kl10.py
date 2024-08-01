import pickle

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

with open('lista.txt', 'w', encoding='utf-8') as f:
    f.write(str(lista))

with open('lista.txt', "r", encoding='utf-8') as file:
    dane = file.read()

print(dane)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(dane))  # <class 'str'>
print(dane[0])  # [
print(dane.split(","))  # ['[1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9]']

# serializacja - zamiana na postać bajtową
with open('lista.pickle', "wb") as f:
    pickle.dump(lista, f)

# deserializacja
with open('lista.pickle', "rb") as file:
    loaded_list = pickle.load(file)

print(loaded_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(loaded_list))  # <class 'list'>
print(loaded_list[0])  # 1

# serializac
ser_lista = pickle.dumps(lista)
print(ser_lista)
# b'\x80\x04\x95\x17\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05K\x06K\x07K\x08K\te.'
print(type(ser_lista))  # <class 'bytes'>

# deserializacja
lista_desrializacja = pickle.loads(ser_lista)
print(lista_desrializacja)
print(type(lista_desrializacja))
print(lista_desrializacja[0])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# <class 'list'>
# 1
