import chardet

# pip install chardet  - do wpisania w konsoli

with open('test.log', 'rb') as f:  # rb - odczyt binarny
    raw_data = f.read()

print(raw_data)
# b'Nadpisane\r\nDodane\r\nDodane\r\nDodane\r\nDo\xc5\x9bdane\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6658130518007462, 'language': 'Turkish'}
# po zwiększeniu ilośći polskich liter w pliku odczytało prawidłowo
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
print(type(result))  # <class 'dict'>
encoding = result['encoding']
print(raw_data.decode(encoding=encoding))
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
# <class 'dict'>
# Nadpisane
# Dodane
# Dodane
# Dodane
# Dośdane
# Dośąćdane
