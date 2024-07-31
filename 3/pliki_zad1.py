# działania z plikami
# context manager - usprawnia prace z pliki
# with - context manager w python
# open() - operacje na plikach
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:  # filehandler
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

# w - tworzy nowy plik, nadpisuje jeśli istnieje
with open('test.log', 'w', encoding='utf-8') as f:
    f.write("Nadpisane\n")

# a - dopisanie do istniejącego pliku
with open('test.log', "a", encoding='utf-8') as file:
    file.write('Dodane\n')
    file.write('Dodane\n')
    file.write('Dodane\n')
    file.write('Dośdane\n')

with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()

print(lines)
# Nadpisane
# Dodane
# Dodane
# Dodane
# Dośdane
