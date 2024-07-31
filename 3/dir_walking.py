import os

for root, dirs, files in os.walk("../"):
    # print(files)
    for file in files:
        # if file == "main.py":
        if file == "test.log":
            file_path = os.path.join(root, file)
            print(file_path)  # ../3\test.log
