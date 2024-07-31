import os

for root, dirs, files in os.walk("../"):
    # print(files)
    for file in files:
        # if file == "main.py":
        if file == "test.log":
            file_path = os.path.join(root, file)
            print(file_path)  # ../3\test.log

with open("C:\\Users\\CSComarch\\PycharmProjects\\pdnp-29-07-24\\main.py") as f:
    lines = f.read()

print(lines)
# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# # 2 x shift - podrÄ™czne menu wyszukiwania
# # ctrl alt l - formatowanie kodu do zasad PEP8
# # theme - wybĂłr wyglÄ…du
# # wheel - wĹ‚aczenie powiÄ™kszania znakĂłw
# # python.exe .\main.py - uruchomienie pliku pythona czyli pliku z rozszerzeniem .py
# # ctrl shift f10 - uruchomienie pliku
