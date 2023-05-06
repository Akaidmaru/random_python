import os


os.chdir("/Users/Reddmar/Desktop")

with open("ebooks_ext.txt", "r", encoding='utf8') as f:
    data = f.readlines()

    for count, element in enumerate(data):
        print(f"{count}) {element.strip()}")
