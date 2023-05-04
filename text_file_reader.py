import os


os.chdir("/Users/Reddmar/Desktop")

with open('ebooks_ext.txt', 'r') as f:
    data = f.readlines()
    ext_list = [i.strip().lower() for i in data if len(i.strip()) == 4]
    print(ext_list)
